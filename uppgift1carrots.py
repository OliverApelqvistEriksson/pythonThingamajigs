Tor = float(input("Tors tid: "))
Mor = float(input("Mors tid: "))
tid = 0
mormoroter = 0
tormoroter = 0
morsekund = 0
torsekund = 0
moroter = 40
while moroter > 1 :
    if morsekund == tid :
        mormoroter += 1
        morsekund += Mor
        moroter -= 1
    if torsekund == tid :
        tormoroter += 1
        torsekund += Tor
        moroter -= 1
    tid += 1
if moroter == 2 and morsekund == torsekund :
    morsekund += 1
    torsekund += 1
elif morsekund > torsekund and moroter > 0:
    tormoroter += 1
elif morsekund < torsekund and moroter > 0:
    mormoroter += 1
print("Tor: ", tormoroter)
print("Mor: ", mormoroter)