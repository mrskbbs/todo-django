function showNodeForm(){
    const form = document.querySelector("#node_content");
    const wrapper = document.querySelector("#wrapper");
    wrapper.style.filter = "blur(5px)";
    form.style.display = "flex";
}
function saveNodes(){
    const form = document.querySelector("#node-list");
    const exit = document.createElement("input");
    exit.type = "text";
    exit.name = "exit";
    form.appendChild(exit);
    form.submit();
}
function deleteNode(object){
    const input = document.createElement("input");
    const form = document.querySelector("#node-list");
    input.type = "text";
    input.name = "delete";
    input.value = object.id.split("_")[1];
    input.style.display = "none";
    object.parentElement.prepend(input);    
    form.submit();
}
function createNode(){
    const form = document.querySelector("#node-list");
    form.submit();
}