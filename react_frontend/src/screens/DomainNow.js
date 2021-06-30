import React, { useState } from "react";
import { domainNow, domains } from "../actions/domains";
import Results from "../components/AllDomains";
import FilteredDomains from "../components/FilteredDomains";
function DomainNow() {
  const [price, setPrice] = useState(2000);
  const [domainNo, setDomainNo] = useState(25);
  const [scrapedResults, setScrapedResults] = useState([]);
  const [filteredResults, setFilteredResults] = useState([]);
  const [loader, setLoader] = useState(false);
  const [filterLoader, setFilterLoader] = useState(false);
  const handleSubmit = (e) => {
    e.preventDefault();
    setLoader(true);
    setFilterLoader(true);
    domains(domainNo).then((res) => {
      setScrapedResults([...res.data.data]);
      setLoader(false);
      domainNow(price).then((res) => {
        setFilteredResults(res.data.domains);
        setFilterLoader(false);
      });
    });
  };
  const handleChange = (e) => {
    if (e.target.value >= 25) {
      setDomainNo(25);
    } else {
      setDomainNo(e.target.value);
    }
  };
  return (
    <div className="container mt-5">
      <h2 className="text-center">Domain Checker on Random Appraisal</h2>

      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="price" className="form-label">
            Enter appraisal value in <small>(Default is $2000)</small>
          </label>
          <input
            type="text"
            className="form-control"
            id="price"
            value={price}
            placeholder="2000"
            onChange={(e) => setPrice(e.target.value)}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="limit" className="form-label">
            Please enter no of domains you want to check on appraisal tool{" "}
            <small>(MAX is 25)</small>
          </label>
          <input
            type="text"
            className="form-control"
            id="limit"
            placeholder="50"
            value={domainNo}
            onChange={handleChange}
          />
        </div>
        <button className="btn btn-primary mt-4" type="submit">
          Search
        </button>
      </form>

      <div className="row">
        <div className="col">
          <Results other={scrapedResults} otherLoader={loader} />
        </div>
        <div className="col">
          <FilteredDomains domains={filteredResults} loader={filterLoader} />
        </div>
      </div>
    </div>
  );
}

export default DomainNow;
