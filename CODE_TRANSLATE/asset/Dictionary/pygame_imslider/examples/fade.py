#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame_imslider as imslider
from pygame_imslider.examples.default import main


if __name__ == '__main__':
    main(False, 9, {'stype': imslider.STYPE_FADE, 'rewind': True, 'focus': False})
