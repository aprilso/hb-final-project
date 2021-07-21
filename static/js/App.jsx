function App() {
  return <div>
        <Greeting /> 
        <Task task="task"/>
        <AddTaskToSchedule />
        </div>
  
}
// Can surround with a React.Fragment instead of a div. Return is like html

function Greeting(props) {
  return <h3>Test Greeting!</h3>;
  //return <h1>Hello {props.name}</h1>;
}

function Task(props) {
  return (
    <div className="task">
      <p>Task: {props.task} </p> 
      <p>Instructions: {props.instructions} </p>
      <p>Frequency: {props.frequency}</p>
      <p>Created by (optional): {props.user_id}</p> 
    </div>
  );
}

function ViewSchedule() {
  //TO-DO - view all the tasks, array of objects to loop over, generate a component for each one


}

function AddTaskToSchedule(props) {
  const[task, setTask] = React.useState("");
  const[frequency, setFrequency] = React.useState("");
  const[instructions, setInstructions] = React.useState("");
  function addNewTask() {
    fetch("add-task", {
      method: "POST",
      headers: {
        "Content-Type": "application/json", //example - 
      },
      body: JSON.stringify({ task, frequency, instructions }), //example - 
      }).then((response) => response.json())
        .then((jsonResponse) => { 
          const {
            taskAdded: { taskId, task, frequency, instructions },
          } = jsonResponse; 
          props.addTask(taskId, task, frequency, instructions );
      });
  }
  return (
    <React.Fragment>
      <h2>Add New Task</h2>
      <label htmlFor="taskInput">Task Name</label>
      <input
        value={task}
        onChange={(event) => setTask(event.target.value)}
        id="taskInput"
      ></input>
      <label htmlFor="frequencyInput">Frequency (make this an enum dropdown)</label>
      <input
        value= {frequency}
        onChange={(event) =>setFrequency(event.target.value)}
        id="frequencyInput"
      ></input>
      <label htmlFor="taskInstructions">Instructions</label>
      <input
        value={instructions}
        onChange= {(event) => setInstructions(event.target.value)}
        id="taskInstructions"
      ></input>
      <button onClick = {addNewTask}>
        Add
      </button>
    </React.Fragment>
  );
}

function MarkTaskComplete() {
  //TO-DO
}

function AddNoteToCalendar() {
  //TO-DO
}

function AddEventoccurrence() {
  //TO-DO 
}



// ----- All of the above will render on the html page with the tag root -----
ReactDOM.render(<App />, document.querySelector("#root"));
