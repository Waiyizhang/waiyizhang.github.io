<template>
  <div v-html="htmlContent"></div>
</template>

<script>
export default {
  props: {
    src: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      htmlContent: "",
    };
  },
  async mounted() {
    try {
      // 使用 fetch 加载本地 HTML 文件
      const response = await fetch(this.src);
      const html = await response.text();
      this.htmlContent = html;
      console.log("HTML content loaded:", html);
    } catch (error) {
      console.error("Failed to load HTML content:", error);
      this.htmlContent = "<p>Failed to load content.</p>";
    }
  },
};
</script>
