funcDocs = {
  backward: {
    name: "Backward",
    desc: "Powers motor to reverse rover bot. Takes a numeric distance.",
    argc: 1
  },
  forward: {
    name: "Forward",
    desc: "Powers motor to advance rover bot. Takes a numeric distance.",
    argc: 1
  },
  turnLeft: {
    name: "Turn Left",
    desc: "Rotates 90 degrees to the left.",
    argc: 0
  },
  turnRight: {
    name: "Turn Right",
    desc: "Rotates 90 degrees to the right.",
    argc: 0
  }
}

document.getElementById("funcSel").addEventListener("change", (signal) => {
  displayDoc(signal.target.value);
  document.getElementById("push").disabled = false;
});

displayDoc = function(name) {
  docArea = document.getElementById("funcDoc");
  docArea.innerHTML = funcDocs[name].desc;
  argArea = document.getElementById("argList");
  argArea.innerHTML = "";
  for(i = 0; i < funcDocs[name].argc; i++) {
    temp = document.createElement("input");
    temp.type = "text";
    temp.className = "argv";
    argArea.innerHTML += "<label>Argument " + (i + 1) + ":</label> ";
    argArea.appendChild(temp);
  }
  return;
}

document.getElementById("push").addEventListener("click", (signal) => {
  funcName = document.getElementById("funcSel").value;
  argFlds = document.getElementsByClassName("argv");
  
  disLabel = funcName + "( ";
  for(i = 0; i < argFlds.length; i++) {
    val = argFlds[i].value;
    disLabel += (i != 0 ? ", " : "") + val + " ";
    if(isNaN(parseFloat(val))) {
      window.alert("Improper argument passed to function.");
      return;
    }
  }
  
  disLabel += ");"
  
  document.getElementById("funcSel").getElementsByTagName("option")[0].selected = true;
  
  stack = document.getElementById("stack");
  listIt = document.createElement("li");
  listIt.innerHTML = disLabel;
  stack.append(listIt);
  
  document.getElementById("push").disabled = true;
  document.getElementById("pop").disabled = false;
  document.getElementById("funcDoc").innerHTML = "Function Created";
  document.getElementById("argList").innerHTML = ""
});

document.getElementById("pop").addEventListener('click', (signal) => {
  stack = document.getElementById("stack");
  items = stack.getElementsByTagName("li");
  if(items.length > 0) {
    stack.removeChild(items[items.length - 1]);
  }
  if(items.length == 0) {
    document.getElementById("pop").disabled = true;
  }
})

document.getElementById("commit").addEventListener('click', (signal) => {
  window.alert("your bitch ass really thought this would work")
});
