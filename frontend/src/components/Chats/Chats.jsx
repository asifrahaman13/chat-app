import React, { useState, useEffect } from "react";

import "./Chats.css";
import Navbar from "../Header/Header";
import UserChat from "../UsesrChat/UserChat";

const Chats = () => {
  return (
    <>
      <Navbar />
     <UserChat/>
    </>
  );
};

export default Chats;
