<template>
    <div>
      <a-row gutter="16">
        <a-col :span="12">
          <a-card :title="card_title">
            <p style="text-align: center">
              <audio class="audio" ref="audio" controls @ended="handleNext()">
                <source src="" />
              </audio>
            </p>
            <p style="text-align: center">Part 1</p>
            <p>
              <a-list item-layout="horizontal" bordered :data-source="IELTS1Topicdata">
                <a-list-item slot="renderItem" slot-scope="item, index">
                  <a-list-item-meta>
                    <a slot="title" @click="onitemclick1(item.id)">{{ item.Topic }}</a>
                  </a-list-item-meta>
                </a-list-item>
              </a-list>
            </p>
            <p style="text-align: center">Part 2</p>
            <p>
              <a-list item-layout="horizontal" bordered :data-source="IELTS23Topicdata">
                <a-list-item slot="renderItem" slot-scope="item, index">
                  <a-list-item-meta>
                    <a slot="title" @click="onitemclick2(item.id)">{{ item.Topic }}</a>
                  </a-list-item-meta>
                </a-list-item>
              </a-list>
            </p>
            <p style="text-align: center">Part 3</p>
            <p>
              <a-list item-layout="horizontal" bordered :data-source="IELTS23Topicdata">
                <a-list-item slot="renderItem" slot-scope="item, index">
                  <a-list-item-meta>
                    <a slot="title" @click="onitemclick3(item.id)">{{ item.Topic }}</a>
                  </a-list-item-meta>
                </a-list-item>
              </a-list>
            </p>
          </a-card>
        </a-col>

        <a-col :span="12">
          <a-card title="Questions">
            <a slot="extra">
              <a-switch
                checked-children="Not Show Questions" 
                un-checked-children="Show Questions"
                :checked="Show_question"
                @change="triggerShowQuestions"
              />
            </a>
            <div v-if="Show_question||Show_description">
              <p v-for="item in Questions" @click="onclickQuestion(item.id)">
                <strong>{{item.Question}}</strong>
              </p>
            </div>
            <a-list v-else item-layout="horizontal" :data-source="data">
              <a-list-item slot="renderItem" slot-scope="item, index">
                <a-list-item-meta>
                </a-list-item-meta>
              </a-list-item>
            </a-list>
            <p v-if="Show_description" v-for="item in Requirements">
              {{item}}
            </p>
          </a-card>
          <a-card title="Notes">
            <p>
              You are allowed to write down notes only in Part 2.
              <a-textarea class="info-textarea" v-model="value" :auto-size="{ minRows: 8}"/>
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
        IELTS1Topicdata: [],
        IELTS23Topicdata: [],
        Questions: [],
        Requirements: [],
        src_list: [],
        Show_question: false,
        Show_description: false,
        card_title: "IELTS Mock Speaking Exam",
        song_src : null,
        loading: false
      };
    },
    methods: {
      onitemclick1(item) {
        axios.get('http://127.0.0.1:8000/api/IELTS/detail/1/'+item+'/').then(response => {
          this.Show_description = false  
          console.log(response.data)
          this.Questions = response.data
          this.src_list = []
          this.src_list.push('./corpus/IELTS1/introduce/question'+ (response.data[0].id) + '.wav')
          for(var i=1;i<response.data.length;i++){
            this.src_list.push('./corpus/IELTS1/question'+ (response.data[i].id) + '.wav')
          }
          console.log(this.src_list)
        });
      },
      onitemclick2(item) {
        console.log(item)
        axios.get('http://127.0.0.1:8000/api/IELTS/detail/2/'+item+'/').then(response => {
            console.log(response.data)
            this.Questions = response.data
            this.Requirements = response.data[0].Requirement.split('\n')
            console.log(this.Requirements)
            this.Show_description = true
            this.src_list = []
            for(var i=0;i<response.data.length;i++){
              this.src_list.push('./corpus/IELTS2/question'+ (response.data[i].id) + '.wav')
            }
            console.log(this.src_list)
        });
      },
      onitemclick3(item) {
        console.log(item)
        axios.get('http://127.0.0.1:8000/api/IELTS/detail/3/'+item+'/').then(response => {
            this.Show_description = false
            console.log(response.data)
            this.Questions = response.data
            this.src_list = []
            this.src_list.push('./corpus/IELTS3/introduce/question'+ (response.data[0].Topic) + '_1.wav')
            for(var i=1;i<response.data.length;i++){
              this.src_list.push('./corpus/IELTS3/question'+ (response.data[i].Topic) + '_'+(i+1)+'.wav')
            }
            console.log(this.src_list)
        });
      },
      handleNext(){

      },
      audio_play(src){
        let music1 = new Audio();
        music1 = require(src);
        this.$refs.audio.src = music1;
        this.$refs.audio.play();
      },
      triggerShowQuestions(ShowQuestions){
        this.Show_question = ShowQuestions
      },
      onclickQuestion(id){
        console.log(id)
      },
      fetchIELTS1Data(id){
        axios.get('http://127.0.0.1:8000/api/IELTS/1/'+id+'/').then(response => {
            console.log(response.data)
            this.IELTS1Topicdata = response.data
        });
      },
      fetchIELTS23Data(id){
        axios.get('http://127.0.0.1:8000/api/IELTS/23/'+id+'/').then(response => {
            console.log(response.data)
            this.IELTS23Topicdata = response.data
        });
      }
    },
    created () {
      console.log('Dictation---------------->created')
      //获取相关数据
      this.fetchIELTS1Data(0)
      this.fetchIELTS23Data(0)
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
  