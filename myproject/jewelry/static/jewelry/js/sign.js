const forms = document.querySelector(".forms"),
pwShowHide = document.querySelectorAll(".eye-icon"),
links = document.querySelectorAll(".link");

pwShowHide.forEach(eyeIcon => {
eyeIcon.addEventListener("click", () => {
  let pwField = eyeIcon.previousElementSibling;
  if (pwField.type === "password") {
      pwField.type = "text";
      eyeIcon.classList.replace("bx-hide", "bx-show");
  } else {
      pwField.type = "password";
      eyeIcon.classList.replace("bx-show", "bx-hide");
  }
});
});

links.forEach(link => {
link.addEventListener("click", e => {
  e.preventDefault(); //preventing form submit
  forms.classList.toggle("show-signup");
});
});