<template>
<div class="container">
    <div class="row">
      <div class="col">
        <h1>Journeys</h1>
      </div>
      <div class="col">
        <input class="form-control" type="number" placeholder="Filter by percentage of sold seats..." v-model="porcentage" @keyup.enter="retriveJourneys(porcentage)">
      </div>
      <div class="col">
        <router-link
            class="btn btn-success float-right ml-2"
            :to="{name: 'JourneysEdit', params: {id:'new'}}"
        >
          <i class="bi bi-plus-circle"></i> New
        </router-link>
      </div>
    </div>
    <table class="table table-bordered">
      <thead>
      <tr>
        <th>#</th>
        <th width="24%">Route</th>
        <th width="20%">Bus</th>
        <th width="20%">Driver</th>
        <th width="20%">Date</th>
        <th width="20%">Average passengers</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-if="journeys.length === 0">
        <td colspan="6">No journeys found</td>
      </tr>
      <tr
          v-for="(journeys, index) in journeys"
          :key="index"
      >
        <td>{{ journeys.id }}</td>
        <td>
          {{journeys.route.origin }} hasta {{ journeys.route.destiny }}
        </td>
        <td>
          {{ journeys.bus.license_plate }}
        </td>
        <td>
          {{ journeys.bus.driver.name}} {{ journeys.bus.driver.last_name }}
        </td>

        <td>
          {{ journeys.check_out_time}}
        </td>
        <td>
          {{ journeys.percentage_passengers }} %
        </td>
        <td>
          <div class="btn-group">
            
            <router-link
                title="Edit"
                class="btn btn-warning"
                :to="{name: 'JourneysEdit', params: {id: journeys.id}}"
            >
              <i class="bi bi-eye"></i>
            </router-link>
            <router-link
                title="Sell Ticket"
                class="btn btn-success"
                :to="{name: 'TicketsEdit', params: {journeyId: journeys.id, id: 'new'}}"
            >
              <i class="bi bi-ticket-detailed-fill"></i>
            </router-link>
            <button
                title="Delete"
                class="btn btn-danger"
                @click="deleteJourney(ride.id)"
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
    name: "Journeys",
    data() {
        return {
            journeys : [],
            porcentage: 0,
        }
    },
methods: {
  async retriveJourneys(porcentage) {
    porcentage = porcentage ? porcentage : 0
    await APIService.getAll(`journeys?percentage=${porcentage}`).then(response => {this.journeys = response.data.results}).catch(e => {console.log(e)})
  },
  async deleteRide(id) {

    await APIService.delete(`journeys`, id).then(response => {this.retriveJourneys()}).catch(e => {console.log(e)})
  }
},
mounted() {
  this.retriveJourneys()
}
}
</script>

<style>

</style>