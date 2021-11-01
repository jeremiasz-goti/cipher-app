<template>
  <div class="Cipher">
  
        <div class="form-group">
            <label for="encode">Zakoduj wiadomość: </label><br/>
            <div class="input-group pt-1">
              <input id="encode" style="text-align:center;" class="amounts" type="text" v-model="encode" placeholder="Twoja wiadomość"
                     min="0">
            </div>

            <label for="shift">Przestawienie: </label><br/>
            <div class="input-group pt-1">
              <input id="shift" class="amounts" style="text-align:center;" type="text" v-model="shift" placeholder="wpisz liczbe"
                     min="0">
            </div>

            



            <h4> Twoja wiadomość :</h4>
            <h4> {{ encrypted }} </h4>
            <h4> Klucz: {{ this.shift }}  </h4>
            <br>
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" @click="encodeText()">Zakoduj</button>
            <br><br>
          </div>
       

  </div>
</template>

<script>
export default {
  name: 'Cipher',
  data() {
    return {
      encode: '',
      shift: '',
      encrypted: ''
    }
  },
  methods : {
    encodeText() {
      fetch("http://127.0.0.1:5000/encode/msg=" + this.encode + "&shift=" + this.shift )
      .then(async response => {
        const apidata = await response.json();        
        this.encrypted = apidata.message;
        this.errorMessage = false;
      })
      .catch(error => {
        this.errorMessage = error;
        console.error(error);
      });
    }
  }
}
</script>

