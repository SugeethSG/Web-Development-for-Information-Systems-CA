import User from "../store/user";
async function login(user) {
console.log({user})
		var response = await fetch('https://sugeethsg.pythonanywhere.com/Login', {method: "POST",
    body: JSON.stringify({ "username": user.email,
    "password": user.password})});
		var result = await response.json();
    if (result.status == 200){
      let token = "123";
      let username = user.email;
      localStorage.setItem("token", token);
      localStorage.setItem("username", user.email);
      User.set({ isAuthenticated: true, token, username });
      return true;
    }
		return false;
  // let success = true;
  // let token = "123";
  // if (success) {
  //   localStorage.setItem("token", token);
  //   User.set({ isAuthenticated: true, token });
  // }
  // return success;
}

export { login };
