# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = ''
insta_password = ''

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)
comments = []

with smart_run(session):
  """ Activity flow """		
  # general settings		
  session.set_dont_include(["grgortiz"])		
  
  #general settings
  session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=7500,
                                    max_following=3000,
                                    min_followers=25,
                                    min_following=25,
                                    min_posts=20)
  session.set_do_like(enabled=True, percentage=100)
  session.set_do_follow(enabled=True, percentage=100, times=1)                               

  # follower activity		
  session.interact_user_followers(['sequoiacapital'], amount=10, randomize=True)
  session.interact_user_followers(['ycombinator'], amount=10, randomize=True)
  
  # like by hashtag
  session.like_by_tags(["travelgrams", "familyonmission", "entrepreneurlife", "exploretocreate", "siliconslopes", "dadlife", "coworkinglife"], amount=5, randomize=True, media='Photo') 
  
  # follow by hashtag
  session.follow_by_tags(["travelgrams", "familyonmission", "entrepreneurlife", "exploretocreate", "siliconslopes", "dadlife", "coworkinglife"], amount=5, randomize=True)

  # Joining Engagement Pods
  session.join_pods()
