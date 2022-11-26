post = [{"id": 1, "date": "2014-03-05T22:42:27", "date_gmt": "2014-03-06T06:42:27", "guid": {"rendered": "http:\/\/math.berkeley.edu\/wp\/?p=1"}, "modified": "2018-09-10T10:41:24", "modified_gmt": "2018-09-10T17:41:24", "slug": "home", "status": "publish", "type": "post", "link": "https:\/\/math.berkeley.edu\/wp\/blog\/home\/", "title": {"rendered": "WordPress Hosting for Math Department"}, "content": {"rendered": "<p>Math department offers WordPress hosting to seminar organizers and project coordinators. You can use WordPress to blog, or use it as a general content management system for your site.<\/p>\n<p>The department webmaster manages the WordPress installation, taking care of all security patches, software updates, and plugins. We also provide support for WordPress users and help with site setup and maintenance.<\/p>\n<p>If you are a faculty, postdoc or graduate student and interested in hosting your WordPress site here, please contact us at webmaster@math.berkeley.edu.<\/p>\n<p>Posts and comments on WordPress sites are the opinions of their authors, and do not necessarily represent the position of the Department of Mathematics, the College of Letters &amp; Science, or the University.<\/p>\n", "protected": False}, "excerpt": {"rendered": "<p>Math department offers WordPress hosting to seminar organizers and project coordinators. You can use WordPress to blog, or use it as a general content management system for your site. The department webmaster manages the WordPress installation, taking care of all security patches, software updates, and plugins. We also provide support for WordPress users and help &hellip; <a href=\"https:\/\/math.berkeley.edu\/wp\/blog\/home\/\" class=\"more-link\">Continue reading <span class=\"screen-reader-text\">WordPress Hosting for Math Department<\/span> <span class=\"meta-nav\">&rarr;<\/span><\/a><\/p>\n",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    "protected": False}, "author": 1, "featured_media": 0, "comment_status": "closed", "ping_status": "open", "sticky": False, "template": "", "format": "standard", "meta": [], "categories":[2], "tags":[], "_links":{"self": [{"href": "https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/posts\/1"}], "collection": [{"href": "https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/posts"}], "about": [{"href": "https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/types\/post"}], "author": [{"embeddable": True, "href": "https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/users\/1"}], "replies": [{"embeddable": True, "href": "https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/comments?post=1"}], "version-history": [{"count": 2, "href": "https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/posts\/1\/revisions"}], "predecessor-version": [{"id": 17, "href": "https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/posts\/1\/revisions\/17"}], "wp:attachment": [{"href": "https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/media?parent=1"}], "wp:term": [{"taxonomy": "category", "embeddable": True, "href": "https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/categories?post=1"}, {"taxonomy": "post_tag", "embeddable": True, "href": "https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/tags?post=1"}], "curies": [{"name": "wp", "href": "https:\/\/api.w.org\/{rel}", "templated": True}]}}]


post_title = post[0].get('title').get('rendered')
# print(post_title)

post_excerpt = post[0].get('excerpt').get('rendered')
# print(post_excerpt)


# Users

users = [
    {
        "id": 1,
        "name": "Igor",
        "url": "",
        "description": "",
        "link": "https://math.berkeley.edu/wp/blog/author/admin/",
        "slug": "admin",
        "avatar_urls": {
            "24": "https://secure.gravatar.com/avatar/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=24&d=identicon&r=g",
            "48": "https://secure.gravatar.com/avatar/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=48&d=identicon&r=g",
            "96": "https://secure.gravatar.com/avatar/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=96&d=identicon&r=g"
        },
        "meta": [

        ],
        "_links": {
            "self": [
                {
                    "href": "https://math.berkeley.edu/wp/wp-json/wp/v2/users/1"
                }
            ],
            "collection": [
                {
                    "href": "https://math.berkeley.edu/wp/wp-json/wp/v2/users"
                }
            ]
        }
    }
]


name = users[0].get('name')
slug = users[0].get('slug')
profile_url = users[0].get('link')


print(name, slug, profile_url, sep=' --- ')
