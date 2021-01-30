function move(direction) {  
    fetch(`/move`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(direction),
        cache: "no-cache",
        headers: new Headers({"content-type": "application/json"})
    })
      .then(function (response) {
          return response.text();
      })
      .then(function (text) {
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
