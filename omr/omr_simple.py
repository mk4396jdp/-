import cv2
import numpy as np

TOTAL_QUESTION = 20
OPTIONS_PER_QUESTION = 4
ANSWER_KEY = {i: 'A' for i in range(1, TOTAL_QUESTION+1)}
W, H = 1654, 2339

def build_bubble_centers():
    centers = []
    x_base = 220
    y_base = 420
    x_step = 150
    y_step = 120
    for q in range(TOTAL_QUESTION):
        y = y_base + q * y_step
        arr = []
        for i in range(OPTIONS_PER_QUESTION):
            x = x_base + i * x_step
            arr.append((x, y))
        centers.append(arr)
    return centers

BUBBLE_CENTERS = build_bubble_centers()

def score_paper(image_path, answer_key=ANSWER_KEY, save_annotated_path=None):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"找不到图像: {image_path}")
    warped = img
    th = cv2.adaptiveThreshold(cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 31, 10)
    results = []
    total_score = 0
    for q_idx in range(TOTAL_QUESTION):
        centers = BUBBLE_CENTERS[q_idx]
        selected = []
        for idx, center in enumerate(centers):
            x, y = int(center[0]), int(center[1])
            r = 25
            x1, y1 = max(0, x - r), max(0, y - r)
            x2, y2 = min(th.shape[1], x + r), min(th.shape[0], y + r)
            roi = th[y1:y2, x1:x2]
            black = cv2.countNonZero(roi)
            filled = 1.0 - black / (roi.shape[0] * roi.shape[1]) if roi.size>0 else 0
            if filled > 0.18:
                selected.append(idx)
        choice = None
        if len(selected) == 1:
            choice = chr(ord('A') + selected[0])
        elif len(selected) > 1:
            choice = 'MULTI'
        expected = answer_key.get(q_idx+1, None)
        status = 'WRONG'
        if choice == expected:
            total_score += 1
            status = 'RIGHT'
        results.append({'q': q_idx+1, 'choice': choice, 'status': status})
    if save_annotated_path:
        cv2.imwrite(save_annotated_path, warped)
    return {'total': total_score, 'max': TOTAL_QUESTION, 'per_question': results}
