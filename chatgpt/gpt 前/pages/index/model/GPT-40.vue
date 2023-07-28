<template>
	<div class="total">
		<div class="nav">
			<div class="label">
				<image src="../../../static/googlePalmAvatar.5ca326b0.webp" style="height: 50px;width: 50px;margin-right: 0px; "></image>
				<h2>AI智能助手</h2>
			</div>
			<div class="menu">
				<ul>
	
					<li  @click="gotoChatGPT35">
						<image src="../../../static/chatGPTAvatar.webp" style="height: 50px;width: 50px;border-radius: 50%; margin-left: 30px;"></image>
						<p style="font-size:1.1pc">ChatGPT-3.5</p>
					</li>
					<li style="background-color: #e6e6e6;" @click="gotoChatGPT40">
						<image src= '../../../static/openAIBlue.webp'style="height: 50px;width: 50px;border-radius: 50%;margin-left: 30px;"></image>
						<p style="font-size:1.1pc">ChatGPT-4.0</p>
						<p>(limited)</p>
					</li>
					<li @click="gotoChatGPT40">
						<image src= '../../../static/openAIBlue.webp'style="height: 50px;width: 50px;border-radius: 50%;margin-left: 30px;"></image>
						<p style="font-size:1.1pc">ChatGPT-4.0</p>
						<p>(limited)</p>
					</li>
					<li @click="gotoChatGPT40">
						<image src= '../../../static/openAIBlue.webp'style="height: 50px;width: 50px;border-radius: 50%;margin-left: 30px;"></image>
						<p style="font-size:1.1pc">ChatGPT-4.0</p>
						<p>(limited)</p>
					</li>
					<li @click="gotoChatGPT40">
						<image src= '../../../static/openAIBlue.webp'style="height: 50px;width: 50px;border-radius: 50%;margin-left: 30px;"></image>
						<p style="font-size:1.1pc">ChatGPT-4.0</p>
						<p>(limited)</p>
					</li>
					<li @click="gotoChatGPT40">
						<image src= '../../../static/openAIBlue.webp'style="height: 50px;width: 50px;border-radius: 50%;margin-left: 30px;"></image>
						<p style="font-size:1.1pc">ChatGPT-4.0</p>
						<p>(limited)</p>
					</li>
					<li @click="gotoChatGPT40">
						<image src= '../../../static/openAIBlue.webp'style="height: 50px;width: 50px;border-radius: 50%;margin-left: 30px;"></image>
						<p style="font-size:1.1pc">ChatGPT-4.0</p>
						<p>(limited)</p>
					</li>
					<li @click="gotoChatGPT40">
						<image src= '../../../static/openAIBlue.webp'style="height: 50px;width: 50px;border-radius: 50%;margin-left: 30px;"></image>
						<p style="font-size:1.1pc">ChatGPT-4.0</p>
						<p>(limited)</p>
					</li>
					<li @click="gotoChatGPT40">
						<image src= '../../../static/openAIBlue.webp'style="height: 50px;width: 50px;border-radius: 50%;margin-left: 30px;"></image>
						<p style="font-size:1.1pc">ChatGPT-4.0</p>
						<p>(limited)</p>
					</li>
					<li @click="gotoChatGPT40">
						<image src= '../../../static/openAIBlue.webp'style="height: 50px;width: 50px;border-radius: 50%;margin-left: 30px;"></image>
						<p style="font-size:1.1pc">ChatGPT-4.0</p>
						<p>(limited)</p>
					</li>
					<li @click="gotoChatGPT40">
						<image src= '../../../static/openAIBlue.webp'style="height: 50px;width: 50px;border-radius: 50%;margin-left: 30px;"></image>
						<p style="font-size:1.1pc">ChatGPT-4.0</p>
						<p>(limited)</p>
					</li>
					<li @click="gotoChatGPT40">
						<image src= '../../../static/openAIBlue.webp'style="height: 50px;width: 50px;border-radius: 50%;margin-left: 30px;"></image>
						<p style="font-size:1.1pc">ChatGPT-4.0</p>
						<p>(limited)</p>
					</li>
					<li @click="gotoChatGPT40">
						<image src= '../../../static/openAIBlue.webp'style="height: 50px;width: 50px;border-radius: 50%;margin-left: 30px;"></image>
						<p style="font-size:1.1pc">ChatGPT-4.0</p>
						<p>(limited)</p>
					</li>
				</ul>
			</div>
		</div>
		<div class="chat">
			<div class="model-name">
				
				<h2 style="text-align: center;line-height: 52px;">ChatGPT-3.5</h2>
			</div>
			
			<div class="output">
				<div v-for="(msg, index) in messages" :key="index" class="message" :class="[msg.sender === 'user' ? 'user-message' : 'bot-message']" style="display: block; padding: 10px;border-radius: 10px;">
				  <span v-bind:style="{ 'user-select': 'text' }" class="word" v-html="msg.message"></span>
				
				</div>
				<image src="../../../static/83620e745a0b30717a384e16b115e0db.gif" class="loading" v-if="isSending"></image>
			</div>
		
			<div class="input">
				<a href="#"><image class="quick" src="../../../static/删除.png" @click="deletemessage" style="width: 45px;height: 45px; "></image></a>
				<div class="chat-input-box">
					<textarea class="chat-input" v-model="message" v-on:keypress.enter="sentmessage" maxlength="1000" placeholder="   请输入问题...." :disabled="isSending"></textarea>
				</div>
				
				<a href="#" ><image class="quick" src="../../../static/发送.png" @click="sentmessage" style="width: 45px;height: 45px; " :disabled="isSending"></image></a>
			</div>
		</div>
	</div>
