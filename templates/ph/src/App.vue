<template>
  <div id="app" class="container">
      <div>
        <form>
          <div class="form-group">
            <label for="red_val">Enter Red Value</label>
            <input type="text" class="form-control" v-model.number="r"
              id="red_val" placeholder="Enter value between 0 & 255">
          </div>
          <div class="form-group">
            <label for="green_val">Enter Green Value</label>
            <input type="text" class="form-control" v-model.number="g"
              id="green_val" placeholder="Enter value between 0 & 255">
          </div>
          <div class="form-group">
            <label for="blue_val">Enter Blue Value</label>
            <input type="text" class="form-control" v-model.number="b"
              id="blue_val" placeholder="Enter value between 0 & 255">
          </div>
          <button @click.prevent="send" class="btn btn-primary">Submit</button>
          <button id="capture" @click.stop.prevent="link">capture</button>
        </form>
        <h4 class="highlight">{{ msg }}</h4>
        <video id="player" autoplay width="100" height="100"></video>
        <canvas id="canvas" width="100" height="100" style="border: 5px solid black">
        </canvas>
        <br>
        <div>
          <!-- <img src="img.png" alt="" width="200px"> -->
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      msg: 'Hello!',
      r: null,
      g: null,
      b: null,
    };
  },
  methods: {
    sendData(payload) {
      const path = 'http://127.0.0.1:5000/predict';
      console.log(payload);
      axios.post(path, payload)
        .then((res) => {
          this.msg = `Predicted pH value is - ${res.data.prediction}`;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    send() {
      const payload = {
        r: this.r,
        g: this.g,
        b: this.b,
      };
      console.log(payload);
      this.sendData(payload);
    },
    link() {
      console.log('hi');
      document.getElementById('canvas').getContext('2d').drawImage(document.getElementById('player'), 0, 0, 100, 100);
    },
  },
  mounted() {
    const constraints = { video: true };

    navigator.mediaDevices.getUserMedia(constraints).then((stream) => {
      document.getElementById('player').srcObject = stream;
    });
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 2rem;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
