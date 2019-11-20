<template>
  <div class="home">
    <h1>Todo</h1>
    <!-- TodoInput 에서 createTodo 이벤트가 발생하면 createTodo 함수를 실행하겠다! -->
    <TodoInput @createTodo="createTodo" />
    <!-- TodoList 에서 todo 를 출력할 수 있도록 props 로 todo 값을 넘겨준다. -->
    <TodoList :todos="todos" />
  </div>
</template>
<script>
import axios from "axios";
// import jwtDecode from 'jwt-decode' // JWT 의 payload 값을 해석해서 보여주는 library
// getters를 한번에 불러오는 library 호출
import { mapGetters } from "vuex"; // import vuex from 'vuex'; vuex.mapGetters
import TodoList from "@/components/TodoList";
import TodoInput from "@/components/TodoInput";
import router from "@/router";
export default {
  name: "Home",
  data() {
    return {
      todos: []
    };
  },
  // getters 활용(mapGetters)
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  // Home component 가 사용할 component 들을 등록
  components: {
    TodoList,
    TodoInput
  },
  methods: {
    // 사용자 로그인 유무를 확인하여 로그인되어있지 않을 시 로그인 페이지로 보내겠다.
    checkLoggedIn() {
      // 1. 세션을 시작해서
      // this.$session.start()
      // 2. 'jwt' 가 있는지 확인하겠다.
      // if(!this.$session.has('jwt')) {
      // session 으로 계속 접근하는 걸 isLoggedIn으로 처리하는것
      if (!this.isLoggedIn) {
        // 로그인 페이지로 보내겠다.
        router.push("/login");
      }
    },
    // 우리가 만든 django API 서버로 todos 를 달라는 요청을 보낸 뒤
    // todos data 에 할당하는 함수
    getTodo() {
      // 반복되는 거 지우기
      // this.$session.start()
      // session 에 저장되어 있는 JWT 값을 가져온다.
      // const token = this.$session.get('jwt')
      // JWT 에 담겨있는 user_id 값을 추출
      // const userId = jwtDecode(token).user_id
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      // JWT 를 axios 요청에 담아서 보낼 옵션을 정의
      // const options = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }

      // axios.get(URL, 옵션)
      axios
        .get(`${SERVER_IP}/api/v1/users/${this.userId}/`, this.options)
        .then(response => {
          // Django 에서 응답받은 todo 목록을 todos 데이터에 할당
          this.todos = response.data.todo_set;
        })
        .catch(error => {
          console.error(error);
        });
    },
    // TodoInput 에서 발생하는 createTodo 이벤트에서 title 값을 넘겨받는다.
    createTodo(title) {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      // const userId = jwtDecode(token).user_id
      // const options = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      // 요청을 보낼 data 를 작성
      const data = {
        title,
        user: this.userId
      };
      // axios.post(URL, 보낼 데이터, 옵션)
      axios
        .post(`${SERVER_IP}/api/v1/todos/`, data, this.options)
        .then(response => {
          this.todos.push(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  // Vue 가 화면에 그려지면 실행하는 함수
  mounted() {
    if (this.isLoggedIn) {
      this.checkLoggedIn();
      this.getTodo();
    }
  },
  watch: {
    isLoggedIn() {
      this.getTodo();
    }
  }
};
</script>
<style>
</style>