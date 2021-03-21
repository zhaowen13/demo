<template>
  <div>
    <el-divider content-position="left">{{ form.name }}</el-divider>
    <el-form ref="form" :inline="true" :model="form" label-width="80px">
      <el-form-item label="路径">
        <el-input style="width: 400px" v-model="form.url"></el-input>
      </el-form-item>
      <el-form-item label="请求方式">
        <el-select v-model="form.method" placeholder="请选择请求方式">
          <el-option label="get" value="get"></el-option>
          <el-option label="post" value="post"></el-option>
          <el-option label="put" value="put"></el-option>
          <el-option label="login" value="login"></el-option>
          <el-option label="delete" value="delete"></el-option>
        </el-select>
      </el-form-item>
    </el-form>
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="请求头">
        <el-input
          type="textarea"
          style="width: 500px"
          :autosize="{ minRows: 5, maxRows: 10 }"
          v-model="form.headers"
        ></el-input>
      </el-form-item>
      <el-form-item label="请求体">
        <el-input
          style="width: 500px"
          :autosize="{ minRows: 10, maxRows: 20 }"
          type="textarea"
          v-model="form.body"
        ></el-input>
      </el-form-item>
      <el-form ref="form" :inline="true" :model="form" label-width="80px">
        <el-form-item label="预期结果">
          <el-input style="width: 300px" v-model="form.expected"></el-input>
        </el-form-item>
        <el-form-item label="实际结果">
          <el-input style="width: 300px" v-model="form.actual"></el-input>
        </el-form-item>
      </el-form>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即创建</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  props: ['form'],
  data() {
    return {
      // form:this.case_data,
    };
  },
  methods: {},
};
</script>
<style>

</style>