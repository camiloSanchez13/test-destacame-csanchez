<template>
<div class="container">
    <h1 v-if="ticket.id === null && journey.id">New Ticket for Journey #{{ journey.id }} [{{ journey.route.origin }} - {{ journey.route.destiny }}]</h1>
    <h1 v-else>Ticket Editor for Journey <span v-if="journey.id">#{{ journey.id }} [{{ journey.route.origin }} - {{ journey.route.destiny }}]</span></h1>
    <form @submit.prevent="savePassenger()">
      <div class="form-group">
        <label for="passenger">Passenger</label>
        <select class="form-control" id="passenger" v-model="passengerId" required>
          <option disabled>Select an element</option>
          <option
              v-for="passenger in passengers"
              :value="passenger.id"
              :key="passenger.id"
              :selected="passenger.id === passengerId"
          >
            {{ passenger.name }} {{ passenger.last_name }}
          </option>
        </select>
        <small v-for="(error, index) in errors.passenger" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="seat">Seat</label>
        <select class="form-control" id="seat" v-model="seat" required>
          <option disabled v-if="seats.length > 0">Select an element</option>
          <option disabled v-else>Sold Out!</option>
          <option
              v-for="seat_ in seats"
              :value="seat_"
              :key="seat_"
              :selected="seat_ === ticket.seat"
          >
            {{ seat_ }}
          </option>
        </select>
        <small v-for="(error, index) in errors.seat" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="row">
        <div class="col">
          <router-link
              class="btn btn-primary mt-4"
              :to="{name: 'Journeys'}"
          >
            <i class="bi bi-arrow-left"></i> Back
          </router-link>
          &nbsp;
          <router-link
              class="btn btn-primary mt-4"
              :to="`/journeys/${journey.id}`"
          >
            <i class="bi bi-arrow-left"></i> Back To The Journey
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
  name: "TicketsEdit",
  data() {
    return {
      ticket: {
        id: null,
        journey: null,
        passenger: null,
        seat: null
      },
      journeyId: null,
      journey: {
        id: null
      },
      passengers: null,
      passengerId: null,
      seat: null,
      seats: [],
      errors: {
        passenger: [],
        seat: []
      }
    }
  },
  mounted() {

    this.journeyId = this.$route.params.journeyId

    this.fetchJourney()
    this.fetchPassengers()
    const id = this.$route.params.id

    if (id !== 'new') this.fetchTicket(id)
  },
  methods: {
    async fetchTicket(id) {

      await APIService.get(`journeys/${this.journeyId}/tickets`, id).then( r => {

        this.ticket = r.data
        this.passengerId = r.data.passenger.id
        this.seat = r.data.seat

      }).catch(e => {console.log(e)})

    },
    async fetchJourney() {
        console.log("ento al fetch journey")
        await APIService.get(`journeys`, this.journeyId).then(response => {
            this.journey = response.data
            this.seats = response.data.dispo_seats
            
            }).catch(e => {console.log(e)})
    },
    async fetchPassengers() {
      await APIService.getAll(`passengers`).then(r => { this.passengers = r.data.results }).catch(e => {console.log(e)})
    },
    async savePassenger() {
      if (this.ticket.id)
        await APIService.update(`journeys/${this.journeyId}/tickets`, this.ticket.id, {passenger: this.passengerId, seat: this.seat, journey: this.journeyId}).catch(e => {this.errors = e.response.data})
      else
        await APIService.create(`journeys/${this.journeyId}/tickets`, {passenger: this.passengerId, seat: this.seat, journey: this.journeyId}).catch(e => {this.errors = e.response.data})
    }
  }
}
</script>

<style scoped>

</style>