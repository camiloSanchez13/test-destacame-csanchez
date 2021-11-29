<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Routes</h1>
      </div>
      <div class="col">
        <div class="d-flex flex-row-reverse">
          <router-link
              class="btn btn-success float-right"
              :to="{name: 'RoutesEdit', params: {id:'new'}}"
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
        <th width="33%">Origin</th>
        <th width="33%">Destiny</th>
        <th class="33%">Average Passengers</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-if="routes.length === 0">
        <td colspan="6">No routes found</td>
      </tr>
      <tr
          v-for="(route, index) in routes"
          :key="index"
      >
        <td>{{ route.id }}</td>
        <td>{{ route.origin }}</td>
        <td>{{ route.destiny }}</td>
        <td>{{ route.average_passengers }}</td>
        <!-- <td>{{ route.passengers_average }}</td> -->
        <td>
          <div class="btn-group">
            <router-link
                title="Edit"
                class="btn btn-warning"
                :to="{name: 'RoutesEdit', params: {id: route.id}}"
            >
              <i class="bi bi-eye"></i>
            </router-link>
            <button
                title="Delete"
                class="btn btn-danger"
                @click="deleteRoute(route.id)"
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
  name: "Routes",
  data() {
    return {
      routes: []
    }
  },
  methods: {
    async fetchRoutes() {
        await APIService.getAll(`routes`).then(r => {this.routes = r.data.results}).catch(e => {console.log(e)})
    },
    async deleteRoute(id) {
      await APIService.delete('routes', id).then(r => {this.fetchRoutes()}).catch(e => {console.log(e)})
    }
  },
  mounted() {
    this.fetchRoutes();
  }
}
</script>

<style scoped></style>