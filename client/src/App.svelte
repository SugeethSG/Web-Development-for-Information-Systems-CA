<script>
  import { onMount } from "svelte";
  import { Router, Route } from "svelte-navigator";
  import user from "./store/user";
  import Home from "./lib/Home/Home.svelte";
  import Navbar from "./lib/common/Navbar.svelte";
  import Footer from "./lib/common/Footer.svelte";
  import Blog from "./lib/Blog/Blog.svelte";
  import Login from "./lib/Login/Login.svelte";
  import Dashboard from "./lib/Dashboard/Dashboard.svelte";
  import PrivateRoute from "./lib/common/PrivateRoute.svelte";

  onMount(() => {
    let token = localStorage.getItem("token");
    if (token !== null) {
      $user.isAuthenticated = true;
      $user.token = token;
    }
  });
</script>

<Router primary={false}>
  <Navbar />
  <main>
    <div>
      <Route path="/"><Home /></Route>
      <Route path="blog/:id" let:params>
        <Blog id={params.id} />
      </Route>
      <Route path="login"><Login /></Route>
      <Route path="dashboard/*"><PrivateRoute Component={Dashboard} /></Route>
      <Route
        ><section class="bg-white">
          <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
            <div class="mx-auto max-w-screen-sm text-center">
              <h1
                class="mb-4 text-7xl tracking-tight font-extrabold lg:text-9xl text-primary-600"
              >
                404
              </h1>
              <p
                class="mb-4 text-3xl tracking-tight font-bold text-gray-900 md:text-4xl"
              >
                Something's missing.
              </p>
              <p class="mb-4 text-lg font-light text-gray-500">
                Sorry, we can't find that page. You'll find lots to explore on
                the home page.
              </p>
            </div>
          </div>
        </section></Route
      >
    </div>
  </main>
  <Footer />
</Router>

<style>
  main {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 80vh;
  }
</style>
