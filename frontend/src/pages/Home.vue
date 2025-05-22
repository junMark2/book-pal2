<template>
  <div>
    <h1>Home</h1>
    <div v-if="userColor">
      <h2>Your Color Summary</h2>
      <div :style="{ backgroundColor: userColor }" class="color-box"></div>
    </div>
    <div v-if="recommendedBooks.length">
      <h2>Recommended Books</h2>
      <ul>
        <li v-for="book in recommendedBooks" :key="book.id">
          <h3>{{ book.title }}</h3>
          <p>{{ book.author }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userColor: null,
      recommendedBooks: []
    };
  },
  created() {
    this.fetchUserColor();
    this.fetchRecommendedBooks();
  },
  methods: {
    async fetchUserColor() {
      try {
        const response = await axios.get('/api/user-represent-color/');
        this.userColor = response.data.represent_color;
      } catch (error) {
        console.error('Error fetching user color:', error);
      }
    },
    async fetchRecommendedBooks() {
      try {
        const response = await axios.get('/api/recommended-books/');
        this.recommendedBooks = response.data;
      } catch (error) {
        console.error('Error fetching recommended books:', error);
      }
    }
  }
};
</script>

<style scoped>
.color-box {
  width: 100px;
  height: 100px;
  border: 1px solid #000;
}
</style>
