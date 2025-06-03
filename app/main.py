from nicegui import ui
import json
import os
from typing import List, Dict, Any, Optional
from datetime import datetime

# Load portfolio data
def load_portfolio_data() -> Dict[str, Any]:
    """Load portfolio data from JSON file or return default data if file doesn't exist."""
    try:
        with open('static/data/portfolio_data.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return default data if file doesn't exist or is invalid
        return {
            "personal_info": {
                "name": "Alex Johnson",
                "title": "NLP Engineer & Data Scientist",
                "bio": "Passionate NLP engineer with 5+ years of experience developing cutting-edge language models and applications. Specialized in transformer architectures, sentiment analysis, and conversational AI.",
                "email": "alex.johnson@example.com",
                "github": "github.com/alexjohnson-nlp",
                "linkedin": "linkedin.com/in/alexjohnson-nlp",
                "profile_image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fHByb2ZpbGV8ZW58MHx8MHx8fDA%3D"
            },
            "skills": [
                {"name": "Natural Language Processing", "level": 95},
                {"name": "Machine Learning", "level": 90},
                {"name": "Python", "level": 95},
                {"name": "PyTorch", "level": 85},
                {"name": "TensorFlow", "level": 80},
                {"name": "Hugging Face Transformers", "level": 90},
                {"name": "BERT/GPT Models", "level": 85},
                {"name": "Sentiment Analysis", "level": 90},
                {"name": "Text Classification", "level": 85},
                {"name": "Named Entity Recognition", "level": 80},
                {"name": "Data Visualization", "level": 75},
                {"name": "SQL", "level": 70}
            ],
            "projects": [
                {
                    "title": "Multilingual Sentiment Analysis Engine",
                    "description": "Developed a state-of-the-art sentiment analysis system supporting 15+ languages using fine-tuned XLM-RoBERTa models. Achieved 92% accuracy across diverse domains including social media, product reviews, and news articles.",
                    "technologies": ["PyTorch", "Transformers", "FastAPI", "Docker"],
                    "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                    "github_link": "https://github.com/alexjohnson-nlp/multilingual-sentiment"
                },
                {
                    "title": "Conversational Customer Support Bot",
                    "description": "Built an end-to-end conversational AI system for a major e-commerce platform that handles 60% of customer inquiries automatically. Implemented context-aware dialogue management and seamless human handoff protocols.",
                    "technologies": ["Rasa", "TensorFlow", "MongoDB", "Kubernetes"],
                    "image": "https://images.unsplash.com/photo-1531746790731-6c087fecd65a?q=80&w=2006&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                    "github_link": "https://github.com/alexjohnson-nlp/conv-support-bot"
                },
                {
                    "title": "Document Intelligence Platform",
                    "description": "Created an NLP pipeline for extracting structured information from legal and financial documents. The system processes contracts, invoices, and reports with 95% extraction accuracy, saving 1000+ manual processing hours monthly.",
                    "technologies": ["spaCy", "BERT", "Flask", "PostgreSQL"],
                    "image": "https://images.unsplash.com/photo-1568027762272-e4da8b8dde3d?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                    "github_link": "https://github.com/alexjohnson-nlp/doc-intelligence"
                },
                {
                    "title": "Semantic Search Engine",
                    "description": "Developed a semantic search system using dense vector embeddings that improved search relevance by 40% compared to keyword-based approaches. Implemented efficient ANN search with FAISS for sub-second query times over millions of documents.",
                    "technologies": ["Sentence-Transformers", "FAISS", "Elasticsearch", "React"],
                    "image": "https://images.unsplash.com/photo-1555952494-efd681c7e3f9?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                    "github_link": "https://github.com/alexjohnson-nlp/semantic-search"
                }
            ],
            "experience": [
                {
                    "company": "AI Language Labs",
                    "position": "Senior NLP Engineer",
                    "period": "2021 - Present",
                    "description": "Lead development of production NLP systems for Fortune 500 clients. Architect and implement custom language models for domain-specific applications."
                },
                {
                    "company": "TechCorp Solutions",
                    "position": "Machine Learning Engineer",
                    "period": "2019 - 2021",
                    "description": "Developed and deployed NLP models for text classification, named entity recognition, and sentiment analysis. Improved model accuracy by 25% through advanced feature engineering."
                },
                {
                    "company": "DataScience Innovations",
                    "position": "Data Scientist",
                    "period": "2017 - 2019",
                    "description": "Implemented machine learning solutions for text and time-series data. Created NLP pipelines for processing customer feedback and support tickets."
                }
            ],
            "education": [
                {
                    "institution": "Stanford University",
                    "degree": "M.S. in Computer Science, NLP Specialization",
                    "period": "2015 - 2017"
                },
                {
                    "institution": "University of Washington",
                    "degree": "B.S. in Computer Science and Linguistics",
                    "period": "2011 - 2015"
                }
            ],
            "publications": [
                {
                    "title": "Improving Cross-lingual Transfer Learning in Transformer Models",
                    "venue": "ACL 2022",
                    "year": 2022,
                    "link": "https://example.com/paper1"
                },
                {
                    "title": "Efficient Fine-tuning Strategies for Domain Adaptation in NLP",
                    "venue": "EMNLP 2021",
                    "year": 2021,
                    "link": "https://example.com/paper2"
                },
                {
                    "title": "Attention Mechanisms for Low-Resource Language Processing",
                    "venue": "NAACL 2020",
                    "year": 2020,
                    "link": "https://example.com/paper3"
                }
            ]
        }

# Create directory for static data if it doesn't exist
os.makedirs('static/data', exist_ok=True)

# Save default data if file doesn't exist
if not os.path.exists('static/data/portfolio_data.json'):
    with open('static/data/portfolio_data.json', 'w') as f:
        json.dump(load_portfolio_data(), f, indent=2)

# Add custom CSS
ui.add_head_html("""
<style>
    :root {
        --primary: #4F46E5;
        --primary-dark: #4338CA;
        --secondary: #10B981;
        --dark: #1F2937;
        --light: #F9FAFB;
        --gray: #6B7280;
        --light-gray: #E5E7EB;
    }
    
    body {
        font-family: 'Inter', sans-serif;
        color: var(--dark);
        background-color: var(--light);
    }
    
    .page-container {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--dark);
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid var(--primary);
        display: inline-block;
    }
    
    .card {
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
    }
    
    .project-card {
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    
    .project-image {
        height: 200px;
        object-fit: cover;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
    }
    
    .skill-bar {
        height: 10px;
        background-color: var(--light-gray);
        border-radius: 5px;
        margin-top: 5px;
        overflow: hidden;
    }
    
    .skill-progress {
        height: 100%;
        background-color: var(--primary);
        border-radius: 5px;
    }
    
    .nav-link {
        padding: 0.5rem 1rem;
        color: var(--dark);
        text-decoration: none;
        font-weight: 500;
        border-radius: 4px;
        transition: background-color 0.3s ease;
    }
    
    .nav-link:hover, .nav-link.active {
        background-color: rgba(79, 70, 229, 0.1);
        color: var(--primary);
    }
    
    .contact-icon {
        font-size: 1.5rem;
        color: var(--primary);
        margin-right: 1rem;
        transition: transform 0.3s ease;
    }
    
    .contact-icon:hover {
        transform: scale(1.2);
    }
    
    .profile-image {
        border-radius: 50%;
        border: 4px solid white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .experience-item, .education-item, .publication-item {
        position: relative;
        padding-left: 20px;
        margin-bottom: 1.5rem;
    }
    
    .experience-item:before, .education-item:before, .publication-item:before {
        content: "";
        position: absolute;
        left: 0;
        top: 5px;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: var(--primary);
    }
    
    .tech-tag {
        background-color: rgba(79, 70, 229, 0.1);
        color: var(--primary);
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 500;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        display: inline-block;
    }
    
    @media (max-width: 768px) {
        .profile-section {
            flex-direction: column;
            text-align: center;
        }
        
        .profile-image {
            margin-bottom: 1rem;
        }
    }
</style>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""")

# Load portfolio data
portfolio_data = load_portfolio_data()

@ui.page('/')
def index():
    ui.add_head_html("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Professional portfolio of an NLP Engineer showcasing projects, skills, and experience in natural language processing and machine learning.">
    """)
    
    with ui.column().classes('page-container w-full max-w-screen-xl mx-auto px-4 py-8'):
        # Navigation
        with ui.row().classes('w-full justify-between items-center mb-8'):
            ui.label(portfolio_data['personal_info']['name']).classes('text-2xl font-bold')
            
            with ui.row().classes('gap-2'):
                ui.link('Home', '#home').classes('nav-link active')
                ui.link('Projects', '#projects').classes('nav-link')
                ui.link('Skills', '#skills').classes('nav-link')
                ui.link('Experience', '#experience').classes('nav-link')
                ui.link('Contact', '#contact').classes('nav-link')
        
        # Hero Section
        with ui.row().classes('w-full items-center mb-16 profile-section') as hero_section:
            hero_section.style('scroll-margin-top: 2rem;')
            hero_section.props('id=home')
            
            ui.image(portfolio_data['personal_info']['profile_image']).classes('w-48 h-48 profile-image')
            
            with ui.column().classes('ml-8 flex-1'):
                ui.label(portfolio_data['personal_info']['name']).classes('text-4xl font-bold mb-2')
                ui.label(portfolio_data['personal_info']['title']).classes('text-xl text-gray-600 mb-4')
                ui.label(portfolio_data['personal_info']['bio']).classes('text-gray-700 mb-6')
                
                with ui.row().classes('gap-4'):
                    with ui.link(target=f"mailto:{portfolio_data['personal_info']['email']}").classes('flex items-center'):
                        ui.icon('mail').classes('contact-icon')
                        ui.label('Email').classes('text-gray-700')
                    
                    with ui.link(target=f"https://{portfolio_data['personal_info']['github']}", new_tab=True).classes('flex items-center'):
                        ui.html('<i class="fab fa-github contact-icon"></i>')
                        ui.label('GitHub').classes('text-gray-700')
                    
                    with ui.link(target=f"https://{portfolio_data['personal_info']['linkedin']}", new_tab=True).classes('flex items-center'):
                        ui.html('<i class="fab fa-linkedin contact-icon"></i>')
                        ui.label('LinkedIn').classes('text-gray-700')
        
        # Projects Section
        with ui.column().classes('w-full mb-16') as projects_section:
            projects_section.style('scroll-margin-top: 2rem;')
            projects_section.props('id=projects')
            
            ui.label('Projects').classes('section-title')
            
            with ui.grid(columns=2).classes('gap-6'):
                for project in portfolio_data['projects']:
                    with ui.card().classes('project-card card'):
                        ui.image(project['image']).classes('project-image')
                        
                        with ui.card_section():
                            ui.label(project['title']).classes('text-xl font-bold mb-2')
                            ui.label(project['description']).classes('text-gray-700 mb-4')
                            
                            with ui.row().classes('flex-wrap mb-4'):
                                for tech in project['technologies']:
                                    ui.label(tech).classes('tech-tag')
                            
                            with ui.link(target=project['github_link'], new_tab=True).classes('text-primary font-medium'):
                                ui.html('<i class="fab fa-github mr-2"></i> View on GitHub')
        
        # Skills Section
        with ui.column().classes('w-full mb-16') as skills_section:
            skills_section.style('scroll-margin-top: 2rem;')
            skills_section.props('id=skills')
            
            ui.label('Skills').classes('section-title')
            
            with ui.grid(columns=2).classes('gap-6'):
                for skill in portfolio_data['skills']:
                    with ui.column().classes('mb-4'):
                        with ui.row().classes('justify-between w-full'):
                            ui.label(skill['name']).classes('font-medium')
                            ui.label(f"{skill['level']}%").classes('text-gray-600')
                        
                        with ui.element('div').classes('skill-bar'):
                            ui.element('div').classes('skill-progress').style(f"width: {skill['level']}%")
        
        # Experience Section
        with ui.column().classes('w-full mb-16') as experience_section:
            experience_section.style('scroll-margin-top: 2rem;')
            experience_section.props('id=experience')
            
            ui.label('Experience').classes('section-title')
            
            for exp in portfolio_data['experience']:
                with ui.column().classes('experience-item'):
                    with ui.row().classes('justify-between w-full'):
                        ui.label(exp['position']).classes('text-lg font-bold')
                        ui.label(exp['period']).classes('text-gray-600')
                    ui.label(exp['company']).classes('text-primary font-medium mb-2')
                    ui.label(exp['description']).classes('text-gray-700')
        
        # Education Section
        with ui.column().classes('w-full mb-16'):
            ui.label('Education').classes('section-title')
            
            for edu in portfolio_data['education']:
                with ui.column().classes('education-item'):
                    with ui.row().classes('justify-between w-full'):
                        ui.label(edu['degree']).classes('text-lg font-bold')
                        ui.label(edu['period']).classes('text-gray-600')
                    ui.label(edu['institution']).classes('text-primary font-medium')
        
        # Publications Section
        with ui.column().classes('w-full mb-16'):
            ui.label('Publications').classes('section-title')
            
            for pub in portfolio_data['publications']:
                with ui.column().classes('publication-item'):
                    ui.link(pub['title'], target=pub['link'], new_tab=True).classes('text-lg font-bold hover:text-primary')
                    ui.label(f"{pub['venue']} • {pub['year']}").classes('text-gray-600')
        
        # Contact Section
        with ui.column().classes('w-full mb-8') as contact_section:
            contact_section.style('scroll-margin-top: 2rem;')
            contact_section.props('id=contact')
            
            ui.label('Contact').classes('section-title')
            
            with ui.row().classes('gap-8 flex-wrap'):
                with ui.column().classes('flex-1 min-w-[300px]'):
                    ui.label('Get in touch').classes('text-xl font-bold mb-4')
                    ui.label("I'm always open to discussing new projects, creative ideas, or opportunities to be part of your vision.").classes('text-gray-700 mb-6')
                    
                    with ui.row().classes('mb-4'):
                        ui.icon('mail').classes('text-primary mr-2')
                        ui.link(portfolio_data['personal_info']['email'], target=f"mailto:{portfolio_data['personal_info']['email']}").classes('text-gray-700')
                    
                    with ui.row().classes('mb-4'):
                        ui.html('<i class="fab fa-github text-primary mr-2"></i>')
                        ui.link(portfolio_data['personal_info']['github'], target=f"https://{portfolio_data['personal_info']['github']}", new_tab=True).classes('text-gray-700')
                    
                    with ui.row():
                        ui.html('<i class="fab fa-linkedin text-primary mr-2"></i>')
                        ui.link(portfolio_data['personal_info']['linkedin'], target=f"https://{portfolio_data['personal_info']['linkedin']}", new_tab=True).classes('text-gray-700')
                
                with ui.column().classes('flex-1 min-w-[300px]'):
                    ui.label('Send a message').classes('text-xl font-bold mb-4')
                    
                    name = ui.input('Name').classes('w-full mb-4')
                    email = ui.input('Email').classes('w-full mb-4')
                    message = ui.textarea('Message').classes('w-full mb-4').style('min-height: 120px')
                    
                    def send_message():
                        if name.value and email.value and message.value:
                            ui.notify('Message sent successfully!', type='positive')
                            name.value = ''
                            email.value = ''
                            message.value = ''
                        else:
                            ui.notify('Please fill all fields', type='negative')
                    
                    ui.button('Send Message', on_click=send_message).classes('bg-primary text-white')
        
        # Footer
        with ui.row().classes('w-full justify-between items-center pt-8 border-t border-gray-200'):
            ui.label(f"© {datetime.now().year} {portfolio_data['personal_info']['name']}. All rights reserved.").classes('text-gray-600')
            
            with ui.row().classes('gap-4'):
                ui.link(target=f"mailto:{portfolio_data['personal_info']['email']}").classes('text-gray-600 hover:text-primary'):
                    ui.icon('mail')
                
                ui.link(target=f"https://{portfolio_data['personal_info']['github']}", new_tab=True).classes('text-gray-600 hover:text-primary'):
                    ui.html('<i class="fab fa-github"></i>')
                
                ui.link(target=f"https://{portfolio_data['personal_info']['linkedin']}", new_tab=True).classes('text-gray-600 hover:text-primary'):
                    ui.html('<i class="fab fa-linkedin"></i>')

# Health check endpoint
@ui.page('/health')
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}