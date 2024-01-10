function showBoardForm(){
    const form = document.querySelector("#board_name");
    const wrapper = document.querySelector("#wrapper");
    wrapper.style.filter = "blur(5px)";
    form.style.display = "flex";
}