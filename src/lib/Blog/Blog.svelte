<script>
  import { getBlog } from "../../api/blogs";
  import { onMount } from "svelte";
  export let id;

  let blog;
  onMount(async () => {
    blog = await getBlog(id);
    let converter = new showdown.Converter();
    blog.content = converter.makeHtml(blog.content);
  });

  function handleImgError(blog){
    //blog.img = 'https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png';
  }
</script>

<main class="pt-8 pb-16 lg:pt-16 lg:pb-24 bg-white">
  <div class="flex justify-between px-4 mx-auto max-w-screen-xl">
    <article
      class="mx-auto w-full max-w-2xl format format-sm sm:format-base lg:format-lg format-blue"
    >
      {#if blog}
        <header class="mb-4 lg:mb-6 not-format">
          <address class="flex items-center mb-6 not-italic">
            <div class="inline-flex items-center mr-3 text-sm text-gray-900">
              <img
                class="mr-4 w-16 h-16 rounded-full"
                src="https://media-exp1.licdn.com/dms/image/C5603AQHwuJeAhkDc0A/profile-displayphoto-shrink_400_400/0/1650447367710?e=1673481600&v=beta&t=_SZPeof_SYTuRzta2AI1lyEHZvwNzGPLGBz_xVodg38"
                alt="Sugeeth"
              />
              <div>
                <a href="/" rel="author" class="text-xl font-bold text-gray-900"
                  >Sugeeth</a
                >
                <p class="text-base font-light text-gray-500">
                  IT Professional
                </p>
                <p class="text-base font-light text-gray-500">
                  {blog.date}
                </p>
              </div>
            </div>
          </address>
          <h1
            class="mb-4 text-3xl font-extrabold leading-tight text-gray-900 lg:mb-6 lg:text-4xl"
          >
            {blog.title}
          </h1>
        </header>
        <figure>
          <img class="m-auto" src={blog.img} alt="" />
        </figure>
        {@html blog.content}
      {:else}
        <div class="text-center">
          <div role="status">
            <svg
              class="inline mr-2 w-8 h-8 text-gray-200 animate-spin fill-blue-600"
              viewBox="0 0 100 101"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                fill="currentColor"
              />
              <path
                d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                fill="currentFill"
              />
            </svg>
            <span class="sr-only">Loading...</span>
          </div>
        </div>
      {/if}
    </article>
  </div>
</main>
