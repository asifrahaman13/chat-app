import React from "react";

const Header = () => {
  return (
    <>
      <section className="text-gray-600 body-font">
        <div className="container px-5 py-24 mx-auto">
          <div className="flex flex-col text-center w-full mb-20">
            <h2 className="text-xs text-indigo-500 tracking-widest font-medium title-font mb-1">
              ASTRA
            </h2>
            <h1 className="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-100">
              CHAT WITH OUR APPLICATION
            </h1>
            <p className="lg:w-2/3 mx-auto leading-relaxed text-base text-gray-100">
              Our application is capable of chatting with high level of
              accuracy. Get the responses without much delay with good amount of
              latency. You will get to the point answers.
            </p>
          </div>
          <div className="flex flex-wrap">
            <div className="xl:w-1/3 lg:w-1/2 md:w-full px-8 py-6 border-l-2 border-gray-200 border-opacity-60">
              <h2 className="text-lg sm:text-xl text-indigo-500  font-medium title-font mb-2">
                Examples
              </h2>
              <p className="leading-relaxed text-base mb-4">
                Explain about the quantum computing in few words.
              </p>
              <p className="leading-relaxed text-base mb-4">
                Who is Elon Musk?
              </p>
              <p className="leading-relaxed text-base mb-4">
                Give me nice pick up lines for my loved one.
              </p>
              <p className="leading-relaxed text-base mb-4">
                Describe about the recent incident of Apple visiting in India.
              </p>
            </div>
            <div className="xl:w-1/3 lg:w-1/2 md:w-full px-8 py-6 border-l-2 border-gray-200 border-opacity-60">
              <h2 className="text-lg sm:text-xl text-indigo-500  font-medium title-font mb-2">
                Cpabilities
              </h2>
              <p className="leading-relaxed text-base mb-4">
                The application is able to remember your previous responses
              </p>
              <p className="leading-relaxed text-base mb-4">
                It can search over the internet and give recent happenings of
                the world. The result is based on the google search index.
              </p>
            </div>
            <div className="xl:w-1/3 lg:w-1/2 md:w-full px-8 py-6 border-l-2 border-gray-200 border-opacity-60">
              <h2 className="text-lg sm:text-xl text-indigo-500  font-medium title-font mb-2">
                Limitations
              </h2>
              <p className="leading-relaxed text-base mb-4">
                At times it may not give proper response. Please be patient and
                try with newer prompts.
              </p>
              <p className="leading-relaxed text-base mb-4">
                Sometimes it may give weird answers. Plesae check your prompt
                and rewrite it to get better result. Refresh it if such case
                exists repeatedly.
              </p>
            </div>
            <div className="xl:w-1/3 lg:w-1/2 md:w-full px-8 py-6 border-l-2 border-gray-200 border-opacity-60 mt-4">
              <h2 className="text-lg sm:text-xl text-indigo-500  font-medium title-font mb-2">
                How to use it
              </h2>
              <p className="leading-relaxed text-base mb-4">
                You can either type or can open the microphone to enable voice
                chat.
              </p>
              <p className="leading-relaxed text-base mb-4">
                Click on voice to enable voice chat. This will allow you to use
                both the voice chat as well as editing the text.
              </p>
              <p className="leading-relaxed text-base mb-4">
                If you want to use only the text then click on the "Only chat"
                option. You can reset the text using the 'Reset' button. When
                you are done click on the 'Send' button.
              </p>
            </div>
            <div className="xl:w-1/3 lg:w-1/2 md:w-full px-8 py-6 border-l-2 border-gray-200 border-opacity-60 mt-4">
              <h2 className="text-lg sm:text-xl text-indigo-500  font-medium title-font mb-2">
                Your response and latency
              </h2>
              <p className="leading-relaxed text-base mb-4">
                You do not need to wait long! If it is subjective question wait for 5-7 sec at max. It it is objective one then you will probably get instant results.
              </p>
              <p className="leading-relaxed text-base mb-4">
                Ensure that you are connected to the internet throughout the process.
              </p>
              <p className="leading-relaxed text-base mb-4">
                Dont refresh the page in between. Your response will be lost if you refresh it. 
              </p>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Header;
