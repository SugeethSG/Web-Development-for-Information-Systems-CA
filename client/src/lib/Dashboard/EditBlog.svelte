<script>
  import { onMount } from "svelte";
  import { navigate } from "svelte-navigator";
  import { editBlog, addBlog, getBlog } from "../../api/blogs";
  export let id;
  let simplemde;
  let blog = {
    title: "",
    img: "",
    content: "",
  };
  onMount(async () => {
    simplemde = new SimpleMDE({ element: document.getElementById("md") });
    if (id !== null) {
      blog = await getBlog(id);
      // console.log({id});
      // console.log({blog});
      simplemde.value(blog.content);
    }
  });
  async function submit() {
    blog.content = simplemde.value();
    if (id !== null) {
      await editBlog(blog);
      navigate("/dashboard", { replace: true });
    } else {
      await addBlog(blog);
      navigate("/dashboard", { replace: true });
    }
  }
</script>

<div class="container px-5 py-24 mx-auto">
  <div class="mb-6">
    <label for="title" class="block mb-2 text-sm font-medium text-gray-900"
      >Blog Title</label
    >
    <input
      type="text"
      id="title"
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
      placeholder="Daily dev tips"
      required
      bind:value={blog.title}
    />
  </div>
  <div class="mb-6">
    <label for="image" class="block mb-2 text-sm font-medium text-gray-900"
      >Blog Image</label
    >
    <input
      type="text"
      id="image"
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
      placeholder="https://dummyimage.com/423x263"
      required
      bind:value={blog.img}
    />
  </div>
  <textarea name="md" id="md" />
  <button
    on:click={submit}
    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full px-5 py-2.5 text-center"
    >Submit</button
  >
</div>
