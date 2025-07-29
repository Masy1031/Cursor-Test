// スムーススクロール
const ctaBtn = document.querySelector('.cta-btn');
if (ctaBtn) {
  ctaBtn.addEventListener('click', function(e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
}

// 今後の拡張用: 例) セクションのアニメーションやFAQ開閉など
// document.addEventListener('DOMContentLoaded', () => {
//   // ここに追加のJSを書く
// }); 