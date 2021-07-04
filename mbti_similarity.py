import math

import numpy as np


def similarity(v1, v2):
    dot = np.dot(v1, v2)
    mag1 = np.linalg.norm(v1)
    mag2 = np.linalg.norm(v2)
    return dot / (mag1 * mag2)


def angle(v1, v2):
    sim = similarity(v1, v2)
    return math.degrees(math.acos(sim))


def mbti_similarity(mbti1, mbti2):
    m1 = np.array(mbti1)
    m2 = np.array(mbti2)
    m1 = m1 - 0.5
    m2 = m2 - 0.5
    return math.fabs(angle(m1, m2))


if __name__ == "__main__":
    mbti1_str = input("mbti 1의 E. N. T. J의 함량을 입력하세요")
    mbti2_str = input("mbti 2의 E. N. T. J의 함량을 입력하세요")
    mbti1 = [float(x) for x in mbti1_str.split()]
    mbti2 = [float(x) for x in mbti2_str.split()]
    deg = mbti_similarity(mbti1, mbti2)
    print("각도(0-180):", deg)
