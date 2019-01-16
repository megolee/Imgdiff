<template>
  <div>
    <p>Hello Vue</p>
    <el-upload
      class="upload-demo"
      ref="upload"
      action="https://jsonplaceholder.typicode.com/posts/"
      :limit="2"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      :on-exceed="handleExceed"
      :on-change="handleChange"
      :file-list="fileList"
      :auto-upload="false">
      <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
      <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
      <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
    </el-upload>
  </div>
</template>

<script>
export default {
  name: 'ImageDiff',
  data () {
    return {
      fileList: [
      ]
    }
  },
  methods: {
    submitUpload () {
      console.log(this.fileList.length)
      if (this.fileList.length !== 2) {
        this.$message.error('最少要上传2张图片哦')
        return
      }
      console.log('2 Images')
      this.$refs.upload.submit()
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    handleExceed (file, fileList) {
      console.log('Hi')
      this.$message.error('最多可以上传2张图片哦')
    },
    handleChange (file, fileList) {
      console.log('handleChnage')
    }
  }
}
</script>

<style scoped>

</style>
