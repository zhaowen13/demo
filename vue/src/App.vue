<template>
  <div id="app">
    <div id="head" v-if="status">
      <el-button
        style="color:#FFFFFF;border-color:#545C64;background-color:#545C64;"
        :icon="type"
        @click="setisCollapse()"
      ></el-button>
    </div>
    <div id="main" :style="style">
      <div v-if="status">
      <el-menu 
        :default-active="$route.path"
        mode="vertical"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        @close="handleClose"
        :collapse="isCollapse"
        show-timeout="1"
      > 
        <template  v-for="item in items" >
          <el-submenu :index="item.index" :key="item.index">
            <template slot="title">
              <i :class="item.icon"></i>
              <span slot="title">{{item.title}}</span>
            </template>
            <template v-for="sub in item.subs">
              <el-menu-item :index="sub.index" :key="sub.index" >
                <div @click="addtags(sub)" >
                  <i class="el-icon-remove"></i>
                  <span slot="title">{{ sub.title }}</span>
                </div>
              </el-menu-item>
            </template>
          </el-submenu>
        </template>
      </el-menu>
      </div>
      <el-main style="background-color:#eaedf1">
        <el-tabs v-if="status"
          v-model="editableTabsValue"
          @tab-click="goto"
          type="border-card"
          closable
          @tab-remove="removeTab"
        >
          <el-tab-pane
            v-for="(item, index) in editableTabs"
            :key="item.index"
            :label="item.title"
            :name="item.index"
          ></el-tab-pane>
        </el-tabs>
        <router-view></router-view>
      </el-main>
    </div>
    <div id="bottom" v-if="status"></div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      status: true,
      background:"background-color:#46A3FF",
      style:"display: flex;height: 90%;width: 100%;",
      editableTabsValue: "",
      editableTabs: [],
      tabIndex: 1,
      isCollapse: false,
      type: "el-icon-s-fold",
      items: [
        {
          icon: "el-icon-s-order",
          index: "3",
          title: "任务管理",
          subs: [
            {
              index: "/test",
              title: "用例管理",
            },
            {
              index: "/index",
              title: "基本表单",
            },
          ],
        },
        {
          icon: "el-icon-s-platform",
          index: "dashboard",
          title: "测试",
          subs: [
            {
              index: "tags",
              title: "UI测试",
            },
            {
              index: "apptest",
              title: "APP测试",
            },
            {
              index: "apitest",
              title: "API测试",
            },
          ],
        },
        {
          icon: "el-icon-s-tools",
          index: "table",
          title: "配置管理",
        },
        {
          icon: "el-icon-user-solid",
          index: "tabs",
          title: "权限管理",
        },
      ],
    };
  },
  created: function () {
    if (this.$route.path == "/login"||this.$route.path == "/login/") {
      this.status = false;
      this.style="display: flex;height:100%;width: 100%;";
    }
    //在页面创建时执行
    // if (JSON.stringify(localStorage != "{}")) {
    //   this.editableTabs.push(JSON.parse(localStorage.getItem("editableTabs"))); //localStorage中的数据存到editableTabs中
    // }
    if (this.editableTabs.length == 0) {
      // editableTabs如果为空就添加路由到标签页
      if (this.items) {
        //遍历之前先判断数组是否为空不然会报错
        this.items.forEach((element) => {
          if (element.subs) {
            element.subs.forEach((sub) => {
              if (sub.index == this.$route.path) {
                //找到路由对应的标题加到标签页中
                this.editableTabs.push({
                  index: sub.index,
                  title: sub.title,
                });
              }
            });
          }
        });
      }
    }
    this.editableTabsValue = this.$route.path; //设置路由为当前标签选中页
    console.log(this.editableTabsValue);
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    setisCollapse() {
      //菜单是否折叠
      this.isCollapse = !this.isCollapse;
    },
    addtags(sub) {
      //点击菜单调用添加标签页面方法，并把数据存到localStorage中  也可以用select方法回调
      let findItem = this.editableTabs.find((item) => item.index == sub.index); //查找editableTabs中的标签页，如果标签页已经存在则不添加
      if (!findItem) {
        this.editableTabs.push({
          index: sub.index,
          title: sub.title,
        });
      }
      localStorage.setItem("editableTabs", JSON.stringify(this.editableTabs));
      this.editableTabsValue = sub.index;
      this.$router.push(sub.index); //跳转到添加的页面
    },
    removeTab(targetName) {
      //删除标页面
      let tabs = this.editableTabs;
      let activeName = this.editableTabsValue;
      if (activeName === targetName) {
        tabs.forEach((tab, index) => {
          if (tab.index === targetName) {
            let nextTab = tabs[index + 1] || tabs[index - 1];
            if (nextTab) {
              activeName = nextTab.index;
            }
          }
        });
      }
      this.editableTabsValue = activeName;
      this.editableTabs = tabs.filter((tab) => tab.index !== targetName);
      localStorage.setItem("editableTabs", JSON.stringify(this.editableTabs));
    },
    goto(tab) {
      //点击标签页，跳转路由
      this.$router.push(tab.name);
    },
  },
};
</script>

<style>
#app {
  height: 100%;
  width: 100%;
}
#head,
#bottom {
  height: 5%;
  background: #545c64;
}

.el-menu {
  border-color: #545c64;
  height: 100%;
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 100%;
}
.el-menu-item.is-active {
          color: #0080FF;
          background-color: #4A5259 !important;
        }
</style>

