<script>
  import { Router, Route, navigate } from "svelte-navigator";
  import Blogs from "../Home/Blogs.svelte";
  import EditBlog from "./EditBlog.svelte";
</script>

<Router>
  <Route path="/edit/:id" let:params><EditBlog id={params.id} /></Route>
  <Route path="/add"><EditBlog id={null} /></Route>
  <Route
    ><Blogs isEditable />
    <button
      class="flex ml-auto text-white bg-green-500 border-0 py-2 px-6 focus:outline-none hover:bg-green-600 rounded"
      on:click={() => navigate("/dashboard/add", { replace: true })}>Add</button
    ></Route
  >
</Router>
