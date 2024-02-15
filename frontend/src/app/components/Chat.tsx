/* eslint-disable @next/next/no-img-element */
"use client";
import axios from "axios";
import React, { useEffect, useState } from "react";
import { v4 as uuidv4 } from "uuid";
import { Interactions, Session, CurrentSessionButtonProps, SessionButtonProps } from "../Types/Chat_types";
import { ReactTyped } from "react-typed";

const CurrentSessionButton: React.FC<CurrentSessionButtonProps> = ({ onClick }) => (
  <button className="flex items-center bg-gray-700 m-3 h-24 rounded-md p-4" onClick={onClick}>
    <div className="w-1/2 flex justify-start text-white">Current Session</div>
    <div className="ml-auto">{""}</div>
  </button>
);

const SessionButton: React.FC<SessionButtonProps> = ({ session, onClick }) => (
  <button className="flex items-center bg-chat-gpt m-3 h-24 rounded-md p-4 text-white border border-white" onClick={() => onClick(session.session_id)}>
    <div className="w-1/2 flex justify-start">{session.id}</div>
    <div className="ml-auto">{session.session_id}</div>
  </button>
);

const Chat = () => {
  const [question, setQuestion] = useState("");
  const [sessionId, setSessionId] = useState("");
  const [previousSessionData, setPreviousSessionData] = useState<Session[]>([]);
  const [allInteractions, setAllInteractions] = useState<Interactions[] | null>(null);
  const [history, setHistory] = useState([
    {
      id: 1,
      user_id: "",
      session_id: "",
    },
  ]);
  const [responseState, setResponseState] = useState("Click Here");

  useEffect(() => {
    const randomString = uuidv4();
    setSessionId(randomString);
    const accessToken = localStorage.getItem("access_token");
    async function getPreviousQuestions() {
      const response = await axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/chat/sessions`, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });
      console.log(response);
      if (response.status == 200) {
        setHistory(response.data);
      }
    }
    getPreviousQuestions();
  }, []);

  async function getAnswer() {
    setResponseState("Generating");
    const accessToken = localStorage.getItem("access_token");
    try {
      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/chat/askquestion`,
        {
          question: question,
          session_id: sessionId,
        },
        {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        }
      );
      console.log(response);
      if (response.status === 200) {
        setAllInteractions((prev) => [...(prev ?? []), { question: question, answer: response?.data.response }]);
      }

      setQuestion("");
    } catch (error) {
      console.log(error);
    }
    setResponseState("Done");

    setTimeout(() => {
      setResponseState("Click Here");
    }, 3000);
  }

  const [prevSession, setPrevSession] = useState(false);

  async function PreviousSessionData(session_id: string) {
    setPrevSession(true);
    try {
      const accessToken = localStorage.getItem("access_token");
      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/chat/session-data`,
        {
          session_id: session_id,
        },
        {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        }
      );
      console.log(response);
      if (response.status == 200) {
        setPreviousSessionData(response.data);
      }
    } catch (error) {
      console.log(error);
    }
  }

  // Function to format text with bold and italic tags
  const formatText = (text: string) => {
    // Replace **text** with <b> tags for bold text
    text = text.replace(/\*\*(.*?)\*\*/g, "<b>$1</b>");

    // Replace _text_ with <i> tags for italic text
    text = text.replace(/_(.*?)_/g, "<i>$1</i>");

    return text;
  };

  return (
    <>
      <div className="h-full flex overflow-y-hidden bg-chat-gpt">
        <div className="w-1/5 flex flex-col gap-2 h-screen items-center  overflow-y-scroll border-r border-white no-scrollbar">
          <div className="w-full flex flex-col gap-4  justify-center">
            <CurrentSessionButton onClick={() => setPrevSession(false)} />

            {history?.map((item, index) => (
              <SessionButton key={index} session={item} onClick={PreviousSessionData} />
            ))}
          </div>
        </div>

        {prevSession == true && (
          <>
            <div className="w-4/5 flex flex-col items-center p-4 overflow-y-scroll h-screen border border-white">
              <div className="flex flex-col items-center w-5/6 p-2 ">
                {previousSessionData?.map((session, index) => (
                  <React.Fragment key={index}>
                    {session.session_data.map((item, idx) => (
                      <React.Fragment key={idx}>
                        <div className="flex w-full">
                          <div className="w-3/5 ml-auto items-start rounded-md bg-chat-gpt p-2 text-white text-right">{item.question}</div>
                          <img src="/person.png" alt="" className="h-12" />
                        </div>
                        <div className="flex w-full">
                          <img src="/bot.png" alt="" className="h-12" />
                          <div className="w-3/5 mr-auto rounded-md bg-chat-gpt p-2 text-white text-justify">{item.answer}</div>
                        </div>
                      </React.Fragment>
                    ))}
                  </React.Fragment>
                ))}
              </div>
            </div>
          </>
        )}

        {prevSession == false && (
          <>
            <div className="w-4/5 flex flex-col items-center  p-4 h-screen overflow-y-scroll ">
              <div className="flex flex-col items-center w-5/6 p-2 h-5/6 overflow-y-scroll no-scrollbar">
                {allInteractions != null &&
                  allInteractions?.map((item, index) => (
                    <>
                      <div className="flex w-full m-1">
                        <div className="w-3/5 ml-auto rounded-md bg-chat-gpt p-2 m-1 text-white text-right ">{item.question}</div>

                        <img src="/person.png" alt="" className="h-12" />
                      </div>
                      <div className="flex w-full ">
                        <img src="/bot.png" alt="" className="h-12" />

                        <div className="w-3/5  mr-auto rounded-md bg-chat-gpt p-2 text-white text-justify">
                          <ReactTyped strings={[formatText(item.answer)]} typeSpeed={10}>
                            <p
                              className="leading-relaxed text-base text-white"
                              style={{ whiteSpace: "pre-line" }}
                              dangerouslySetInnerHTML={{
                                __html: formatText(item.answer),
                              }}
                            ></p>
                          </ReactTyped>
                        </div>
                      </div>
                    </>
                  ))}
              </div>
              <div className="mt-auto flex flex-col items-center gap-2 w-full">
                <textarea
                  name=""
                  id=""
                  className="w-5/6 outline-none border border-black p-2 rounded-xl"
                  value={question}
                  onChange={(e) => {
                    setQuestion(e.target.value);
                  }}
                ></textarea>
                <button
                  onClick={(e) => {
                    getAnswer();
                  }}
                  className={`${responseState === "Generating" ? "bg-gray-500" : ""} bg-black w-5/6 rounded-xl p-4 text-white`}
                >
                  {responseState}
                </button>
              </div>
            </div>
          </>
        )}
      </div>
    </>
  );
};

export default Chat;
