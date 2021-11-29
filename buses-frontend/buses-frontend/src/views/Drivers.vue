
<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Drivers</h1>
      </div>
    <div class="col">
        <div class="d-flex flex-row-reverse">
          <router-link
            class="btn btn-success float-right"
            :to="{name: 'DriverEdit', params: {id:'new'}}"
          >
            <i class="bi bi-plus-circle"></i> add
          </router-link>
        </div>
      </div>
    </div>
    <table class="table table-bordered">
      <thead>
      <tr>
        <th>#</th>
        <th width="25%">Name</th>
        <th width="25%">Last Name</th>
        <th width="25%">Rut</th>
        <th width="25%">Dv</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-if="drivers.length === 0">
        <td colspan="4">No drivers found</td>
      </tr>
      <tr
          v-for="(driver, index) in drivers"
          :key="index"
      >
        <td>{{ driver.id }}</td>
        <td>{{ driver.name }}</td>
        <td>{{ driver.last_name }}</td>
        <td>{{ driver.rut }}</td>
        <td>{{ driver.dv }}</td>
        <td>

            <div class="btn-group">
            <router-link
                title="Edit"
                class="btn btn-warning"
                :to="{name: 'DriverEdit', params: {id: driver.id}}"
            >
              <i class="bi bi-eye"></i>
            </router-link>
            <button
                title="Delete"
                class="btn btn-danger"
                @click="deleteDriver(driver.id)"
            >
              <i class="bi bi-trash"></i>
            </button>
            </div>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>
<script>

import APIService from "@/common/api.service"

export default {
  name: 'Drivers',
  data() {
    return {
      drivers: []
    }
  },
  methods: {
    async fetchDrivers() {
      await APIService.getAll(`drivers`).then(response => {this.drivers = response.data.results}).catch(e => {console.log(e)})
  },
   async deleteDriver(id) {
      await APIService.delete(`drivers`, id).then(response => {this.fetchDrivers()}).catch(e => {console.log(e)})
  }
},
  mounted() {
    this.fetchDrivers()
  }
}
</script>