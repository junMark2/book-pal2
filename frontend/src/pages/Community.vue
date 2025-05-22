<template>
  <div>
    <h1>Community</h1>
    <div v-if="threads.length">
      <ul>
        <li v-for="thread in threads" :key="thread.id">
          <router-link :to="{ name: 'ThreadDetail', params: { id: thread.id } }">{{ thread.content }}</router-link>
          <p>{{ thread.user.username }}</p>
          <p>{{ thread.created_at }}</p>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>No threads available.</p>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';
import axios from 'axios';

export default defineComponent({
  name: 'Community',
  setup() {
    const threads = ref([]);

    const fetchThreads = async () => {
      try {
        const response = await axios.get('/api/threads/');
        threads.value = response.data;
      } catch (error) {
        console.error('Error fetching threads:', error);
      }
    };

    onMounted(() => {
      fetchThreads();
    });

    return {
      threads,
    };
  },
});
</script>

<style scoped>
/* Add any necessary styles here */
</style>
