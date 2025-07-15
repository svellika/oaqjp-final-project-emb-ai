import unittest
from EmotionDetection import emotion_detector

class TestMyModule(unittest.TestCase):
    def test_joy_emotion(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_anger_emotion(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_disgust_emotion(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()