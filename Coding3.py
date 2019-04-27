if not fluidsynth.init(SF2):
    print "Couldn't load soundfont", SF2
    sys.exit(1)