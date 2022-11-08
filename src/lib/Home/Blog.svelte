<script>
  import { Link, navigate } from "svelte-navigator";
  import { deleteBlog } from "../../api/blogs";
  export let id;
  export let img;
  export let title;
  export let date;
  export let isEditable;
  export let blogDeleted;

  async function deleteblog() {
    await deleteBlog(id);
    blogDeleted();
  }
</script>

<div class="lg:w-1/4 md:w-1/2 p-4 w-full">
  <Link class="block relative h-48 rounded overflow-hidden" to="/blog/{id}">
    <img
      alt="ecommerce"
      class="object-cover object-center w-full h-full block"
      src={img}
    />
  </Link>
  <div class="mt-4">
    <h2 class="text-gray-900 title-font text-lg font-medium">
      {title}
    </h2>
    <p class="mt-1">{date}</p>
  </div>
  {#if isEditable}
    <div style="display: flex;justify-content:space-between">
      <button
        class="flex text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded"
        on:click={() => navigate(`/dashboard/edit/${id}`, { replace: true })}
        >Edit</button
      >
      <button
        class="flex text-white bg-red-500 border-0 py-2 px-6 focus:outline-none hover:bg-red-600 rounded"
        on:click={deleteblog}>Delete</button
      >
    </div>
  {/if}
</div>
