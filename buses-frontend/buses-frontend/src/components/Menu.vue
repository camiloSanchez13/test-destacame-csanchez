<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <li class="navbar-brand">Buses Destacame</li>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/journeys" class="nav-link">Journeys</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/routes" class="nav-link">Routes</router-link>
        </li>

        <li class="nav-item">
          <router-link to="/buses" class="nav-link">Buses</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/drivers" class="nav-link">Drivers</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/passengers" class="nav-link">Passengers</router-link>
        </li>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Menu"
};
</script>
