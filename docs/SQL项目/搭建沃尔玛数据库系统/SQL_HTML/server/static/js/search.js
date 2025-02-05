(function () {
  let typeValue = "";
  let secondTypeValue = "";
  let dataTypeValue = "";

  const SalesSecondOptionMap = [
    {
      value: "fetch_gender_purchase_count",
      label: "By gender",
      children: window.genderOptions,
    },
    {
      value: "fetch_age_group_purchase_count",
      label: "By age",
      children: window.ageOptions,
    },
    {
      value: "get_city_category_purchases",
      label: "By city",
      children: window.cityOptions,
    },
    {
      value: "get_occupation_preference",
      label: "By occupation",
      children: window.occupationOptions,
    },
    {
      value: "get_marital_status_preference",
      label: "By marriage",
    },
    {
      value: "get_stay_duration_purchases",
      label: "By duration",
    },
  ];

  const PreferenceSecondOptionMap = [
    {
      value: "get_product_category_purchases",
      label: "By category",
    },
  ];

  const getValueOptionMap = (e) =>
    ({ sales: SalesSecondOptionMap, preference: PreferenceSecondOptionMap }[
      e
    ] || "");

  //  缓存二级联动的option
  const SalesSecondOption = window.createOptions(SalesSecondOptionMap);
  const categorySecondOption = window.createOptions(PreferenceSecondOptionMap);

  const typeChangeHandle = (e) => {
    const value = e.target.value;
    typeValue = value;

    const select = document.querySelector("#SecondOptions");

    select.innerHTML = "";
    // 二级联动
    const emptyOption = window.createOptions(window.emptyOption);
    if (value === "sales") {
      select.appendChild(emptyOption[0]);
      SalesSecondOption.forEach((option) => {
        select.appendChild(option);
      });
    } else if (value === "preference") {
      select.appendChild(emptyOption[0]);

      categorySecondOption.forEach((option) => {
        select.appendChild(option);
      });
    } else {
      if (value === "get_top_selling_products") {
        submitHandle("get_top_selling_products");
      }
    }

    // 清空三级联动内容
    document.querySelector("#DataOptions").innerHTML = "";
    dataTypeValue = "";
  };

  const secondTypeChangeHandle = (e) => {
    const value = e.target.value;
    secondTypeValue = value;

    const optionMap = getValueOptionMap(typeValue);
    if (!optionMap) {
      return;
    }
    // optionMap找到对应的option配置
    const currentOption = optionMap.find((option) => option.value === value);
    const children = currentOption.children || [];
    const optionElements = window.createOptions(children);

    const select = document.querySelector("#DataOptions");
    select.innerHTML = "";
    const emptyOption = window.createOptions(window.emptyOption);

    select.appendChild(emptyOption[0]);
    optionElements.forEach((option) => {
      select.appendChild(option);
    });
  };

  const dataChangeHandle = (e) => {
    dataTypeValue = e.target.value;
    submitHandle();
  };

  const submitHandle = (type) => {
    const data = type
      ? {
          type: type,
          params: "",
        }
      : {
          type: secondTypeValue,
          params: dataTypeValue || "",
        };

    // 调用接口
    fetch("http://localhost:8081/searchType", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((res) => {
        if (res.code === 200) {
          const data = res.data;
          document.querySelector("#resolve").style.display = "block";
          // chart加载背景图
          document.querySelector("#chart").style.backgroundImage =
            "url(" + data.image + ")";
          document.querySelector("#summary").innerHTML = data.summary;
        }
      });
  };
  const init = () => {
    document
      .querySelector("#typeOptions")
      .addEventListener("change", typeChangeHandle);

    document
      .querySelector("#SecondOptions")
      .addEventListener("change", secondTypeChangeHandle);

    document
      .querySelector("#DataOptions")
      .addEventListener("change", dataChangeHandle);
  };

  init();
})();
