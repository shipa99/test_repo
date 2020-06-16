<template>
    <mu-container>
        <Home></Home>
        <mu-col span='2'>
                <div v-for="patient in patients">
                    <h3 v-if="auth" @click="openMedCard(patient.id)">{{patient.id}} {{patient.surname}} {{patient.name}}</h3>
                    <p>{{patient.birth_date}}</p>
                </div>
        </mu-col>
        <MedCard v-if="med_record.show" :id="med_record.id"></MedCard>
        <mu-col>
               <mu-text-field v-model="form.surname" placeholder="фамилия">
               </mu-text-field>
               <mu-text-field v-model="form.name" placeholder="имя">
               </mu-text-field>
               <mu-text-field v-model="form.patronymic" placeholder="отчество">
               </mu-text-field>
               <input type="datetime" v-model="form.birth_date" placeholder="дата рождения">
               </input>
               <select v-model="form.sex" placeholder="пол">
                  <option>М</option>
                  <option>Ж</option>
               </select>
               <mu-button class="btn-send" round color="success" @click="addPatient">Добавить</mu-button>
        </mu-col>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    import MedCard from '@/components/MedCard.vue'
    import Home from '@/components/Home.vue'

    export default {
        name: 'Patient',
        components: {
            MedCard,
            Home,
        },
        data() {
            return {
                patients: '',
                med_record: {
                    id: '',
                    show: false,
                },
                form: {
                    surname: '',
                    name: '',
                    patronymic: '',
                    birth_date: '',
                    sex: '',
                }
            }
        },
        created() {
            $.ajaxSetup({
                  headers: {'Authorization': "Token" + sessionStorage.getItem('auth_token')},
              });
              this.loadPatient()
        },
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            loadPatient() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/patients/",
                    type: "GET",
                    success: (response) => {
                    this.patients = response.data.data
                    }
                })
            },
            addPatient() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/hospital/patients/",
                    type: "POST",
                    data: {
                        surname: this.form.surname,
                        name: this.form.name,
                        patronymic: this.form.patronymic,
                        birth_date: this.form.birth_date,
                        sex: this.form.sex,

                    },
                    success: (response) => {
                        this.loadPatient()
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            },
            openMedCard(id) {
                this.med_record.id = id
                this.med_record.show = true
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
