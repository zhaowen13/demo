<template>
  <div class="main">
    <div>
      <el-row>
        <el-col :span="4">
          <el-input
            size="mini"
            placeholder="输入关键字进行过滤"
            v-model="filterText"
            style="width:150px;"
          >
          </el-input>
          <el-tree
            class="filter-tree"
            :data="data"
            :props="defaultProps"
            default-expand-all
            :filter-node-method="filterNode"
            @node-click="getData"
            show-checkbox
            ref="tree"
          >
            <span
              class="custom-tree-node"
              slot-scope="{ node, data }"
              @mouseenter="data.style = 'display:block'"
              @mouseleave="data.style = 'display:none'"
            >
              <span>{{ node.label }}</span>
              <span :style="data.style">
                <el-button
                  type="text"
                  size="mini"
                  icon="el-icon-plus"
                  @click="openAppend(data)"
                >
                </el-button>
                <el-button
                  type="text"
                  size="mini"
                  icon="el-icon-edit"
                  @click="openUpdate(data)"
                >
                </el-button>
                <el-button
                  type="text"
                  size="mini"
                  icon="el-icon-delete"
                  @click="openRemove(node, data)"
                >
                </el-button>
              </span>
            </span>
          </el-tree>
        </el-col>
        <el-col :span="20">
          <mycase :form="set_case_data"></mycase>
        </el-col>
      </el-row>
    </div>
    <div>
      <el-dialog
        title="修改子模块"
        :visible.sync="update_dialog"
        :width="width"
      >
        <el-form :model="form">
          <el-form-item label="子模块名称" :label-width="formLabelWidth">
            <el-input v-model="form.label" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="update_dialog = false">取 消</el-button>
          <el-button type="primary" @click="update">确 定</el-button>
        </div>
      </el-dialog>
    </div>
    <div>
      <el-dialog title="添加子模块" :visible.sync="add_dialog" :width="width">
        <el-form :model="form">
          <el-form-item label="子模块名称" :label-width="formLabelWidth">
            <el-input v-model="form.label" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="add_dialog = false">取 消</el-button>
          <el-button type="primary" @click="append">确 定</el-button>
        </div>
      </el-dialog>
    </div>
    <div>
      <el-dialog title="提示" :visible.sync="del_dialog" width="30%">
        <span>确认要删除此模块吗？？？</span>
        <span slot="footer" class="dialog-footer">
          <el-button @click="del_dialog = false">取 消</el-button>
          <el-button type="primary" @click="remove">确 定</el-button>
        </span>
      </el-dialog>
    </div>
  </div>
</template>
<script>
import mycase from "@/components/case";
export default {
  components: { mycase },
  watch: {
    filterText(val) {
      this.$refs.tree.filter(val);
    },
  },
  data() {
    return {
      filterText: "",
      set_case_data: {},
      form: {
        id: "",
        label: "",
      },
      update_dialog: false,
      add_dialog: false,
      del_dialog: false,
      formLabelWidth: "120px",
      width: "600px",
      id: 1000,
      new_data: {},
      new_node: {},
      data: [
        {
          id: 1,
          label: "熟仁直聘",
          style: "display:none",
          children: [
            {
              id: 4,
              label: "精选",
              style: "display:none",
              children: [
                {
                  id: 9,
                  label: "case名称",
                  style: "display:none",
                },
                {
                  id: 10,
                  label: "三级 1-1-2",
                  style: "display:none",
                },
              ],
            },
            {
              id: 4,
              label: "首页",
              style: "display:none",
              children: [
                {
                  id: 9,
                  label: "case名称",
                  style: "display:none",
                },
                {
                  id: 10,
                  label: "三级 1-1-2",
                  style: "display:none",
                },
              ],
            },
          ],
        },
      ],
      defaultProps: {
        children: "children",
        label: "label",
      },
    };
  },
  methods: {
    filterNode(value, data) {
      if (!value) return true;
      return data.label.indexOf(value) !== -1;
    },
    openAppend(data) {
      this.add_dialog = true;
      this.new_data = data;
    },
    openUpdate(data) {
      this.update_dialog = true;
      this.form.label = data.label;
      this.new_data = data;
    },
    update() {
      this.new_data.label = this.form.label;
      this.update_dialog = false;
    },
    append() {
      const newChild = {
        id: 1000,
        label: this.form.label,
        children: [],
        style: "display:none",
      };
      if (!this.new_data.children) {
        this.$set(this.new_data, "children", []);
      }
      this.new_data.children.push(newChild);
      this.add_dialog = false;
    },
    openRemove(node, data) {
      this.del_dialog = true;
      this.new_node = node;
      this.new_data = data;
    },
    remove() {
      const parent = this.new_node.parent;
      const children = parent.data.children || parent.data;
      const index = children.findIndex((d) => d.id === this.new_data.id);
      children.splice(index, 1);
      this.del_dialog = false;
    },
    getData(data) {
      if (!data.children) {
        this.set_case_data = {
          name: data.label,
          url: "/login",
          method: "post",
          headers: "11111",
          body: "22222",
          expected: "2222",
          actual: "3333",
        };
      }
    },
    onSubmit() {
      console.log("submit!");
    },
  },
};
</script>
<style>
.main {
  height: 99%;
  background-color: white;
}
.custom-tree-node {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 14px;
  padding-right: 8px;
}
.el-input {
  width: 300px;
}
</style>