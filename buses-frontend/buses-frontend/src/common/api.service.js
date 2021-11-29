import http from "./config";

class APIService {
    getAll(resource) {
      return http.get(`/${resource}`);
    }
  
    get(resource, id) {
      return http.get(`/${resource}/${id}`);
    }
  
    create(resource, data) {
      return http.post(`/${resource}`, data);
    }
  
    update(resource, id, data) {
      return http.put(`/${resource}/${id}`, data);
    }
  
    delete(resource, id) {
      return http.delete(`/${resource}/${id}`);
    }
  }
  
  export default new APIService();