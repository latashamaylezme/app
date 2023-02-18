

// input box 222222222222222
loginForm.addEventListener("input",()=>{
  

  if(password.value.length >1){
    show_hidee.textContent = "Minimum 8 characters";
    show_hidee.style.color = "red";
    under.style.color = "red";
    
  }if(password.value.length >7){
    show_hidee.textContent = "password are case-sensitiv";
    show_hidee.style.color = "rgba(0, 0, 0, 0.54)";
    under.style.color = "#4f6df5";
    
  }
  if(password.value.length <0){
        show_hidee.textContent = "Required";
      show_hidee.style.color = "red";
    
  }

    else{
      // show_hidee.textContent = "Required";
      // show_hidee.style.color = "red";
      }

});








// password FileSystemDirectoryEntry

  loginForm.addEventListener("input", () =>{
  if (Name.value.length >0 && password.value.length >8){
    submit.removeAttribute("disabled");
    
  }

  else{
    submit.setAttribute("disabled", "disabled")
  }
});

   




// scrol|??
