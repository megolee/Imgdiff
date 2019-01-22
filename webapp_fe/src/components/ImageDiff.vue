<template>
  <el-form>
    <el-row type="flex" justify="center">
      <el-col class="label_input">
        <el-form-item label="活动名称">
          <el-input v-model="form.name" ref="image1Input" :disabled="true"></el-input>
        </el-form-item>
      </el-col>
      <el-col>
          <el-upload action="" :show-file-list="false" :auto-upload="false" :on-change="changeImage1Handle" accept="image/png,image/jpeg">
            <el-button type="primary">选择文件</el-button>
          </el-upload>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col class="label_input">
        <el-form-item label="活动名称">
          <el-input v-model="form.name" ref="image2Input" :disabled="true"></el-input>
        </el-form-item>
      </el-col>
      <el-col>
          <el-upload action="" :show-file-list="false" :auto-upload="false" :on-change="changeImage2Handle" accept="image/png,image/jpeg">
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
    },
    changeImage1Handle (file, fileList) {
      console.log(file.name)
      if (fileList.length !== 1) {
        fileList.shift()
      }
      this.$refs.image1Input.value = file.name
      console.log(fileList.length)
      console.log(fileList[0].name)
    },
    changeImage2Handle (file, fileList) {
      console.log(file.name)
      if (fileList.length !== 1) {
        fileList.shift()
      }
      this.$refs.image2Input.value = file.name
      console.log(fileList.length)
      console.log(fileList[0].name)
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
