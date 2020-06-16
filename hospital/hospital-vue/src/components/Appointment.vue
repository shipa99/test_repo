<template>
    <mu-container>
        <Home></Home>
        <mu-col>
            <div v-for="app in apps">
                <h2>Прием # {{app.id}}</h2>
                <h3>Врач – {{app.doc.surname}} {{app.doc.name}} {{app.doc.patronymic}}</h3>
                <p>Пациент – {{app.patient.surname}}</p>
                <p>Время приема: {{app.date}} {{app.time}}</p>
            </div>
        </mu-col>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Home from '@/components/Home.vue'

    export default {
        name: 'Appointment',
        components: {
            Home,
        },
        data() {
            return {
                apps: '',
            }
        },
        created() {
            $.ajaxSetup({
                  headers: {'Authorization': "Token" + sessionStorage.getItem('auth_token')},
              });
              this.loadApp()
        },
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            loadApp() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/apps/",
                    type: "GET",
                    success: (response) => {
                    this.apps = response.data.data
                    }
                })
            }
        }
    }
</script>

<style scoped>

h3 {
        cursor: pointer;
    }
    .patients-list {
        margin: 0 10px 0 0;
        box-shadow: 1px 4px 5px #848181;
    }

</style>
