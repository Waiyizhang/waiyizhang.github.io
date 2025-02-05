import { defineConfig } from "vitepress";
import { generateSidebar } from "vitepress-sidebar";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: process.env.NODE_ENV === 'production' ? '/waiyizhang.github.io/' : '/',
  title: "Waiyizhang",
  description: "A VitePress Site",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "Home", link: "/" },
      { text: "Examples", link: "/markdown-examples" },
    ],

    sidebar: generateSidebar({
      documentRootPath: "/docs", // 指定文档根目录
      useTitleFromFileHeading: true, // 使用文件中的标题作为侧边栏标题
      useFolderTitleFromIndexFile: true, // 使用文件夹中的 `index.md` 文件作为标题
      sortMenusByFrontmatterOrder: true, // 根据 frontmatter 中的 order 字段排序
      collapsed: false,
      collapseDepth: 2,
      manualSortFileNameByPriority: ["header.md"],
    }),

    socialLinks: [
      { icon: "github", link: "https://github.com/vuejs/vitepress" },
    ],
  },
  vite: {
    plugins: [],
  },
});
