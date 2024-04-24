<template>
    <a-layout id="components-layout-demo-top-side">
      <a-layout-content style="padding: 0 0px">
        <a-layout style="padding: 24px 0; background: #fff">
          <a-layout-sider width="200" style="background: #fff">
            <a-menu
              mode="inline"
              :default-selected-keys="['1']"
              :default-open-keys="['sub1']"
              style="height: 100%"
              @click="handleClick"
            >
              <a-sub-menu key="sub1">
                <span slot="title"><a-icon type="like" />Practice</span>
                <a-menu-item key="1">
                  Mock-exam
                </a-menu-item>
                <a-menu-item key="2">
                  Mock Part 1
                </a-menu-item>
                <a-menu-item key="3">
                  Mock Part 2&3
                </a-menu-item>
                <a-menu-item key="4">
                  Quick Test
                </a-menu-item>
              </a-sub-menu>
              <a-sub-menu key="sub2">
                <span slot="title"><a-icon type="file-text" />Corpus</span>
                <a-menu-item key="5">
                  IELTS part 1
                </a-menu-item>
                <a-menu-item key="6">
                  IELTS part 2&3
                </a-menu-item>
                <a-menu-item key="7">
                  Quick Test
                </a-menu-item>
              </a-sub-menu>
              <a-sub-menu key="sub3">
                <span slot="title"><a-icon type="setting" />Settings</span>
                <a-menu-item key="8">
                  Audio
                </a-menu-item>
                <a-menu-item key="9">
                  Others
                </a-menu-item>
              </a-sub-menu>
            </a-menu>
          </a-layout-sider>
          <a-layout-content :style="{ padding: '0 24px', minHeight: '280px' }">
            <router-view/>
          </a-layout-content>
        </a-layout>
      </a-layout-content>
    </a-layout>
</template>

<script>
export default {
  methods: {
    handleClick(item) {
      if(item["key"]==='1'){
        console.log("Mock-exam")
        this.$router.replace({
          path: '/Speaking/Mock_exam/',
        })
      }else if(item["key"]==='2'){
        console.log("Mock Part 1")
        this.$router.replace({
          path: '/Speaking/Mock_Part1/',
        })
      }else if(item["key"]==='3'){
        console.log("Mock Part 2&3")
      }else if(item["key"]==='4'){
        console.log("Quick Test")
      }else if(item["key"]==='5'){
        console.log("IELTS part 1 Corpus")
      }else if(item["key"]==='6'){
        console.log("IELTS part 2&3 Corpus")
      }else if(item["key"]==='7'){
        console.log("Quick Test")
      }else if(item["key"]==='8'){
        console.log("Audio")
      }else if(item["key"]==='9'){
        console.log("Others")
      }else{
        console.log("wrong post")
      }
    },
  },
  // beforeCreate () {
  //   console.log('Listening---------------->beforeCreate')
  // },
  // created () {
  //   console.log('Listening---------------->created')
  // },
  beforeMount () {
    console.log('Listening---------------->beforeMount')
    //获取相关数据
  },
  mounted () {
    console.log('Listening---------------->mounted')
  },
  // beforeUpdate () {
  //   console.log('Listening---------------->beforeUpdate')
  // },
  // updated () {
  //   console.log('Listening---------------->updated')
  // },
};

</script>

<style>

</style>
  
  