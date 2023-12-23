function route_getLocation() {
    return document.getElementsByClassName("current")[0];
}

// function route_showLocation() {
//     let elem = route_getLocation();
//     let bounding = elem.getBoundingClientRect();
//     if (bounding.top < 0 || bounding.left < 0 || (bounding.bottom > (window.innerHeight || document.documentElement.clientHeight)) || (bounding.right > (window.innerWidth || document.documentElement.clientWidth))) {
//         elem.scrollIntoView({
//             "smooth": true
//         });
//     }
// }

function route_getNext() {
    current = route_getLocation();
    if (current) {
        return current.nextElementSibling;
    } else {
        return null;
    }
}

function route_getPrevious() {
    current = route_getLocation();
    if (current) {
        return current.previousElementSibling;
    } else {
        return null;
    }
}

function route_setLocation(location) {
    let locations = document.getElementsByClassName("ort");
    for (let i = 0; i < locations.length; i++) {
        locations[i].classList.remove("current");
    }
    location.classList.add("current");
    document.getElementById("locationurl").href = location.getAttribute("data-url");
    document.getElementById("locationid").innerHTML = location.getAttribute("data-id");
    document.getElementById("locationname").innerHTML = location.getAttribute("data-name");
    document.getElementById("locationaddress").innerHTML = location.getAttribute("data-address");
    console.log("[Route] - Changed Location!");

    if (route_getPrevious()) {
        document.getElementById("buttonprevious").classList.remove("disabled");
    } else {
        document.getElementById("buttonprevious").classList.add("disabled");
    }
    if (route_getNext()) {
        document.getElementById("buttonnext").classList.remove("disabled");
    } else {
        document.getElementById("buttonnext").classList.add("disabled");
    }

    if (!window.matchMedia("(max-width: 600px)").matches) {
        route_getLocation().scrollIntoView();
    }
}

function route_start() {
    first = document.getElementsByClassName("ort")[0];
    if (first) {
        route_setLocation(first);
        console.info("[Route] - Started!");
    } else {
        alert("Diese Route enthält keine Ziele!");
    }
}

function route_next() {
    current = route_getLocation();
    if (current) {
        next = route_getNext();
        if (next) {
            console.log("[Route] - Next location");
            route_setLocation(next);
        } else {
            console.warn("[Route] - This was the last location!")
        }
    }
}

function route_back() {
    current = route_getLocation();
    if (current) {
        previous = route_getPrevious();
        if (previous) {
            console.log("[Route] - Previous location");
            route_setLocation(previous);
        } else {
            console.warn("[Route] - This was the first location!")
        }
    }
}

window.addEventListener("load", e => {
    route_start();
});