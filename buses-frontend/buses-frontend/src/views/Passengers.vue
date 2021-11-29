<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Passengers</h1>
      </div>
      <div class="col">
        <div class="d-flex flex-row-reverse">
          <router-link
              class="btn btn-success float-right"
              :to="{name: 'PassengersEdit', params: {id:'new'}}"
          >
            <i class="bi bi-plus-circle"></i> Add
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
      <tr v-if="passengers.length === 0">
        <td colspan="4">No passengers found</td>
      </tr>
      <tr
          v-for="(passenger, index) in passengers"
          :key="index"
      >
        <td>{{ passenger.id }}</td>
        <td>{{ passenger.name }}</td>
        <td>{{ passenger.last_name }}</td>
        <td>{{ passenger.rut }}</td>
        <td>{{ passenger.dv }}</td>
        <td>
          <div class="btn-group">
            <router-link
                title="Edit"
                class="btn btn-warning"
                :to="{name: 'PassengersEdit', params: {id: passenger.id}}"
            >
              <i class="bi bi-eye"></i>
            </router-link>
            <button
                title="Delete"
                class="btn btn-danger"
                @click="deletePassenger(passenger.id)"
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
import APIService from "@/common/api.service";

export default {
  name: "Passengers",
  data() {
    return {
      passengers: []
    }
  },
  methods: {
    async fetchPassengers() {
      await APIService.getAll(`passengers`).then(r => { this.passengers = r.data.results }).catch(e => {console.log(e)})
    },
    async deletePassenger(id) {
        await APIService.delete('passengers', id).then(r => {this.fetchPassengers()}).catch(e => {console.log(e)})
    }
  },
  mounted() {
    this.fetchPassengers();
  }
}
</script>

<style scoped></style>