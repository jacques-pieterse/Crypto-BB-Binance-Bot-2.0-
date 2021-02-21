function changeForm(evt, botType) {
    // Declare all variables
    var i, selectcontent, selectlinks;
  
    // Get all elements with class="tabcontent" and hide them
    selectcontent = document.getElementsByClassName("selectcontent");
    for (i = 0; i < selectcontent.length; i++) {
      selectcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    selectlinks = document.getElementsByClassName("selectlinks");
    for (i = 0; i < selectlinks.length; i++) {
      selectlinks[i].className = selectlinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(botType).style.display = "block";
    evt.currentTarget.className += " active";
  }