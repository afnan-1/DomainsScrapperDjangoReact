import React from "react";
import { useHistory } from "react-router-dom";

function FilteredDomains({ loader, domains }) {
  const history = useHistory();
  return (
    <div>
      <h4 className="text-center">
        {history.location.pathname.startsWith("/random")
          ? "Random Appraisal Tool"
          : "Godaddy Appraisal Tool"}
      </h4>
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Domain Name</th>
            <th scope="col">Appraisal value</th>
          </tr>
        </thead>
        <tbody>
          {!loader ? (
            domains.map((v, i) => (
              <tr key={i}>
                <th scope="row">{i + 1}</th>
                <td>{v.domain}</td>
                <td>${v.Estimated_price}</td>
              </tr>
            ))
          ) : (
            <tr>
              <th colSpan="3">Loading...</th>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default FilteredDomains;
