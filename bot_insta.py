from instapy import InstaPy 

session = InstaPy(username="login",password="senha") 

session.login()

    session.set_relationship_bounds(enabled=True,
                    potency_ratio=1.34,
                    delimit_by_numbers=True,
                    max_followers=2000,
                        max_following=500,
                        min_followers=80,
                        min_following=500)

    session.set_quota_supervisor(enabled=True,
                                    peak_comments_daily=250,
                                    peak_comments_hourly=30,
                                    peak_likes_daily=250,
                                    peak_likes_hourly=30,
                                    sleep_after=['likes', 'follows', 'comments'])

    session.set_relationship_bounds(enabled=False)
    session.set_dont_like(['#store'])


    #Curtir imagens no feed
    session.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)

    #Seguir de acordo com #
    session.follow_by_tags(['#', '#'], amount=5)

    #Seguir pessoas que seguem @conta
    session.follow_user_followers(['@conta', '@conta'], amount=10, randomize=False, interact=True)

    #Seguir quem curte e comenta em publicações das @conta informadas.
    session.follow_likers (['@conta' , '@conta'], photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=False)
    session.follow_commenters(['@conta', '@conta'], amount=100, daysold=365, max_pic = 100, sleep_delay=600, interact=False)
    
    #Deixar de seguir usuarios que não seguem de volta
    session.unfollow_users(amount=25, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=600)
    
    #Deixar de seguir qualquer um.
    session.unfollow_users(amount=40, allFollowing=True, style="LIFO", unfollow_after=3*60*60, sleep_delay=450)

    session.end()