import Vue from 'vue'
import React from 'react'

// import all the vue components and consolidate it under one main.js which is to be compiled/repacked by webpack.
import eventList from './components/event-list.vue'
import eventDetail from './components/event-detail.vue'
import eventForm from './components/event-form.vue'

new Vue({
    // entry point based on what defined in base.html
    el: '#body',
    components: {
        eventList,
        eventDetail,
        eventForm
    }
})