from pyscript import window, document
#my_element = document.querySelector("#my-id")
#my_element.innerText = window.location.hostname
content = document.querySelector(".form_container")
content.style.display = 'block'

def dosomething(event):
    print("Button clicked!")

def doLogin(event):
    print("login clicked")
    email = document.querySelector("#email").value
    password = document.querySelector("#password").value
    print("email : ",email)
    print("password :",password)
    result = document.querySelector(".result")
    result.innerHTML = f'<h3>Your {email= } and {password= } </h3>'
    result.style.color=r'red'
