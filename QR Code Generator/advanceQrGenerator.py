#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Aman Kumar
# Version: 1.0.0 

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H, box_size=10, border=4)

qr.add_data("https://github.com/Pinku-code")
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')
img.save('./advanceQR.png')