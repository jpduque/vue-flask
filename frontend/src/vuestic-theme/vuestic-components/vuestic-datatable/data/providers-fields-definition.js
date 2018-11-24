export default {
  tableFields: [
    {
      name: '__component:badge-column',
      title: '',
      dataClass: 'text-center',
      width: '4%'
    },
    {
      name: 'providerId',
      sortField: 'providerId',
      title: 'Provider Id',
      width: '24%'
    },
    {
      name: 'providerName',
      sortField: 'providerName',
      title: 'Provider Name',
      width: '24%'
    }
  ],
  sortFunctions: {
    'name': function (item1, item2) {
      return item1 >= item2 ? 1 : -1
    },
    'email': function (item1, item2) {
      return item1 >= item2 ? 1 : -1
    }
  }
}
