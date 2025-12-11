import{initializeApp} from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";
import {
      getFirestore,collection,addDoc,onSnapshot,deleteDoc,doc

} from "https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyCJuakB85bs7lTn55ls-WKrc41G8uLnJsI",
  authDomain: "sample-app-17724.firebaseapp.com",
  projectId: "sample-app-17724"};

  const app= initializeApp(firebaseConfig);
  const db= getFirestore(app);

  window.addNote = async function () 
  {
    const noteInput = document.getElementById("noteInput");
    const note = noteInput.value;

    if (note.trim() === ""){
        alert("Please write a note");
        return;
    }

    await addDoc(collection(db, "notes"),{
        text: note,
        createdAt: Date.now()
    });

    noteInput.value= "";
    
  };

  onSnapshot(collection(db, "notes"), (Snapshot) => {
    const note= document.getElementById("note");
    note.innerHTML= "";

    Snapshot.forEach((docItem) => {
        const li= document.createElement("li");
        li.innerHTML = `
        ${docItem.data().text}
        <button onclick="deleteNote('${docItem.id}')"> Delete Note</button>
        `;
        note.appendChild(li);
    });

    window.deleteNote = async function (id){
        await deleteDoc(doc(db, "notes",id));

    };
  });