const imgs = Array.from(document.querySelectorAll("img"));
const bullets = Array.from(document.querySelectorAll(".bullet"));
const controlBox = document.querySelector(".control");
const form = document.querySelector("form");
const submit = document.querySelector(".submit");
const submitBtnTxt = document.querySelector(".submit .txt");
const submitBtnSpinner = document.querySelector(".submit .spinner");
let interval;
let idx = 0;

// Slider
const activeImg = idx => {
  for (const img of imgs) {
    img.classList.remove("active");
  }
  imgs[idx].classList.add("active");
};
const activeBullets = idx => {
  for (const bullet of bullets) {
    bullet.classList.remove("active");
  }
  bullets[idx].classList.add("active");
};

const autoPlay = () => {
  interval = setInterval(() => {
    if (idx === imgs.length) {
      idx = 0;
    }

    activeImg(idx);
    activeBullets(idx);

    idx++;
  }, 6000);
};

bullets.forEach((bullet, _idx) => {
  bullet.addEventListener("click", e => {
    activeImg(_idx);
    activeBullets(_idx);
    idx = _idx;
  });
});

controlBox.addEventListener("mouseenter", () => {
  clearInterval(interval);
});
controlBox.addEventListener("mouseleave", () => {
  autoPlay();
});

autoPlay();

// Form
form.addEventListener("submit", e => {
  e.preventDefault();
  submitBtnTxt.style.display = "none";
  submitBtnSpinner.style.display = "initial";
  submit.classList.add("disabled");
  form.reset();

  setTimeout(() => {
    submitBtnTxt.style.display = "initial";
    submitBtnSpinner.style.display = "none";
    submit.classList.remove("disabled");
  }, 5000);
});