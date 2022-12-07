import datetime, calendar, random

def greeting(l,s,e):
    l = ['Hi', 'Hello', 'Hey', 'Howdy!', 'G\'day Mate!', 'Whatsup?', 'Hiya!', 'I\'m fine. how about you?',
         'I\'m good. How are you?', 'Sorry couldn\'t get that right', 'Not Found']
    print(l[random.randrange(s, e)])

print('Start your conversation the 🤖 chatbot now\n')

print('How can I help you?\n')

userName = 'user'

while True:
    M = str(input(userName+': '))
    print()
    m = M.lower()
    l = m.split(' ')
    sysTime = datetime.datetime.now()
    print('🤖: ', end='')

    for i in l:
        if i in ['date']:
            print(sysTime.strftime('The date is, %d-%m-%Y, %a\n'))

        elif i in ['time']:
            print(sysTime.strftime('The time is, %I:%M %p\n'))

        elif i in ['cal', 'calendar']:
            print(calendar.month(eval(sysTime.strftime('%Y')), eval(sysTime.strftime('%m'))),'\n')

        elif i in ['hi','hello', 'ello', 'hey'] or i in 'hiiiiiiiii':
            greeting(l,0,6)
            print()

        elif i in ['principal','princi']:
            print('Smt. Chitra Raghavan, refer home page for further information')

        elif i in ['school', 'scl', 'skl', 'about', 'abt', 'dav']:
            print('D.A.V. Boys Senior Secondary School situated at Gopalapuram, Chennai is the first branch of the D.A.V. Group of Schools managed by Tamil Nadu Arya Samaj Educational Society which is registered under the Societies Act. It was established in 1970 and is affiliated to and fully recognized up to the class XII level by the C.B.S.E. New Delhi.')
            print('Visit "https://bgpm.davchennai.org/about-us/" for more details')
            print()

        elif i in ['address', 'addr', 'add']:
            print('212-213, Avvai Shanmugam (Lloyds) Road, Gopalapuram, Chennai – 600 086')
            print()

        elif i in ['announcements', 'announce', 'recent']:
            print('Visit "https://bgpm.davchennai.org/announcements/" for more details')
            print()

        elif i in ['admission', 'ad det', 'adm det']:
            print('LKG: "https://forms.zohopublic.in/itservices/form/LKGADMISSIONS20222023/formperma/q5XPo-KCiuWMLFd7ZxHZXhqDkwHJE_ctKYzGdKbNb4k"\nClass 6: "https://app.neverskip.com/application/202223/davgpm_UKG_IX/index.php"\nOther classes: "https://forms.zohopublic.in/itservices/form/PreRegistrationForm202220232/formperma/bx37OdWp5vhKBBE7rVZ7sCkDg4V8it4Kr4LCP9tvhtE"')
            print()

        elif i in ['fees', 'fee', 'fee']:
            print('Our current fee structure is elucidated in the link given below: "https://parent.neverskip.com/#/auth/login"')
            print()

        elif i in ['achievements','acheivements', 'acheivers', 'achievers']:
            print('DAV has always had a track record of producing stellar achievers. For more information on our high flying superstars, refer the following links:')
            print('\tAcademic: "https://bgpm.davchennai.org/achievements/academics/state/"')
            print('\tSports: "https://bgpm.davchennai.org/achievements/sports/state/"')
            print('\tCo-Scholastic: "https://bgpm.davchennai.org/achievements/coscholastic/state/"')
            print()

        elif i in ['enquiry', 'enquiries', 'problems', 'faq']:
            print('Mail us at: "boys.gpm@davchennai.org"')

        elif i in ['staff', 'teachers', 'attenders']:
            print('Our school has been blessed with some of the best teachers available in the planet, in every possible subject. For further information on our architects of tomorrow, refer the link given below:')
            print('"https://bgpm.davchennai.org/static/pdf/staff_list_2022-23.pdf"')
            print()

        elif i in ['results']:
            print('DAV has always been a synonym for academic achievement. Our students have always been at the top, no matter what. For more information on our doyens of academic excellence, refer the link given below:')
            print('"https://bgpm.davchennai.org/results"')
            print()

        elif i in ['headmistress', 'hm', 'headmaster']:
            print('Smt. Swarna Karpagavalli is our current headmistress.')
            print()

        elif i in ['podcast', 'spectra']:
            print('Our podcast is a reliable source of information on what\'s cooking in our school. To listen to our musings, visit the link given below:')
            print('"https://redcircle.com/shows/dav-boys-senior-secondary-school-gopalaouram-chennai-86"')
            print()

        elif i in ['blog', 'blogs', 'blogspot']:
            print('Want to hear, or rather, see the thoughts of our students? Take a quick peek at or blog!')
            print('"https://davbgpm.blogspot.com/"')
            print()

        elif i in ['yt', 'youtube', 'utube']:
            print('Missed an event? Don\'t worry! Our YouTube channel contains recordings of all the important events which go on in school.')
            print('"https://www.youtube.com/channel/UCjJg-YwGv4ZBUckgkBB1Eqw"')
            print()

        elif i in ['channels', 'channel']:
            print('Spectra: "https://redcircle.com/shows/dav-boys-senior-secondary-school-gopalaouram-chennai-86"\nBlog: "https://davbgpm.blogspot.com/"\nYouTube: "https://www.youtube.com/channel/UCjJg-YwGv4ZBUckgkBB1Eqw"')
            print()

        elif i in ['info', 'contacts']:
            print('''Mail us at: boys.gpm@davchennai.org
Contact Numbers:    tel:044-28352866
                    tel:044-28351370''')
            print()

        elif i in ['magazine', 'mag', 'publications']:
            print('Visit: "https://bgpm.davchennai.org / publications"')
            print()

        elif i in ['deepika']:
            print('Online copies of our school magazines can be downloaded here:')
            print('"https://bgpm.davchennai.org/publications/#deepika"')
            print()

        elif i in ['branches', 'schools']:
            print('''Owned Schools:
DAV Girls, Mogappair - CBSE
DAV Boys, Mogappair - CBSE
DAV Co-Ed, Mogappair - CBSE
DAV Girls, Gopalapuram - CBSE
DAV Boys , Gopalapuram - CBSE
DAV Co-Ed, Gill Nagar - Matric
DAV Co-Ed, Puducherry - CBSE
DAV Co-Ed, Pallikaranai
SNCP School, Sowcarpet
Arya Samaj School - Vyasarpadi

Managed Schools:
DAV-BHEL School, Ranipet - CBSE
RSK School , Tiruchirappalli - CBSE
BHEL School , Tiruchirappalli - Matric''')

        elif i in ['alumni']:
            print('Visit: "https://alumni.davchennai.org/"')
            print()

        elif i in ['insight', 'insights', 'mission', 'vision' ,'vedic', 'hawan']:
            print('View: "https://bgpm.davchennai.org/static/pdf/NL%202021-22.pdf"')
            print()

        elif i in ['career']:
            print('Visit: "https://davchennai.darwinbox.in/ms/candidate/careers"')
            print()

        elif i in ['username']:
            userName=str(input('What do you wanna call yourself? '))
            print()

        elif i in ['initiatives', 'iniative']:
            print('''PiVerb: https://www.piverb.com/dav-piverb.shtml
Prashasti: https://prashasti.davchennai.org/
Birthday Agnihotra:- https://davchennai.org/birthday-agnihotra/
Academic Associations :- https://davchennai.org/academic-associations/
Prajya :- https://davchennai.org/publications/prajya-news-magazine/
Vedic Vidya Kendra :- https://vvk.davchennai.org/
Vedic Sanskirt school :- https://vss.davchennai.org/
Arya Samaj :- https://aryasamaj.davchennai.org/''')

        elif i in ['thank', 'thanks']:
            print('You are welcome!')
            exit()

        elif i in ['sect', 'secretary', 'seceratary']:
            print('Our current Secretary is Shri Vikas Arya. To hear from him, visit our homepage.')

        elif i in ['dir', 'director']:
            print('Our current Academic Director is Smt Shanthy Ashokan. To hear from her, visit our homepage.')
            print()

        elif i in ['activities','clubs', 'sports', 'ncc', 'scouts' 'lectures' 'events' 'chronicles' 'stories' 'story' 'camp']:
            print('''Clubs: https://bgpm.davchennai.org/activities/clubs/
Sports: https://bgpm.davchennai.org/activities/sports/
NCC Army: https://bgpm.davchennai.org/activities/ncc/
NCC Naval: https://bgpm.davchennai.org/activities/ncc-navy/
Scouts: https://bgpm.davchennai.org/activities/scouts/
Guest Lectures: https://bgpm.davchennai.org/activities/guest-lectures/
Career Counselling: https://bgpm.davchennai.org/activities/career-counselling/
Events:- https://bgpm.davchennai.org/activities/events/
campus chronicles: https://bgpm.davchennai.org/activities/campus-chronicles/
Summer Camp 22: https://bgpm.davchennai.org/activities/summer-camp/''')
            print()

        elif i in ['captains', 'capts']:
            print('''School Pupil Leader :- Rohit Chidambaram
Assistant school pupil leader :- Sriram S

Cultural secretary :- Tharun aravind
Assistant cultural secretary :- Vijay Narayana
Alumni secretary :- Arnav V 
Assistant Alumni Secretary :- Karnam Roopesh
Sports Secretary :- Vir Dhada
Assistant Sports Secretary :- Srinath 

House captains 
Barathi house 
(i) Captain    :  Sundaram V
(ii) Assistant :  Tanish Yashneil 

Shivaji house
(i) Captain    : Vishnu Subramanian
(ii) Assistant : Kunal 

Pratap house
(i) Captain    : Ashwath
(ii) Assistant : Sri Hari

Tagore house
(i) Captain    : Akshay Varun CR
(ii) Assistant : Kanish  ''')


    if l[0] in 'how' and l[1] in 'are' and l[2] in 'you':
            greeting(l,7,8)
            print()
