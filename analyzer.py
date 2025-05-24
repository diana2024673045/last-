def analyze_personality(mbti, zodiac, animal, lang):
    if lang == "en":
        return f"""
### 🧠 MBTI: `{mbti}`
You are **{mbti}-type**, which reflects your mental structure and how you approach the world.

---

### 🌟 Zodiac Sign: `{zodiac}`
Your Western zodiac sign is **{zodiac}**, which is often linked to your emotional energy and outward expression.

---

### 🐉 Eastern Sign: `{animal}`
Your Eastern zodiac sign is the **{animal}**, representing your inner instincts and lifetime traits.

---

👉 **Combined**, this shows you're a creative, balanced personality who connects logic and heart 💖🧠!
        """
    else:
        return f"""
### 🧠 MBTI: `{mbti}`
당신의 MBTI는 **{mbti}형**으로, 세상을 바라보는 사고방식을 보여줍니다.

---

### 🌟 별자리: `{zodiac}`
서양 별자리인 **{zodiac}**는 감정과 외부 표현의 에너지를 상징합니다.

---

### 🐉 띠: `{animal}`
당신의 동양 띠인 **{animal}**는 본능과 평생의 특성을 반영합니다.

---

👉 **세 가지 조합**은 당신이 논리와 감성을 모두 갖춘 조화로운 성격임을 보여줍니다 💖🧠!
        """
