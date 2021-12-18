import unittest
import pygame
import FlappyBird


class TestsGame(unittest.TestCase):
    def test_creating_plat(self):
        pygame.init()
        screen = pygame.display.set_mode((288,512))
        platform = pygame.image.load('assets/platform.png').convert()
        try:
            FlappyBird.create_plat(screen, platform, 0)
            self.assertEqual(1, 1)
            FlappyBird.create_plat(None, platform, 0)
            self.assertEqual(1, 0)
        except AttributeError:
            self.assertEqual(1, 1)


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


if __name__ == '__main__':
    unittest.main()
