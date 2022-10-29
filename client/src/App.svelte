<script>
  import { Router, Route } from "svelte-navigator";
  import Home from "./lib/Home/Home.svelte";
  import Navbar from "./lib/common/Navbar.svelte";
  import Footer from "./lib/common/Footer.svelte";
  import Blog from "./lib/Blog/Blog.svelte";
  import Login from "./lib/Login/Login.svelte";
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
      <Route>not found</Route>
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
