// document.querySelector("body").innerHTML = location.href

let listOfImg = [
    "clothes/home_img1.jpg",
    "computure/home_img2.jpg",
    "clothes/home_img3.jpg",
    "clothes/home_img4.jpg",
    "background/eco_back_1.jpg"
]

let counImg = 1;

let btnIcon = document.querySelectorAll(".containner_slider .icon");

let imgPlaceMov = document.querySelector(".containner-back-photo")

let cont_Links = document.querySelector(".header");

let childOfTxtSlide = document.querySelector(".parentTxt");

let ContoverlayOfProduct = document.querySelectorAll(".parentOfImg .containner-img");

let overlayOfProduct = document.querySelectorAll(".parentOfImg .overlay_img");

let part_img = document.querySelectorAll(".part_img");

let watchPic = document.querySelector(".watch");

let filterBtn = document.querySelectorAll(".filter_btn_parent .btn");
let filterBox = document.querySelector(".filter_btn_parent");

let product = {

    phone: [{

        images: ["arr_img4.jpg", "g_img1.jpg", "g_img2.jpg"],
        name: "Téléphoner",
        price: [1000, 1500, 2000]

    }],
    laptop: [{

        images: ["g_img3.jpg", "g_img5.jpg", "arr_img1.jpg"],
        name: "Ordinateur Portable",
        price: [2000, 2500, 1000]

    }],
    headphone: [{

        images: ["g_img6.jpg", "g_img8.jpg", "g_img9.jpg"],
        name: "Casque De Musique",
        price: [100, 250, 200, 150]

    }],
    shoes: [{

        images: [
            "arr_img3.jpg", "buy-2.jpg", "g_img4.jpg", "g_img7.jpg",
            "product-2.jpg", "product-5.jpg"
        ],
        name: "Des Chaussures",
        price: [250, 300, 450, 150, 55, 500, 300, 1245]

    }],

    all: [{

        images: [],
        name: [],
        price: []

    }],
}

let menu = document.querySelector(".anchor .newLink");

menu.addEventListener("click", function (e) {

    if (this.classList.contains("menu")) {

        this.firstElementChild.style.display = "none"
        this.lastElementChild.style.display = "block"

        this.classList.add("remove");
        this.classList.remove("menu")

        fetshing(document.querySelector(".newparentLinks"), -50)

    } else {

        this.firstElementChild.style.display = "block"
        this.lastElementChild.style.display = "none"

        this.classList.remove("remove");
        this.classList.add("menu")

        fetshing(document.querySelector(".newparentLinks"), -225)

    }

})

// this is function fetsh the links 

function fetshing(ell, top) {

    "use strict";
    ell.style = `transform: translate(${-50}%, ${top}%);`

}
fetshing(document.querySelector(".newparentLinks"), -225)

document.querySelectorAll(".product_img .parent-content").forEach(el => {

    product.all[0].name.push(el.firstElementChild.innerHTML);
    product.all[0].images.push(el.parentElement.parentElement.firstElementChild.firstElementChild.firstElementChild.getAttribute("src"));
    product.all[0].price.push(el.parentElement.parentElement.lastElementChild
        .firstElementChild.lastElementChild.firstElementChild
        .firstElementChild.innerHTML)
})

function framing(ell) {

    "use strict";
    if (window.innerWidth > 991) {

        ell.forEach(e => {

            // e.style.width = "calc(49% - 3px)";

            if (e.classList.contains("fram-three") || e.classList.contains("fram-one")) {

                e.classList.remove("fram-three");
                e.classList.remove("fram-one");

            }

            e.classList.add("fram-one")

        })

    } else if (window.innerWidth <= 991 && window.innerWidth > 768) {

        ell.forEach(e => {

            e.classList.add("fram-three");

            if (e.classList.contains("fram-two") || e.classList.contains("fram-one")) {

                e.classList.remove("fram-two");
                e.classList.remove("fram-one");

            }

        })

    } else if (window.innerWidth < 767 && window.innerWidth > 420) {
        ell.forEach(e => {
            e.classList.add("fram-one");
            if (e.classList.contains("fram-two") || e.classList.contains("fram-three")) {

                e.classList.remove("fram-two");
                e.classList.remove("fram-three");

            }
        })

    }

}

function customWidth(len) {

    let i = 0;

    if (len == 2) {

        // for (i; i < len; i++) {

        console.log("u")

        // }

    } else {

        console.log(len)

    }

}

window.onresize = function () {

    framing(document.querySelectorAll(".product_img"))

}

