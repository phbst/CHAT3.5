<!-- <template>
	<view>
		
		
		<button  size="default" type="primary" class="send-button" @click="send" plain>注销</button>
		
		<image src="../../static/0.gif" mode="aspectFill"></image>
		
	</view>
</template>

<script>
	
	export default{
		data()
		{
			return{
				mes:'hello,world!',
				fag:true,
				kk:'https://c-ssl.dtstatic.com/uploads/item/202004/11/20200411172647_ffbxt.thumb.1000_0.jpg'
			}
		},
		methods:{
			send(){
				 //    const token = localStorage.getItem('token');
					// alert(token)
					localStorage.removeItem('token');
					const url = 'https://chatgpt4.codetest.ink/#/pages/index/login';
					window.open(url, '_self');
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

<style>
	.a{
		width: 100px;
		height: 100px;
		background-color:green;
	}
	.b{

		background-color:red;
	}
	.send-button {
	  
	  width: 200px;
	  height: 70px;
	}

</style> -->