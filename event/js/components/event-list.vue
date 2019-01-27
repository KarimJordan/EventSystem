<template>
    <div>
        <div class="col-sm-12">
            <table class="table table-striped">
                <thead>
                <tr class="table-active">
                    <th scope="col">Event Name</th>
                    <th scope="col">Venue</th>
                    <th scope="col">Start Date</th>
                    <th scope="col">End Date</th>
                    <th scope="col">No. Of Guest</th>
                    <th col="1"></th>
                </tr>
                </thead>
                <tbody>
                <tr scope="row" v-for="event in events">
                    <td><a :href="event.id + '/'">{{event.name}}</a></td>
                    <td>{{event.venue}}</td>
                    <td>{{event.start_date}}</td>
                    <td>{{event.end_date}}</td>
                    <td>{{event.no_of_guest}}</td>
                    <td>
                        <form :action="/events/ + event.id + '/'" method="post" role="form">
                            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                            <input type="hidden" name="_method" value="delete">
                            <button class="btn btn-danger" type="submit">DELETE EVENT</button>
                        </form>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
        <div class="row">
            <div class="col-md-4 pb-2">
                <form method="post">
                    <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                    <button type="submit" class="btn-primary">Create Event</button>
                </form>
            </div>
        </div>
    </div>
</template>
<script type="text/babel">
    export default {
        name: 'EventList',
        data() {
            return {
                events: events,
                csrf
            }
        },
    }
</script>