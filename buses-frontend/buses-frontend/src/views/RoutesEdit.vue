<template>
  <div class="container">
    <h1 v-if="route.id === null">New Route</h1>
    <h1 v-else>Route Editor</h1>
    <form @submit.prevent="saveRoute()">
      <div class="form-group mt-4">
        <label for="origin">Origin</label>
        <input type="text" class="form-control" id="origin" v-model="route.origin" required/>
        <small v-for="(error, index) in errors.origin" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="form-group mt-4">
        <label for="destiny">Destiny</label>
        <input type="text" class="form-control" id="destiny" v-model="route.destiny" required/>
        <small v-for="(error, index) in errors.destiny" :key="index" class="d-block text-danger">{{ error }}</small>
      </div>
      <div class="row">
        <div class="col">
          <router-link
              class="btn btn-primary mt-4"
              :to="{name: 'Routes'}"
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
  name: "RoutesEdit",
  data() {
    return {
      route: {
        id: null,
        origin: null,
        destiny: null
      },
      errors: {
        origin: [],
        destiny: []
      }
    };
  },
  mounted() {
    const id = this.$route.params.id;
    if (id !== "new")
      this.fetchRoute(id);
  },
  methods: {
    async fetchRoute(id) {
        await APIService.get('routes', id).then(r => {this.route = r.data}).catch(e => console.log(e))
    },
    async saveRoute() {
      if (this.route.id)
        await APIService.update(`routes`, this.route.id, this.route).then(r => {
          this.route = r.data
          this.$router.push({name: "Routes"}
          )}).catch(e => {this.errors = e.response.data})
      else
        await APIService.create(`routes`, this.route).then(r => {
          this.route = r.data
          this.$router.push({name: "Routes"})
          }).catch(e => {this.errors = e.response.data})
    }
  }
}
</script>

<style scoped>

</style>