<template>
  <div>
    <a-row gutter="16">
      <a-col :span="12">
        <a-card :title="card_title">
          <p style="text-align: center">
            <audio class="audio" ref="audio" controls>
              <source src="" />
            </audio>
          </p>
          <p>
            <a-list item-layout="horizontal" bordered :data-source="data">
              <a-list-item slot="renderItem" slot-scope="item, index">
                <a-list-item-meta>
                  <a slot="title" @click="onitemclick(item['title'])">{{ item['title'] }}</a>
                </a-list-item-meta>
              </a-list-item>
            </a-list>
          </p>
        </a-card>
      </a-col>
      <a-col :span="12">
        <a-card title="听写本">
          <p>
            <a-textarea class="info-textarea" v-model="value" :auto-size="{ minRows: 60}" size="large"/>
          </p>
        </a-card>
      </a-col>
    </a-row>
    
  </div>
  
</template>

<script>
import axios from 'axios'
export default {

  data() {
    return {
      data: [],
      card_title: "雅思王听力语料库",
      song_src : null,
      loading: false
    };
  },
  methods: {
    onitemclick(item) {
      let music1 = new Audio();
      music1 = require('./corpus/'+ item + '.mp4');
      this.$refs.audio.src = music1;
      this.$refs.audio.play();
      console.log('./corpus/'+ item + '.mp4')
    },
    fetchData(id){
      axios.get('http://127.0.0.1:8000/api/Listening/dictation/'+id+'/').then(response => {
      this.data = response.data["message"]
      console.log(id, "ok ", this.data.length)
    });
    }
  },
  created () {
    console.log('Dictation---------------->created')
    //获取相关数据
    this.fetchData(1)
  },
  beforeMount () {
    console.log('Dictation---------------->beforeMount')
    //获取相关数据
    this.fetchData(1)
  },
};
</script>
<style>
.info-textarea {
    width: 100%;
    margin-top: 14px;
    border: 1px solid #DDDDDD;
    box-sizing: border-box;
    padding-left: 13px;
    padding-top: 13px;
    resize: none;
    font-family:"微软雅黑";
    font-size: 18px;
    box-shadow: 0px 13px 10px -15px #ccc inset;
};
</style>
