"use client";

import axios from "axios";
import Chat from "./components/Chat";
import Login from "./components/Login";
import { useEffect, useState } from "react";

export default function Home() {
  const [loggedIn, setLoggedIn] = useState(false);
  useEffect(() => {
    const accessToken = localStorage.getItem("access_token");
    async function checkLoggedIn() {
      const response = await axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/auth/authenticate`, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });

      if (response.status === 200) {
        if (response.data.message === true) {
          setLoggedIn(true);
        }
      }
    }
    checkLoggedIn();
  }, []);

  return <>{loggedIn == false ? <Login /> : <Chat />}</>;
}
