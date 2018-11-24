<template>
  <div class="providers">
    <div class="row">
      <div id="providersForm" class="col-md-12">
        <vuestic-widget :headerText="'forms.inputs.title' | translate">
          <form>
            <div class="row">
              <div class="col-md-4">
                <fieldset>
                  <div class="form-group">
                    <div class="input-group">
                      <input ref="providerId" type="number" required/>
                      <label class="control-label" for="simple-input">{{'forms.inputs.providerId' | translate}}</label><i class="bar"></i>
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="input-group">
                      <input ref="providerName" required/>
                      <label class="control-label" for="simple-input">{{'forms.inputs.providerName' | translate}}</label><i class="bar"></i>
                    </div>  
                  </div>
                </fieldset>
              </div> 
            </div>
          <div class="row btn-margin-row">
            <div class="col-sm-6 col-lg-6 col-xl-3 d-flex justify-content-center">
              <button class="btn btn-primary" @click="sendData()" type="submit"> {{'buttons.button' | translate}}</button>
            </div>
          </div>
          </form>
        </vuestic-widget>
      </div>
    </div>
  </div>
</template>

<script>
import CountriesList from "data/CountriesList";

const apiUrl = "/api/providers";

export default {
  name: "providers",
  computed: {},
  methods: {
    clearField() {
      this.$refs.providerId.value = '';
      this.$refs.providerName.value = '';
    },

    sub: function(event) {
      this.log(this.field.providerId);
    },
    sendData() {
      const providerId = this.$refs.providerId.value;
      const providerName = this.$refs.providerName.value;
      if (providerId && providerName) {
        if (!isNaN(providerId)) {
          const data = { providerId, providerName };
          fetch(apiUrl, {
            method: "POST", // or 'PUT'
            body: JSON.stringify(data), // data can be `string` or {object}!
            headers: {
              "Content-Type": "application/json"
            }
          })
            .then(res => {
              if (res.status == 200) {
                console.log("Success");
                this.clearField();
              } else {
                alert("Error on saving data, check the data and retry")
              }
              return res.json();
            })
            .then(res => console.log('msg: ', res))
            .catch(error => console.error("Error:", error));
        } else {
          alert("el campo id debe ser numerico");
        }
      } else {
        alert("algunos de los campos esta vacio");
      }
    }
  },
  created() {
    this.$nextTick(() => {
      this.$validator.validateAll();
    });
  }
};
</script>
