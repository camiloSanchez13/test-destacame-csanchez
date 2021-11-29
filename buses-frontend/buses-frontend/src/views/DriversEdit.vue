<template>
  <div class="container">
    <h1 v-if="driver.id === null">New Driver</h1>
    <h1 v-else>Driver Editor</h1>
    <form @submit.prevent="saveDriver()">
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" class="form-control" id="name" v-model="driver.name" required/>
        <small v-for="(error, index) in errors.name" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="last-name">Last Name</label>
        <input type="text" class="form-control" id="last-name" v-model="driver.last_name" required/>
        <small v-for="(error, index) in errors.last_name" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>

      <div class="form-group mt-4">
        <label for="rut">Rut</label>
        <input type="text" class="form-control" id="rut" v-model="driver.rut" required/>
        <small v-for="(error, index) in errors.rut" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="dv">Dv</label>
        <input type="text" class="form-control" id="dv" v-model="driver.dv" required/>
        <small v-for="(error, index) in errors.dv" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="row">
        <div class="col">
          <router-link
              class="btn btn-primary mt-4"
              :to="{name: 'Drivers'}"
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
import APIService from "@/common/api.service"
export default {
    name: "DriverEdit",
    data() {
    return {
        driver: {
            id: null,
            name: null,
            last_name: null,
            rut: null,
            dv: null,
        },
        errors: {
            name: [],
            last_name: [],
            rut: [],
            dv: []
        }
    }
  },
  mounted() {
    const id = this.$route.params.id;
    if (id !== "new")
        this.fetchDriver(id);
  },
  methods: {
     async fetchDriver(id) {
       await APIService.get('drivers', id).then(response => {this.driver =  response.data}).catch(e => {console.log(e)})
    },
    async saveDriver(){
              
        if (this.driver.id){
            await APIService.update(`drivers`, this.driver.id, this.driver).then(response => {
               this.driver =  response.data 
               this.$router.push({name: "Drivers"})
               }).catch(e => {this.errors = e.response.data})
        }else {
            await APIService.create(`drivers`, this.driver).then(response => {
              this.driver =  response.data 
              this.$router.push({name: "Drivers"})
              }).catch(e => {this.errors = e.response.data})

        }
    }
    
  }

}
</script>

<style>

</style>