import React, { useState } from "react";
import axios from "axios";

function App() {
  const base_url = "http://127.0.0.1:5000";
  const [loading, setLoading] = useState();
  const [data, setData] = useState();
  const getData = async () => {
    setLoading(true);
    setData();
    try {
      const response = await axios.get(`${base_url}/get-trending`);
      setLoading(false);
      setData(response.data);
      console.log(response);
    } catch (error) {
      console.error("Error during Login:", error);
    }
  };
  return (
    <div id="main-page">
      <section id="content">
        <h1>Get a list of trending topics from twitter</h1>
        <p onClick={getData}>
          <u>Click here to run the script or get the data</u>
        </p>
        {loading && (
          <div className="loading">
            <p>Loading...</p>
          </div>
        )}
        {data && (
          <div>
            <h3>These are the most happening topics as on {data.timestamp}</h3>
            <ul>
              <li>{data.trend1}</li>
              <li>{data.trend2}</li>
              <li>{data.trend3}</li>
              <li>{data.trend4}</li>
              <li>{data.trend5}</li>
            </ul>
            <h3>The IP address used for this query was {data.ip}</h3>
            <h3 className="json">
              Here's a JSON extract of this record from the MongoDB:
            </h3>
            <pre
              style={{
                backgroundColor: "#f4f4f4",
                padding: "10px",
                borderRadius: "5px",
              }}
            >
              {JSON.stringify(data, null, 2)}
            </pre>
            <p onClick={getData}>
              <u>Click here to run the query again.</u>
            </p>
          </div>
        )}
      </section>
    </div>
  );
}

export default App;
