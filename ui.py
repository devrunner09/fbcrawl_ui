import streamlit as st 
import requests
import json 

st.title("MYLA - FBCrawl")

with st.sidebar:
    st.text("Enter facebook account.")
    with st.form("facebook_account_form"):
        email = st.text_input('Email', value="sadieclemens8241@hotmail.com")
        password = st.text_input('Password', value="vmloheprdxk")
        secret_code = st.text_input('Secret Code', value="652DPA7CIXTBUQ4S5UPNDI7X6TZKC4RE")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Use this account")
        if submitted:
            st.write("Using \nEmail: {}\nPassword: {}\nSecret Code: {}".format(email, password, secret_code))

features = ["User Profile", 
            "Fanpage",
            "Group",
            "Post with link"
            ]


api_url = 'http://54.238.137.100:5000/crawl'

# Insert containers separated into tabs:
craw_user_profile_tab, craw_fanpage_tab, craw_group_tab, \
craw_post_with_link_tab = st.tabs(features)

# You can also use "with" notation:
with craw_user_profile_tab:

    user_profiles = st.text_area(
    "Liệt kê các link profile theo từng dòng, dòng bắt đầu bằng dấu # sẽ được ignore",
    "# https://www.facebook.com/astutasdpp"
    )

    user_modules = ['User Contact Info', 'User Posts', 'User Friends', 'User Photos', 'User Videos', 'User Reels', 'User About', 'User Profile and Cover Pic', 'User Likes', 'User Events', 'User Check-Ins', 'User Reviews']
    user_modules_need_to_crawl = st.multiselect(
        "Select informations need to crawl",
        user_modules,
        default=['User Contact Info']
    )

    min_user_scroll = 0
    max_user_scroll = 150

    tabl1_col1, tab1_col2 = st.columns(2)
    with tabl1_col1:
        user_post_scrolls = st.number_input("User's post scrolls (5-6 posts/ 1 scroll)", min_value=min_user_scroll, max_value=max_user_scroll, value=5)  # 1 scroll fetches 5-6 posts.
        user_reels_scrolls = st.number_input("User's reels scrolls (9-10 reels/ 1 scroll)", min_value=min_user_scroll, max_value=max_user_scroll, value=0)  # 1 scroll fetches 9-10 reels.
        user_friends_scrolls = st.number_input("User's friends scrolls (8 friends/ 1 scroll)", min_value=min_user_scroll, max_value=max_user_scroll, value=0)  # 1 scroll fetches 8 friends.
        user_photos_scrolls =  st.number_input("User's photos scrolls (8 photos/ 1 scroll)", min_value=min_user_scroll, max_value=max_user_scroll, value=0)  # 1 scroll fetches 8 photos.
    with tab1_col2:
        user_videos_scrolls = st.number_input("User's videos scrolls (8 videos/ 1 scroll)", min_value=min_user_scroll, max_value=max_user_scroll, value=0)  # 1 scroll fetches 8 videos.
        user_check_ins_scrolls = st.number_input("User's check-ins scrolls (7-8 check-ins/ 1 scroll)", min_value=min_user_scroll, max_value=max_user_scroll, value=0)  # 1 scroll fetches 7-8 check-ins.
        user_events_scrolls = st.number_input("User's event scrolls (7-8 events/ 1 scroll)", min_value=min_user_scroll, max_value=max_user_scroll, value=0)  # 1 scroll fetches 7-8 events.
        user_reviews_scrolls = st.number_input("User's review scrolls (7-8 reviews/ 1 scroll)", min_value=min_user_scroll, max_value=max_user_scroll, value=0)  # 1 scroll fetches 7-8 reviews.

    scrape_user_post_reactions = st.toggle("Lấy reactions posts of users", value=True)  # If True then scrapes reactions for posts
    scrape_user_post_comments = st.toggle("Lấy comments posts of users", value=True)  # If True then scrapes comments for posts
    scrape_user_photos_comments = st.toggle("Lấy comments photos of users", value=False)  # If True then scrapes comments for photos
    scrape_user_videos_comments = st.toggle("Lấy comments videos of users", value=False)  # If True then scrapes comments for videos

    crawl_user_profile_button = st.button("Start Crawl", type="primary")
    if crawl_user_profile_button:
        data_post = {

            "feature" : "user_profile",
            "username" : email,
            "password" : password, 
            "secret_code": secret_code,
            "user_profile_links" : user_profiles, 

            "config" : {
                "scrape_users" : True,
                "user_profile_modules": user_modules_need_to_crawl, 
                "user_post_scrolls": user_post_scrolls,
                "user_reels_scrolls": user_reels_scrolls,
                "user_friends_scrolls": user_friends_scrolls,
                "user_photos_scrolls":user_photos_scrolls,
                "user_videos_scrolls": user_videos_scrolls,
                "user_check_ins_scrolls":user_check_ins_scrolls,
                "user_events_scrolls" : user_events_scrolls,
                "user_reviews_scrolls": user_reviews_scrolls, 
                "scrape_user_post_reactions": scrape_user_post_reactions,
                "scrape_user_post_comments": scrape_user_post_comments,
                "scrape_user_photos_comments": scrape_user_photos_comments, 
                "scrape_user_videos_comments": scrape_user_videos_comments
            }
        }
        print(data_post)
        response = requests.post(api_url, data=json.dumps(data_post))
        st.text(response)

