from tkinter import *
a=Tk()
a.title("Drawing 36")
a.geometry("1200x1080")
w=Canvas(a, width=900, height=900, bg="white")
w.place(x=100, y=100)

# 1. Trafic light, top-left.

sx=100
sy=50
w.create_rectangle([120+sx-100, 100+sy-70],
                   [280+sx-100, 460+sy-70], fill="#999999", width=0)

w.create_polygon([200+sx-100, 30+sy-70],
                 [80+sx-100, 100+sy-70],
                 [320+sx-100, 100+sy-70],
                 fill="#535353", width=0)

w.create_oval([150+sx-100, 120+sy-70],
              [250+sx-100, 220+sy-70], fill="#09bd00", width=0)

w.create_oval([150+sx-100, 230+sy-70],
              [250+sx-100, 330+sy-70], fill="#eaff00", width=0)

w.create_oval([150+sx-100, 340+sy-70],
              [250+sx-100, 440+sy-70], fill="#ff0000", width=0)

# 2. House, top-right.

bx=300
by=0
w.create_rectangle([200+bx, 180+by],
                   [400+bx, 380+by], fill="#7C4496", width=0)
w.create_rectangle([260+bx, 240+by],
                   [340+bx, 300+by], fill="#DDDDDD", width=0)
w.create_rectangle([205+bx, 120+by],
                   [230+bx, 180+by], fill="#56e06d", width=0)
w.create_line([260+bx, 270+by],
              [340+bx, 270+by], fill="black", width=2)
w.create_line([300+bx, 240+by],
              [300+bx, 300+by], fill="black", width=2)
w.create_polygon([300+bx, 100+by],
                 [170+bx, 200+by],
                 [430+bx, 200+by], fill="#2b71e0", width=0)

# 3. Emoji, the bottom-left.

mx=50
my=400
w.create_oval([9+mx, 140+my],
              [300+mx, 440+my], fill="#fff049",
              width=2, outline="#fd3b00")

w.create_polygon([160+mx, 380+my],
                 [65+mx, 350+my],
                 [250+mx, 350+my],
                 fill="#DD9542", width=2, outline="#000000")

w.create_rectangle([152+mx, 285+my],
                   [168+mx, 325+my], fill="#38387f", width=0)

w.create_oval([180+mx, 270+my],
              [230+mx, 220+my], fill="#e7e7e7", width=2)
w.create_oval([205+mx, 265+my],
              [225+mx, 245+my], fill="#000000", width=2)
w.create_oval([80+mx, 270+my],
              [130+mx, 220+my], fill="#e7e7e7", width=2)
w.create_oval([105+mx, 265+my],
              [125+mx, 245+my], fill="#000000", width=2)
#4. CIircle, bottom-right.

kx = 450
ky = 400
w.create_oval([9+kx, 140+ky], [300+kx, 445+ky], fill="#853131", width=0)
w.create_oval([40+kx, 180+ky], [290+kx, 440+ky], fill="#0f1169", width=0)
w.create_oval([55+kx, 205+ky], [280+kx, 440+ky], fill="#853131", width=0)
w.create_oval([65+kx, 232+ky], [270+kx, 438+ky], fill="#0f1169", width=0)
w.create_oval([85+kx, 260+ky], [260+kx, 438+ky], fill="#853131", width=0)
w.create_oval([115+kx, 290+ky], [255+kx, 430+ky], fill="#0f1169", width=0)
w.create_oval([130+kx, 310+ky], [246+kx, 428+ky], fill="#853131", width=0)
w.create_oval([160+kx, 350+ky], [230+kx, 420+ky], fill="#0f1169", width=0)
a.mainloop()
