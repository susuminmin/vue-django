<template>
  <div id="app">
    <div id="nav">
      <!-- isLoggedIn 값에 따라서 조건부 렌더링 -->
      <div v-if="isLoggedIn">
        <router-link to="/">Home</router-link>|
        <!-- prevent 를 사용하는 이유는 href 로 redirect 를 방지하기 위함 -->
        <a @click.prevent="logout" href="/logout">Logout</a>
      </div>
      <div v-else>
        <router-link to="/login">Login</router-link>
      </div>
    </div>
    <div class="container col-6">
      <router-view />
    </div>
  </div>
</template>

<script>
import router from "@/router";

export default {
  name: "App",
  // data() {
  //   return {
  //     // 사용자의 로그인 상태 값, jwt 가 있으면 true
  //     isLoggedIn: this.$session.has("jwt")
  //   };
  // },
  //
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },
  mounted() {
    if (this.$session.has("jwt")) {
      const token = this.$session.get("jwt");
      this.$store.dispatch("logIn", token); // token 값 통해 자동 로그인
    }
  },
  methods: {
    logout() {
      // 1. session 통째로 삭제
      this.$session.destroy();
      this.$store.dispatch("logOut");
      // 2. 삭제 후 로그인 페이지로 보냄
      router.push("/login");
    }
  }

  // data 에 변화가 일어나는 시점에 실행하는 함수
  //   updated() {
  //     this.isLoggedIn = this.$session.has("jwt"); // 그 때마다 isLoggedIn 값 바꿔줌
  //   }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
