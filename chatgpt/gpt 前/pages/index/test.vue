<!-- <template>
  <div class="wrapper">
    <nav>
      <h2 class="daohan">AI语言助手</h2>
      <ul>
		<li v-for="(lang, index) in languages" :key="index" :class="{ 'active': currentLanguage === lang.code }">
			
		  <a href="#" @click="changeLanguage(lang.code)">{{ lang.name }}</a>
		</li>
      </ul>
    </nav>
	
   <div class="chat-box">
      <div class="chat-messages">
        <p v-for="(message, index) in messages" :key="index">{{ message }}</p>
      </div>
      <form  @submit.prevent="sendMessage">
		<div class="shuru">
			  
			<input type="text" v-model="newMessage" placeholder="请输入消息..." class="message-input">
			<button  class="message-sent" type="submit">发送</button>
			  
			  
		</div>
        
      </form>
	  
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      languages: [
        { name: 'Chatgpt-3.5', code: 'en' },
        { name: 'Chatgpt-4.0', code: 'fr' },
		{ name: 'Bing', code: 'bi' },
		{ name: '文心一言', code: 'wx' },
		


      ],
      currentLanguage: 'en',
      messages: [],
      newMessage: ''
    }
  },
  methods: {
	
    changeLanguage(code) {
      // 切换语言
      this.currentLanguage = code;
      // 清空消息
      this.messages = [];
    },
    sendMessage() {
      // 发送消息
      this.messages.push(this.newMessage);
      this.newMessage = '';
    }
  },
		created() {
			const token = localStorage.getItem('token');
			if (token) {}
			else{
				    const url = 'https://chatgpt4.codetest.ink/#/pages/index/login';
					window.open(url, '_self');
			}
		}
		
}
</script>

<style scoped>

.wrapper {
  display: flex;
  height: 100%;
  flex-wrap: wrap;
}
.daohan{
	display: flex;
	flex-wrap: wrap;
	justify-content: center;
}
nav li.active a {
  background-color: #007bff;
  color: #fff;
}
	

nav {

  width: 20%;
  height: 100%;
  flex-direction: row;
  padding: 20px;
  box-sizing: border-box;
  position: relative; /* 添加position属性 */
  overflow-y: scroll;
}

nav::after {
  content: "";
  width: 1px; /* 分界线宽度 */
  height: 100%; /* 分界线高度 */
  background-color: #ccc; /* 分界线颜色 */
  position: absolute;
  top: 0;
  right: 0; /* 分界线位置 */
}

nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

nav li {
  margin: 0;
  padding: 0;
  margin-bottom: 10px;
}

nav a {
  display: block;
  background-color: #f5f5f5;
  color: #333;
  text-decoration: none;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  text-align: center;
}

nav a:hover {
  background-color: #007bff;
  color: #fff;
}

.chat-box {
  width: 80%;
  padding: 20px;
  box-sizing: border-box;
}

.chat-messages {
  height: 650px;
  overflow-y: scroll;
  border: 1px solid skyblue;
}

form {
  display: flex;
  margin-top: 20px;
}

/* input[type="text"] {
  margin-right: 10px;
  border: 1px solid skyblue;

} */
.message-input{
	margin-right: 10px;
	border: 1px solid skyblue;
	width:800px;
	height: 45px;
	border-radius: 30px;
	white-space: pre-wrap; /* 自动换行 */
	word-wrap: break-word; /* 单词断行 */
}

button[type="submit"] {
  background-color: #007bff;
  color: #fff; 
  height: 60px;
  width: 120px;
  
}
.shuru {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  
}


</style> -->