from django.shortcuts import render
from datetime import date
all_posts=[
    {
        "slug":"video-edting",
        "image":"edit.jpg",
        "author":"MP Abhimanue",
        "date": date(2021,8,14),
        "title":"Video Editing",
        "excerpt":"Editing your own video is like 'letting a caged bird free', The places it will fly off too are limitless'.So,editing my own videos has made me acheive a deep realization of my selfish mind.",
        "content":"Would you like me to give you a formula for success? It's quite simple, really: Double your rate of failure. You are thinking of failure as the enemy of success. But it isn't at all. You can be discouraged by failure or you can learn from it, so go ahead and make mistakes. Make all you can. Because remember that's where you will find success."

    },
    {
        "slug": "Streaming",
        "image": "stream.jpg",
        "author": "MP Abhimanue",
        "date": date(2021, 7, 21),
        "title": "Streaming Games",
        "excerpt": "There's nothing like Streaming online . It kicks in the adrenaline to show the best in you!!",
        "content": 
         "I used to stream a lot.It helped me capture some amazing moments of my online life and share it with my firends."
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "MP Abhimanue",
        "date": date(2019, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me everytime...",
        "content":
            "I love to code my ides's into reality!! First,I try solving the problem. Then, I write the code.For me,Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday’s code and I beleive in the phrase 'Programming is not about what you know; its about what you can figure out."
      
    },
    {
        "slug": "Making-Websites",
        "image": "home_page.png",
        "author": "MP Abhimanue",
        "date": date(2021, 8, 12),
        "title": "My First Website",
        "excerpt": "It was the best moment when i coded my first ever website and seeing it working was quite overwhelming!!",
        "content": """
            when i was introduce into Django . All i had in my hand was some python and some basic html codes.But,Building my First Webpage was a route of frequent dilemma which made me stop in every new code i implemented.
            It took me few sleepless nights to figure out everything and create my First Wepage
        """
    }
]
def get_date(post):
    return post['date']

def index(request):
    sorted_post=sorted(all_posts,key=get_date)
    latest_post=sorted_post[-3:]
    return render(request,"blog/index.html",{"posts":latest_post})

def post(request):
    return render(request,"blog/all-posts.html",{"all_posts":all_posts})


def post_detail(request,slug):
    identified_post=next(post for post in all_posts if post['slug']==slug)
    return render(request,"blog/post-detail.html",{
        "post":identified_post
    })