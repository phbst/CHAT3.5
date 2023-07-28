<template>
	<view>
		<view class="head">
			<image class="src" src="../../static/屏幕截图 2023-07-11 152705.png"></image>

		</view>
	
		<view style="height: 75px;"></view>
		
		<view class="password-biginput">
			<input type="safe-password" class="password-input"  v-model="user" placeholder="请输入账号...." />
		</view>
		
		<view style="height: 45px;"></view>
		
		<view class="password-biginput">
			<input type="safe-password" password="true" class="password-input" v-model="password"  placeholder="请输入密码...." />
		</view>
		
		<view style="height: 100px;"></view>
		
		<view>
			<button class="login-button" @click="login" >登录</button>
		</view>
		
		<view style="height: 5px;"></view>
		<view>
			<button class="login-button" @click="signup" >注册</button>
		</view>
		
	</view>
</template>
<script>
	import VueRouter from 'vue-router'
	export default{
		data(){
			return {
				user:"",
				password:""
			}
		},
		methods:{
			login() {
			const url = 'https://login.codetest.ink';
			const data = { "username": this.user, "password": this.password ,"type":"login"};
			const options = {
			  method: 'POST',
			  headers: {
				'Content-Type': 'application/json'
			  },
			  body: JSON.stringify(data)
			};
			fetch(url, options)
			  .then(response => response.json())
			  .then(data => {
				console.log(JSON.stringify(data));
				
				if(data.code===0){
					alert("密码错误或用户不存在")
				}
				else if(data.code===1){
					localStorage.setItem('token', data.token);
					alert("密码正确")
					window.location.href = 'https://chatgpt4.codetest.ink/#/pages/index/model/GPT-35';
				}

				//在这里处理响应数据
			  })
			  .catch(error => {
				console.error(error);
				// 在这里处理请求错误
			  });  
			},
			signup()
			{
				const url = 'https://chatgpt4.codetest.ink/#/pages/index/signup';
				window.open(url, '_self');
			}
			
		},
		created() {
		  const token = localStorage.getItem('token');
		  if (token){ 
		    this.$router.push('/pages/index/model/GPT-35');
			}
		
		
		}
	}
</script>

<style>
.head{
	display: flex;
	justify-content: center;
	align-items: center;
	height: 125px;
}
.src{
	width: 80px;
	height: 75px;
}
.password-biginput{
	border: 1px solid black;
	border-radius: 30px;
	
}
.password-input{
	padding: 10px;
}
.login-button{
	height: 43px;
	border: 1px solid skyblue;
	background-color:grey;
}
</style>