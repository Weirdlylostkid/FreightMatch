<template>
<div>
<h2>Upload Routes</h2>
<form @submit.prevent="handleSubmit">
<input type="file" @change="handleFileChange" />
<button type="submit">Upload</button>
</form>
</div>
</template>
 
    <script>
    import axios from 'axios';
 
    export default {
      data() {
        return {
          file: null,
        };
      },
      methods: {
        handleFileChange(e) {
          this.file = e.target.files[0];
        },
        handleSubmit() {
          const formData = new FormData();
          formData.append('file', this.file);
 
          axios.post('http://localhost:8000/api/upload-routes/', formData)
            .then(response => {
              alert('File uploaded successfully');
            })
            .catch(error => {
              console.error('There was an error uploading the file!', error);
            });
        },
      },
    };
</script>