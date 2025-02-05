(function () {
  const initGender = () => {
    const select = document.querySelector("#userForm #gender");
    const emptyOption = window.createOptions(window.emptyOption);
    select.appendChild(emptyOption[0]);
    const options = window.createOptions(window.genderOptions);
    options.forEach((option) => {
      select.appendChild(option);
    });
  };

  const initCityCategory = () => {
    const select = document.querySelector("#userForm #cityCategory");
    const emptyOption = window.createOptions(window.emptyOption);
    select.appendChild(emptyOption[0]);
    const options = window.createOptions(window.cityOptions);
    options.forEach((option) => {
      select.appendChild(option);
    });
  };

  const initOccupation = () => {
    const select = document.querySelector("#userForm #Occupation");
    const emptyOption = window.createOptions(window.emptyOption);
    select.appendChild(emptyOption[0]);
    const options = window.createOptions(window.occupationOptions);
    options.forEach((option) => {
      select.appendChild(option);
    });
  };

  const initMaritalStatus = () => {
    const select = document.querySelector("#userForm #Marital_Status");
    const emptyOption = window.createOptions(window.emptyOption);
    select.appendChild(emptyOption[0]);
    const options = window.createOptions(window.maritalStatusOptions);
    options.forEach((option) => {
      select.appendChild(option);
    });
  };

  const initAge = () => {
    const select = document.querySelector("#userForm #Age");
    const emptyOption = window.createOptions(window.emptyOption);
    select.appendChild(emptyOption[0]);
    const options = window.createOptions(window.ageOptions);
    options.forEach((option) => {
      select.appendChild(option);
    });
  };

  const initStayInCurrentCityYears = () => {
    const select = document.querySelector(
      "#userForm #Stay_In_Current_City_Years"
    );
    const emptyOption = window.createOptions(window.emptyOption);
    select.appendChild(emptyOption[0]);
    const options = window.createOptions(window.stayInCurrentCityYearsOptions);
    options.forEach((option) => {
      select.appendChild(option);
    });
  };

  document
    .getElementById("userForm")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      const formData = new FormData(event.target);
      const data = {};
      for (const [key, value] of formData.entries()) {
        data[key] = value;
      }
      console.log(data);

      // 调用接口
      fetch("http://localhost:8081/insertData", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
        .then((response) => response.json())
        .then((res) => {
          if (res.code === 200) {
            alert(res.message);
          }
        });
    });

  initGender();
  initCityCategory();
  initOccupation();
  initMaritalStatus();
  initAge();

  initStayInCurrentCityYears();
})();
