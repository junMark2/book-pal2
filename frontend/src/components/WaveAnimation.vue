<template>
  <div class="wave-container">
    <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
      <path
        :d="wavePath"
        :fill="waveColor"
      ></path>
    </svg>
  </div>
</template>

<script>
export default {
  props: {
    waveColor: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      wavePath: '',
    };
  },
  mounted() {
    this.generateWavePath();
  },
  methods: {
    generateWavePath() {
      const points = [];
      for (let i = 0; i <= 1200; i += 50) {
        const y = 60 + 20 * Math.sin((i / 1200) * 2 * Math.PI);
        points.push(`${i},${y}`);
      }
      this.wavePath = `M${points.join(' L')} L1200,120 L0,120 Z`;
    },
  },
};
</script>

<style scoped>
.wave-container {
  width: 100%;
  height: 100px;
  overflow: hidden;
}
</style>
