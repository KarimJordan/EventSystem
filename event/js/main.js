import Vue from 'vue'

import eventList from './components/event-list.vue'
import eventDetail from './components/event-detail.vue'
import eventForm from './components/event-form.vue'

new Vue({
    el: '#body',
    components: {
        eventList,
        eventDetail,
        eventForm
    }
})