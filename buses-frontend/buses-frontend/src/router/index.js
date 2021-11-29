import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/journeys',
    alias: "/journeys",
    name: 'Journeys',
    component: () => import("@/views/Journeys")
  },
{
  path: '/journeys/:id',
  name: 'JourneysEdit',
  component: () => import("@/views/JourneysEdit")
},
  {

    path: '/drivers',
    alias: "/drivers",
    name: 'Drivers',
    component: () => import("@/views/Drivers")

  },
  {
    path: '/drivers/:id',
    name: 'DriverEdit',
    component: () => import("@/views/DriversEdit")
    
    
},
{
  path: '/passengers',
  name: 'Passengers',
  component: () => import("@/views/Passengers")
},
{
  path: '/passengers/:id',
  name: 'PassengersEdit',
  component: () => import("@/views/PassengersEdit")
}
,
{
  path: '/buses',
  name: 'Buses',
  component: () => import("@/views/Buses")
}
,
{
  path: '/buses/:id',
  name: 'BusesEdit',
  component: () => import("@/views/BusesEdit")
}
,
{
  path: '/routes',
  name: 'Routes',
  component: () => import("@/views/Routes")
}
,
{
  path: '/routes/:id',
  name: 'RoutesEdit',
  component: () => import("@/views/RoutesEdit")
},
{
  path: '/journeys/:journeyId/tickets/:id',
  name: 'TicketsEdit',
  component: () => import("@/views/TicketsEdit")
}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
