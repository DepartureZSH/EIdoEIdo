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
                雅思王听力
              </a-menu-item>
            </a-sub-menu>
            <a-sub-menu key="sub2">
              <span slot="title"><a-icon type="file-text" />Corpus</span>
              <a-menu-item key="2">
                雅思王听力
              </a-menu-item>
            </a-sub-menu>
            <a-sub-menu key="sub3">
              <span slot="title"><a-icon type="setting" />Settings</span>
              <a-menu-item key="3">
                Audio(void)
              </a-menu-item>
              <a-menu-item key="4">
                Others(void)
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
        console.log("Pratice 雅思王听力")
        this.$router.replace({
          path: '/Listening/Dictation',
        })
      }else if(item["key"]==='2'){
        console.log("Corpus 雅思王听力")
        this.$router.replace({
          path: '/Listening/Corpus',
        })
      }else if(item["key"]==='3'){
        console.log("Settings Audio(void)")
      }else if(item["key"]==='4'){
        console.log("Settings Others(void)")
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