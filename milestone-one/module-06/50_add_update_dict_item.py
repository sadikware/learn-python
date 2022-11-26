
post = {
    'id': 100,
    'title': 'This is awesome title',
    'content': 'These are awesome contents',
    'author': 'Awesome Name',
    'category': 'Awesome',
    'slug': 'awesome-title'

}

# Update
# post['category'] = 'Genius'
post.update({'category': 'Genius'})
post.update({'sticky': True})

print(post)
