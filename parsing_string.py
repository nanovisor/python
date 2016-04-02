text = "X-DSPAM-Confidence:    0.8475";

start = text.find(':')

piece = float( text[start :] )

print piece, type(piece)
