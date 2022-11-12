import streamlit as slt
from streamlit_lottie import st_lottie
import requests
slt.set_page_config(page_title="Royal Gym",layout='wide',page_icon=':muscle:')
hide = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;} 
    header {visibility: hidden;}
    </style>
"""
def local_css(file_name):
    with open(file_name) as f:
        slt.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

def anm1(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

table1 = ({"SNo.":[1,2,3,4,5,6,7,8,9,10],"Food":['Egg','Milk','Chicken','Mutton','Peanuts','Fruits','Peas','Yoghurt','Walnuts','Tofu'],
"Contains Protein":['23.3g','21.98g','64.114g','32.56g','12.514per/g','18.56g','19.714per/g','27.56g','24.231g','20.562g']})

lottie_coding1 = anm1("https://assets1.lottiefiles.com/packages/lf20_n1oyepxw.json")
lottie_coding2 = anm1("https://assets6.lottiefiles.com/packages/lf20_tqagefcc.json")
lottie_coding3 = anm1("https://assets5.lottiefiles.com/private_files/lf30_NcpRyD.json")
lottie_coding4 = anm1("https://assets4.lottiefiles.com/packages/lf20_2udfm2de.json")
lottie_coding5 = anm1("https://assets7.lottiefiles.com/packages/lf20_l0u0rf4r.json")
lottie_coding6 = anm1("https://assets9.lottiefiles.com/packages/lf20_VMnqvY.json")
lottie_coding7 = anm1("https://assets2.lottiefiles.com/packages/lf20_iegqiiek.json")
lottie_coding8 = anm1("https://assets8.lottiefiles.com/packages/lf20_igizh2.json")
lottie_coding9 = anm1("https://assets4.lottiefiles.com/packages/lf20_0o3rc85i.json")
lottie_coding10 = anm1("https://assets4.lottiefiles.com/private_files/lf30_b8oxhxr5.json")

slt.markdown(hide,unsafe_allow_html=True)
slt.subheader("Hi! Welcome To Royal Gym :wave:")
slt.title("Build More! Live More! :speaker:")
slt.write('---')
with slt.container():
    left_column, right_column = slt.columns(2)
    with left_column:
        slt.write("""
            This Gym contains a lot of valuable products to build up your body:-
            - Provided body build up machines
            - Provided nutrients and proteins
            - Clean and well among inside, to protect the environment
            - Must have a lot of weights and machines for every exercising of our whole body
        """)
        slt.write('Open Timing: Morning - 7:00AM To 12:00PM , Evening - 5:00PM To 8:00PM')
        slt.write('Sunday Closed')
        slt.write('Fees: Boys-Rs 500 , Girls-Rs 600 , Mens/Womens-Rs 800 (Cardigo+Strength)')
    with right_column:
        st_lottie(lottie_coding1,height=300,key="Gym")

slt.write("---")

with slt.container():
    left_column, right_column = slt.columns(2)
    with left_column:
        slt.subheader("Best way to gain your weight - There are some good food source requirements:-")
        slt.dataframe(table1,width=450)
    with right_column:
        st_lottie(lottie_coding2,height=350,key="Food")

slt.write("Set of execrcises to build up your body")

with slt.container():
    left1,right1 = slt.columns(2)
    with left1:
        slt.write("""
        1. Chest
        - Push Up
        - Barbell Flat Bench Press
        - Chest Flye
        - Dip
        - Barbell Incline Bench Press
        - Barbell Decline Bench Press
        """)
    with right1:
        st_lottie(lottie_coding3,height=200,key="Chest")
slt.write("---")
with slt.container():
    left2,right2 = slt.columns(2)
    with left2:
        slt.write(""" 
        2. Back
        - Lat pulldown
        - Back extension
        - Suspended row
        - Wood chop
        - Quadruped single-arm dumbbell row
        - Wide dumbbell bent-over row
        """)
    with right2:
        st_lottie(lottie_coding4,height=200,key="Back")
slt.write("---")
with slt.container():
    left3,right3 = slt.columns(2)
    with left3:
        slt.write(""" 
        3. Biceps
        - Barbell-Curl
        - Chin-up
        - Hammer Curl
        - Incline Dumbbell Curl
        - Cable Curl
        - Facing-Away Cable Curl
        """)
    with right3:
        st_lottie(lottie_coding5,height=200,key="Biceps")
slt.write("---")
with slt.container():
    left4,right4 = slt.columns(2)
    with left4:
        slt.write("""
        4. Triceps
        - Diamond Push-Ups
        - Triceps Kickbacks
        - Triceps Dips
        - Rope Pushdowns
        - Bar Pushdowns
        - Lying Triceps Extensions
        """)
    with right4:
        st_lottie(lottie_coding6,height=200,key="Triceps")
slt.write("---")
with slt.container():
    left5,right5 = slt.columns(2)
    with left5:
        slt.write("""
        5. Shoulder
        - Barbell Standing Press
        - Arnold Press
        - Seated Dumbbell Press
        - Upright Row
        - Front Raises
        - Bent-Over Reverse Fly
        """)
    with right5:
        st_lottie(lottie_coding7,height=200,key="Shoulder")
slt.write("---")
with slt.container():
    left6,right6 = slt.columns(2)
    with left6:
        slt.write(""" 
        6. Thigh
        - Sqauts
        - Lunges
        - Plank Leg Lifts
        - Single-Leg Deadlifts
        - Steps-Ups
        - Box Jumps
        """)
    with right6:
        st_lottie(lottie_coding8,height=200,key="Thigh")
slt.write("---")
with slt.container():
    left7,right7 = slt.columns(2)
    with left7:
        slt.write(""" 
        7. Abs
        - Pilates
        - Plank Poses
        - Get In The Ring
        - Get Moving
        - Captain's Chair
        - Biycycle Crunches
        """)
    with right7:
        st_lottie(lottie_coding9,height=200,key="Abs")

slt.write("---")
with slt.container():
    slt.write('Join Now! :thought_balloon:'); slt.write("##")
    contact_form = """
    <form action="https://formsubmit.co/3469harshsharma@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_column,right_column = slt.columns(2)
    with left_column:
        slt.markdown(contact_form,unsafe_allow_html=True)
        local_css("style/style.css")
    with right_column:
        st_lottie(lottie_coding10,height=350,key="Join Us")
slt.write('---')
slt.write('If you guys have any query, so send me your details above. Thanks!!!')

