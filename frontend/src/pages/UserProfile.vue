<template>
  <div>
    <h1>User Profile</h1>
    <div v-if="user">
      <h2>{{ user.username }}</h2>
      <img :src="user.profile_image" alt="Profile Image" />
      <div :style="{ backgroundColor: user.represent_color }" class="color-box"></div>
      <h3>Reading Statistics</h3>
      <ul>
        <li>Total Books Read: {{ readingStats.totalBooksRead }}</li>
        <li>Total Books in Wishlist: {{ readingStats.totalBooksWishlist }}</li>
        <li>Total Books Completed: {{ readingStats.totalBooksCompleted }}</li>
      </ul>
    </div>
    <div v-else>
      <p>Loading user profile...</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: null,
      readingStats: {
        totalBooksRead: 0,
        totalBooksWishlist: 0,
        totalBooksCompleted: 0,
      },
    };
  },
  created() {
    this.fetchUserProfile();
    this.fetchReadingStatistics();
  },
  methods: {
    async fetchUserProfile() {
      try {
        const response = await axios.get('/api/user-profile/');
        this.user = response.data;
      } catch (error) {
        console.error('Error fetching user profile:', error);
      }
    },
    async fetchReadingStatistics() {
      try {
        const response = await axios.get('/api/user-reading-stats/');
        this.readingStats = response.data;
      } catch (error) {
        console.error('Error fetching reading statistics:', error);
      }
    },
  },
};
</script>

<style scoped>
.color-box {
  width: 100px;
  height: 100px;
  border: 1px solid #000;
}
</style>
