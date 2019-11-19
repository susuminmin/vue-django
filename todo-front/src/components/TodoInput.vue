<template>
  <div class="todo-input">
    <form class="input-group mb-3" @submit.prevent="onSubmit">
      <!-- prevent: 실제 제출까지는 막아서 redirect 발생 안케끔 -->
      <input v-model="title" type="text" class="form-control" />
      <button type="submit" class="btn btn-success">add</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "TodoInput",
  data() {
    return {
      title: ""
    };
  },
  // 홈이 넘겨주는 정보 실행만 시켜줄 것
  methods: {
    onSubmit() {
      // emit 은 컴포넌트가 이벤트를 발생하게 하는 함수 
      this.$emit("createTodo", this.title); // createTodo 라는 이름의 event 발생, 발생 때마다 title 값 넘김
      this.title = ""; // title 값 넘기고 나서 다시 초기화
    }
  }
};
</script>

<style>
</style>