from django.test import TestCase
from .models import Articles
from django.test.client import Client
from django.contrib.auth.models import User
from django.urls import reverse

OK = 200


class NewsDetailView(TestCase):
    """Test for filmwork list view."""

    def setUp(self):
        """Set up client, user and create filmworks before tests."""
        self.client = Client()
        self.user = User.objects.create_user('user', 'mail@mail.com', 'itsok')
        self.client.login(username='user', password='itsok')

        number_of_articles = 5
        for num in range(number_of_articles):
            tit = 'Articles {0}'.format(num)
            anon = 'Anons {0}'.format(num)
            fullt = 'full_text {0}'.format(num)
            date = '2022-12-16 10:10:10'
            owner = self.user
            Articles.objects.create(title=tit, anons = anon, full_text = fullt, date = date, owner = owner)

    def test_view_url_exists_at_desired_location(self):
        """Tests if the view exists at url."""
        resp = self.client.get('/news/')
        self.assertEqual(resp.status_code, OK)

    # def test_view_url_accessible_by_name(self):
    #     """Tests if the view is accessible by its name."""
    #     resp = self.client.get(reverse('news/0'))
    #     self.assertEqual(resp.status_code, OK)

    def test_view_uses_correct_template(self):
        """Tests if view uses the correct template."""
        resp = self.client.get('/news/')
        self.assertEqual(resp.status_code, OK)
        self.assertTemplateUsed(resp, 'news/news_home.html')

class NewsUpdateView(TestCase):
    """Test for filmwork list view."""

    def setUp(self):
        """Set up client, user and create filmworks before tests."""
        self.client = Client()
        self.user = User.objects.create_user('user', 'mail@mail.com', 'itsok')
        self.client.login(username='user', password='itsok')

        number_of_articles = 5
        for num in range(number_of_articles):
            tit = 'Articles {0}'.format(num)
            anon = 'Anons {0}'.format(num)
            fullt = 'full_text {0}'.format(num)
            date = '2022-12-16 10:10:10'
            owner = self.user
            Articles.objects.create(title=tit, anons = anon, full_text = fullt, date = date, owner = owner)

    def test_view_url_exists_at_desired_location(self):
        """Tests if the view exists at url."""
        resp = self.client.get('/news/1/update')
        self.assertEqual(resp.status_code, OK)

    # def test_view_url_accessible_by_name(self):
    #     """Tests if the view is accessible by its name."""
    #     resp = self.client.get(reverse('news/0'))
    #     self.assertEqual(resp.status_code, OK)
    #
    def test_view_uses_correct_template(self):
        """Tests if view uses the correct template."""
        resp = self.client.get('/news/1/update')
        self.assertEqual(resp.status_code, OK)
        self.assertTemplateUsed(resp, 'news/create.html')

class NewsDeleteView(TestCase):
    """Test for filmwork list view."""

    def setUp(self):
        """Set up client, user and create filmworks before tests."""
        self.client = Client()
        self.user = User.objects.create_user('user', 'mail@mail.com', 'itsok')
        self.client.login(username='user', password='itsok')

        number_of_articles = 5
        for num in range(number_of_articles):
            tit = 'Articles {0}'.format(num)
            anon = 'Anons {0}'.format(num)
            fullt = 'full_text {0}'.format(num)
            date = '2022-12-16 10:10:10'
            owner = self.user
            Articles.objects.create(title=tit, anons = anon, full_text = fullt, date = date, owner = owner)

    def test_view_url_exists_at_desired_location(self):
        """Tests if the view exists at url."""
        resp = self.client.get('/news/1/delete')
        self.assertEqual(resp.status_code, OK)

    # def test_view_url_accessible_by_name(self):
    #     """Tests if the view is accessible by its name."""
    #     resp = self.client.get(reverse('news/0'))
    #     self.assertEqual(resp.status_code, OK)
    #
    def test_view_uses_correct_template(self):
        """Tests if view uses the correct template."""
        resp = self.client.get('/news/1/delete')
        self.assertEqual(resp.status_code, OK)
        self.assertTemplateUsed(resp, 'news/news-delete.html')