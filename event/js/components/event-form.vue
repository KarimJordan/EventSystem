<template>
    <div class="col-md-6 order-md-1">
        <form method="POST" role="form">
            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
            <input v-if="event.name" type="hidden" name="_method" value="update"    />
            <div class="container">
                <h3>Event Details</h3>
                <div class="row">
                    <form-cell v-model="event.name" title="Event Name" dateTitle=""
                               name="name"
                               type="input"
                               :required="true" :autofocue="true"/>
                </div>

                <div class="row">
                    <form-cell value="" title="Venue" dateTitle=""
                               name="venue" type="input"
                               v-model="event.venue"
                               :required="true" :autofocus="true"/>
                </div>

                <div class="row">
                    <form-cell value="" title="No. Of Guest" dateTitle=""
                               name="no_of_guest" type="number"
                               v-model="event.no_of_guest"
                               :required="false" :autofocus="false"/>
                </div>

                <div class="row">
                    <form-cell value="" title="Start Date" dateTitle=""
                               name="start_date" type="date"
                               v-model="event.start_date"/>
                </div>

                <div class="row">
                    <form-cell value="" title="End Date" dateTitle=""
                               name="end_date" type="date"
                               v-model="event.end_date"/>
                </div>

                <div class="row">
                    <div class="col-sm-6">
                        <ul class="list-inline">
                            <li>
                                <button class="btn btn-primary" type="submit">SAVE EVENT</button>
                            </li>
                            <li>
                                 <button @click="cancel_button" class="btn btn-block btn-preview btn-ignore"
                                        type="button">
                                    CANCEL
                                </button>
                            </li>
                        </ul>
                    </div>
                </div>

            </div>
        </form>
    </div>
</template>
<script type="text/babel">

    import FormCell from '../../../core/js/components/form-cell.vue'

    export default {
        name: 'EventForm',
        data() {
            return {
                event: event,
                csrf
            }
        },
        components: {FormCell},
        methods: {
            cancel_button() {
                if(this.event.name != null){
                    let url = '/events/' + this.event.id + '/'
                    window.location.replace(url);
                }else{
                    window.location.replace('/events/');
                }

            },
        }
    }
</script>