function previewFile() {
  const file = document.querySelector('input[type=file]').files[0];
  const preview = document.getElementById('image-preview');
  const img = document.getElementById('preview-thumb');

  if (file && file.type.startsWith("image")) {
    const reader = new FileReader();
    reader.onloadend = () => {
      img.src = reader.result;
      preview.style.display = 'block';
    };
    reader.readAsDataURL(file);
  } else {
    preview.style.display = 'none';
  }
}

document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');
  form.addEventListener('submit', function () {
    const loader = document.getElementById('loader');
    if (loader) loader.style.display = 'block';
  });
});
