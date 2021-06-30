import React, { useState } from "react";
import { rword } from "rword";
import { randomDomainGenerator } from "../actions/domains";

function RandomDomain() {
  const [domainLength, setDomainLength] = useState(5);
  const [domainNo, setDomainNo] = useState(5);
  const [contains, setContains] = useState("");
  const [randomWords, setRandomWords] = useState([]);
  const [generatedWords, setGeneratedWords] = useState([]);
  const [loader, setLoader] = useState(false);
  const handleSubmit = (e) => {
    e.preventDefault();
    setLoader(true);
    setRandomWords([]);
    setGeneratedWords([]);
    let words;
    if (contains === "") {
      words = rword.generate(Number(domainNo), {
        length: Number(domainLength),
      });
    } else {
      words = rword.generate(Number(domainNo), {
        length: Number(domainLength),
        contains: contains,
      });
    }
    let newArr = [];
    words.map((v, i) => {
      newArr.push(v + ".com");
      newArr.push(v + ".co.uk");
      newArr.push(v + ".org");
    });
    setGeneratedWords([...newArr]);
    randomDomainGenerator(words).then((res) => setRandomWords([...res.data]));
  };
const handleChange=(e)=>{
    if (e.target.value>=25){
        setDomainNo(25)
    }
    else{
        setDomainNo(e.target.value)
    }
}
  return (
    <div className="container mt-5">
      <h2>Random Domain Generator</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="price" className="form-label">
            Enter Number of Domains <small>(Max(5))</small>
          </label>
          <input
            type="text"
            className="form-control"
            id="price"
            value={domainNo}
            placeholder="5"
            onChange={handleChange}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="limit" className="form-label">
            Enter length of domain <small>(Example(4))</small>
          </label>
          <input
            type="text"
            className="form-control"
            id="limit"
            placeholder="4"
            value={domainLength}
            onChange={(e) => setDomainLength(e.target.value)}
          />
        </div>
        <button className="btn btn-primary mt-4" type="submit">
          Generate
        </button>
      </form>
      <div className="row">
        <div className="col">
          <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Generated Domains</th>
              </tr>
            </thead>
            <tbody>
              {generatedWords.length > 0 &&
                generatedWords.map((v, i) => {
                  return (
                    <tr key={i}>
                      <th scope="row">{i + 1}</th>
                      <td>{v}</td>
                    </tr>
                  );
                })}
            </tbody>
          </table>
        </div>
        <div className="col">
          <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Availible Domains</th>
              </tr>
            </thead>
            <tbody>
              {randomWords.length > 0 ? (
                randomWords.map((v, i) => {
                  return (
                    <tr key={i}>
                      <th scope="row">{i + 1}</th>
                      <td>{v}</td>
                    </tr>
                  );
                })
              ) : (
                <tr>
                  <th colSpan="2">{loader && "Loading..."}</th>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default RandomDomain;
