import { Link, useNavigate } from "react-router-dom";
import React, { useState } from "react";
import {
    signInWithGoogle,
    signInWithEmailAndPassword,
    signInWithFacebook,
    signInWithMicrosoft,
} from "../firebase";

function LogIn() {
    const [loginEmail, setLoginEmail] = useState("");
    const [loginPassword, setLoginPassword] = useState("");
    const [password, setPassword] = useState("");
    const navigate=useNavigate()

    return (
        <>
            <div class="fixed bg-trasparent w-screen h-screen flex justify-center items-center">
                <div class="w-full lg:w-4/12 px-4 mx-auto pt-6 ">
                    <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-white border-0">
                        <div class="rounded-t mb-0 px-6 py-6">
                            <div class="text-center mb-3">
                                <h6 class="text-blueGray-500 text-sm font-Stevens ">
                                    Sign in with
                                </h6>
                            </div>
                            <div class="flex items-center justify-center gap-2">
                                <button
                                    class="bg-white active:bg-blueGray-50 text-black px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1 uppercase shadow hover:shadow-md inline-flex items-center font-bold text-xs ease-linear transition-all duration-150"
                                    type="button"
                                    onClick={()=>signInWithGoogle(()=>navigate('/'))}
                                >
                                    <img
                                        alt="..."
                                        class="w-5 mr-1"
                                        src="https://demos.creative-tim.com/notus-js/assets/img/google.svg"
                                    />
                                    Google
                                </button>
                                {/* Add Microsoft sign-in button */}
                                <button
                                    class="bg-white active:bg-blueGray-50 text-black px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1 uppercase shadow hover:shadow-md inline-flex items-center font-bold text-xs ease-linear transition-all duration-150"
                                    type="button"
                                    onClick={()=>signInWithMicrosoft(()=>navigate('/'))}
                                >
                                    <img
                                        alt="..."
                                        class="w-5 mr-1"
                                        src="https://th.bing.com/th/id/R.3d6a2ad56bc3403c5cfcc3efe09b741b?rik=gnNKMMZSvZ3uMA&riu=http%3a%2f%2fpurepng.com%2fpublic%2fuploads%2flarge%2fpurepng.com-microsoft-logo-iconlogobrand-logoiconslogos-251519939091wmudn.png&ehk=1%2fl4i5MeDLTCpvZhUZlCefvhSzsGR16HIPqagpDxYDg%3d&risl=&pid=ImgRaw&r=0"
                                    />
                                    Microsoft
                                </button>
                                {/* Add Facebook sign-in button */}
                                <button
                                    class="bg-white active:bg-blueGray-50 text-black px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1 uppercase shadow hover:shadow-md inline-flex items-center font-bold text-xs ease-linear transition-all duration-150"
                                    type="button"
                                    onClick={()=>signInWithFacebook(()=>navigate('/'))}
                                >
                                    <img
                                        alt="..."
                                        class="w-5 mr-1"
                                        src="https://upload.wikimedia.org/wikipedia/commons/0/05/Facebook_Logo_(2019).png"
                                    />
                                    Facebook
                                </button>
                            </div>
                            <hr class="mt-6 border-b-1 border-blueGray-300" />
                        </div>
                        <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
                            <div class="text-blueGray-400 text-center mb-3 font-Stevens text-xl">
                                <small>sign in with credentials</small>
                            </div>
                            <form className="flex flex-col items-center">
                                <div class="relative w-full mb-3">
                                    <input
                                        type="email"
                                        placeholder="Enter email"
                                        value={loginEmail}
                                        onChange={(e) => setLoginEmail(e.target.value)}
                                        class="font-Stevens text-xs border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                                    />
                                </div>
                                <div class="relative w-full mb-3">
                                    <input
                                        type="password"
                                        placeholder="Password"
                                        value={loginPassword}
                                        onChange={(e) => setLoginPassword(e.target.value)}
                                        class="font-Stevens text-xs border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                                    />
                                </div>
                                <div>
                                    <label class="flex cursor-pointer justify-end ">
                                        <span className="font-Stevens text-xs">
                                            don’t have account?{" "}
                                            <Link
                                                to="/Signup"
                                                className="text-blue-600 hover:underline"
                                            >
                                                SIGN UP
                                            </Link>{" "}
                                        </span>
                                    </label>
                                </div>
                                <div className="text-center mt-6 w-1/2 flex justify-center">
                                    <button
                                        class="bg-blue-600 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150 font-Collingar"
                                        // type="submit"
                                        type="button"
                                        onClick={() => {
                                            signInWithEmailAndPassword(loginEmail, loginPassword,()=>()=>navigate('/'));
                                        }}
                                    >
                                        {" "}
                                        Sign In{" "}
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}

export default LogIn;