</template>


<script>
	export default{
		data(){
			return{
				message:"",
				messages:[],
				isSending:false
			}
		},
		methods:{
			gotoChatGPT40() {
			      // 跳转到 ChatGPT-4.0 页面
			      
			    },
			gotoChatGPT35() {
				window.location.href = 'https://chatgpt4.codetest.ink/#/pages/index/model/GPT-35';
			      // 跳转到 ChatGPT-3.5 页面
			      // window.location.href = "https://www.baidu.com";
			    },
			sentmessage()
			{
				event.preventDefault();
				if (this.isSending) {
					return;
				}
				if (this.message) {
						this.isSending = true;
						const formattedMessage = this.message.replaceAll('\n', '<br>').replaceAll(' ', '&nbsp;');
						this.messages.push({"sender":"user","message":formattedMessage});
						const chat=formattedMessage;
						
						this.message = "";
						const token = localStorage.getItem('token');
						fetch('https://api.codetest.ink', {
							method: 'POST',
							headers: {
							  'Content-Type': 'application/json',
							  'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjkwMzU5NTMwfQ.2Hr1n8CgEKhQNGnToHPAY8I2PtvtzwXI7-ioQdQBPJc'
							},
							body: JSON.stringify({ "question": chat })
						  })
						  .then(response => {
							if (!response.ok) {
							  throw new Error('Network response was not ok');
							}
							return response.json();
						  })
						  .then(data => {
							console.log(data);
							if(data.code==="401"){
								alert("登陆已过期或者未登录！")
								localStorage.removeItem('token');
								window.location.href = 'https://chatgpt4.codetest.ink/#/pages/index/login';
								
							}
							const formattedAnswer = data.answer.replaceAll('\n', '<br>').replaceAll(' ', '&nbsp;');
							this.messages.push({"sender":"bot","message":formattedAnswer});;
							this.isSending = false;
							
						  })
						  .catch(error => {
							console.error('There was a problem with the fetch operation:', error);
							this.isSending = false;
						  });
					
				}
			},
			deletemessage()
			{
				this.messages=[]
			}
		},
		created() {
		  const token = localStorage.getItem('token');
		  if (token){} 
		  else
		  {
		    window.location.href = 'https://chatgpt4.codetest.ink/#/pages/index/login';
			}
		}
		
		
	}

