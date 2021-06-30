import React from "react";
import { Link } from "react-router-dom";
function Header() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container-fluid">
        <a className="navbar-brand" href="#">
          Domain Scraper
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon" />
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link className="nav-link active" aria-current="page" to="/">
                Go Daddy appraise Tool
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/randomdomaingenerator">
                Random Domain Generator
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/randomappraisaltool">
                Random Appraise Tool
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/domainnow">
                25 Domains per request Appraisal
              </Link>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/admin">
                Admin Panel
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Header;
