function App() {

  function viewSchedule() {
    //TO-DO
  }

  function viewTask(props) {
    return (
      <div className="task">
        <p>Task: {props.task} </p> 
        <p>Instructions: {props.instructions} </p>
        <p>Frequency: {props.frequency}</p>
        <p>Created by (opional): {props.user_id}</p> 
      </div>
    );
  }

  function addTaskToSchedule(props) {
    const[task, setTask] = React.useState("");
    const[frequency, setFrequency] = React.useState("");
    const[instructions, setInstructions] = React.useState("");
    function addNewTask() {
      fetch("add-task", {
        method: "POST",
        headers: {
          "Content-Type": "application/json", //example - 
        },
        body: JSON.stringify({ task, frequency }), //example - 
        }).then((response)) => { //JSON EXAMPLE BELOW
          response.json().then((jsonResponse) => {
            const {
              taskAdded: { taskId, task, frequency },
            } = jsonResponse; 
            props.addCard(cardId, name, skill);
        });
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

  function markTaskComplete() {
    //TO-DO
  }

  function addNoteToCalendar() {
    //TO-DO
  }

  function addEventoccurrence() {
    //TO-DO 
  }


}
// ----- All of the above will render on the html page with the tag root -----
ReactDOM.render(<App />, document.querySelector("#root"));
