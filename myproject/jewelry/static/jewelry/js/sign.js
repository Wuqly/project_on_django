document.addEventListener("DOMContentLoaded", () => {
  const pwShowHide = document.querySelectorAll(".eye-icon");

  pwShowHide.forEach(eyeIcon => {
      eyeIcon.addEventListener("click", () => {
          let pwField = eyeIcon.previousElementSibling.querySelector("input");
          if (pwField.type === "password") {
              pwField.type = "text";
              eyeIcon.classList.replace("bx-hide", "bx-show");
          } else {
              pwField.type = "password";
              eyeIcon.classList.replace("bx-show", "bx-hide");
          }
      });
  });
});
