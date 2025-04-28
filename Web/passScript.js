async function postData (url = '', data = {}) {
  try {
    const response  = await fetch(url , {
      method: 'POST' , 
      headers: {'Content-Type' : 'application/json'},
      body: JSON.stringify(data)
    });
    return await response.json();
  } catch(error) {
    console.error('Error' , error);
    return {error: 'Something Went Wrong!'};
  }
}

async function generatePassword() {
  const length = document.getElementById('Length').value;
  const uppercase = document.getElementById('uppercase').checked;
  const number = document.getElementById('numbers').checked;
  const special = document.getElementById('special').checked;

  const data = await postData('/generate' , {length , uppercase , number , special});
   
  const resultDiv = document.getElementById('generatedResult');

  if (data.error) {
    resultDiv.textContent = data.error;
  } else {
    resultDiv.textContent = `Password: ${data.password} | Strength: ${data.strength}`;
  }
}

async function strengthChecker () {

  const password = document.getElementById('checkPassword').value
  const data = await postData('/check' , {password});

  const checkResultDiv = document.getElementById('checkResult');
  
  if(data.error) {
    checkResultDiv.textContent = data.error;
  } else {
    checkResultDiv.textContent = `Strength: ${data.strength}`
  }
}