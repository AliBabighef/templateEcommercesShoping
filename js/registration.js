// const { sign } = require("crypto");

let allInput = document.querySelectorAll(".formContainner input");
let containnerForm = document.querySelector(".formContainner");

let allImges = document.querySelectorAll(".image-con img");

let signUp = document.querySelector(".register");

let signIn = document.querySelector(".log_in");

let containner = document.querySelector(".containner");

let conFormL = document.querySelector(".logLeft");
let conFormR = document.querySelector(".logRight");

let floatRight = document.querySelector(".floatRight");
let floatLeft = document.querySelector(".floatLeft");

let svgElL = document.querySelector(".floatLeft");
let svgER = document.querySelector(".floatRight");

let svgEll = document.querySelector(".con-svg");
let svgEllChild = document.querySelector(".con-svg .svg");

console.log(signIn)

function clicking(event) {

    "use strict";


    event.addEventListener("click", function () {
        if (event.className == "sign_up register") {

            containner.classList.toggle("active");
            floatLeft.classList.toggle("active");
            floatRight.classList.toggle("active")
            conFormR.classList.add("active");
            conFormL.classList.remove("active");
            svgEll.classList.toggle("trans");
            svgEllChild.classList.toggle("trans");
            containnerForm.classList.toggle("trans");

        } else if (event.className == "sign_up log_in") {

            containner.classList.toggle("active");
            floatRight.classList.toggle("active");
            floatLeft.classList.toggle("active");
            conFormL.classList.add("active");
            conFormR.classList.remove("active");
            svgEll.classList.toggle("trans");
            svgEllChild.classList.toggle("trans");
            containnerForm.classList.toggle("trans");

        } else {

            return false;

        }


    })




}

clicking(signUp)
clicking(signIn)

function addingClass() {

    for (let l = 0; l < allInput.length, l < allImges.length; l++) {

        allInput[l].addEventListener("click", function (e) {

            e.stopPropagation();

            removingAllClass(allImges);

            if (e.target.name === allImges[l].dataset.st) {

                allImges[l].classList.add("active");


            } else {

                return false;

            }

        })
    }

    document.addEventListener("click", function () {

        removingAllClass(allImges);

    })

}
addingClass(allInput)

function removingAllClass(elRm) {

    elRm.forEach(eR => {

        eR.classList.remove("active");


    });

}

// cheicking and matching if datset of input equal className of images
