<script>
  import { navigate } from "svelte-navigator";
</script>

<section class="text-gray-600 body-font">
  <div
    class="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center"
  >
    <div
      class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center"
    >
      <h1
        class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900"
      >
         IT Support Engineer
      </h1>
      <p class="mb-8 leading-relaxed">
        Hello, I am an IT Professional. 
      </p>
      <div class="flex justify-center">
        <button
          on:click={() => navigate("/blog/1", { replace: true })}
          class="inline-flex text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg"
          >Read my latest blog</button
        >
      </div>
    </div>
    <div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6">
      <img
        class="object-cover object-center rounded"
        alt="hero"
        src="https://media-exp1.licdn.com/dms/image/C5603AQHwuJeAhkDc0A/profile-displayphoto-shrink_400_400/0/1650447367710?e=1673481600&v=beta&t=_SZPeof_SYTuRzta2AI1lyEHZvwNzGPLGBz_xVodg38"
      />
    </div>
  </div>
</section>
