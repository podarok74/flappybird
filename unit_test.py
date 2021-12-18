import unittest
import pygame
import FlappyBird


class TestsGame(unittest.TestCase):
    def test_creating_plat(self):
        pygame.init()
        screen = pygame.display.set_mode((288,512))
        platform = pygame.image.load('assets/platform.png').convert()
        FlappyBird.create_plat(screen, platform, 0)
        with self.assertRaises(AttributeError):
            FlappyBird.create_plat(None, platform, 0)

    def test_creating_colones(self):
        pygame.init()
        screen = pygame.display.set_mode((288,512))
        colone = pygame.image.load('assets/colone.png').convert()
        self.assertIsNotNone(FlappyBird.create_colone([200, 300, 400], colone)[0])
        self.assertIsNone(FlappyBird.create_colone(None, None)[0])
        self.assertEqual(FlappyBird.create_colone(None, None)[1], 'TypeError')
        self.assertIsNone(FlappyBird.create_colone([200, 300, 400], None)[0])
        self.assertEqual(FlappyBird.create_colone([200, 300, 400], None)[1], 'AttributeError')
        self.assertIsNone(FlappyBird.create_colone(None, colone)[0])
        self.assertEqual(FlappyBird.create_colone(None, colone)[1], 'TypeError')
        self.assertIsNone(FlappyBird.create_colone([], colone)[0])
        self.assertEqual(FlappyBird.create_colone([], colone)[1], 'IndexError')
        self.assertIsNone(FlappyBird.create_colone([], None)[0])
        self.assertEqual(FlappyBird.create_colone([], None)[1], 'IndexError')


    def test_updating_score(self):
        self.assertEqual(FlappyBird.update_score(0, 1), 1)
        self.assertEqual(FlappyBird.update_score(0, 0), 0)
        self.assertEqual(FlappyBird.update_score(1, 0), 1)


    def test_checking_collision(self):
        pygame.init()
        screen = pygame.display.set_mode((288,512))
        bird = pygame.image.load('assets/bird.png').convert_alpha()
        colone = pygame.image.load('assets/colone.png').convert()
        b_rect = bird.get_rect(center = (50,256))
        colone_list = []
        colone_list.extend(FlappyBird.create_colone([400], colone))
        self.assertTrue(FlappyBird.check_collision(colone_list, b_rect))
        b_rect.center = (400,256)
        self.assertFalse(FlappyBird.check_collision(colone_list, b_rect))
        b_rect.center = (50,-50)
        self.assertFalse(FlappyBird.check_collision(colone_list, b_rect))
        b_rect.center = (50,450)
        self.assertFalse(FlappyBird.check_collision(colone_list, b_rect))


if __name__ == '__main__':
    unittest.main()
