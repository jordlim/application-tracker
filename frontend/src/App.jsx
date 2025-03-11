import { useState, useEffect } from 'react'
import './App.css'
import './services/apiService'
import { getApplications } from './services/apiService'

const Jobs = ({job}) => {
  return (
    <div className="card">
      <h2>{job.title}</h2>
      <p>{job.company}</p>
      <p>{job.date_applied}</p>
    </div>
  )
}

const App = () => {
  const [count, setCount] = useState(0)
  const [data, setData] = useState([]);

  useEffect(() => {
    const getData = async () => {
      try {
        const applications = await getApplications();
        setData(applications);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    getData();
  }, []);

  return (
    <>
      <div>
        <ul>
          {data.map((job) => (
            <li key={job.id}>
              <Jobs job={job} />
            </li>
          ))}
        </ul>
      </div>
      <h1>Application Tracker</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
      </div>
    </>
  )
}

export default App
