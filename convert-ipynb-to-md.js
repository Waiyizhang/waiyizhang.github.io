const fs = require("fs");
const path = require("path");
const { exec } = require("child_process");
const { promisify } = require("util");
const execAsync = promisify(exec);

// 递归遍历目录
async function walk(dir) {
  const files = await fs.promises.readdir(dir, { withFileTypes: true });
  const result = [];

  for (const file of files) {
    const filePath = path.join(dir, file.name);
    if (file.isDirectory()) {
      result.push(...(await walk(filePath)));
    } else if (file.name.endsWith(".ipynb")) {
      result.push(filePath);
    }
  }

  return result;
}

// 转换 .ipynb 文件为 .md 文件
async function convertIpynbToMd(sourceDir) {
  const ipynbFiles = await walk(sourceDir);

  for (const filePath of ipynbFiles) {
    const mdFilePath = `${filePath.replace(".ipynb", "")}.md`;
    await execAsync(
      `jupyter nbconvert --to markdown "${filePath}" --output "${mdFilePath}"`
    );
    console.log(
      `Converted ${path.basename(filePath)} to ${path.basename(mdFilePath)}`
    );
  }
}

// 调用函数，指定源文件夹路径
convertIpynbToMd("./docs")
  .then(() => {
    console.log("All .ipynb files have been converted to .md format.");
  })
  .catch((error) => {
    console.error("Error during conversion:", error);
  });
