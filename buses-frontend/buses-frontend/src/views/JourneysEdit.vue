<template>
  <div class="container">
    <h1 v-if="journey.id === null">New Journey</h1>
    <h1 v-else>Journey Editor</h1>
    <form @submit.prevent="saveJourney()">
      <div class="form-group">
        <label for="route">Route</label>
        <select class="form-control" id="route" v-model="route_id" required>
          <option disabled>Select an element</option>
          <option
              v-for="route in routes"
              :value="route.id"
              :key="route.id"
              :selected="route.id === route_id"
          >
            Desde {{ route.origin }} hasta {{ route.destiny }}
          </option>
        </select>
        <small v-for="(error, index) in errors.route" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="bus">Bus</label>
        <select class="form-control" id="bus" v-model="bus_id" required>
          <option disabled>Select an element</option>
          <option
              v-for="bus in buses"
              :value="bus.id"
              :key="bus.id"
              :selected="bus.id === bus_id"
          >
            {{ bus.license_plate }}
            <span v-if="bus.driver">driven by {{ bus.driver.name }} {{ bus.driver.last_name }}</span>
            <span v-else>no driver set yet...</span>
          </option>
        </select>
        <small v-for="(error, index) in errors.bus" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="check_out_time">Check out Time</label>
        <input type="datetime-local" class="form-control" id="check_out_time" v-model="journey.check_out_time" required maxlength="6" minlength="6"/>
        <small v-for="(error, index) in errors.check_out_time" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="row">
        <div class="col">
          <router-link
              class="btn btn-primary mt-4"
              :to="{name: 'Journeys'}"
          >
            <i class="bi bi-arrow-left"></i> Back
          </router-link>
        </div>
        <div class="col d-flex flex-row-reverse">
          <button class="btn btn-success mt-4"><i class="bi bi-check"></i> Save</button>
        </div>
      </div>
    </form>
    <div v-if="journey.id">
      <div class="row mt-5">
        <div class="col">
          <h2>Tickets</h2>
        </div>
        <div class="col">
          <div class="d-flex flex-row-reverse">
            <router-link
                class="btn btn-success float-right"
                :to="{name: 'TicketsEdit', params: {journeyId: journey.id, id: 'new'}}"
            >
              <i class="bi bi-plus-circle"></i> New
            </router-link>
          </div>
        </div>
      </div>
      <table class="table table-bordered mb-5">
        <thead>
        <tr>
          <th>#</th>
          <th width="23%">Passenger</th>
          <th width="5%">Seat</th>
          <th width="23%">Bus</th>
          <th width="23%">Driver</th>
          <th width="26%">Date</th>
          <th>Actions</th>
        </tr>
        </thead>
        <tbody>
        <tr v-if="tickets.length === 0">
          <td colspan="7">No tickets found</td>
        </tr>
        <tr
            v-for="ticket in tickets"
            :key="ticket.id"
        >
          <td>{{ ticket.id }}</td>
          <td>
            ASDSA
          </td>
          <td align="center">{{ ticket.seat }}</td>
          <td>
            License plate: <strong>{{ journey.bus.license_plate }}</strong>
          </td>
          <td>
            <span v-if="journey.bus.driver">
              {{ journey.bus.driver.name }} {{ journey.bus.driver.last_name }}
            </span>
            <span v-else>No driver set yet...</span>
          </td>
          <td>{{ journey.check_out_time }}</td>
          <td>
            <div class="btn-group">
              <router-link
                  title="Edit"
                  class="btn btn-warning"
                  :to="{name: 'TicketsEdit', params: {journeyId: journey.id, id: ticket.id}}"
              >
                <i class="bi bi-eye"></i>
              </router-link>
              <button
                  title="Delete"
                  class="btn btn-danger"
                  @click="deleteTicket(ticket.id)"
              >
                <i class="bi bi-trash"></i>
              </button>
            </div>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import APIService from "@/common/api.service"

export default {
  name: "JourneysEdit",
  data() {
    return {
        journey: {
        id: null,
        route: null,
        bus: null,
        check_out_time: null
      },
      route_id: null,
      bus_id: null,
      buses: [],
      routes: [],
      tickets: [],
      errors: {
        route: [],
        bus: [],
        check_out_time: []
      }
    }
  },
  mounted() {
    this.fetchRoutes()
    this.fetchBuses()
    const id = this.$route.params.id;
    if (id !== "new") {
      this.fetchJourney(id)
      this.fetchTickets(id)
    }
  },
  methods: {
    async fetchRoutes() {
      await APIService.getAll(`routes`).then(response => {this.routes = response.data.results}).catch(e => {console.log(e)})
  },
  async fetchBuses() {

    await APIService.getAll(`buses`).then(response => {this.buses = response.data.results}).catch(e => {console.log(e)})
  },
  
  async fetchJourney(id){

     await APIService.get('journeys', id).then(response => {
        this.journey =  response.data
        this.bus_id = response.data.bus.id
        this.route_id = response.data.route.id       
      }).catch(e => {console.log(e)})
  },
  async saveJourney() {

      const route = this.routes.find(route => route.id === this.route_id)
      const bus = this.buses.find(bus => bus.id === this.bus_id)
      if (this.journey.id)
        await APIService.update(`journeys`, this.journey.id, {...this.journey, route: route.id, bus: bus.id})
        .then(response => {
          console.log("entro actualizar Journey")
            this.journey =  response.data
            this.$router.push({name: "Journeys"})
           }).catch(e => {this.errors = e.response.data})
      else
        await APIService.create(`journeys`, {...this.journey, route: route.id, bus: bus.id})
        .then(response => {
           this.journey =  response.data 
           this.$router.push({name: "Journeys"})
           }).catch(e => {this.errors = e.response.data})
},
async fetchTickets(id){
  await APIService.getAll(`journeys/${id}/tickets`).then( r => {
    this.tickets = r.data.results
    }).catch( e => console.log(e))
  
},
async deleteTicket(id) {

 await APIService.delete(`journeys/${this.journey.id}/tickets`, id).then(response => {this.fetchTickets(this.journey.id)}).catch(e => {console.log(e)})
}
}
}
</script>

<style scoped></style>