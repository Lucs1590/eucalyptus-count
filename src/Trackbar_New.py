#!/usr/bin/python
# Python 2/3 compatibility
import cv2
import numpy as np


def filter_mask(im_filter_mask):
    kernel = np.ones((5, 5), np.uint8)
    erode = cv2.erode(im_filter_mask, kernel, iterations=1)
    dilate = cv2.dilate(erode, kernel, iterations=1)
    gaussian = cv2.GaussianBlur(dilate, (5, 5), 1)

    return gaussian


def update(*arg):
    h0 = cv2.getTrackbarPos('h min', 'control')
    h1 = cv2.getTrackbarPos('h max', 'control')
    s0 = cv2.getTrackbarPos('s min', 'control')
    s1 = cv2.getTrackbarPos('s max', 'control')
    v0 = cv2.getTrackbarPos('v min', 'control')
    v1 = cv2.getTrackbarPos('v max', 'control')

    lower = np.array((h0, s0, v0))
    upper = np.array((h1, s1, v1))
    mask = cv2.inRange(hsv, lower, upper)

    gaussian = filter_mask(mask)

    cv2.imshow('GAUSSIAN:', gaussian)

    cv2.imshow('mask', mask)

    contours, hierarchy = cv2.findContours(
        gaussian,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )
    total_contours = len(contours)
    result = src.copy()
    #cv2.drawContours(result, contours, 1, (0,255,0), 3)

    contours_error = []

    contours_ok = []
    for cont_contours in contours:
        area = cv2.contourArea(cont_contours)
        print("area: ", area)

        if (area > 50 and area < 400):
            contours_ok.append(cont_contours)
        else:
            print("ERROR_AREA: ", area)
            contours_error.append(cont_contours)

    cv2.drawContours(result, contours_ok, -1, (0, 255, 0), 3)
    cv2.drawContours(result, contours_error, -1, (0, 0, 255), 3)

    print("TOTAL: ", total_contours)
    print("OK_IF: ", len(contours_ok))
    print("ERROR_IF: ", len(contours_error))

    cv2.imshow('result:', result)


def main():
    cv2.namedWindow('control', 0)
    cv2.createTrackbar('h min', 'control', 32, 255, update)
    cv2.createTrackbar('h max', 'control', 38, 255, update)
    cv2.createTrackbar('s min', 'control', 0, 255, update)
    cv2.createTrackbar('s max', 'control', 176, 255, update)
    cv2.createTrackbar('v min', 'control', 106, 255, update)
    cv2.createTrackbar('v max', 'control', 255, 255, update)
    # trackbar(nome controle, janela, default, max, funcao)

    im = cv2.resize(src, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('control', im)
    update()
    while 1:
        ch = cv2.waitKey(30)
        if (ch == 27):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    import sys
    try:
        fn = sys.argv[1]
        print("parametro:", fn)
    except:
        fn = 'images/hortomosaico_eucalipto.png'

    src = cv2.imread(fn)

    # resize(imagem_entrada, None, scala x, escala y, flag interpolacao  )
    src = cv2.resize(
        src,
        None,
        fx=0.25,
        fy=0.25,
        interpolation=cv2.INTER_CUBIC
    )
    print("resized shape:", src.shape)
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    main()
