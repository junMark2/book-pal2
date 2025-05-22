<template>
  <div>
    <h1>Books</h1>
    <div v-if="books.length">
      <ul>
        <li v-for="book in books" :key="book.id">
          <router-link :to="{ name: 'BookDetail', params: { id: book.id } }">{{ book.title }}</router-link>
          <p>{{ book.author }}</p>
          <p>{{ book.publisher }}</p>
          <p>{{ book.published_at }}</p>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>No books available.</p>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';
import axios from 'axios';

export default defineComponent({
  name: 'Books',
  setup() {
    const books = ref([]);

    const fetchBooks = async () => {
      try {
        const response = await axios.get('/api/books/');
        books.value = response.data;
      } catch (error) {
        console.error('Error fetching books:', error);
      }
    };

    onMounted(() => {
      fetchBooks();
    });

    return {
      books,
    };
  },
});
</script>

<style scoped>
/* Add any necessary styles here */
</style>
