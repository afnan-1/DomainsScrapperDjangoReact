import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export const filteredDomains = (price) => {
  try {
    const res = axios.get(`/api/domainsfilter/${price}`, { timeout: 1000000 });
    return res;
  } catch (err) {
    return "Server Error Please Try Later";
  }
};

export const domains = (limit) => {
  try {
    const res = axios.get(`/api/domains/${limit}`);
    return res;
  } catch (err) {
    return "Server Error Please Try Later";
  }
};

export const random_appraisal_domains = (price) => {
  const res = axios.get(`/api/randomappraisal/${price}`, { timeout: 1000000 });
  return res;
};

export const randomDomainGenerator = (domains) => {
  const config = {
    headers: {
        'Content-type': 'application/json',
    }
}
  const res = axios.post(`/api/randomdomainchecker/`, { domains: domains },config);
  return res;
};

export const domainNow = (price) => {
  const res = axios.get(`/api/domainnow/${price}`);
  return res;
};
