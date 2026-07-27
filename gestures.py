class GestureDetector:

    @staticmethod
    def finger_up(hand_landmarks, tip, pip):
        return hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y

    def detect(self, hand_landmarks, hand_label):
        index = self.finger_up(hand_landmarks, 8, 6)
        middle = self.finger_up(hand_landmarks, 12, 10)
        ring = self.finger_up(hand_landmarks, 16, 14)
        pinky = self.finger_up(hand_landmarks, 20, 18)

        # Specific finger combos first
        if index and not middle and not ring and not pinky:
            return "INDEX"

        if index and middle and not ring and not pinky:
            return "TWO_FINGERS"

        fingers = [index, middle, ring, pinky]
        extended = sum(fingers)

        if extended >= 4:
            return "OPEN_PALM"

        if extended <= 1:
            return "FIST"

        return "UNKNOWN"
