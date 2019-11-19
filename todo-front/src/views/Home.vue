<template>
  <div class="home">
    <h1>Todo</h1>
    <TodoInput @createTodo="createTodo" />
    <!-- createTodo 라는 이벤트 넘겨지면 createTodo 실행하겠음 -->
    <TodoList :todos="todos" />
    <!-- [3] 사용 -->
  </div>
</template>

<script>
import axios from "axios"
import jwtDecode from "jwt-decode" // JWT 의 payload 값을 해석해서 보여주는 library
import TodoList from "@/components/TodoList" // [1] 호출
import TodoInput from "@/components/TodoInput" // [1] 호출 --> 등록 --> 템플릿에서 사용
import router from "@/router"

export default {
  name: "home",
  data() {
    return {
      todos: [] // 부모 페이지에서 보내고 TodoList.vue 에서 props 로 받음
    };
  },
  // [2] 등록
  components: {
    TodoList,
    TodoInput
  },
  methods: {
    // 사용자 로그인 유무 확인하여, 로그인 되어있지 않을 시 로그인 페이지로 보내겠다.
    checkLoggedIn() {
      // 1. 세션을 시작해서
      this.$session.start()

      // 2. 'jwt' 가 있는지 확인하겠다.
      // jwt가 없다면
      if (!this.$session.has("jwt")) {
        // 로그인 페이지로 보내겠다.
        router.push("/login")
      }
    },
    // 우리가 만든 django API 서버로 todos 를 달라는 요청을 보낸 뒤, todos 데이터에 할당하는 함수
    getTodo() {
      this.$session.start()
      const token = this.$session.get("jwt")
      const userId = jwtDecode(token).user_id
      // 환경 변수에 넣었던 것 꺼내오기
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      // axios 로 요청 보낸다.

      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };

      axios
        .get(`${SERVER_IP}/api/v1/users/${userId}/`, options)
        .then(response => {
          // console.log(response)
          this.todos = response.data.todo_set
        })
        .catch(error => {
          console.error(error)
        })
    },
      createTodo(title) {
    this.$session.start()
    const token = this.$session.get("jwt")
    const SERVER_IP = process.env.VUE_APP_SERVER_IP
    const userId = jwtDecode(token).user_id
    const options = {
      headers: {
        Authorization: "JWT " + token
      }
    }
    // 요청을 보낼 data 를 작성
    const data = {
      title,
      user: userId
    }
    axios.post(`${SERVER_IP}/api/v1/todos/`, data, options)
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.error(error)
      })
  },
  },


  // Vue 가 화면에 그려지면 실행하는 함수
  mounted() {
    this.checkLoggedIn();
    this.getTodo();
  }
};
</script>

<style>
</style>