<template>
  <div class="row">
    <div class="col-xs-12 col-md-12">
      <vuestic-widget :headerText="'otro nombre'">
        <div class="table-responsive">
          <table class="table table-striped first-td-padding">
            <thead>
            <tr>
              <td>ID</td>
              <td>Value</td>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(item, index) in registryList" :key="index">
              <td>{{ item.providerId }}</td>
              <td>{{ item.providerName }}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </vuestic-widget>
    </div>
  </div>
</template>

<script>

const apiUrl = "/api/providers";

export default {
  name: "Table",
  data() {
    return {
      registryList: []
    }
  },
  created() {
    const that = this;
    fetch(apiUrl)
      .then(function(response) {
        return response.json();
      })
      .then(function(myJson) {
        console.log(myJson);
        that.registryList = myJson;
      });
  }
};
</script>

<style lang="scss">
.color-icon-label-table {
  td:first-child {
    width: 1rem;
  }
}
</style>
