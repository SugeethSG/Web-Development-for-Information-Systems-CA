import { writable } from "svelte/store";

const user = writable({ isAuthenticated: false, token: "", username:"" });

export default user;
