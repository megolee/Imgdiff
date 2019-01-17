<template>
  <el-form>
    <el-row type="flex" justify="center">
      <el-col class="label_input">
        <el-form-item label="活动名称">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
      </el-col>
      <el-col>
          <el-upload action="" :show-file-list="false" :auto-upload="false">
            <el-button type="primary">选择文件</el-button>
          </el-upload>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col class="label_input">
        <el-form-item label="活动名称">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
      </el-col>
      <el-col>
          <el-upload action="" :show-file-list="false" :auto-upload="false">
            <el-button type="primary">选择文件</el-button>
          </el-upload>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">对比图片</el-button>
        </el-form-item>
      </el-col>
    </el-row>
  </el-form>
</template>

<script>

export default {
  name: 'ImageDiff',
  data () {
    return {
      form: [
      ]
    }
  },
  methods: {
    onSubmit () {
      console.log('Message')
    }
  }
}
</script>

<style scoped>
  .el-col{
    width: 100px;
  }
  .label_input{
    width: 400px;
  }
  .el-input{
    width: 300px;
  }
</style>
