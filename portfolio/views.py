import logging
import traceback

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

logger = logging.getLogger(__name__)


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            try:
                sent = send_mail(
                    subject=f"Portfolio Contact from {contact.name}",
                    message=(
                        f"You have a new message from your portfolio contact form.\n\n"
                        f"Name: {contact.name}\n"
                        f"Email: {contact.email}\n\n"
                        f"Message:\n{contact.message}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_RECIPIENT_EMAIL],
                    fail_silently=False,
                )
                if sent:
                    logger.info("Contact email delivered to %s", settings.CONTACT_RECIPIENT_EMAIL)
                    messages.success(request, 'Thank you! Your message has been sent successfully.')
                else:
                    logger.error("send_mail returned 0 - email NOT delivered.")
                    messages.error(request, 'Message saved, but email delivery failed. Check server logs.')
            except Exception as exc:
                logger.error("Email send failed: %s\n%s", exc, traceback.format_exc())
                print("\n[CONTACT FORM EMAIL ERROR]", exc, "\n", traceback.format_exc())
                messages.error(
                    request,
                    f'Message saved, but email could not be sent ({exc.__class__.__name__}). '
                    f'Check Gmail App Password / .env config.'
                )
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'skills': [
            {'name': 'Python', 'level': 90, 'icon': 'fab fa-python'},
            {'name': 'C', 'level': 80, 'icon': 'fas fa-code'},
            {'name': 'C++', 'level': 80, 'icon': 'fas fa-code'},
            {'name': 'Django', 'level': 85, 'icon': 'fas fa-server'},
            {'name': 'DRF', 'level': 80, 'icon': 'fas fa-network-wired'},
            {'name': 'FastAPI', 'level': 80, 'icon': 'fas fa-bolt'},
            {'name': 'HTML5', 'level': 95, 'icon': 'fab fa-html5'},
            {'name': 'CSS3', 'level': 90, 'icon': 'fab fa-css3-alt'},
            {'name': 'JavaScript', 'level': 80, 'icon': 'fab fa-js'},
            {'name': 'SQL', 'level': 85, 'icon': 'fas fa-database'},
            {'name': 'PostgreSQL', 'level': 80, 'icon': 'fas fa-database'},
            {'name': 'Machine Learning', 'level': 75, 'icon': 'fas fa-brain'},
            {'name': 'AI', 'level': 80, 'icon': 'fas fa-microchip'},
            {'name': 'Generative AI', 'level': 78, 'icon': 'fas fa-magic'},
            {'name': 'Agentic AI', 'level': 75, 'icon': 'fas fa-robot'},
        ],
        'projects': [
            {
                'title': 'Driver Drowsiness Detection System',
                'description': 'Developed a real-time driver drowsiness detection system using Python and OpenCV that analyzes eye behavior using EAR. The system generates structured events, integrates with a backend via REST API, and stores data for monitoring and analysis.',
                'technologies': ['Django', 'Python', 'JavaScript', 'PostgreSQL'],
                'icon': 'fas fa-shopping-cart',
            },
            {
                'title': 'AI Chatbot Assistant',
                'description':'An intelligent chatbot powered by NLP and machine learning to answer user queries VoiceWeb AI Project: Built a real-time voice assistant using Groq LLM with Google/Azure STT-TTS for human-like conversation',
 
                'technologies': ['Python', 'TensorFlow', 'NLTK', 'Flask'],
                'icon': 'fas fa-robot',
            },
             
            {
                'title': 'Image Classification Model',
                'description': 'Deep learning model trained to classify images into multiple categories with high accuracy.',
                'technologies': ['Python', 'Keras', 'TensorFlow', 'NumPy'],
                'icon': 'fas fa-image',
            },
        ],
        'services': [
            {
                'title': 'Python Full Stack Development',
                'description': 'Building responsive, modern, and interactive websites with cutting-edge technologies.',
                'icon': 'fas fa-laptop-code',
            },
            {
                'title': 'Backend Development',
                'description': 'Designing scalable backend systems, REST APIs, and database architectures using Django.',
                'icon': 'fas fa-database',
            },
            {
                'title': 'AI/ML Software Development',
                'description': 'Delivering intelligent solutions powered by machine learning and data-driven insights.',
                'icon': 'fas fa-brain',
            },
        ],
        'education': [
            {
                'degree': 'Post-Graduation (MCA)',
                'institution': 'Pursuing Master of Computer Applications',
                'year': '2025 - 2027',
                'icon': 'fas fa-user-graduate',
                'link': 'https://siddhantcoe.in/',
            },
            {
                'degree': 'Graduation (BCA)',
                'institution': 'Bachelor of Computer Applications',
                'year': '2023 - 2025',
                'icon': 'fas fa-graduation-cap',
                'link': 'https://www.rcpimrd.ac.in/',
            },
            {
                'degree': 'HSC (12th)',
                'institution': 'Higher Secondary Certificate',
                'year': '2022 - 2023',
                'icon': 'fas fa-school',
                'link': 'https://www.google.com/search?q=rdmp+jr+collage+dondaich',
            },
            {
                'degree': 'SSC (10th)',
                'institution': 'Secondary School Certificate',
                'year': '2020 - 2022',
                'icon': 'fas fa-book',
                'link': 'https://www.google.com/search?q=dr+hidhschool+dondaicha',
            },
        ],
    }
    return render(request, 'portfolio/index.html', context)
