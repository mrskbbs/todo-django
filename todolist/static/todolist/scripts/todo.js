function showNodeForm(){
    const form = document.querySelector("#node_content");
    const wrapper = document.querySelector("#wrapper");
    wrapper.style.filter = "blur(5px)";
    form.style.display = "flex";
}