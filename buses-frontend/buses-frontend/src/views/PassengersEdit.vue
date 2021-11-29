<template>
  <div class="container">
    <h1 v-if="passenger.id === null">New Passenger</h1>
    <h1 v-else>Passenger Edit</h1>
    <form @submit.prevent="savePassenger()">
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" class="form-control" id="name" v-model="passenger.name" required/>
        <small v-for="(error, index) in errors.name" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="last-name">Last Name</label>
        <input type="text" class="form-control" id="last-name" v-model="passenger.last_name" required/>
        <small v-for="(error, index) in errors.last_name" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="rut">Rut</label>
        <input type="text" class="form-control" id="rut" v-model="passenger.rut" required/>
        <small v-for="(error, index) in errors.rut" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="dv">Dv</label>
        <input type="text" class="form-control" id="dv" v-model="passenger.dv" required/>
        <small v-for="(error, index) in errors.dv" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="row">
        <div class="col">
          <router-link
              class="btn btn-primary mt-4"
              :to="{name: 'Passengers'}"
          >
            <i class="bi bi-arrow-left"></i> Back
          </router-link>
        </div>
        <div class="col d-flex flex-row-reverse">
          <button class="btn btn-success mt-4"><i class="bi bi-check"></i> Save</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import APIService from "@/common/api.service";
export default {
  name: "PassengersEdit",
  data() {
    return {
      passenger: {
            id: null,
            name: null,
            last_name: null,
            rut: null,
            dv: null
      },
      tickets: [],
      errors: {
        name: [],
        last_name: []
      }
    };
  },
  mounted() {

    const id = this.$route.params.id;
    if (id !== "new") {
      this.fetchPassenger(id);
    }
  },
    methods: {
     fetchPassenger(id) {
        APIService.get('passengers', id).then(response => {
            this.passenger =  response.data
        })
        .catch(e => {
          console.log(e)
        })
    },
    savePassenger(){
      
        if (this.passenger.id){
            APIService.update(`passengers`, this.passenger.id, this.passenger).then(response => {
               this.passenger =  response.data 
               this.$router.push({name: "Passengers"})
               }).catch(e => {this.errors = e.response.data})
        }else {
            APIService.create(`passengers`, this.passenger).then(response => {
              this.passenger =  response.data 
              this.$router.push({name: "Passengers"})
              }).catch(e => {this.errors = e.response.data})
        }
    }
    
  }
}
</script>

<style scoped></style>