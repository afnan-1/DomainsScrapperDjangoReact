import React from "react";

function AllDomains({ other, otherLoader }) {
  return (
    <div>
      <h4 className="text-center"> Deleted Domains</h4>
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Domain Name</th>
          </tr>
        </thead>
        <tbody>
          {!otherLoader ? (
            other.map((v, i) => (
              <tr key={i}>
                <th scope="row">{i + 1}</th>
                <td>{v}</td>
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

export default AllDomains;
