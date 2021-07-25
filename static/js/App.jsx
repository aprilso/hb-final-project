function App() {
  return <div>
        <Greeting /> 
        <ViewSchedule />
    
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
      <p>Task: {props.task_name} </p> 
      <p>Instructions: {props.instructions} </p>
      <p>Frequency: {props.frequency}</p>
      <p>Created by (optional): {props.user_id}</p> 
    </div>
  );
}

function ViewSchedule() {
  //TO-DO - view all the tasks, array of objects to loop over, generate a component for each one
  let dogId = parseInt(window.location.pathname.replace("/dogs/", "").replace("/schedule", ""))
  const [schedule, setSchedule] = React.useState([]);

  React.useEffect(() => {
    fetch(`/api/dogschedule/${dogId}`) 
      .then((response) => response.json())
      .then((result) => {
        setSchedule(result);
      });
  }, []);

  const scheduleListItems = [];

  for (let each of schedule) {
    scheduleListItems.push(<li key={each.taskId}>{each.taskName} | {each.frequency} | {each.instructions}</li>);
  }
  return <React.Fragment>
    <h2>Current Overall Schedule: </h2>
    <ul>{scheduleListItems}</ul>;
    <AddTaskToSchedule setSchedule={setSchedule} schedule={schedule}/>
    </React.Fragment>
    
}

function AddTaskToSchedule(props) {
  const[task_name, setTask] = React.useState("");
  const[frequency, setFrequency] = React.useState("");
  const[instructions, setInstructions] = React.useState("");
  

  function addNewTask() {
    fetch("/add-task", {
      method: "POST",
      headers: {
        "Content-Type": "application/json", 
      },
      body: JSON.stringify({ task_name, frequency, instructions }), 
      }).then((response) => response.json())
        .then((jsonResponse) => { 
          props.setSchedule([...props.schedule, jsonResponse.taskAdded])
          setTask("")
          setFrequency("")
          setInstructions("")
      });
  }

  return (
    <React.Fragment>
      <h2>Add New Task</h2>
      <label htmlFor="taskInput">Task Name</label>
      <input
        value={task_name}
        onChange={(event) => setTask(event.target.value)}
        id="taskInput"
      ></input><br></br>
      <label htmlFor="frequencyInput">Frequency (make this a dropdown)</label>
      <input
        value={frequency}
        onChange={(event) =>setFrequency(event.target.value)}
        id="frequencyInput"
      ></input>
      
      <br></br>
      <label htmlFor="taskInstructions">Instructions</label>
      <input
        value={instructions}
        onChange= {(event) => setInstructions(event.target.value)}
        id="taskInstructions"
      ></input><br></br>
      <button onClick = {addNewTask}> 
        Add
      </button>
    </React.Fragment>
  );
}

function TodaysScheduleList() {
  //TO-DO - view today's schedule 
  // can use FullCalendar list view
}

function MarkTaskComplete() {
  //TO-DO
}

function AddNoteToCalendar() {
  //TO-DO
}

function AddEventOccurrence() {
  //TO-DO 
}

// ----- All of the above will render on the html page with the tag root -----
ReactDOM.render(<App />, document.querySelector("#root"));
