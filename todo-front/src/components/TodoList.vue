<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body d-flex justify-content-between mb-1">
        <span>{{ todo.title }}</span>
        <span @click="deleteTodo(todo)">삭제</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"; // 요청 보낼 때는 엑시오스 가져오기

export default {
  name: "TodoList",
  props: {
    todos: {
      type: Array,
      required: true
    }
  },
  computed: {
    options() {
      return this.$store.getters.options;
    }
  },
  methods: {
    deleteTodo(todo) {
      // option 때문에 아래 로직 모두 필요 없어짐
      // this.$session.start();
      // const token = this.$session.get("jwt");
      // const options = {
      //   headers: {
      //     Authorization: "JWT " + token
      //   }
      // };
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;

      axios
        .delete(`${SERVER_IP}/api/v1/todos/${todo.id}/`, this.options) // vuex store 에서 꺼내 온 옵션
        .then(response => {
          console.log(response);
          const idx = this.todos.indexOf(todo);
          if (idx > -1) {
            this.todos.splice(idx, 1);
          }
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style>
</style>