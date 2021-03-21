<template>
  <div>
    <table border="1">
      <tr>
        <th v-for="heade in heades" :key="heade">{{heade}}</th>
      </tr>
      <tr v-for="data in tableData" :key="data">
        <td v-for="heade in data" :key="heade">
          <!-- <el-input v-model="user" placeholder="审批人"></el-input> -->
          <span> {{heade}}</span>
         
        </td>
      </tr>
    </table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      heades: [
        "用例编号",

        "用例名称",

        "模块",

        "操作步骤",

        "预期结果",

        "执行情况",

        "覆盖情况",
      ],
      tableData: [
        {
          no: "2016-05-02",
          name: "第二页",
          module: "第二页第二页第二页第二页第二页",
          show: false,
        },
        {
          no: "2016-05-04",
          name: "第二页",
          module: "第二页第二页第二页第二页第二页",
          show: false,
        },
        {
          no: "2016-05-01",
          name: "第二页",
          module: "第二页第二页第二页第二页第二页",
          show: false,
        },
        {
          no: "2016-05-03",
          name: "第二页",
          module: "第二页第二页第二页第二页第二页",
        },
      ],
    };
  },
  methods: {
    update(row, column, cell, event) {
      row.show = true;
    },
  },
};
</script>