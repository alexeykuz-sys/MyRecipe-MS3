 document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll(".sidenav");
    var instances = M.Sidenav.init(elems, {edge: 'right'});
  });

  
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
  });

   document.addEventListener('DOMContentLoaded', function () {
    let sidenavs = document.querySelectorAll(".sidenav");
    let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right"});
    let collapsibles = document.querySelectorAll(".collapsible");
    let collapsiblesInstance = M.Collapsible.init(collapsibles);
    let tooltips = document.querySelectorAll(".tooltipped");
    let tooltipsInstance = M.Tooltip.init(tooltips);
    let selects = document.querySelectorAll("select");
    let selectsInstance = M.FormSelect.init(selects);
    let datepickers = document.querySelectorAll(".datepicker");
    let datepickersInstance = M.Datepicker.init(datepickers, {
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = "border-bottom: 1px solid #4caf50; box-shadow: 0 1px 0 0 #4caf50;";
        let classInvalid = "border-bottom: 1px solid #f44336; box-shadow: 0 1px 0 0 #f44336;";
        let selectValidate = document.querySelector("select.validate");
        let selectWrapperInput = document.querySelector(".select-wrapper input.select-dropdown");
        if (selectValidate.hasAttribute("required")) {
            selectValidate.style.cssText = "display: block; height: 0; padding: 0; width: 0; position: absolute;";
        }
        selectWrapperInput.addEventListener("focusin", (e) => {
            e.target.parentNode.addEventListener("change", () => {
                ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
                for (let i = 0; i < ulSelectOptions.length; i++) {
                    if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled") {
                        e.target.style.cssText = classValid;
                    }
                }
            });
        });
        selectWrapperInput.addEventListener("click", (e) => {
            ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
            for (let i = 0; i < ulSelectOptions.length; i++) {
                if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled" && ulSelectOptions[i].style.backgroundColor == "rgba(0, 0, 0, 0.03)") {
                    e.target.style.cssText = classValid;
                } else {
                    e.target.addEventListener("focusout", () => {
                        if (e.target.parentNode.childNodes[3].hasAttribute("required")) {
                            if (e.target.style.borderBottom != "1px solid rgb(76, 175, 80)") {
                                e.target.style.cssText = classInvalid;
                            }
                        }
                    });
                }
            }
        });
    }
});

// var deleteLinks = document.querySelectorAll('.delete-btn');

// for (var i = 0; i < deleteLinks.length; i++) {
//   deleteLinks[i].addEventListener('click', function(event) {
//       event.preventDefault();

//       var choice = confirm(this.getAttribute('data-confirm'));

//       if (choice) {
//         window.location.href = this.getAttribute('href');
//       }
//   });
// }

var modalBtn = document.getElementById('modal-btn');
var modalCloseBtn = document.getElementById('modal-close');
var modal = document.querySelector('.modal-delete');

function modalHandler(){
    modal.classList.add('show')
}
modalBtn.addEventListener('click', modalHandler);


function modalClose(){
    modal.classList.remove('show');
}
modalCloseBtn.addEventListener('click', modalClose);