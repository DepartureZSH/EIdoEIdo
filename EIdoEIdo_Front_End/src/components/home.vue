<template>
  <div class="register" :style="{width: fullWidth+'px', height:fullHeight-64+'px'}">
    <img class="img_box" :src="url"></img>
  </div>
</template>
  
<script>
  import axios from 'axios'
  export default {
    name: 'Home',
    data () {
      return {
        url: require('@/assets/demo.png'),
        fullWidth: document.documentElement.clientWidth,
        fullHeight: document.documentElement.clientHeight
      }
    },
  
    methods: {
      getProjects() {
        axios.get('http://127.0.0.1:8000/api/IELTS1/1/').then(response => {this.UserData = response.data["message"], this.msg = 'get projects data from django api'});
      },
      //定义数据获取方法
      handleResize () {
        this.fullWidth = document.documentElement.clientWidth
        this.fullHeight = document.documentElement.clientHeight
      }
    },
    //两个生命周期中监听窗口大小变化
    //参数1：监听的事件
    //参数2：一个回调函数，用于赋值
    created () {
    window.addEventListener('resize', this.handleResize)
    },
    beforeUnmount () {
      window.removeEventListener('resize', this.handleResize)
    }
  }
</script>

<style scoped>
.register {
  position: fixed;
  text-align: center;
  margin-top: 64px;
  background-color: black; 
  .img_box {
    max-width: 100%;
    max-height: 100%;
    width: auto;
    height: auto;
  }
}
</style>