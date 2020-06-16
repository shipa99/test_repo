<template>
  <mu-col span='8' xl="9">
      <mu-container class='med_card'>
          <mu-row v-for="med_record in med_records"
                    direction="column"
                    justify-content="start">
              <h3>Лечащий врач – {{med_record.doc.surname}}{{med_record.doc.name}}</h3>
              <p>{{med_record.patient.id}}</p>
              <p>{{med_record.record}}</p>
              <small>{{med_record.date}}</small>
          </mu-row>
      </mu-container>
  </mu-col>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: 'MedCard',
        props: {
          id: ''
        },
        data() {
            return {
                med_records: {}
            }
        },
        created() {
            $.ajaxSetup({
                  headers: {'Authorization': "Token" + sessionStorage.getItem('auth_token')},
              });
              this.loadMedCard()
        },
        methods: {
            loadMedCard() {
                  $.ajax({
                      url: "http://127.0.0.1:8000/api/v1/hospital/med_card/",
                      type: "GET",
                      data: {
                          patient: this.id,
                      },
                      success: (response) => {
                          this.med_records = response.data.data
                      }
                  })
            }
        }
    }
</script>

<style scoped>
    .med_card {
            border: 1px solid #000;
        }
</style>
