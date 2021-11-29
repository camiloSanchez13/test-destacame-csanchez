<template>
  <div class="container">
    <h1 v-if="bus.id === null">New Bus</h1>
    <h1 v-else>Bus Editor</h1>
    <form @submit.prevent="saveBus()">
      <div class="form-group">
        <label for="driver">Driver</label>
        <select class="form-control" id="driver" v-model="driver_id">
          <option disabled>Select an element</option>
          <option
              v-for="driver in drivers"
              :value="driver.id"
              :key="driver.id"
              :selected="driver.id === driver_id"
          >
            {{ driver.name }} {{ driver.last_name }}
          </option>
        </select>
        <small v-for="(error, index) in errors.driver" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="licence-plate">License Plate</label>
        <input type="text" class="form-control" id="license-plate" v-model="bus.license_plate" required maxlength="6" minlength="6"/>
        <small v-for="(error, index) in errors.license_plate" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="row">
        <div class="col">
          <router-link
              class="btn btn-primary mt-4"
              :to="{name: 'Buses'}"
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
  name: "BusEditor",
  data() {
    return {
      bus: {
        id: null,
            driver: {
            id: null,
            name: null,
            last_name: null
        },
        license_plate: null
      },
      driver_id: null,
      drivers: [],
      errors: {
        driver: [],
        licence_plate: []
      }
    };
  },
  mounted() {
    this.fetchDrivers();
    const id = this.$route.params.id;
    if (id !== "new")
      this.fetchBus(id);
  },
  methods: {
    async fetchDrivers() {
        await APIService.getAll('drivers').then(r => {this.drivers = r.data.results}).catch(e => {console.log(e)})
      
    },
    async fetchBus(id) {
        await APIService.get('buses', id).then(r => {
            this.bus = r.data
            this.driver_id = r.data.driver ? r.data.driver.id : null 
        }).catch(e => {console.log(e)})
    },
    async saveBus() {
        
      if (this.bus.id){
        await APIService.update(`buses`, this.bus.id, {...this.bus, driver: this.driver_id}).then(r => {
          this.bus = r.data
          console.log("actualizara buses")
          this.$router.push({name: "Buses"})
        }).catch(e => {this.errors = e.response.data})
      }else{
        await APIService.create(`buses`, {...this.bus, driver: this.driver_id}).then(r => {
          this.bus = r.data
          this.$router.push({name: "Buses"})
          }).catch(e => {this.errors = e.response.data})
      }
    }
  }
}
</script>

<style scoped></style>