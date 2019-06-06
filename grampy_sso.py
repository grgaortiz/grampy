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
  session.set_dont_include(["siliconslopes", "siliconslopes_ogden", "grgortiz"])		
  
  #general settings
  session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=7500,
                                    max_following=3000,
                                    min_followers=25,
                                    min_following=25,
                                    min_posts=20)


  # activity		
  session.like_by_tags(["siliconslopes", "utahisrad", "utahbusiness", "utahtech", "startuplife"], amount=2, randomize=True, media='Photo')
  
  # follow
  session.follow_by_tags(["siliconslopes", "utahisrad", "utahbusiness", "utahtech", "startuplife"], amount=2)

  # Joining Engagement Pods
  session.set_do_comment(enabled=False, percentage=35)
  session.set_comments(comments)
  session.join_pods()
