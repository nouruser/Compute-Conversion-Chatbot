import firebase from 'firebase/compat/app';
import { getFirestore, collection, where, doc, query, getDocs, setDoc } from 'firebase/firestore';
import 'firebase/compat/auth';
import { useNavigate } from 'react-router-dom';

const firebaseConfig = {
  apiKey: "AIzaSyBpxhgBaL84KqPdMqhLQDO1tMMy5Ut8yPU",
  authDomain: "chatbot-c0f3f.firebaseapp.com",
  projectId: "chatbot-c0f3f",
  storageBucket: "chatbot-c0f3f.appspot.com",
  messagingSenderId: "737595013770",
  appId: "1:737595013770:web:763d51e24202cb18510b73",
  measurementId: "G-XYTTSDR2ZN"
};


export const app = firebase.initializeApp(firebaseConfig);
export const db = getFirestore(app);

const provider = new firebase.auth.GoogleAuthProvider();
provider.setCustomParameters({ prompt: 'select_account' });

const facebookProvider = new firebase.auth.FacebookAuthProvider();
const microsoftProvider = new firebase.auth.OAuthProvider('microsoft.com');

export const auth = firebase.auth();
export default firebase;

export const signInWithGoogle = async (redirectCallback) => {
  try {
    const res = await auth.signInWithPopup(provider);
    const user = res.user;
    const userRef = collection(db, 'users');
    const result = await getDocs(query(userRef, where('uid', '==', user.uid)));
    if (result.empty) {
      await setDoc(doc(db, 'users', user.uid), {
        uid: user.uid,
        name: user.displayName,
        authProvider: 'google',
        email: user.email,
      });
    }
    redirectCallback(); // Redirect after successful sign-in
  } catch (err) {
    alert(err.message);
  }
};

export const signInWithFacebook = async (redirectCallback) => {
  try {
    const res = await auth.signInWithPopup(facebookProvider);
    const user = res.user;
    const userRef = collection(db, 'users');
    const result = await getDocs(query(userRef, where('uid', '==', user.uid)));
    if (result.empty) {
      await setDoc(doc(db, 'users', user.uid), {
        uid: user.uid,
        name: user.displayName,
        authProvider: 'facebook',
        email: user.email,
      });
    }
    redirectCallback(); // Redirect after successful sign-in
  } catch (err) {
    alert(err.message);
  }
};

export const signInWithMicrosoft = async (redirectCallback) => {
  try {
    const res = await auth.signInWithPopup(microsoftProvider);
    const user = res.user;
    const userRef = collection(db, 'users');
    const result = await getDocs(query(userRef, where('uid', '==', user.uid)));
    if (result.empty) {
      await setDoc(doc(db, 'users', user.uid), {
        uid: user.uid,
        name: user.displayName,
        authProvider: 'microsoft',
        email: user.email,
      });
    }
    redirectCallback(); // Redirect after successful sign-in
  } catch (err) {
    alert(err.message);
  }
};

export const signInWithEmailAndPassword = async (email, password, redirectCallback) => {
  try {
    await auth.signInWithEmailAndPassword(email, password);
    redirectCallback(); // Redirect after successful login
  } catch (err) {
    alert(err.message);
  }
};

export const registerWithEmailAndPassword = async (name, email, password, redirectCallback) => {
  try {
    const res = await auth.createUserWithEmailAndPassword(email, password);
    const user = res.user;
    await setDoc(doc(db, 'users', user.uid), {
      uid: user.uid,
      name,
      authProvider: 'local',
      email,
    });
    redirectCallback(); // Redirect after successful registration
  } catch (err) {
    alert(err.message);
  }
};