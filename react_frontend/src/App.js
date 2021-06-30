import logo from "./logo.svg";
import "./App.css";
import Header from "./components/Header";
import { HashRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./screens/Home";
import RandomAppraisal from "./screens/RandomAppraisal";
import RandomDomain from "./screens/RandomDomain";
import DomainNow from "./screens/DomainNow";
function App() {
  return (
    <Router>
      <Header />
      <Switch>
        <Route path="/" exact component={Home}></Route>
        <Route path="/randomappraisaltool" exact component={RandomAppraisal} />
        <Route path="/randomdomaingenerator" exact component={RandomDomain} />
        <Route path="/domainnow" exact component={DomainNow} />
      </Switch>
    </Router>
  );
}

export default App;
