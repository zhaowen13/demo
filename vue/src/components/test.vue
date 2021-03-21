 <template>
  <mytable :data="set_data"></mytable>
</template>
<script>
import mytable from "@/components/table";
export default {
  components: { mytable },
  data() {
    return {
      set_data: {
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
            prop: "result",
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
        tableData: [],
        dialogFormVisible: false,
        title: "新增用例",
        from: {},
      },
    };
  },
};
</script>