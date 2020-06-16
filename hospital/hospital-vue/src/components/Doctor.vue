<template>
    <mu-container>
        <Home></Home>
        <mu-col>
            <div v-for="doc in doctors">
                <h3>{{doc.surname}} {{doc.name}} {{doc.patronymic}}</h3>
                <p>{{doc.education}}</p>
                <p>{{doc.category}}</p>
            </div>
        </mu-col>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    import Home from '@/components/Home.vue'

    export default {
        name: 'Doctor',
        components: {
            Home,
        },
        data() {
            return {
                doctors: '',
            }
        },
        created() {
            $.ajaxSetup({
                  headers: {'Authorization': "Token" + sessionStorage.getItem('auth_token')},
              });
              this.loadDoctor()
        },
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            loadDoctor() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/doctors/",
                    type: "GET",
                    success: (response) => {
                    this.doctors = response.data.data
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