</script>

<style>

	.total {
		display: flex;
		/* width: 100vh; */
		height: 100vh;
		
	}
	.nav{
		height: 100%;
		width: 20%;
		background-color: #55aaff;
		display: flex;
		flex-direction: column;
	}
	.chat {
		display: flex;
		height: 100%;
		width: 80%;
		flex-direction: column;
		
	}
	


	.input {
		flex: 1;
		background-color: #ffffff;
/* 		border: 1px solid #e6e6e6; */
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
	}
	.model-name{
		flex:1;
		background-color: #a6a6a6;
		border: 1px solid #e6e6e6;
	}
	.label{
		flex: 1;
		background-color: #a6a6a6;
		display: flex;
		flex-direction: row;
/* 		text-align: center; */
/* 		line-height: 52px; */
		border: 1px solid #e6e6e6;
		align-items: center;
		justify-content: center;
	}
	.menu{
		flex: 15;
		background-color: #ffffff;
		display: flex;
		flex-direction: column;
		border: 1px solid #e6e6e6;
		overflow-y: auto;
	}
	.menu ul{
		list-style: none;
		padding: 0;
		margin: 0;
	}
	.menu ul li {
		display: flex;
		flex-direction: row;

		padding: 10px;
		text-align: center;
		line-height: 50px;
/* 		justify-content: center;
		align-items: center; */
		
	}
	.menu ul li:hover {
		background-color: #e6e6e6;
	}
	.menu::-webkit-scrollbar {
	  width: 6px;
	}
	
	.menu::-webkit-scrollbar-track {
	  background-color: #f1f1f1;
	}
	
	.menu::-webkit-scrollbar-thumb {
	  background-color: #888;
	  border-radius: 3px;
	}
	
	.menu::-webkit-scrollbar-thumb:hover {
	  background-color: #555;
	}
	.chat-input-box
	{
		border: 1px solid #000;
		border-radius:30px;
		width: 70%;
		height: 80%;
		display: flex;
		align-items: center;
	}
	.chat-input{
	  width: 100%;
	  height: 20px;
	  display: flex;
	  margin-left: 5px;
	  margin-right: 5px;
	  border: none;
	  outline: none;
	  font-size: 15px;
	  border-radius: 25px;
	  background-color: #fff;
	}

	.quick:hover {
	    background-color: #e6e6e6;
	}
	.output {
	  flex: 14;
	  background-color: #ffffff;
	  display: flex;
	  flex-direction: column;
	  align-items: flex-start;
	  overflow-y: auto;
	  padding: 10px;
	  margin-left: 14%;
	  margin-right: 14%;


	}
	
	.message {
	  margin-bottom: 15px;
	  padding: 10px;
	  border-radius: 4px;
	}
	
	.user-message {
	  align-self: flex-end;
	  background-color: #aaffff;
	  color: #000000;
	  max-width: 70%;
	    word-wrap: break-word; /* 允许文本在空格处自动换行 */
	    word-break: break-all; /* 允许文本在任意字符处自动换行 */
	  
	}
	
	.bot-message {
	  align-self: flex-start;
	  background-color: #6c757d;
	  color: #FFFFFF;
	  max-width: 70%;
		word-wrap: break-word; /* 允许文本在空格处自动换行 */
	    word-break: break-all; /* 允许文本在任意字符处自动换行 */
	}
	.loading{
		align-self: flex-start;
		width: 60px;
		height: 60px;
		border-radius: 50%;
		
	}
/* S */

	.output::-webkit-scrollbar {
	  width: 0;
	  height: 0;
	}
	
	.output::-webkit-scrollbar-track {
	  background-color: #e6e6e6;
	}
	
	.output::-webkit-scrollbar-thumb {
	  background-color: #888;
	  border-radius: 3px;
	}
	
	.output::-webkit-scrollbar-thumb:hover {
	  background-color: #555;
	}
</style>
