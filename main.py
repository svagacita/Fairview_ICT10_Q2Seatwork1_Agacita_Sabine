from pyscript import document

members = ("Sabine Agacita", "Rodolfo Lao", "Raven Denum", "Maria Coronel", "Lance Catu", "Rohan Tabasan")

def verify(event):
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    fullname = fname + " " + lname
    result = fullname in members

    congrats = {
        True: "Congratulations, " + fullname + "! You are part of the SocSci club.",
        False: "Sorry " + fullname + ", your name is not on the list."
    }

    document.getElementById("result").innerText = congrats[result]