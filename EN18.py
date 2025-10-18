from re import A
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
import random
import time
from datetime import datetime
import requests
import json
import hashlib
import os
import csv

warnings.filterwarnings('ignore')

# ✅✅✅ PASTIKAN FOLDER DATA ADA ✅✅✅
os.makedirs('data', exist_ok=True)

# ==================== KONFIGURASI & WARNA ====================
st.set_page_config(
    page_title="EasyNatorics - Jelajah Kombinatorika", 
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# FUTURISTIC COLOR PALETTE
COLORS = {
    'primary': '#00D4FF',
    'secondary': '#FF0080', 
    'accent1': '#7928CA',
    'accent2': '#FF6B35',
    'accent3': '#00F5FF',
    'dark': '#0A0A0A',
    'darker': '#111111',
    'light': '#1A1A1A',
    'text': '#FFFFFF'
}

# ==================== CSS MODERN & UNIK DENGAN ANIMASI ====================
def apply_futuristic_style():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600&display=swap');
    
    .stApp {{
        background: linear-gradient(135deg, {COLORS['dark']} 0%, {COLORS['darker']} 100%);
        color: {COLORS['text']};
    }}
    
    .main-title {{
        font-family: 'Orbitron', monospace;
        font-weight: 900;
        background: linear-gradient(90deg, {COLORS['primary']}, {COLORS['accent2']});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3.5rem;
        margin-bottom: 2rem;
        text-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
    }}
    
    .section-header {{
        font-family: 'Orbitron', monospace;
        font-weight: 700;
        color: {COLORS['primary']};
        font-size: 2rem;
        margin: 2rem 0 1rem 0;
        border-left: 4px solid {COLORS['secondary']};
        padding-left: 1rem;
    }}
    
    .metric-card {{
        background: linear-gradient(145deg, {COLORS['light']}, {COLORS['darker']});
        border: 1px solid {COLORS['primary']}33;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
        backdrop-filter: blur(10px);
    }}
    
    .stat-value {{
        font-family: 'Orbitron', monospace;
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, {COLORS['primary']}, {COLORS['accent2']});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }}
    
    .research-card {{
        background: linear-gradient(145deg, {COLORS['light']}, {COLORS['darker']});
        border: 1px solid {COLORS['primary']}33;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        animation: cardSlideIn 0.6s ease-out;
    }}
    
    .test-card {{
        background: linear-gradient(135deg, {COLORS['secondary']} 0%, {COLORS['accent2']} 100%);
        color: white;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(255, 0, 128, 0.3);
        animation: pulseGlow 2s infinite;
        border: 2px solid rgba(255,255,255,0.3);
    }}
    
    .learning-card {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['accent3']} 100%);
        color: white;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.3);
        animation: learningCardFloat 3s ease-in-out infinite;
    }}
    
    .success-card {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['accent3']} 100%);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border: 3px solid {COLORS['accent2']};
        animation: successCelebrate 0.6s ease-out, pulse 2s infinite 0.6s;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
    }}
    
    .explanation-box {{
        background: linear-gradient(135deg, {COLORS['light']} 0%, {COLORS['darker']} 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1.5rem 0;
        border-left: 5px solid {COLORS['primary']};
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        animation: explanationReveal 0.8s ease-out;
    }}
    
    .stButton button {{
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
        background: linear-gradient(135deg, {COLORS['primary']}, {COLORS['accent1']});
        color: white;
    }}
    
    .stButton button:hover {{
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 20px rgba(0, 212, 255, 0.3);
    }}
    
    @keyframes cardSlideIn {{
        from {{ opacity: 0; transform: translateY(30px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    @keyframes pulseGlow {{
        0%, 100% {{ box-shadow: 0 8px 25px rgba(255, 0, 128, 0.3); }}
        50% {{ box-shadow: 0 8px 30px rgba(255, 0, 128, 0.6); }}
    }}
    
    @keyframes learningCardFloat {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-3px); }}
    }}
    
    @keyframes successCelebrate {{
        0% {{ transform: scale(0.8); opacity: 0; }}
        70% {{ transform: scale(1.1); }}
        100% {{ transform: scale(1); opacity: 1; }}
    }}
    
    @keyframes explanationReveal {{
        from {{ opacity: 0; transform: translateX(-20px); max-height: 0; }}
        to {{ opacity: 1; transform: translateX(0); max-height: 500px; }}
    }}
    </style>
    """, unsafe_allow_html=True)

# ==================== UTILITY FUNCTIONS ====================
def hash_answer(answer):
    """Hash answer for secure comparison"""
    return hashlib.sha256(str(answer).encode()).hexdigest()

def validate_demographics(demographics):
    """Validate participant demographics"""
    errors = []
    
    if not demographics.get('nama') or len(demographics['nama'].strip()) < 2:
        errors.append("Nama harus minimal 2 karakter")
    
    if not demographics.get('kelas'):
        errors.append("Kelas harus dipilih")
    
    if not demographics.get('usia') or demographics['usia'] not in range(15, 19):
        errors.append("Usia harus antara 15-18 tahun")
    
    if not demographics.get('pengalaman'):
        errors.append("Pengalaman matematika harus dipilih")
    
    return errors

def create_confetti():
    """Create confetti effect"""
    confetti_html = """
    <div id="confetti-container" style="position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:1000;">
    """
    colors = [COLORS['primary'], COLORS['secondary'], COLORS['accent1'], COLORS['accent2'], COLORS['accent3']]
    for i in range(50):
        color = random.choice(colors)
        size = random.randint(8, 15)
        left = random.randint(0, 100)
        delay = random.uniform(0, 2)
        duration = random.uniform(3, 6)
        confetti_html += f"""
        <div class="confetti" style="
            background: {color};
            width: {size}px;
            height: {size}px;
            left: {left}%;
            animation-delay: {delay}s;
            animation-duration: {duration}s;
        "></div>
        """
    confetti_html += "</div>"
    return confetti_html

def show_celebration():
    """Show celebration effects"""
    st.markdown(create_confetti(), unsafe_allow_html=True)
    
    emojis = ["🎉", "🎊", "🌟", "🚀", "💫", "🔥", "⭐", "✨"]
    emoji_html = "<div style='text-align: center; margin: 2rem 0;'>"
    for emoji in random.sample(emojis, 4):
        emoji_html += f"<span style='animation: floatAround 6s ease-in-out infinite; display: inline-block; font-size: 2rem; margin: 0 10px;'>{emoji}</span> "
    emoji_html += "</div>"
    st.markdown(emoji_html, unsafe_allow_html=True)

# ==================== AI LAYER - DEEPSEEK INTEGRATION ====================
class DeepSeekAI:
    def __init__(self):
        try:
            self.api_key = st.secrets["DEEPSEEK_API_KEY"]
            self.client = DeepSeekAI(
                api_key=self.api_key,
                base_url="https://api.deepseek.com",
                timeout=30
            )
            self.demo_mode = False
            st.success("✅ AI Tutor Connected!")
        except Exception as e:
            self.demo_mode = True
            st.warning("🔧 Demo Mode - Add DeepSeek API Key for full features")
    
    def get_ai_explanation(self, concept, student_level, previous_answers=None):
        """Dapatkan penjelasan AI yang personalized"""
        
        if self.demo_mode:
            return self._get_demo_explanation(concept)
        else:
            try:
                prompt = f"""
                Berikan penjelasan tentang {concept} dalam kombinatorika untuk siswa SMA level {student_level}.
                
                Buat penjelasan yang:
                1. Mudah dipahami dengan analogi sehari-hari
                2. Menyertakan contoh konkret  
                3. Menjelaskan kapan konsep ini digunakan
                4. Berikan tips mengerjakan soal
                5. Gunakan format Markdown dengan emoji
                6. Maksimal 400 kata
                7. Bahasa Indonesia yang friendly
                """
                
                response = self.client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": "Anda adalah tutor matematika yang sabar dan ahli menjelaskan konsep sulit dengan cara mudah."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=800
                )
                return response.choices[0].message.content
            except Exception as e:
                return self._get_demo_explanation(concept)
    
    def _get_demo_explanation(self, concept):
        """Fallback explanations for demo mode"""
        explanations = {
            "prinsip_perkalian": """
            **🎯 PRINSIP PERKALIAN - Seni Menghitung Kemungkinan**
            
            **Konsep Inti:** Jika ada n₁ cara melakukan hal pertama, n₂ cara melakukan hal kedua, maka total cara = n₁ × n₂ × ...
            
            **🧠 Analogi Seru:**
            Bayangkan kamu punya:
            - 3 kaos (Merah, Biru, Hijau)
            - 2 celana (Jeans, Cargo)
            
            Total outfit = 3 × 2 = **6 kombinasi**!
            
            **📊 Contoh Lain:**
            - Menu: 4 makanan × 3 minuman = 12 kombinasi
            - Password: 10 angka × 10 angka = 100 kombinasi
            
            **💡 Tips:** Kalau pilihan independen, selalu pakai perkalian!
            """,
            
            "permutasi": """
            **🔄 PERMUTASI - Seni Menyusun dengan Urutan**
            
            **Konsep Inti:** Menyusun objek dengan memperhatikan URUTAN (A-B-C ≠ C-B-A)
            
            **Formula:** P(n,r) = n! / (n-r)!
            
            **🎭 Contoh Seru:**
            Mau menyusun 3 buku dari 5 buku berbeda?
            P(5,3) = 5 × 4 × 3 = **60 susunan**!
            
            **📊 Real-World:**
            - Podium juara: 8 peserta → P(8,3) = 336 susunan
            - Password unik: 4 huruf berbeda → P(26,4) = 358,800
            
            **💡 Tips:** Urutan penting? Pakai permutasi!
            """,
            
            "kombinasi": """
            **👥 KOMBINASI - Power of Team Selection**
            
            **Konsep Inti:** Memilih objek TANPA memperhatikan urutan (A-B-C = C-B-A)
            
            **Formula:** C(n,r) = n! / (r!(n-r)!)
            
            **🤝 Contoh Seru:**
            Memilih 2 orang dari 5 orang untuk tim?
            C(5,2) = 10 tim berbeda!
            
            **📊 Real-World:**
            - Komite: Pilih 3 dari 10 → C(10,3) = 120 komite
            - Menu combo: Pilih 2 dari 6 → C(6,2) = 15 combo
            
            **💡 Tips:** Urutan tidak penting? Pakai kombinasi!
            """
        }
        return explanations.get(concept, "Penjelasan lengkap tersedia dengan API key.")
    
    def ask_ai_tutor(self, user_question, context=""):
        """Fungsi untuk chat dengan AI tutor"""
        
        if self.demo_mode:
            return self._get_demo_tutor_response(user_question)
        else:
            try:
                prompt = f"""
                Anda adalah AI Tutor matematika untuk siswa SMA.
                
                KONTEKS: {context}
                PERTANYAAN: {user_question}
                
                Tolong berikan:
                - Penjelasan mudah dipahami
                - Analogi sehari-hari  
                - Contoh konkret
                - Langkah-langkah sederhana
                - Format markdown dengan emoji
                - Maksimal 300 kata
                - Bahasa Indonesia friendly
                """
                
                response = self.client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": "Anda adalah tutor matematika yang sabar, ramah, dan ahli menjelaskan konsep sulit dengan cara mudah."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=600
                )
                return f"🤖 **AI Tutor:**\n\n{response.choices[0].message.content}"
            except Exception as e:
                return self._get_demo_tutor_response(user_question)
    
    def _get_demo_tutor_response(self, question):
        """Demo responses for tutor"""
        demo_responses = {
            "prinsip perkalian": "**Prinsip Perkalian** 🧮\n\nContoh: 3 baju × 2 celana = 6 outfit!\n\nSetiap pilihan independen dikalikan.",
            "permutasi": "**Permutasi** 🔄\n\nUrutan penting! Contoh: P(5,3) = 5×4×3 = 60 susunan",
            "kombinasi": "**Kombinasi** 👥\n\nUrutan tidak penting! Contoh: C(5,2) = 10 tim"
        }
        
        question_lower = question.lower()
        for topic, response in demo_responses.items():
            if topic in question_lower:
                return f"🤖 **AI Tutor (Demo):**\n\n{response}"
        
        return "🤖 **AI Tutor (Demo):**\n\nFitur lengkap tersedia dengan API key DeepSeek! Tanya tentang: Prinsip Perkalian, Permutasi, atau Kombinasi."

    def generate_adaptive_questions(self, concept, difficulty="medium", count=5, student_level="beginner"):
        """Generate unlimited adaptive questions using AI"""
        
        if self.demo_mode:
            return self._get_demo_questions(concept, count)
        
        try:
            prompt = f"""
            Generate {count} {concept} practice problems for {student_level} level high school students.
            Difficulty: {difficulty}
            Language: Indonesian
            Format: JSON with questions, options, answer, explanation, hint
            Concepts: {concept}
            
            Requirements:
            - Real-world scenarios that students can relate to
            - Multiple choice format with 4 options
            - Clear step-by-step explanations
            - Helpful hints
            - Varying difficulty levels
            - Return as JSON array
            - Make it engaging and fun for teenagers
            """
            
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are a creative math teacher creating engaging practice problems. Always return valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                response_format={"type": "json_object"},
                max_tokens=2000
            )
            
            result = json.loads(response.choices[0].message.content)
            return result.get('questions', [])
            
        except Exception as e:
            return self._get_demo_questions(concept, count)
    
    def _get_demo_questions(self, concept, count):
        """Fallback demo questions"""
        question_banks = {
            'prinsip_perkalian': [
                {
                    "question": "Kamu punya 3 kaos (Merah, Biru, Hijau) dan 2 celana (Jeans, Cargo). Berapa banyak outfit berbeda?",
                    "options": ["5", "6", "8", "10"],
                    "answer": "6",
                    "explanation": "Prinsip perkalian: 3 kaos × 2 celana = 6 outfit berbeda",
                    "hint": "Setiap kaos bisa dipasang dengan setiap celana"
                },
                {
                    "question": "Password 2 digit menggunakan angka 0-9. Berapa banyak password yang mungkin?",
                    "options": ["90", "100", "110", "120"],
                    "answer": "100", 
                    "explanation": "10 pilihan digit pertama × 10 pilihan digit kedua = 100 password",
                    "hint": "Setiap digit punya 10 kemungkinan (0-9)"
                }
            ],
            'permutasi': [
                {
                    "question": "Berapa banyak cara menyusun 4 buku berbeda di rak?",
                    "options": ["16", "24", "32", "48"],
                    "answer": "24",
                    "explanation": "4! = 4 × 3 × 2 × 1 = 24 susunan berbeda",
                    "hint": "Ini adalah permutasi dari 4 objek berbeda"
                },
                {
                    "question": "Dalam lomba dengan 5 peserta, berapa banyak kemungkinan juara 1, 2, dan 3?",
                    "options": ["60", "50", "40", "30"],
                    "answer": "60",
                    "explanation": "P(5,3) = 5 × 4 × 3 = 60 kemungkinan podium",
                    "hint": "Urutan juara penting (juara 1 ≠ juara 2)"
                }
            ],
            'kombinasi': [
                {
                    "question": "Dari 7 orang, berapa banyak cara memilih 3 orang untuk panitia?",
                    "options": ["35", "30", "25", "20"],
                    "answer": "35",
                    "explanation": "C(7,3) = 7!/(3!×4!) = 35 cara",
                    "hint": "Urutan pemilihan tidak penting"
                },
                {
                    "question": "Dalam menu ada 8 hidangan. Berapa banyak cara memilih 3 hidangan?",
                    "options": ["56", "48", "40", "32"],
                    "answer": "56",
                    "explanation": "C(8,3) = 8!/(3!×5!) = 56 kombinasi menu",
                    "hint": "Urutan pemilihan hidangan tidak penting"
                }
            ]
        }
        
        base_questions = question_banks.get(concept, [])
        # Duplicate questions to reach count if needed
        while len(base_questions) < count:
            base_questions.extend(base_questions)
        return base_questions[:count]

# ==================== SISTEM DATA PENELITIAN ====================
class ResearchDataSystem:
    def __init__(self):
        if 'research_data' not in st.session_state:
            st.session_state.research_data = {
                'participants': {},
                'current_participant': None,
                'study_start_time': datetime.now().isoformat()
            }
        
        if 'participant_data' not in st.session_state:
            st.session_state.participant_data = self._create_new_participant()
            
        if 'current_module' not in st.session_state:
            st.session_state.current_module = None

    def _create_new_participant(self):
        """Create a new participant template"""
        return {
            'participant_id': None,
            'demographics': {},
            'pre_test': {
                'score': None,
                'answers': [],
                'start_time': None,
                'completion_time': None
            },
            'post_test': {
                'score': None, 
                'answers': [],
                'start_time': None,
                'completion_time': None
            },
            'anxiety_survey': {
                'pre_score': None,
                'post_score': None,
                'amas_score': None,
                'responses': []
            },
            'satisfaction_survey': {
                'score': None,
                'responses': [],
                'testimonial': ''
            },
            'learning_progress': {
                'concepts_learned': [],
                'problems_attempted': 0,
                'problems_correct': 0,
                'total_time': 0,
                'current_module': 0,
                'module_progress': {
                    'prinsip_perkalian': {'completed': False, 'score': 0, 'time_spent': 0},
                    'permutasi': {'completed': False, 'score': 0, 'time_spent': 0},
                    'kombinasi': {'completed': False, 'score': 0, 'time_spent': 0}
                }
            },
            'adaptive_learning': {
                'current_levels': {
                    'prinsip_perkalian': 'beginner',
                    'permutasi': 'beginner', 
                    'kombinasi': 'beginner'
                },
                'performance_history': {
                    'prinsip_perkalian': {'attempts': 0, 'correct': 0},
                    'permutasi': {'attempts': 0, 'correct': 0},
                    'kombinasi': {'attempts': 0, 'correct': 0}
                }
            },
            'registration_time': datetime.now().isoformat()
        }

    def register_participant(self, demographics):
        """Register new participant with validation"""
        try:
            errors = validate_demographics(demographics)
            if errors:
                raise ValueError("; ".join(errors))
            
            participant_id = f"P{len(st.session_state.research_data['participants']) + 1:03d}"
            
            new_participant = self._create_new_participant()
            new_participant['participant_id'] = participant_id
            new_participant['demographics'] = demographics
            new_participant['pre_test']['start_time'] = datetime.now().isoformat()
            
            st.session_state.participant_data = new_participant
            st.session_state.research_data['participants'][participant_id] = new_participant
            st.session_state.research_data['current_participant'] = participant_id
            
            return participant_id
        
        except ValueError as e:
            st.error(f"❌ Validasi gagal: {e}")
            return None
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan: {e}")
            return None

    def calculate_amas_score(self, responses):
        """Hitung skor AMAS berdasarkan respon"""
        if not responses:
            return None
        try:
            return np.mean([r['response'] for r in responses])
        except:
            return None

    def get_anxiety_level(self, amas_score):
        """Kategorikan tingkat kecemasan"""
        if amas_score is None:
            return "Tidak Terukur"
        elif amas_score <= 2.0:
            return "Rendah"
        elif amas_score <= 3.5:
            return "Sedang"
        else:
            return "Tinggi"

    def update_learning_progress(self, concept, is_correct=False):
        """Update learning progress when student answers a question"""
        try:
            current_id = st.session_state.research_data['current_participant']
            if current_id:
                participant = st.session_state.research_data['participants'][current_id]
                
                participant['learning_progress']['problems_attempted'] += 1
                
                if is_correct:
                    participant['learning_progress']['problems_correct'] += 1
                
                if concept not in participant['learning_progress']['concepts_learned']:
                    participant['learning_progress']['concepts_learned'].append(concept)
                
                # Update adaptive learning performance
                if concept in participant['adaptive_learning']['performance_history']:
                    participant['adaptive_learning']['performance_history'][concept]['attempts'] += 1
                    if is_correct:
                        participant['adaptive_learning']['performance_history'][concept]['correct'] += 1
                
                # Update difficulty level based on performance
                self._update_difficulty_level(participant, concept)
                
                return True
        except Exception as e:
            st.error(f"Error updating progress: {e}")
        return False

    def _update_difficulty_level(self, participant, concept):
        """Update difficulty level based on performance"""
        performance = participant['adaptive_learning']['performance_history'][concept]
        
        if performance['attempts'] >= 3:
            accuracy = performance['correct'] / performance['attempts']
            
            if accuracy >= 0.8:
                participant['adaptive_learning']['current_levels'][concept] = 'advanced'
            elif accuracy >= 0.6:
                participant['adaptive_learning']['current_levels'][concept] = 'intermediate'
            else:
                participant['adaptive_learning']['current_levels'][concept] = 'beginner'

    def complete_module(self, module_key):
        """Mark a module as completed"""
        try:
            current_id = st.session_state.research_data['current_participant']
            if current_id:
                participant = st.session_state.research_data['participants'][current_id]
                participant['learning_progress']['module_progress'][module_key]['completed'] = True
                return True
        except Exception as e:
            st.error(f"Error completing module: {e}")
        return False

    def get_student_level(self, concept):
        """Get student's current level for a concept"""
        try:
            current_id = st.session_state.research_data['current_participant']
            if current_id:
                participant = st.session_state.research_data['participants'][current_id]
                return participant['adaptive_learning']['current_levels'].get(concept, 'beginner')
        except:
            return 'beginner'

# ==================== INSTRUMEN PENELITIAN - AMAS ====================
# ==================== INSTRUMEN PENELITIAN - AMAS ====================
class ResearchInstruments:
    def __init__(self):
        # AMAS (Abbreviated Math Anxiety Scale) - 9 items
        self.amas_questions = [
            {"question": "Mengerjakan soal matematika yang diberikan guru", "category": "Learning Mathematics"},
            {"question": "Mengerjakan soal matematika di papan tulis", "category": "Learning Mathematics"},
            {"question": "Mengerjakan ujian matematika", "category": "Evaluation Mathematics"},
            {"question": "Mempersiapkan ujian matematika", "category": "Evaluation Mathematics"},
            {"question": "Mendengar pelajaran matematika", "category": "Learning Mathematics"},
            {"question": "Mengerjakan PR matematika", "category": "Learning Mathematics"},
            {"question": "Membaca soal matematika di buku", "category": "Learning Mathematics"},
            {"question": "Mendapat nilai matematika yang buruk", "category": "Evaluation Mathematics"},
            {"question": "Memikirkan pelajaran matematika besok", "category": "Evaluation Mathematics"}
        ]
        
        # Pre Test Questions - 10 SOAL
        self.pre_test_questions = [
            {
                "id": 1,
                "question": "Sebuah restoran menawarkan 4 jenis makanan utama, 3 jenis minuman, dan 2 jenis dessert. Berapa banyak kombinasi menu yang berbeda yang dapat dipilih pelanggan?",
                "options": ["9", "12", "24", "36"],
                "correct_answer": "24",
                "concept": "prinsip_perkalian",
                "explanation": "Menggunakan prinsip perkalian: 4 makanan × 3 minuman × 2 dessert = 24 kombinasi"
            },
            {
                "id": 2,
                "question": "Dalam lomba lari 100m, ada 8 peserta. Berapa banyak kemungkinan susunan juara 1, 2, dan 3?",
                "options": ["56", "336", "512", "40320"],
                "correct_answer": "336",
                "concept": "permutasi", 
                "explanation": "Menggunakan permutasi P(8,3) = 8 × 7 × 6 = 336 susunan"
            },
            {
                "id": 3,
                "question": "Dari 10 orang, akan dipilih 4 orang untuk menjadi panitia. Berapa banyak cara memilih panitia tersebut?",
                "options": ["40", "210", "5040", "10000"],
                "correct_answer": "210",
                "concept": "kombinasi",
                "explanation": "Menggunakan kombinasi C(10,4) = 10!/(4!×6!) = 210 cara"
            },
            {
                "id": 4,
                "question": "Berapa banyak kata 4 huruf yang dapat disusun dari huruf-huruf pada kata 'MAJU'?",
                "options": ["16", "24", "256", "12"],
                "correct_answer": "24",
                "concept": "permutasi",
                "explanation": "Menyusun 4 huruf berbeda: 4! = 4 × 3 × 2 × 1 = 24 kata"
            },
            {
                "id": 5,
                "question": "Sebuah tim bola basket terdiri dari 5 pemain. Jika ada 12 pemain yang tersedia, berapa banyak tim berbeda yang dapat dibentuk?",
                "options": ["60", "792", "95040", "248832"],
                "correct_answer": "792", 
                "concept": "kombinasi",
                "explanation": "Menggunakan kombinasi C(12,5) = 12!/(5!×7!) = 792 tim"
            },
            {
                "id": 6,
                "question": "Password terdiri dari 3 huruf berbeda dari alfabet (26 huruf). Berapa banyak password yang mungkin?",
                "options": ["15600", "17576", "7800", "26000"],
                "correct_answer": "15600",
                "concept": "permutasi",
                "explanation": "P(26,3) = 26 × 25 × 24 = 15,600 password"
            },
            {
                "id": 7,
                "question": "Dari 6 buku berbeda, berapa cara memilih 2 buku untuk dibaca?",
                "options": ["12", "15", "30", "36"],
                "correct_answer": "15",
                "concept": "kombinasi",
                "explanation": "C(6,2) = 6!/(2!×4!) = 15 cara"
            },
            {
                "id": 8, 
                "question": "Ada 5 jalur bus dari kota A ke B, dan 3 jalur dari B ke C. Berapa banyak rute dari A ke C melalui B?",
                "options": ["8", "15", "20", "25"],
                "correct_answer": "15",
                "concept": "prinsip_perkalian", 
                "explanation": "5 jalur A→B × 3 jalur B→C = 15 rute"
            },
            {
                "id": 9,
                "question": "Dalam sebuah rapat, 7 orang duduk melingkar. Berapa banyak susunan duduk yang mungkin?",
                "options": ["5040", "720", "120", "2520"],
                "correct_answer": "720",
                "concept": "permutasi",
                "explanation": "Permutasi siklik: (7-1)! = 6! = 720 susunan"
            },
            {
                "id": 10,
                "question": "Menu cafe: 5 jenis kopi, 4 jenis kue. Berapa banyak kombinasi kopi + kue?",
                "options": ["9", "20", "25", "30"],
                "correct_answer": "20",
                "concept": "prinsip_perkalian",
                "explanation": "5 kopi × 4 kue = 20 kombinasi"
            }
        ]
        
        # Post Test Questions - 10 SOAL BERBEDA
        self.post_test_questions = [
            {
                "id": 1,
                "question": "Sebuah kode akses terdiri dari 2 huruf vokal (A,I,U,E,O) diikuti 3 angka. Berapa banyak kode yang mungkin?",
                "options": ["1250", "2500", "5000", "10000"],
                "correct_answer": "1250",
                "concept": "prinsip_perkalian",
                "explanation": "5 huruf vokal × 5 huruf vokal × 10 angka × 10 angka × 10 angka = 2500"
            },
            {
                "id": 2,
                "question": "Dari 9 orang, akan dipilih ketua, sekretaris, dan bendahara. Berapa banyak cara memilih?",
                "options": ["84", "504", "729", "362880"],
                "correct_answer": "504",
                "concept": "permutasi",
                "explanation": "P(9,3) = 9 × 8 × 7 = 504 cara"
            },
            {
                "id": 3, 
                "question": "Dalam sebuah komite yang terdiri dari 8 orang, dipilih 3 orang sebagai tim inti. Berapa banyak tim yang mungkin?",
                "options": ["56", "336", "512", "40320"],
                "correct_answer": "56",
                "concept": "kombinasi",
                "explanation": "C(8,3) = 8!/(3!×5!) = 56 tim"
            },
            {
                "id": 4,
                "question": "Berapa banyak bilangan 3 digit yang dapat dibentuk dari angka 1,2,3,4,5,6 tanpa pengulangan?",
                "options": ["120", "216", "256", "720"],
                "correct_answer": "120",
                "concept": "permutasi",
                "explanation": "P(6,3) = 6 × 5 × 4 = 120 bilangan"
            },
            {
                "id": 5,
                "question": "Dari 15 siswa, akan dipilih 5 siswa untuk lomba cerdas cermat. Berapa banyak cara memilih?",
                "options": ["3003", "3600", "1500", "32760"],
                "correct_answer": "3003",
                "concept": "kombinasi",
                "explanation": "C(15,5) = 15!/(5!×10!) = 3003 cara"
            },
            {
                "id": 6,
                "question": "Sebuah pizza dapat dipilih dengan 3 topping dari 8 topping yang tersedia. Berapa banyak kombinasi pizza?",
                "options": ["24", "56", "336", "512"],
                "correct_answer": "56",
                "concept": "kombinasi", 
                "explanation": "C(8,3) = 8!/(3!×5!) = 56 kombinasi"
            },
            {
                "id": 7,
                "question": "Password 4 digit (0-9) dengan angka tidak berulang. Berapa banyak password?",
                "options": ["10000", "5040", "6561", "210"],
                "correct_answer": "5040",
                "concept": "permutasi",
                "explanation": "P(10,4) = 10 × 9 × 8 × 7 = 5040 password"
            },
            {
                "id": 8,
                "question": "Ada 4 rute dari rumah ke kampus, dan 3 rute dari kampus ke perpustakaan. Berapa banyak perjalanan berbeda dari rumah ke perpustakaan via kampus?",
                "options": ["7", "12", "16", "20"],
                "correct_answer": "12",
                "concept": "prinsip_perkalian",
                "explanation": "4 rute × 3 rute = 12 perjalanan"
            },
            {
                "id": 9,
                "question": "Dalam sebuah kelompok 10 orang, berapa banyak jabat tangan jika setiap orang berjabat tangan sekali?",
                "options": ["45", "90", "100", "20"],
                "correct_answer": "45",
                "concept": "kombinasi",
                "explanation": "C(10,2) = 10!/(2!×8!) = 45 jabat tangan"
            },
            {
                "id": 10,
                "question": "Berapa banyak cara menyusun 5 buku berbeda di rak?",
                "options": ["25", "120", "625", "3125"],
                "correct_answer": "120",
                "concept": "permutasi",
                "explanation": "5! = 5 × 4 × 3 × 2 × 1 = 120 cara"
            }
        ]

    def render_amas_survey(self, survey_type="pre"):
        """Render AMAS anxiety survey"""
        st.markdown(f"""
        <div class='research-card'>
            <h2>📊 Survey Kecemasan Matematika ({'Awal' if survey_type == 'pre' else 'Akhir'})</h2>
            <p>Pilih seberapa cemas Anda merasa pada situasi berikut (1=Tidak Cemas, 5=Sangat Cemas):</p>
        </div>
        """, unsafe_allow_html=True)
        
        responses = []
        participant_id = st.session_state.participant_data.get('participant_id', 'unknown')
        
        for i, item in enumerate(self.amas_questions, 1):
            st.markdown(f"**{i}. {item['question']}**")
            
            unique_key = f"{participant_id}_amas_{survey_type}_{i}"
            
            response = st.radio(
                f"Seberapa cemas Anda?",
                options=[1, 2, 3, 4, 5],
                format_func=lambda x: {
                    1: "Tidak Cemas", 
                    2: "Sedikit Cemas", 
                    3: "Cukup Cemas", 
                    4: "Cemas", 
                    5: "Sangat Cemas"
                }[x],
                key=unique_key,
                horizontal=True
            )
            
            responses.append({
                "question": item['question'],
                "category": item['category'],
                "response": response
            })
        
        return responses

    def render_test(self, test_type="pre"):
        """Render pre/post test"""
        st.markdown(f"""
        <div class='test-card'>
            <h2>🎯 {'Diagnosis Awal' if test_type == 'pre' else 'Evaluasi Akhir'}</h2>
            <p>Jawablah soal-soal berikut untuk mengukur pemahaman Anda:</p>
        </div>
        """, unsafe_allow_html=True)
        
        questions = self.pre_test_questions if test_type == "pre" else self.post_test_questions
        
        answers = []
        score = 0
        participant_id = st.session_state.participant_data.get('participant_id', 'unknown')
        
        for i, question in enumerate(questions, 1):
            st.markdown(f"### Soal {i}")
            st.markdown(f"**{question['question']}**")
            
            unique_key = f"{participant_id}_{test_type}_q{i}"
            
            user_answer = st.radio(
                "Pilih jawaban:",
                options=question['options'],
                key=unique_key
            )
            
            is_correct = (user_answer == question['correct_answer'])
            if is_correct:
                score += 1
            
            answers.append({
                "question_id": question['id'],
                "user_answer": user_answer,
                "correct_answer": question['correct_answer'],
                "is_correct": is_correct,
                "concept": question['concept']
            })
        
        return answers, score
# ==================== ENHANCED LEARNING MODULES ====================
class EnhancedLearningModules:
    def __init__(self):
        self.modules = {
            'prinsip_perkalian': {
                'title': '🔢 Prinsip Perkalian',
                'description': 'Seni Menghitung Kemungkinan',
                'level': 'Dasar',
                'color': COLORS['secondary']
            },
            'permutasi': {
                'title': '🔄 Permutasi', 
                'description': 'Seni Menyusun dengan Presisi',
                'level': 'Menengah',
                'color': COLORS['primary']
            },
            'kombinasi': {
                'title': '👥 Kombinasi',
                'description': 'Power of Team Selection', 
                'level': 'Lanjutan',
                'color': COLORS['accent1']
            }
        }
        self.ai = DeepSeekAI()
    
    def render_module(self, module_key):
        """Render enhanced learning module with unlimited adaptive questions"""
        module = self.modules.get(module_key)
        
        if not module:
            st.error(f"Module {module_key} tidak ditemukan!")
            return
        
        participant_id = st.session_state.participant_data.get('participant_id', 'demo')
        student_level = research_system.get_student_level(module_key)
        
        st.markdown(f"""
        <div class='learning-card' style='background: linear-gradient(135deg, {module['color']} 0%, {module['color']}77 100%);'>
            <h1>{module['title']}</h1>
            <h3>{module['description']}</h3>
            <p>Level: {module['level']} • Sistem: Adaptive Learning • Level Anda: {student_level.title()}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # AI Explanation
        explanation = self.ai.get_ai_explanation(module_key, student_level)
        
        st.markdown(f"""
        <div class='explanation-box'>
            {explanation}
        </div>
        """, unsafe_allow_html=True)
        
        # AI Tutor Chat
        st.markdown("### 🤖 AI Tutor - Tanya Apa Saja!")
        user_question = st.text_input("Punya pertanyaan tentang materi ini?", 
                                    placeholder="Tanyakan apa yang belum kamu pahami...",
                                    key=f"ai_tutor_{module_key}")
        
        if user_question:
            with st.spinner("AI Tutor sedang memikirkan jawaban..."):
                ai_response = self.ai.ask_ai_tutor(user_question, f"Konsep: {module['title']}")
                st.markdown(f"""
                <div class='explanation-box'>
                    <h4>🤖 Jawaban AI Tutor:</h4>
                    {ai_response}
                </div>
                """, unsafe_allow_html=True)
        
        # Unlimited Adaptive Practice Problems
        st.markdown("### 🎯 Latihan Adaptif (Soal Tak Terbatas!)")
        st.info(f"🔍 Sistem menyesuaikan kesulitan soal berdasarkan kemampuan Anda. Level saat ini: **{student_level.title()}**")
        
        # Generate adaptive questions
        questions = self.ai.generate_adaptive_questions(
            concept=module_key,
            difficulty=student_level,
            count=5,
            student_level=student_level
        )
        
        for i, problem in enumerate(questions, 1):
            st.markdown(f"#### Soal {i}")
            st.markdown(f"**{problem['question']}**")
            
            # Display options
            user_answer = st.radio(
                "Pilih jawaban:",
                options=problem['options'],
                key=f"adaptive_{module_key}_{i}_{int(time.time())}"  # Unique key with timestamp
            )
            
            col1, col2 = st.columns([1, 4])
            
            with col1:
                if st.button("✅ Cek Jawaban", key=f"check_adaptive_{module_key}_{i}"):
                    is_correct = (user_answer == problem['answer'])
                    
                    if is_correct:
                        st.success(f"🎉 **BENAR!**")
                        st.info(f"**Penjelasan:** {problem['explanation']}")
                    else:
                        st.error("❌ **Belum tepat**")
                        st.info(f"💡 **Hint:** {problem['hint']}")
                        st.info(f"**Jawaban benar:** {problem['answer']}")
                    
                    # Update progress
                    research_system.update_learning_progress(module_key, is_correct)
            
            with col2:
                if st.button("💡 Butuh Bantuan?", key=f"hint_{module_key}_{i}"):
                    st.info(f"**Hint:** {problem['hint']}")
            
            st.markdown("---")
        
        # More questions button - GENERATE NEW QUESTIONS
        st.markdown("### 🔄 Ingin Latihan Lebih Banyak?")
        if st.button("🎲 Generate Soal Baru", key=f"refresh_{module_key}", use_container_width=True):
            st.rerun()
        
        # Module completion
        st.markdown("---")
        if st.button("✅ Selesaikan Modul", key=f"complete_{module_key}", use_container_width=True, type="primary"):
            if research_system.complete_module(module_key):
                st.success(f"🎊 **Modul {module['title']} berhasil diselesaikan!**")
                show_celebration()
                st.session_state.current_module = None
                st.rerun()
            else:
                st.error("❌ Gagal menyelesaikan modul. Coba lagi.")

# ==================== VISUALIZATION & ANALYTICS ====================
def generate_sample_data():
    """Generate research data from REAL participant data"""
    try:
        participants_data = st.session_state.research_data['participants']
        
        if not participants_data:
            return pd.DataFrame()
        
        participants = []
        for participant_id, data in participants_data.items():
            try:
                def safe_get(value, default=0):
                    if value is None: return default
                    try: return float(value) if value != '' else default
                    except: return default
                
                pre_anxiety = safe_get(data.get('anxiety_survey', {}).get('pre_score'))
                post_anxiety = safe_get(data.get('anxiety_survey', {}).get('post_score'))
                pre_test_score = safe_get(data.get('pre_test', {}).get('score'))
                post_test_score = safe_get(data.get('post_test', {}).get('score'))
                
                anxiety_reduction = pre_anxiety - post_anxiety
                test_improvement = post_test_score - pre_test_score
                
                progress = data.get('learning_progress', {})
                attempted = safe_get(progress.get('problems_attempted'))
                correct = safe_get(progress.get('problems_correct'))
                accuracy = (correct / attempted * 100) if attempted > 0 else 0
                
                # Get time spent
                start_time = data.get('registration_time')
                time_spent = 0
                if start_time:
                    try:
                        start_dt = datetime.fromisoformat(start_time)
                        end_dt = datetime.now()
                        time_spent = (end_dt - start_dt).total_seconds() / 60
                    except:
                        time_spent = 0
                
                participant = {
                    'id': participant_id,
                    'nama': data.get('demographics', {}).get('nama', 'Unknown'),
                    'pre_anxiety': pre_anxiety,
                    'post_anxiety': post_anxiety,
                    'anxiety_reduction': anxiety_reduction,
                    'pre_test_score': pre_test_score,
                    'post_test_score': post_test_score,
                    'test_improvement': test_improvement,
                    'problems_attempted': attempted,
                    'problems_correct': correct,
                    'accuracy': accuracy,
                    'time_spent': time_spent,
                    'concepts_learned': len(progress.get('concepts_learned', []))
                }
                participants.append(participant)
                
            except Exception: continue
        
        return pd.DataFrame(participants) if participants else pd.DataFrame()
        
    except Exception:
        return pd.DataFrame()

def create_progress_charts(participant_data):
    """Create beautiful progress charts for individual analytics"""
    
    # Data untuk charts
    concepts = ['Prinsip Perkalian', 'Permutasi', 'Kombinasi']
    
    # Chart 1: Progress per Konsep
    fig1 = go.Figure()
    
    # Add bars untuk setiap konsep
    for i, concept in enumerate(concepts):
        concept_key = concept.lower().replace(' ', '_')
        performance = participant_data['adaptive_learning']['performance_history'].get(concept_key, {'attempts': 0, 'correct': 0})
        
        if performance['attempts'] > 0:
            accuracy = (performance['correct'] / performance['attempts']) * 100
        else:
            accuracy = 0
            
        fig1.add_trace(go.Bar(
            name=concept,
            x=[concept],
            y=[accuracy],
            text=[f"{accuracy:.1f}%"],
            textposition='auto',
            marker_color=[COLORS['primary'], COLORS['secondary'], COLORS['accent1']][i]
        ))
    
    fig1.update_layout(
        title="📊 Akurasi Belajar per Konsep",
        xaxis_title="Konsep",
        yaxis_title="Akurasi (%)",
        showlegend=False,
        height=400
    )
    
    # Chart 2: Progress Timeline (simulasi)
    dates = pd.date_range(start='2024-01-01', periods=7, freq='D')
    accuracy_scores = np.random.randint(50, 95, 7)  # Simulasi data akurasi
    
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=dates,
        y=accuracy_scores,
        mode='lines+markers',
        name='Akurasi Harian',
        line=dict(color=COLORS['primary'], width=3),
        marker=dict(size=8)
    ))
    
    fig2.update_layout(
        title="📈 Trend Akurasi Belajar",
        xaxis_title="Tanggal",
        yaxis_title="Akurasi (%)",
        height=400
    )
    
    return fig1, fig2

def create_global_charts(df):
    """Create global analytics charts"""
    
    if df.empty:
        return None, None, None
    
    # Chart 1: Peningkatan Nilai
    fig1 = go.Figure()
    
    fig1.add_trace(go.Bar(
        name='Pre-Test',
        x=df['nama'],
        y=df['pre_test_score'],
        marker_color=COLORS['secondary']
    ))
    
    fig1.add_trace(go.Bar(
        name='Post-Test', 
        x=df['nama'],
        y=df['post_test_score'],
        marker_color=COLORS['primary']
    ))
    
    fig1.update_layout(
        title="📈 Perbandingan Nilai Pre-Test vs Post-Test",
        xaxis_title="Peserta",
        yaxis_title="Nilai",
        barmode='group',
        height=500
    )
    
    # Chart 2: Pengurangan Kecemasan
    fig2 = go.Figure()
    
    fig2.add_trace(go.Scatter(
        x=df['nama'],
        y=df['pre_anxiety'],
        mode='markers+lines',
        name='Pre-Survey',
        line=dict(color=COLORS['secondary'], dash='dash'),
        marker=dict(size=10)
    ))
    
    fig2.add_trace(go.Scatter(
        x=df['nama'],
        y=df['post_anxiety'],
        mode='markers+lines', 
        name='Post-Survey',
        line=dict(color=COLORS['primary']),
        marker=dict(size=10)
    ))
    
    fig2.update_layout(
        title="😰 PEnurunan Tingkat Kecemasan",
        xaxis_title="Peserta",
        yaxis_title="Skor Kecemasan",
        height=500
    )
    
    # Chart 3: Hubungan Waktu Belajar vs Akurasi
    fig3 = go.Figure()
    
    fig3.add_trace(go.Scatter(
        x=df['time_spent'],
        y=df['accuracy'],
        mode='markers',
        text=df['nama'],
        marker=dict(
            size=df['test_improvement']*5 + 10,  # Size berdasarkan improvement
            color=df['anxiety_reduction'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Pengurangan<br>Kecemasan")
        )
    ))
    
    fig3.update_layout(
        title="⏱️ Hubungan Waktu Belajar vs Akurasi",
        xaxis_title="Waktu Belajar (menit)",
        yaxis_title="Akurasi (%)",
        height=500
    )
    
    return fig1, fig2, fig3

def render_individual_analytics():
    """Render individual participant analytics dengan charts"""
    participant_data = st.session_state.participant_data
    
    if not participant_data['participant_id']:
        st.warning("⚠️ Silakan daftar terlebih dahulu")
        return
    
    st.markdown("""
    <div class='research-card'>
        <h1>📈 Analisis Perkembangan Individual</h1>
        <p>Lihat perkembangan belajar dan pengurangan kecemasan matematika Anda.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        pre_score = participant_data['pre_test'].get('score', 0) or 0
        post_score = participant_data['post_test'].get('score', 0) or 0
        improvement = post_score - pre_score
        st.markdown(f"""
        <div class='metric-card'>
            <div class='stat-value'>{improvement}</div>
            <div class='stat-label'>Peningkatan Nilai</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        pre_anxiety = participant_data['anxiety_survey'].get('pre_score', 0) or 0
        post_anxiety = participant_data['anxiety_survey'].get('post_score', 0) or 0
        anxiety_reduction = pre_anxiety - post_anxiety
        st.markdown(f"""
        <div class='metric-card'>
            <div class='stat-value'>{anxiety_reduction:.1f}</div>
            <div class='stat-label'>Pengurangan Kecemasan</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        attempted = participant_data['learning_progress'].get('problems_attempted', 0)
        correct = participant_data['learning_progress'].get('problems_correct', 0)
        accuracy = (correct / attempted * 100) if attempted > 0 else 0
        st.markdown(f"""
        <div class='metric-card'>
            <div class='stat-value'>{accuracy:.1f}%</div>
            <div class='stat-label'>Akurasi Belajar</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        # Calculate time spent
        start_time = participant_data.get('registration_time')
        time_spent = 0
        if start_time:
            try:
                start_dt = datetime.fromisoformat(start_time)
                end_dt = datetime.now()
                time_spent = (end_dt - start_dt).total_seconds() / 60
            except:
                time_spent = 0
        st.markdown(f"""
        <div class='metric-card'>
            <div class='stat-value'>{time_spent:.0f}m</div>
            <div class='stat-label'>Waktu Belajar</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Progress Charts
    st.markdown("### 📊 Grafik Perkembangan Belajar")
    
    fig1, fig2 = create_progress_charts(participant_data)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.plotly_chart(fig2, use_container_width=True)
    
    # Adaptive Learning Levels
    st.markdown("### 🎯 Level Pembelajaran Adaptif")
    adaptive_data = participant_data.get('adaptive_learning', {})
    current_levels = adaptive_data.get('current_levels', {})
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        level = current_levels.get('prinsip_perkalian', 'beginner')
        color = "#00D4FF" if level == 'advanced' else "#FF6B35" if level == 'intermediate' else "#7928CA"
        st.markdown(f"""
        <div style='background: {color}; color: white; padding: 2rem; border-radius: 15px; text-align: center;'>
            <h3>Prinsip Perkalian</h3>
            <h2>{level.title()}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        level = current_levels.get('permutasi', 'beginner')
        color = "#00D4FF" if level == 'advanced' else "#FF6B35" if level == 'intermediate' else "#7928CA"
        st.markdown(f"""
        <div style='background: {color}; color: white; padding: 2rem; border-radius: 15px; text-align: center;'>
            <h3>Permutasi</h3>
            <h2>{level.title()}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        level = current_levels.get('kombinasi', 'beginner')
        color = "#00D4FF" if level == 'advanced' else "#FF6B35" if level == 'intermediate' else "#7928CA"
        st.markdown(f"""
        <div style='background: {color}; color: white; padding: 2rem; border-radius: 15px; text-align: center;'>
            <h3>Kombinasi</h3>
            <h2>{level.title()}</h2>
        </div>
        """, unsafe_allow_html=True)

def render_global_analytics():
    """Render global research analytics dengan charts lengkap"""
    df = generate_sample_data()
    
    if df.empty:
        st.info("📊 Data penelitian akan muncul di sini setelah peserta menyelesaikan program.")
        return
    
    st.markdown('<div class="section-header">🌍 ANALISIS DATA GLOBAL</div>', unsafe_allow_html=True)
    
    # Global Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_improvement = df['test_improvement'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <div class="stat-value">{avg_improvement:.1f}</div>
            <div class="stat-label">Rata² Peningkatan Nilai</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        avg_anxiety_reduction = df['anxiety_reduction'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <div class="stat-value">{avg_anxiety_reduction:.1f}</div>
            <div class="stat-label">Rata² Pengurangan Kecemasan</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        avg_accuracy = df['accuracy'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <div class="stat-value">{avg_accuracy:.1f}%</div>
            <div class="stat-label">Rata² Akurasi</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        avg_time = df['time_spent'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <div class="stat-value">{avg_time:.0f}m</div>
            <div class="stat-label">Rata² Waktu Belajar</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Global Charts
    st.markdown("### 📈 Grafik Analisis Global")
    
    fig1, fig2, fig3 = create_global_charts(df)
    
    if fig1 and fig2 and fig3:
        st.plotly_chart(fig1, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(fig2, use_container_width=True)
        
        with col2:
            st.plotly_chart(fig3, use_container_width=True)

# ==================== MAIN APPLICATION FUNCTIONS ====================
def render_dashboard():
    """Render main dashboard"""
    st.markdown("""
    <div class='research-card'>
        <h1>🌟 Selamat Datang di EasyNatorics!</h1>
        <p>Platform pembelajaran kombinatorika dengan <strong>AI personalisasi</strong> untuk mengurangi kecemasan matematika.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Mulai Perjalanan Belajar", use_container_width=True, type="primary"):
        st.session_state.current_page = "Pendaftaran"
        st.rerun()

def render_registration():
    """Render participant registration form"""
    st.markdown("""
    <div class='research-card'>
        <h1>📝 Pendaftaran Peserta Penelitian</h1>
        <p>Isi data diri Anda untuk bergabung dalam penelitian ini.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("registration_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            nama = st.text_input("Nama Lengkap*", placeholder="Masukkan nama lengkap")
            kelas = st.selectbox("Kelas*", ["10", "11", "12"])
        
        with col2:
            usia = st.number_input("Usia*", min_value=15, max_value=18, value=16)
            pengalaman = st.selectbox(
                "Pengalaman Belajar Matematika*",
                ["Pemula", "Menengah", "Lanjutan"]
            )
        
        consent = st.checkbox("Saya setuju untuk berpartisipasi dalam penelitian ini*")
        
        if st.form_submit_button("🚀 Daftar Sekarang", type="primary"):
            if not all([nama, kelas, usia, pengalaman, consent]):
                st.error("❌ Harap lengkapi semua field yang wajib diisi!")
            else:
                demographics = {
                    'nama': nama,
                    'kelas': kelas,
                    'usia': usia,
                    'pengalaman': pengalaman
                }
                
                participant_id = research_system.register_participant(demographics)
                if participant_id:
                    st.success(f"🎉 Pendaftaran berhasil! ID Anda: **{participant_id}**")
                    st.balloons()
                    st.session_state.current_page = "Survey Awal"
                    st.rerun()

def render_pre_survey(instruments):
    """Render pre-anxiety survey"""
    if not st.session_state.participant_data['participant_id']:
        st.warning("⚠️ Silakan daftar terlebih dahulu")
        return
    
    st.markdown("""
    <div class='research-card'>
        <h1>📊 Survey Kecemasan Matematika (Awal)</h1>
        <p>Survey ini mengukur tingkat kecemasan Anda terhadap matematika sebelum memulai pembelajaran.</p>
    </div>
    """, unsafe_allow_html=True)
    
    responses = instruments.render_amas_survey("pre")
    
    if st.button("📨 Submit Survey Awal & Lanjut ke Pre-Test", type="primary", use_container_width=True):
        amas_score = research_system.calculate_amas_score(responses)
        anxiety_level = research_system.get_anxiety_level(amas_score)
        
        st.session_state.participant_data['anxiety_survey']['pre_score'] = amas_score
        st.session_state.participant_data['anxiety_survey']['responses'] = responses
        
        st.success(f"""
        ✅ Survey berhasil disimpan!
        
        **Skor Kecemasan Awal:** {amas_score:.2f}
        **Tingkat Kecemasan:** {anxiety_level}
        """)
        
        st.session_state.current_page = "Pre-Test"
        st.rerun()

def render_pre_test(instruments):
    """Render pre-test assessment"""
    if not st.session_state.participant_data['participant_id']:
        st.warning("⚠️ Silakan daftar terlebih dahulu")
        return
    
    st.markdown("""
    <div class='test-card'>
        <h1>🎯 Pre-Test - Diagnosis Kemampuan Awal</h1>
        <p>Test ini mengukur pemahaman awal Anda tentang kombinatorika.</p>
    </div>
    """, unsafe_allow_html=True)
    
    answers, score = instruments.render_test("pre")
    
    if st.button("📊 Lihat Hasil Pre-Test & Lanjut Belajar", type="primary", use_container_width=True):
        st.session_state.participant_data['pre_test']['answers'] = answers
        st.session_state.participant_data['pre_test']['score'] = score
        st.session_state.participant_data['pre_test']['completion_time'] = datetime.now().isoformat()
        
        st.markdown(f"""
        <div class='success-card'>
            <h2>📊 Hasil Pre-Test</h2>
            <h1>{score}/3</h1>
            <h3>{round(score/3*100)}%</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.session_state.current_page = "Belajar"
        st.rerun()

def render_learning_center(learning_modules):
    """Render interactive learning center"""
    if not st.session_state.participant_data['participant_id']:
        st.warning("⚠️ Silakan daftar terlebih dahulu")
        return
    
    st.markdown("""
    <div class='research-card'>
        <h1>📚 Pusat Pembelajaran Interaktif</h1>
        <p>Jelajahi dunia kombinatorika melalui modul-modul interaktif.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Pilih Modul Pembelajaran")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔢 Prinsip Perkalian", use_container_width=True, type="primary"):
            st.session_state.current_module = 'prinsip_perkalian'
    
    with col2:
        if st.button("🔄 Permutasi", use_container_width=True, type="primary"):
            st.session_state.current_module = 'permutasi'
    
    with col3:
        if st.button("👥 Kombinasi", use_container_width=True, type="primary"):
            st.session_state.current_module = 'kombinasi'
    
    if st.session_state.current_module:
        learning_modules.render_module(st.session_state.current_module)
    else:
        st.markdown("""
        <div class='learning-card'>
            <h2>🚀 Siap Memulai Perjalanan Belajar?</h2>
            <p>Pilih salah satu modul di atas untuk mulai menjelajahi konsep kombinatorika!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Continue to Post-Test button
    completed_modules = sum(1 for module in st.session_state.participant_data['learning_progress']['module_progress'].values() if module['completed'])
    if completed_modules >= 2:
        if st.button("🎯 Lanjut ke Post-Test", type="primary", use_container_width=True):
            st.session_state.current_page = "Post-Test"
            st.rerun()

def render_post_test(instruments):
    """Render post-test assessment"""
    if not st.session_state.participant_data['participant_id']:
        st.warning("⚠️ Silakan daftar terlebih dahulu")
        return
    
    st.markdown("""
    <div class='test-card'>
        <h1>🚀 Post-Test - Evaluasi Peningkatan</h1>
        <p>Test ini mengukur peningkatan pemahaman Anda setelah pembelajaran.</p>
    </div>
    """, unsafe_allow_html=True)
    
    answers, score = instruments.render_test("post")
    
    if st.button("📊 Lihat Hasil Post-Test", type="primary", use_container_width=True):
        st.session_state.participant_data['post_test']['answers'] = answers
        st.session_state.participant_data['post_test']['score'] = score
        st.session_state.participant_data['post_test']['completion_time'] = datetime.now().isoformat()
        
        pre_score = st.session_state.participant_data['pre_test'].get('score', 0) or 0
        improvement = score - pre_score
        
        st.markdown(f"""
        <div class='success-card'>
            <h2>📊 Hasil Post-Test</h2>
            <h1>{score}/3</h1>
            <h3>{round(score/3*100)}%</h3>
            <h4>📈 Peningkatan: +{improvement} poin</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.session_state.current_page = "Survey Akhir"
        st.rerun()

def render_final_survey(instruments):
    """Render final anxiety survey and testimonial"""
    st.markdown("""
    <div class='research-card'>
        <h1>📊 Survey Kecemasan Akhir & Testimoni</h1>
        <p>Isi survey akhir dan berikan testimoni tentang pengalaman belajar Anda.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Survey Kecemasan Akhir")
    post_responses = instruments.render_amas_survey("post")
    
    st.markdown("### 💬 Testimoni")
    testimonial = st.text_area("Bagikan pengalaman belajar Anda dengan EasyNatorics:", 
                              placeholder="Apa yang paling Anda sukai? Apakah ada saran perbaikan?")
    
    if st.button("📨 Submit Semua & Lihat Hasil Akhir", type="primary", use_container_width=True):
        # Save post anxiety survey
        post_amas_score = research_system.calculate_amas_score(post_responses)
        st.session_state.participant_data['anxiety_survey']['post_score'] = post_amas_score
        
        # Save testimonial
        st.session_state.participant_data['satisfaction_survey']['testimonial'] = testimonial
        
        st.success("✅ Semua data berhasil disimpan! Terima kasih telah berpartisipasi.")
        st.session_state.current_page = "Hasil & Analisis"
        st.rerun()

def render_final_results():
    """Render final results with comprehensive analytics"""
    participant_data = st.session_state.participant_data
    
    st.markdown("""
    <div class='research-card'>
        <h1>📈 Hasil Akhir & Analisis Komprehensif</h1>
        <p>Lihat pencapaian dan perkembangan belajar Anda selama program penelitian.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Individual Analytics
    render_individual_analytics()
    
    # Testimonial Display
    if participant_data['satisfaction_survey'].get('testimonial'):
        st.markdown("### 💬 Testimoni Anda")
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {COLORS['accent1']} 0%, {COLORS['secondary']} 100%);
                    color: white; border-radius: 15px; padding: 1.5rem; margin: 1rem 0;'>
            <p>"{participant_data['satisfaction_survey']['testimonial']}"</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Global Analytics
    render_global_analytics()

# ==================== MAIN APPLICATION ====================
def main():
    # Initialize systems
    global research_system
    research_system = ResearchDataSystem()
    instruments = ResearchInstruments()
    learning_modules = EnhancedLearningModules()
    
    apply_futuristic_style()
    
    # Initialize session state for navigation
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Dashboard"
    
    # Main title
    st.markdown("""
    <div class="main-title">
        EasyNatorics
    </div>
    <div style="text-align: center; color: #00D4FF; font-size: 1.5rem; margin-bottom: 3rem;">
        Jelajah Kombinatorika dengan Metakognisi & AI
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    with st.sidebar:
        st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h2 style="color: #00D4FF;">🧭 Navigasi</h2>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.participant_data['participant_id']:
            participant_id = st.session_state.participant_data['participant_id']
            st.success(f"👤 Participant: {participant_id}")
        
        # Navigation options
        nav_options = [
            "🏠 Dashboard", 
            "📝 Pendaftaran", 
            "📊 Survey Awal",
            "🎯 Pre-Test", 
            "📚 Belajar", 
            "🚀 Post-Test",
            "📝 Survey Akhir",
            "📈 Hasil & Analisis"
        ]
        
        page_mapping = {
            "🏠 Dashboard": "Dashboard",
            "📝 Pendaftaran": "Pendaftaran", 
            "📊 Survey Awal": "Survey Awal",
            "🎯 Pre-Test": "Pre-Test",
            "📚 Belajar": "Belajar",
            "🚀 Post-Test": "Post-Test", 
            "📝 Survey Akhir": "Survey Akhir",
            "📈 Hasil & Analisis": "Hasil & Analisis"
        }
        
        current_display = [k for k, v in page_mapping.items() if v == st.session_state.current_page]
        default_index = 0
        if current_display:
            default_index = nav_options.index(current_display[0])
        
        selected_nav = st.radio("Pilih Tahapan:", nav_options, index=default_index)
        st.session_state.current_page = page_mapping[selected_nav]
    
    # Page routing
    if st.session_state.current_page == "Dashboard":
        render_dashboard()
    elif st.session_state.current_page == "Pendaftaran":
        render_registration()
    elif st.session_state.current_page == "Survey Awal":
        render_pre_survey(instruments)
    elif st.session_state.current_page == "Pre-Test":
        render_pre_test(instruments)
    elif st.session_state.current_page == "Belajar":
        render_learning_center(learning_modules)
    elif st.session_state.current_page == "Post-Test":
        render_post_test(instruments)
    elif st.session_state.current_page == "Survey Akhir":
        render_final_survey(instruments)
    elif st.session_state.current_page == "Hasil & Analisis":
        render_final_results()

# ==================== RUN APPLICATION ====================
if __name__ == "__main__":
    main()
