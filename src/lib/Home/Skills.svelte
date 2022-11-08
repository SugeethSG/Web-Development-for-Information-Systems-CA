<script>
  import designer from "../../assets/Images/designer.svg";
  import backend from "../../assets/Images/backend.svg";
  import frontend from "../../assets/Images/frontend.svg";
</script>

<section class="text-gray-600 body-font">
  <div class="container px-5 py-24 mx-auto">
    <h1
      class="sm:text-3xl text-2xl font-medium title-font text-center text-gray-900 mb-20"
      id="skills"
    >
      My Skills
    </h1>
    <div
      class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6"
    >
      <div class="p-4 md:w-1/3 flex">
        <div
          class="w-12 h-12 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 mb-4 flex-shrink-0"
        >
          <img
            height="48px"
            width="40px"
            src={designer}
            alt="designer"
            loading="lazy"
          />
        </div>
        <div class="flex-grow pl-6">
          <h2 class="text-gray-900 text-lg title-font font-medium mb-2">
            Designer
          </h2>
          <p class="leading-relaxed text-base">
            I have designed minimalistic and clean interfaces with subtle
            animations that is pleasing to the eyes.
          </p>
        </div>
      </div>
      <div class="p-4 md:w-1/3 flex">
        <div
          class="w-12 h-12 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 mb-4 flex-shrink-0"
        >
          <img
            height="48px"
            width="40px"
            src={frontend}
            alt="frontend"
            loading="lazy"
          />
        </div>
        <div class="flex-grow pl-6">
          <h2 class="text-gray-900 text-lg title-font font-medium mb-2">
            Front-end Developer
          </h2>
          <p class="leading-relaxed text-base">
            I enjoy working with new technologies and also building things
            without major dependencies.
          </p>
        </div>
      </div>
      <div class="p-4 md:w-1/3 flex">
        <div
          class="w-12 h-12 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 mb-4 flex-shrink-0"
        >
          <img
            height="48px"
            width="40px"
            src={backend}
            alt="backend"
            loading="lazy"
          />
        </div>
        <div class="flex-grow pl-6">
          <h2 class="text-gray-900 text-lg title-font font-medium mb-2">
            Back-end Developer
          </h2>
          <p class="leading-relaxed text-base">
            I have designed, built and maintained back-end applications that are
            simple and scalable.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
