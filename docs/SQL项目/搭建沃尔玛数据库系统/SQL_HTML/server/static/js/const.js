(function () {
  const createOptions = (configMap) => {
    return configMap.map((option) => {
      const optionElement = document.createElement("option");
      optionElement.value = option.value;
      optionElement.innerHTML = option.label;

      return optionElement;
    });
  };

  const ageOptions = [
    "0-17",
    "18-25",
    "26-35",
    "36-45",
    "46-50",
    "51-55",
    "55+",
  ].map((item) => ({
    value: item,
    label: item,
  }));

  const genderOptions = [
    {
      value: "M",
      label: "male",
    },
    {
      value: "F",
      label: "female",
    },
  ];

  const cityOptions = ["A", "B", "C"].map((item) => ({
    value: item,
    label: item,
  }));

  const occupationOptions = new Array(20).fill(1).map((_, key) => ({
    value: key + 1,
    label: key + 1,
  }));

  const maritalStatusOptions = [
    {
      value: "M",
      label: "married",
    },
    {
      value: "S",
      label: "single",
    },
  ];

  //   0,1,2,3,4+
  const stayInCurrentCityYearsOptions = ["0", "1", "2", "3", "4+"].map(
    (item) => ({
      value: item,
      label: item,
    })
  );

  const emptyOption = [
    {
      value: "",
      label: "Please select",
    },
  ];

  window.ageOptions = ageOptions;
  window.genderOptions = genderOptions;
  window.cityOptions = cityOptions;
  window.occupationOptions = occupationOptions;
  window.maritalStatusOptions = maritalStatusOptions;
  window.stayInCurrentCityYearsOptions = stayInCurrentCityYearsOptions;
  window.emptyOption = emptyOption;
  window.createOptions = createOptions;
})();
