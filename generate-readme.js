const fs = require("fs");
const path = require("path");

// 目标目录
const targetDir = "./docs"; // 替换为你的目标文件夹路径，这里以当前目录为例
const outputFilePath = path.join("./README.md"); // 输出文件路径

// 遍历目录并生成目录结构
function generateDirectoryStructure(dir, indent = "") {
  let output = "";
  const items = fs.readdirSync(dir, { withFileTypes: true });

  // 对目录和文件进行排序：目录优先，文件按扩展名排序
  items.sort((a, b) => {
    if (a.isDirectory() && !b.isDirectory()) return -1; // 目录优先
    if (!a.isDirectory() && b.isDirectory()) return 1;
    return a.name.localeCompare(b.name); // 字母顺序排序
  });

  for (let item of items) {
    const fullPath = path.join(dir, item.name);
    //   relativePath加上根目录
    const relativePath = path.join(
      targetDir,
      path.relative(targetDir, fullPath)
    );

    if (item.isDirectory()) {
      // 如果是目录，递归处理
      output += `${indent}- ${item.name}\n`;
      output += generateDirectoryStructure(fullPath, indent + "  "); // 缩进处理
    } else if (item.name.endsWith(".md") || item.name.endsWith(".ipynb")) {
      // 如果是.md或.ipynb文件，生成链接
      const fileName = path.basename(item.name, path.extname(item.name)); // 去掉扩展名
      console.log("relativePath", relativePath);

      output += `${indent}- [${fileName}](${relativePath})\n`;
    }
  }
  return output;
}

// 主函数
function main() {
  const directoryStructure = generateDirectoryStructure(targetDir);

  // 写入README.md
  fs.writeFileSync(outputFilePath, directoryStructure, "utf-8");
  console.log(`Directory structure has been written to ${outputFilePath}`);
}

// 执行主函数
main();
