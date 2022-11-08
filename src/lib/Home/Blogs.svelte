<script>
  import Blog from "./Blog.svelte";
  import { getBlogs } from "../../api/blogs";
  import { onMount } from "svelte";
  export let isEditable;
  let blogs = [];
  onMount(async () => {
    blogs = await getBlogs();
  });
  async function blogDeleted() {
    blogs = await getBlogs();
  }
</script>

<section class="text-gray-600 body-font">
  <div class="container px-5 py-24 mx-auto">
    <h1
      class="sm:text-3xl text-2xl font-medium title-font text-center text-gray-900 mb-20"
      id="blogs"
    >
      My blogs
    </h1>
    <div class="flex flex-wrap -m-4">
      {#each blogs as blog (blog.id)}
        <Blog
          {isEditable}
          id={blog.id}
          img={blog.img}
          title={blog.title}
          date={blog.date}
          {blogDeleted}
        />
      {/each}
    </div>
  </div>
</section>
