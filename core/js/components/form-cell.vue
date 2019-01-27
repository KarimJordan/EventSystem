<template>
    <span>
        <label v-if="title != ''"> {{title}} </label>
        <h3 v-if="dateTitle != ''">{{dateTitle}}</h3>

        <input v-if="type === 'email'"
               :name="name"
               type="email"
               class="form-control"
               :required="required"
               :autofocus="autofocus"
               :value="value"/>

        <input v-if="type === 'input'"
               :name="name"
               type="text"
               class="form-control"
               :placeholder="placeholder"
               :required="required"
               :autofocus="autofocus"
               :value="value"/>

        <input v-if="type === 'number'"
               :name="name"
               type="number"
               class="form-control"
               :placeholder="placeholder"
               :required="required"
               :autofocus="autofocus"
               :value="value"/>

        <input v-if="type === 'date'"
               :name="name"
               type="date"
               class="form-control"
               :required="required"
               :autofocus="autofocus"
               :value="value"/>

    </span>
</template>
<script type="text/babel">
    export default {
        name: 'FormCell',
        props: {
            value: {
                required: false
            },
            placeholder: {
                type: String
            },
            name: {
                default: '',
                type: String
            },
            title: {
                required: false,
            },
            dateTitle: {
                required: false,
            },
            autofocus: {
                default: false,
                type: Boolean
            },
            required: {
                default: false,
                type: Boolean
            },
            type: {
                default: "input",
                type: String
            },
        }
    }
</script>