document.addEventListener("click", function (e) {


    if (e.target.classList.contains("phone")) {

        document.querySelectorAll(".product_img img").forEach((el, i) => {

            el.setAttribute("src", `images/${e.target.dataset.st}/${product.phone[0].images[i]}`)
            let placeNamePro = el.parentElement.parentElement.nextElementSibling.firstElementChild.firstElementChild;
            price = el.parentElement.parentElement.nextElementSibling.firstElementChild.lastElementChild.firstElementChild.firstElementChild;

            placeNamePro.innerHTML = product.phone[0].name;
            price.innerHTML = product.phone[0].price[i] + "DH";

        })

        checking_src(document.querySelectorAll(".product_img img"), e.target.dataset.st)
        framing(document.querySelectorAll(".product_img"), product.phone[0].images)

    } else if (e.target.classList.contains("laptop")) {

        document.querySelectorAll(".product_img img").forEach((el, i) => {

            el.setAttribute("src", `images/${e.target.dataset.st}/${product.laptop[0].images[i]}`)
            let placeNamePro = el.parentElement.parentElement.nextElementSibling.firstElementChild.firstElementChild;
            price = el.parentElement.parentElement.nextElementSibling.firstElementChild.lastElementChild.firstElementChild.firstElementChild;

            placeNamePro.innerHTML = product.laptop[0].name;
            price.innerHTML = product.laptop[0].price[i] + "DH";

        })

        checking_src(document.querySelectorAll(".product_img img"), e.target.dataset.st)
        framing(document.querySelectorAll(".product_img"), product.laptop[0].images)

    } else if (e.target.classList.contains("headphone")) {

        framing(document.querySelectorAll(".product_img"), product.headphone[0].images)

        document.querySelectorAll(".product_img img").forEach((el, i) => {

            el.setAttribute("src", `images/${e.target.dataset.st}/${product.headphone[0].images[i]}`)
            let placeNamePro = el.parentElement.parentElement.nextElementSibling.firstElementChild.firstElementChild;
            price = el.parentElement.parentElement.nextElementSibling.firstElementChild.lastElementChild.firstElementChild.firstElementChild;

            placeNamePro.innerHTML = product.headphone[0].name;
            price.innerHTML = product.headphone[0].price[i] + "DH";
        })

        checking_src(document.querySelectorAll(".product_img img"), e.target.dataset.st)

    } else if (e.target.classList.contains("shoes")) {

        document.querySelectorAll(".product_img img").forEach((el, i) => {

            el.setAttribute("src", `images/${e.target.dataset.st}/${product.shoes[0].images[i]}`)

            let placeNamePro = el.parentElement.parentElement.nextElementSibling.firstElementChild.firstElementChild;
            price = el.parentElement.parentElement.nextElementSibling.firstElementChild.lastElementChild.firstElementChild.firstElementChild;

            placeNamePro.innerHTML = product.shoes[0].name;
            price.innerHTML = product.shoes[0].price[i] + "DH";

        })
        checking_src(document.querySelectorAll(".product_img img"), e.target.dataset.st)
        framing(document.querySelectorAll(".product_img"), product.shoes[0].images)


    } else if (e.target.classList.contains("all")) {


        document.querySelectorAll(".product_img img").forEach((el, i) => {

            el.setAttribute("src", `${product.all[0].images[i]}`)

            let price = el.parentElement.parentElement.nextElementSibling.firstElementChild.lastElementChild.firstElementChild.firstElementChild;
            let title = el.parentElement.parentElement.nextElementSibling.firstElementChild.firstElementChild
            price.innerHTML = product.all[0].price[i] + "DH";
            title.innerHTML = product.all[0].name[i];

        })
        checking_src(document.querySelectorAll(".product_img img"), e.target.dataset.st)
        framing(document.querySelectorAll(".product_img"), product.all[0].images)

    }
})


function checking_src(allEll, dt) {

    allEll.forEach(el => {

        if (el.getAttribute("src") == `images/${dt}/undefined`) {

            el.parentElement.parentElement.parentElement.style.display = "none"
            // console.log(el.getAttribute("src"))

        } else {

            el.parentElement.parentElement.parentElement.style.display = "block"

        }

    })

}
function checking_product(product, e) {

    if (product.length > 1) {

        product.forEach(pro => {

            if (pro.dataset.st == e) {

                console.log(pro)

            } else {

                pro.remove()


            }

        })


    }
}





// this is function making star and append it in product images 
function creatingStar(place) {

    "use strict";
    let i = 0;
    for (i = 0; i < 5; i++) {

        let crSpn = document.createElement("span");
        let crSpnChild = document.createElement("span");
        let crIcon = document.createElement("i");
        crIcon.className = "fa fa-star";
        crSpnChild.appendChild(crIcon);
        crSpn.appendChild(crSpnChild);
        place.appendChild(crSpn);

    }

}



