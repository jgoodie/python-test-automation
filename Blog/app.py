from blog import Blog

MENU_PROMPT ='Enter "c" to create a blog,"l" to list blogs, "r" to read one, "p" to create a post, "q" to quit.'

POST_TEMPLATE = '''
--- {} ---
{}
'''

blogs = dict() # mapping of blog_name : Blog object

def menu():
    # show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def ask_create_blog():
    # {'title':title, 'name': name}
    # add to blogs dict
    title = input("Enter the blog title: ") # first side_efect
    author = input("Enter the author name: ") # second side_effect
    blogs[title] = Blog(title, author)


def ask_read_blog():
    title = input("Enter a blog title: ")
    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    blog_name = input("Enter a blog title: ")
    title = input("Enter a post title: ")
    content = input("Enter your content: ")
    blogs[blog_name].create_post(title, content)

def print_blogs():
    # Print the available blogs
    for key,blog in blogs.items(): # [(blog_name, Blog), (blog_name, Blog)]
        print('- {}'.format(blog))
