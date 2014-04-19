cookiecutter-middleman
----------------------

A [cookiecutter][cookiecutter_project] template for Middleman.

## Features:

* [Middleman][middleman_home] compiler and server
* [Foundation 5.2][foundation_home]


## Usage

First, get cookiecutter. Trust me, it's awesome:

    $ pip install cookiecutter

Now run it against this repo:

    cookiecutter https://github.com/theskumar/cookiecutter-middleman.git

You'll be prompted for some questions, answer them, then it will create a Middleman project for you.

**Warning:** After this point, change 'Saurabh Kumar', 'thes_kumar', etc to your own information.

Enter the project and take a look around:

    $ cd repo_name/
    $ ls

Create a GitHub repo and push it there:

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:theskumar/awesome_project.git
    $ git push -u origin master

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

It's time to write the code!!!

## Not Exactly What You Want?

This is what I want. It might not be what you want. Don't worry, you have options:

### Fork This

If you have differences in your preferred setup, I encourage you to fork this to create your own version. Once you have your fork working, let me know and I'll add it to a 'Similar Cookiecutter Templates' list here. It's up to you whether or not to rename your fork.

If you do rename your fork, I encourage you to submit it to the following places:

* [cookiecutter][cookiecutter_project] so it gets listed in the README as a template.

### Or Submit a Pull Request

I also accept pull requests on this, if they're small, atomic, and if they make my own project development experience better.

[cookiecutter_project]: https://github.com/audreyr/cookiecutter
[middleman_home]: http://middlemanapp.com/
[foundation_home]: http://foundation.zurb.com/
