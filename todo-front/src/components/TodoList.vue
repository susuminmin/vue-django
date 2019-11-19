<template>
  <div class="todo-list">
    <!-- props 로 가져왔기 때문에 todos 사용 가능! -->
    <div class="card mb-1" v-for="todo in todos" :key="todo.id">
      <!-- for 과 key 는 짝꿍! -->
      <div class="card-body d-flex justify-content-between">
        <span>{{ todo.title }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TodoList",
  props: {
    todos: {
      type: Array,
      required: true
    }
  }
};
</script>

<style>
</style>