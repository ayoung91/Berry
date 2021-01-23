function moveForward() {  
    fetch(`/moveForward`)
      .then(function (response) {
          return response.text();
      }).then(function (text) {
          console.log('POST response text:');
          console.log(text); 
      });
}

function turnLeft() {  
    fetch(`/turnLeft`)
      .then(function (response) {
          return response.text();
      }).then(function (text) {
          console.log('POST response text:');
          console.log(text); 
      }); 
}

function turnRight() {  
    fetch(`/turnRight`)
      .then(function (response) {
          return response.text();
      }).then(function (text) {
          console.log('POST response text:');
          console.log(text); 
      }); 
}

function moveBackward() {  
    fetch(`/moveBackward`)
      .then(function (response) {
          return response.text();
      }).then(function (text) {
          console.log('POST response text:');
          console.log(text); 
      });
}

function stopMoving() {
    fetch(`/stopMoving`)
      .then(function (response) {
          return response.text();
      }).then(function (text) {
          console.log('POST response text:');
          console.log(text); 
      });
}