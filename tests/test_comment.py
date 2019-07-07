import unittest
from app.models import Comment, User, Pitch
from app import db


class TestComment(unittest.TestCase):

    def setUp(self):
        self.user_fev = User(
            username='fev', password='123', email='fev@gmail.com')
        self.new_comment = Comment(id=12345, pitch_id='2', user_id='2' pitch_comment='Eat food', user=self.user_James)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id, 12345)
        self.assertEquals(self.new_comment.post_id, '2')
        self.assertEquals(self.new_comment.user_id, '2')
        self.assertEquals(self.new_comment.pitch_comment, 'Eat food')
        self.assertEquals(self.new_comment.user,
        self.assertEquals(self.user_James, self.new_post)

    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comment.query.all()
        self.assertTrue(len(comments) > 0)
