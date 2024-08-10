from wordcloud import WordCloud
import matplotlib.pyplot as plt

themes = {
    "Digital Vulnerability and Exposure": [
        "privacy risks", "data breach", "online threats", "cybersecurity",
        "personal information", "identity theft", "exposure", "deepfake risks"
    ],
    "Impact on Professional Life": [
        "career damage", "reputation harm", "job loss", "professional credibility",
        "workplace trust", "image manipulation", "digital abuse", "reputation management"
    ],
    "Psychological and Emotional Effects": [
        "anxiety", "stress", "fear", "mental health", "emotional trauma",
        "self-esteem", "psychological impact", "trust issues", "emotional distress"
    ],
    "Awareness and Prevention Measures": [
        "education", "digital literacy", "prevention strategies", "multi-factor authentication",
        "media literacy", "community resilience", "crisis communication", "protection tools"
    ]
}

def create_wordcloud(theme_name, words):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(words))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(theme_name, fontsize=20)
    plt.axis('off')
    plt.show()

for theme_name, words in themes.items():
    create_wordcloud(theme_name, words)
