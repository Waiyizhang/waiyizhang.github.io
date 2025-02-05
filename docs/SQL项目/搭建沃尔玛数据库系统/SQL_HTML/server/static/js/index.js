(function () {
  document.getElementById("SearchBtn").addEventListener("click", function () {
    // 点击滑动到 #Search内容
    document.getElementById("Search").scrollIntoView({
      behavior: "smooth",
    });
  });
  document.getElementById("EditBtn").addEventListener("click", function () {
    // 点击滑动到 #Search内容
    document.getElementById("Edit").scrollIntoView({
      behavior: "smooth",
    });
  });
})();
