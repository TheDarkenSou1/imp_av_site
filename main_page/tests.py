from django.test import TestCase
from .models import Category, Dish, Why_us, Chef, Response, Event, Gallery, About, Footer
from django.core.exceptions import ValidationError


# Dish model tests.
class DishModelTests(TestCase):
    def setUp(self):
        category = Category.objects.create(title='Test Category', is_visible=True, position=1)
        Dish.objects.create(
            title='Test Dish',
            ingredients='Test Ingredients',
            price=10.99,
            is_visible=True,
            position=1,
            photo='path/to/photo.jpg',
            category=category
        )

    def test_dish_str_method(self):
        dish = Dish.objects.get(title='Test Dish')
        expected_str = f'Test Dish: 1'
        self.assertEqual(str(dish), expected_str)

    def test_dish_default_visibility(self):
        dish = Dish.objects.get(title='Test Dish')
        self.assertTrue(dish.is_visible)

    def test_dish_position_non_unique(self):
        category = Category.objects.get(title='Test Category')
        Dish.objects.create(
            title='Another Dish',
            ingredients='Other Ingredients',
            price=15.99,
            is_visible=True,
            position=1,
            photo='path/to/other_photo.jpg',
            category=category
        )
        self.assertTrue(Dish.objects.count() == 2)


# Category model tests.
class CategoryModelTests(TestCase):
    def setUp(self):
        Category.objects.create(title='Test Category', is_visible=True, position=1)

    def test_category_str_method(self):
        category = Category.objects.get(title='Test Category')
        expected_str = f'Test Category: 1'
        self.assertEqual(str(category), expected_str)

    def test_category_default_visibility(self):
        category = Category.objects.get(title='Test Category')
        self.assertTrue(category.is_visible)

    def test_category_position_unique(self):
        with self.assertRaises(Exception):
            Category.objects.create(title='Another Category', is_visible=True, position=1)


# Event model tests.
class EventModelTests(TestCase):
    def setUp(self):
        Event.objects.create(
            title='Test Event',
            price=20,
            desc='Test Description',
            photo='path/to/photo.jpg',
            is_visible=True
        )

    def test_event_str_method(self):
        event = Event.objects.get(title='Test Event')
        expected_str = 'Test Event'
        self.assertEqual(str(event), expected_str)

    def test_event_default_visibility(self):
        event = Event.objects.get(title='Test Event')
        self.assertTrue(event.is_visible)

    def test_event_blank_description(self):
        event = Event(title='Blank Description Event', price=10, desc='', photo='path/to/other_photo.jpg')
        event.save()
        self.assertEqual(event.desc, '')


# Gallery model tests.
class GalleryModelTests(TestCase):
    def setUp(self):
        Gallery.objects.create(
            photo='path/to/photo.jpg',
            is_visible=True,
            title='Test Photo'
        )

    def test_gallery_str_method(self):
        gallery = Gallery.objects.get(title='Test Photo')
        expected_str = 'Test Photo'
        self.assertEqual(str(gallery.title), expected_str)

    def test_gallery_default_visibility(self):
        gallery = Gallery.objects.get(title='Test Photo')
        self.assertTrue(gallery.is_visible)


# Chef model tests.
class ChefModelTests(TestCase):
    def setUp(self):
        Chef.objects.create(
            name='John',
            surname='Doe',
            staff='Head Chef',
            photo='path/to/photo.jpg',
            is_visible=True
        )

    def test_chef_str_method(self):
        chef = Chef.objects.get(name='John')
        expected_str = 'John Doe'
        self.assertEqual(str(chef), expected_str)

    def test_chef_default_visibility(self):
        chef = Chef.objects.get(name='John')
        self.assertTrue(chef.is_visible)


# Response model tests.
class ResponseModelTests(TestCase):
    def setUp(self):
        Response.objects.create(
            name='John',
            surname='Doe',
            prof='Chef',
            photo='path/to/photo.jpg',
            resp='Test Response',
            stars=4,
            is_visible=True
        )

    def test_response_str_method(self):
        response = Response.objects.get(name='John')
        expected_str = 'John Doe'
        self.assertEqual(str(response), expected_str)

    def test_response_default_visibility(self):
        response = Response.objects.get(name='John')
        self.assertTrue(response.is_visible)

    def test_response_stars_validation_valid(self):
        response = Response.objects.create(
            name='Alice',
            surname='Johnson',
            prof='Server',
            photo='path/to/alice_photo.jpg',
            resp='Valid Response',
            stars=3
        )
        self.assertTrue(response.stars in range(1, 6))


# WhyUs model tests.
class WhyUsModelTests(TestCase):
    def setUp(self):
        Why_us.objects.create(
            num=1,
            title='Test Reason',
            description='Test Description',
            is_visible=True
        )

    def test_why_us_str_method(self):
        reason = Why_us.objects.get(title='Test Reason')
        expected_str = 'Test Reason: 1'
        self.assertEqual(str(reason), expected_str)

    def test_why_us_default_visibility(self):
        reason = Why_us.objects.get(title='Test Reason')
        self.assertTrue(reason.is_visible)


# About model tests.
class AboutModelTests(TestCase):
    def setUp(self):
        About.objects.create(
            phone_num='+380991234567',
            desc='Test Description',
            video_link='https://www.youtube.com/watch?v=video_id',
            is_visible=True
        )

    def test_about_default_visibility(self):
        about = About.objects.get(phone_num='+380991234567')
        self.assertTrue(about.is_visible)

    def test_about_valid_phone_number(self):
        valid_phone = '+380991234567'
        validator = About.mobile_phone_re
        self.assertIsNone(validator(valid_phone))

    def test_about_invalid_phone_number(self):
        invalid_phone = 'invalid_phone'
        validator = About.mobile_phone_re
        with self.assertRaises(ValidationError):
            validator(invalid_phone)


# Footer model tests.
class FooterModelTests(TestCase):
    def setUp(self):
        Footer.objects.create(
            address='Test Address',
            name_city='Test City',
            phone_num='+380991234567',
            email='test@example.com',
            work_time='9 AM - 6 PM',
            close_time='Sunday'
        )

    def test_footer_str_method(self):
        footer = Footer.objects.get(address='Test Address')
        expected_str = 'Test Address: Test City: +380991234567: : test@example.com'
        self.assertEqual(str(footer), expected_str)

    def test_footer_valid_phone_number(self):
        valid_phone = '+380991234567'
        validator = Footer.mobile_phone_re
        self.assertIsNone(validator(valid_phone))

    def test_footer_invalid_phone_number(self):
        invalid_phone = 'invalid_phone'
        validator = Footer.mobile_phone_re
        with self.assertRaises(ValidationError):
            validator(invalid_phone)

    def test_footer_valid_email(self):
        valid_email = 'test@example.com'
        validator = Footer.email_re
        self.assertIsNone(validator(valid_email))

    def test_footer_invalid_email(self):
        invalid_email = 'invalid_email'
        validator = Footer.email_re
        with self.assertRaises(ValidationError):
            validator(invalid_email)