// this function make hover the overLay For picture 

function hover(loopEll) {

    "use strict";
    loopEll.forEach(el => {

        el.addEventListener("click", function (e) {

            // if (this.className != 'active') {

            //     return false;

            // }
            removing(ContoverlayOfProduct)
            removing(overlayOfProduct)
            removing(part_img)
            removing(filterBtn)

            this.classList.add("active");
            this.lastElementChild.classList.add("active")
            watchPic.firstElementChild.setAttribute("src", e.target.getAttribute("src"))

        })

    })

}
hover(ContoverlayOfProduct)
hover(part_img)
hover(filterBtn)

// this is function make fishing a new silder 

function fitshing(ellChild, ell) {

    "use strict";

    removing(document.querySelectorAll(".txt_slider"))
    removeByPosition(document.querySelectorAll(".txt_slider"))
    ell.children[ellChild].classList.add('active')
    if (ell.children[ellChild].classList.contains("active")) {

        ell.children[ellChild].style = `transform: translateX(${0}%);`

    }
    // console.log()

}

function removeByPosition(all) {

    all.forEach(al => {

        al.style = `transform: translateX(${110}%);`

    })

}

// console.log(childOfTxtSlide.children)
// console.log(childOfTxtSlide.children[0])

// this is function make scrolling
function scrooling(num) {

    "use strict";
    document.onscroll = function () {

        cont_Links.style = `position: fixed; top: ${num} px; `

    }

}

// when scrolling 

let positionEll = [0, 1285, 2005, 2525];

window.onscroll = function () {

    scrooling(scrollNum = 0)
    hidding(document.querySelector(".navBar"));

    // console.log(window.scrollY)
    if (window.scrollY === 0) {

        showing(document.querySelector(".navBar"));
        cont_Links.style = `position: fixed; top: ${25} px; `

    }
    // console.log(window.scrollY)

}

document.onload = scrooling(scrollNum = 0)

function comparing(allE, num) {

    allE.forEach(el => {

        if (el.dataset.scroll == num) {

            console.log(el)

        }

    })


}
comparing(document.querySelectorAll(".scroll"), 0)


// this is function moving the picture 

function moving(ell, src) {

    "use strict";
    ell.style.backgroundImage = `url(images/${src})`

}

// this is fuction make visavlity or showing ellemment

function showing(ell) {

    "use strict";
    ell.style.display = "block";

}

// this is fuction make dispaly or hidding ellemment

function hidding(ell) {

    "use strict";
    ell.style.display = "none";

}

// this is fuction make checking the coutImg 

function checking(numOfImg) {

    "use strict";
    if (numOfImg === (listOfImg.length - 1)) {

        console.log("max_num ", numOfImg)

        // hidding icon right function 
        hidding(document.querySelector(".containner_slider .items_right"))

        // shown icon left function 
        showing(document.querySelector(".containner_slider .items_left"))

    } else if (numOfImg < 1) {

        console.log("min_num ", numOfImg)

        // hidding icon left function 
        hidding(document.querySelector(".containner_slider .items_left"))

        // show icon right function 
        showing(document.querySelector(".containner_slider .items_right"))

    } else {

        showing(document.querySelector(".containner_slider .items_right"))
        showing(document.querySelector(".containner_slider .items_left"))


    }
}

// this is function moving the images 

function couting() {

    "use strict";
    btnIcon.forEach(btn => {

        btn.addEventListener("click", function (bt) {

            if (this.classList.contains("items_right")) {

                console.log("R-", counImg)

                // checking function 
                checking(counImg)

                // moving function 
                moving(imgPlaceMov, listOfImg[counImg])

                // fitshing function 
                fitshing(counImg, childOfTxtSlide)
                // buttun right click 
                counImg += 1;


            } else {

                console.log("L-", counImg)
                // button left click 
                counImg -= 1;

                // checking function 
                checking(counImg)

                // moving function 
                moving(imgPlaceMov, listOfImg[counImg])

                // fitshing function 
                fitshing(counImg, childOfTxtSlide)


            }


        })

    })
}
couting()

let links = document.querySelectorAll(".links li a");

// this is function remove all active 
function removing(ell) {

    "use strict";

    ell.forEach(el => {

        el.classList.remove("active");

    })

}

links.forEach(btn => {

    btn.addEventListener("click", function (b) {

        removing(links)
        b.target.classList.add('active');

    })

})