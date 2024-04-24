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
            >
              <a-sub-menu key="sub1">
                <span slot="title"><a-icon type="like" />Practice</span>
                <a-menu-item key="1">
                  雅思词汇
                </a-menu-item>
                <a-menu-item key="2">
                  我的辞典
                </a-menu-item>
              </a-sub-menu>
              <a-sub-menu key="sub2">
                <span slot="title"><a-icon type="file-text" />Corpus</span>
                <a-menu-item key="3">
                    雅思词汇
                </a-menu-item>
                <a-menu-item key="4">
                    我的辞典
                </a-menu-item>
              </a-sub-menu>
              <a-sub-menu key="sub3">
                <span slot="title"><a-icon type="setting" />Settings</span>
                <a-menu-item key="3">
                  Audio
                </a-menu-item>
                <a-menu-item key="4">
                  Others
                </a-menu-item>
              </a-sub-menu>
            </a-menu>
          </a-layout-sider>
          <a-layout-content :style="{ padding: '0 24px', minHeight: '280px' }">
            Content
          </a-layout-content>
        </a-layout>
      </a-layout-content>
    </a-layout>
</template>

<style>

</style>