const dltButton = document.querySelector("#delete_btn");

dltButton.addEventListener("click", async () => {
  const input = document.querySelector("#id");

  const ids = input.value
    .split(",")
    .map((id) => id.trim())
    .filter((id) => id !== "")
    .map(Number);
  let response = await fetch("/delete", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ ids: ids }),
  });

  response = await response.json();
  alert(response.message);
  window.location.reload();
});
document.querySelector("#create_btn").addEventListener("click", () => {
  window.location.href = "/form";
});

document.querySelector("#update_btn").addEventListener("click", () => {
  window.location.href = "/update";
});
