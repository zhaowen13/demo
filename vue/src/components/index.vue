<template>
  <div>
    <!-- Form -->
    <el-button type="text" @click="dialogFormVisible = true">打开嵌套表单的 Dialog</el-button>
    <el-dialog :title="title" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item v-for="item in heades" :key="item" :label="item.label" label-width="120px">
          <el-input v-model="from[item.prop]" style="width:300px" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
export default {
  data() {
    return {
      dialogFormVisible: false,
      title: "收货地址",
       heades: [
        {
          prop: "name",
          label: "用例名称",
        },
        {
          prop: "module",
          label: "所属模块",
        },
        {
          prop: "step",
          label: "操作步骤",
        },
        {
          prop: "rseult",
          label: "预期结果",
        },
        {
          prop: "grade",
          label: "用例等级",
        },
        {
          prop: "execution",
          label: "执行状态",
        },
        {
          prop: "cover",
          label: "覆盖状态",
        },
      ],
      from:{
          date:"",
          name:"111111",
          text:"",
      }
    };
  },
};
</script>
