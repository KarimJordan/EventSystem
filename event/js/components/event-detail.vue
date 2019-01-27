<template>
    <div class="container">

        <div class="py-5 text-center">
            <center><h4>EVENT PAGE</h4></center>
        </div>
        <!--<div class="col-sm-3">-->
        <!--<div>-->
        <!--<h1>{{ event.no_of_guest }}</h1>-->
        <!--</div>-->
        <!--</div>-->

        <div class="col-md-8 order-md-1">

            <h4 class="d-flex justify-content-between align-items-center mb-3">
                <span class="text-muted">No. Of Guest</span>
                <span class="badge badge-secondary badge-pill">{{event.no_of_guest}}</span>
            </h4>

            <h4 class="mb-3">
                <span class="text-muted">Event: Name: </span>{{event.name}}</h4>

            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>Venue</th>
                        <th>Start Date</th>
                        <th>End Date</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><p>{{event.venue}}</p></td>
                        <td><p>{{event.start_date}}</p></td>
                        <td><p>{{event.end_date}}</p></td>
                    </tr>
                </tbody>
            </table>

        </div>

        <div class="col-md-6 order-md-1">
            <form method="POST">
                <input type="hidden" name="_method" value="update">
                <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                <button type="submit" class="btn-primary">Update Event</button>
            </form>
        </div>

        <div class="col-md-6 order-md-1">
            <button @click="back_to_events" class="btn btn-secondary"
                    type="button">
                BACK TO EVENTS
            </button>
        </div>

    </div>
</template>
<script type="text/babel">
    export default {
        name: 'EventDetail',
        data() {
            return {
                event: event,
                csrf
            }
        },
        methods: {
            back_to_events() {
                window.location.replace('/events/')
            },
        }
    }
</script>