<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Buses</h1>
      </div>
      <div class="col">
        <div class="d-flex flex-row-reverse">
          <router-link
              class="btn btn-success float-right"
              :to="{name: 'BusesEdit', params: {id:'new'}}"
          >
            <i class="bi bi-plus-circle"></i> New
          </router-link>
        </div>
      </div>
    </div>
    <table class="table table-bordered">
      <thead>
      <tr>
        <th>#</th>
        <th width="50%">Driver</th>
        <th width="20%">License Plate</th>
        <th width="30%">Date Created</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-if="buses.length === 0">
        <td colspan="4">No buses found</td>
      </tr>
      <tr
          v-for="(bus, index) in buses"
          :key="index"
      >
        <td>{{ bus.id }}</td>
        <td>
          <span v-if="bus.driver">{{ bus.driver.name }} {{ bus.driver.last_name }}</span>
          <span v-else>No driver set...</span>
        </td>
        <td>{{ bus.license_plate }}</td>
        <td>{{ bus.admission_date }}</td>
        <td>
          <div class="btn-group">
            <router-link
                title="Edit"
                class="btn btn-warning"
                :to="{name: 'BusesEdit', params: {id: bus.id}}"
            >
              <i class="bi bi-eye"></i>
            </router-link>
            <button
                title="Delete"
                class="btn btn-danger"
                @click="deleteBus(bus.id)"
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
  name: "Buses",
  data() {
    return {
        buses: []
    }
  },
  methods: {
    async fetchBuses() {
        await APIService.getAll(`buses`).then( r => {this.buses = r.data.results }).catch(e => {console.log(e)})
    },
    async deleteBus(id) {
        await APIService.delete('buses', id).then(r => {this.fetchBuses()}).catch(e => {console.log(e)})
    }
  },
  mounted() {
    this.fetchBuses();
  }
}
</script>

<style scoped></style>