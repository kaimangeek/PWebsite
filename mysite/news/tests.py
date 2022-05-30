"""Module for our custom tests (can be used in workflow later)."""
from django.test import TestCase
from .models import Articles, Comment
from django.contrib.auth.models import User


class TestArticlesModel(TestCase):
    """Test case for Articles model."""

    def test_articles(self):
        """Creates new articles and tests its attributes."""
        init_kwargs = {'title': 'Title',
                       'anons': 'Anons',
                       'full_text': 'full_text',
                       'date': '2022-12-16 10:10:10'
                       }
        articles = Articles.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(articles, attr), init_kwargs[attr])


class TestCommentModel(TestCase):
    """Test case for Comment model."""

    def test_comment(self):
        """Creates new comment and tests its attributes."""
        user = User.objects.create()
        init_kwargs = {'title': 'Title',
                       'anons': 'Anons',
                       'full_text': 'full_text',
                       'date': '2022-12-16 10:10:10'
                       }
        article = Articles.objects.create(**init_kwargs)

        init_kwargs = {'body': 'body',
                       'owner': user,
                       'articles': article,
                       }
        comment = Comment.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(comment, attr), init_kwargs[attr])




