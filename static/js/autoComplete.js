function autocomplete(inp, arr) {
    var currentFocus;
    inp.addEventListener("input", (e) => {
        let wrapper,
            same,
            re,
            val = inp.value,
            notsame = 0;
        closeAllLists();
        if (!val) {
            return false;
        }
        currentFocus = -1;
        wrapper = document.createElement("DIV");
        wrapper.setAttribute("id", "autocomplete_lists");
        wrapper.setAttribute("class", "autocomplete-lists");
        inp.parentNode.appendChild(wrapper);
        re = new RegExp(`${val}`, "gi");
        for (let idx = 0; idx < arr.length; idx++) {
            if (arr[idx].match(re)) {
                same = document.createElement("P");
                same.setAttribute("class", "autocomplete-item");
                same.innerHTML = arr[idx];
                wrapper.appendChild(same);
                same.addEventListener("click", (e) => {
                    inp.value = arr[idx];
                    inp.focus();
                    closeAllLists();
                });
            } else {
                notsame++;
            }
        }
        if (notsame === arr.length) {
            same = document.createElement("P");
            same.setAttribute("class", "not-autocomplete");
            same.innerHTML = "Tidak ada data tersebut";
            wrapper.appendChild(same);
        }
    });
    inp.addEventListener("keydown", (e) => {
        let elem = document.querySelector(".autocomplete-lists");
        if (elem) {
            elem = elem.querySelectorAll(".autocomplete-item");
        }
        if (e.keyCode == 40) {
            currentFocus++;
            addActive(elem)
        } else if (e.keyCode == 38) {
            currentFocus--;
            addActive(elem);
        } else if (e.keyCode == 13) {
            e.preventDefault();
            if (currentFocus > -1) {
                if (elem) elem[currentFocus].click();
            }
        }
    })

    function addActive(elem) {
        if (!elem) return false;
        removeActive(elem);
        if (currentFocus >= elem.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = elem.length - 1;
        elem[currentFocus].classList.add("autocomplete-active");
    }

    function removeActive(elem) {
        for (let i = 0; i < elem.length; i++) {
            elem[i].classList.remove("autocomplete-active");
        }
    }

    function closeAllLists() {
        var x = document.querySelector(".autocomplete-lists");
        if (x) {
            x.remove();
        }
    }
    document.addEventListener("click", (e) => {
        closeAllLists();
    });
}