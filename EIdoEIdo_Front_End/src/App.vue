<template>
  <a-layout id="components-layout-demo-top-side">
    <a-layout-header class="header">
      <a-row :gutter="[16,16]" type="flex" justify="space-between">
        <a-col :span="4" class="logo">
          <router-link to="/">
            <h3 style="color: #fff;">EIdoEIdo</h3>
          </router-link>
        </a-col>
        <a-col :span="16">
          <div>
            <a-menu
              theme="dark"
              mode="horizontal"
              :selectedKeys="selectedKeys"
              :default-selected-keys="['1']"
              :style="{ lineHeight: '64px'}"
              @select="onselect"
            >
            <!-- <a-menu-item key="0">
              <a-avatar>
                U
              </a-avatar>
            </a-menu-item> -->
            <a-menu-item key="1">
              Listening
            </a-menu-item>
            <a-menu-item key="2">
              Speaking
            </a-menu-item>
            <a-menu-item key="3">
              Writing(void)
            </a-menu-item>
            <a-menu-item key="4">
              Reading(void)
            </a-menu-item>
            <a-menu-item key="5">
              Vocabulary
            </a-menu-item>
            </a-menu>
          </div>
        </a-col>
        <a-col :span="4" style="float: left;">
          <a-avatar>
            U
          </a-avatar>
          <a-button type="link" ghost>
            Login
          </a-button>
          <a-divider type="vertical" />
          <a-button type="link" ghost>
            Register
          </a-button>
        </a-col>
      </a-row>
    </a-layout-header>
    <router-view/>
    <a-layout-footer style="text-align: center">
      <div>{{ UserData }}</div>
    </a-layout-footer>
  </a-layout>
</template>

<script>
export default {
  name: 'App',
  data(){
    return {
      url: require('@/assets/logo.png'),
      UserData: "Powered by 天南之城"
    }
  },
  methods: {
    onselect(item) {
      if(item["key"]==='1'){
        // console.log("Listening")
        this.$router.replace({
          path: '/Listening',
        })
      }else if(item["key"]==='2'){
        // console.log("Speaking")
        this.$router.replace({
          path: '/Speaking',
        })
      }else if(item["key"]==='3'){
        console.log("Writing(void)")
      }else if(item["key"]==='4'){
        console.log("Reading(void)")
      }else if(item["key"]==='5'){
        console.log("Vocabulary")
        this.$router.replace({
          path: '/Vocabulary',
        })
      }else if(item["key"]==='0'){
        console.log("User Center")
      }else{
        console.log("wrong post")
      }
    }
  }
}

</script>

<style scoped>
#components-layout-demo-top-side .logo {
  width: 120px;
  height: 31px;
  /* margin: 16px 28px 16px 0; */
  float: left;
};
.avatar {
  float: right;;
};

</style>
