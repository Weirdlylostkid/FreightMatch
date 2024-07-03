<template>
<div>
<h2>Chatbot</h2>
<div>
<div v-for="(msg, index) in messages" :key="index" :class="msg.sender">
            {{ msg.text }}
</div>
</div>
<input
          type="text"
          v-model="input"
          @keyup.enter="handleSendMessage"
        />
<button @click="handleSendMessage">Send</button>
</div>
</template>
 
    <script>
    import axios from 'axios';
 
    export default {
      data() {
        return {
          messages: [],
          input: '',
        };
      },
      methods: {
        handleSendMessage() {
          const newMessages = [...this.messages, { sender: 'user', text: this.input }];
          this.messages = newMessages;
          this.input = '';
 
          axios.post('http://localhost:8000/api/chatbot/', { message: this.input })
            .then(response => {
              this.messages.push({ sender: 'bot', text: response.data });
            })
            .catch(error => {
              console.error('There was an error sending the message!', error);
            });
        },
      },
    };
</script>
 
    <style>
    .user {
      text-align: right;
      color: blue;
    }
 
    .bot {
      text-align: left;
      color: green;
    }
</style>