with craw_fanpage_tab:

    fanpage_profiles = st.text_area(
    "Liệt kê các link fanpage"
    )

    page_modules = ['Page Contact Info', 'Page Posts', 'Page Videos', 'Page Photos', 'Page About', 'Page Reels', 'Page Profile and Cover Pic']
    page_modules_need_to_crawl = st.multiselect(
        "Select informations need to crawl",
        page_modules,
        default=['Page Posts']
    )

    min_page_scroll = 0
    max_page_scroll = 200

    page_post_scrolls = st.number_input("Page's post scrolls (5-6 posts/ 1 scroll)", min_value=min_page_scroll, max_value=max_page_scroll, value=150)  # 1 scroll fetches 5-6 posts.
    page_photos_scrolls = st.number_input("Page's photos scrolls (7-8 photos/ 1 scroll)", min_value=min_page_scroll, max_value=max_page_scroll, value=0)  # 1 scroll fetches 7-8 photos.
    page_videos_scrolls = st.number_input("Page's videos scrolls (7-8 videos/ 1 scroll)", min_value=min_page_scroll, max_value=max_page_scroll, value=0)  # 1 scroll fetches 7-8 videos.

    scrape_page_post_reactions = st.toggle("Lấy reactions of page posts", value=True)  # If True then scrapes reactions for posts
    scrape_page_post_comments = st.toggle("Lấy comments of page posts", value=True)  # If True then scrapes comments for posts
    scrape_page_photos_comments = st.toggle("Lấy comments of page photos", value=False)  # If True then scrapes comments for Photos
    scrape_page_videos_comments = st.toggle("Lấy comments of page videos", value=False)  # If True then scrapes comments for Videos

    crawl_fanpage_button = st.button("Start Crawl Fanpage", type="primary")
    if crawl_fanpage_button:
        data_post = {
            "feature" : "fanpage",
            "username" : email,
            "password" : password, 
            "secret_code": secret_code,
            "fanpage_links" : fanpage_profiles, 

            "config" : {
                "scrape_pages" : True,
                "page_modules" : page_modules_need_to_crawl,
                "page_post_scrolls" : page_post_scrolls,  
                "page_photos_scrolls" : page_photos_scrolls,  
                "page_videos_scrolls" : page_videos_scrolls, 
                "scrape_page_post_reactions" : scrape_page_post_reactions,  
                "scrape_page_post_comments" : scrape_page_post_comments,  
                "scrape_page_photos_comments" : scrape_page_photos_comments, 
                "scrape_page_videos_comments" : scrape_page_videos_comments
            }
        }
        print(data_post)
        response = requests.post(api_url, data=json.dumps(data_post))
        st.text(response)

with craw_group_tab:
    
    group_profiles = st.text_area(
    "Liệt kê các link group"
    )

    group_modules = ['Group Posts', 'Group Videos', 'Group Photos', 'Group About', 'Group Members', 'Group Cover Pic']
    group_modules_need_to_crawl = st.multiselect(
        "Select informations need to crawl",
        group_modules,
        default=['Group Posts']
    )

    min_group_scroll = 0
    max_group_scroll = 200 

    group_post_scrolls = st.number_input("Group's post scrolls (5-6 posts/ 1 scroll)", min_value=min_group_scroll, max_value=max_group_scroll, value=150)  # 1 scroll fetches 5-6 posts.
    group_photos_scrolls = st.number_input("Group's photos scrolls (8 photos/ 1 scroll)", min_value=min_group_scroll, max_value=max_group_scroll, value=0)  # 1 scroll fetches 8 photos.
    group_videos_scrolls = st.number_input("Group's videos scrolls (8 videos/ 1 scroll)", min_value=min_group_scroll, max_value=max_group_scroll, value=0)  # 1 scroll fetches 8 videos.
    group_members_scrolls = st.number_input("Group's members scrolls (10 members/ 1 scroll)", min_value=min_group_scroll, max_value=max_group_scroll, value=0)  # 1 scroll fetches 10 members.

    scrape_group_post_comments = st.toggle("Lấy comments of group posts", value=True)  # If True then scrapes comments for posts
    scrape_group_post_reactions = st.toggle("Lấy reactions of group posts", value=True)  # If True then scrapes reactions for posts

    crawl_group_button = st.button("Start Crawl Group", type="primary")
    if crawl_group_button:
        data_post = {
            "feature" : "group",
            "username" : email,
            "password" : password, 
            "secret_code": secret_code,
            "group_links" : group_profiles, 

            "config" : {
                "scrape_groups" : True,
                "group_modules" : group_modules_need_to_crawl,
                "group_post_scrolls" : group_post_scrolls, 
                "group_photos_scrolls" : group_photos_scrolls, 
                "group_videos_scrolls" : group_videos_scrolls, 
                "group_members_scrolls" : group_members_scrolls,
                "scrape_group_post_comments" : scrape_group_post_comments , 
                "scrape_group_post_reactions" : scrape_group_post_reactions  
            }
        }
        print(data_post)
        response = requests.post(api_url, data=json.dumps(data_post))
        st.text(response)
    
with craw_post_with_link_tab:

    post_profiles = st.text_area(
    "Liệt kê các link post"
    )

    facebook_posts = ['Facebook Posts']  # don't modify
    # If True then it scrapes the posts using links added in 'posts_links.txt' file under the 'inputs' folder.
    # If False then it doesn't scrape the post links added in 'posts_links.txt'. Moreover, all 'Additional Options' defined for this module will not have any impact.
    scrape_posts_using_links = False

    scrape_posts_using_links_comments = st.toggle("Lấy comments of posts", value=True)  # If True then scrapes comments for posts
    scrape_posts_using_links_reactions = st.toggle("Lấy reactions of posts", value=True)  # If True then scrapes reactions for posts
