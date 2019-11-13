from pyomegle import OmegleClient, OmegleHandler
import time, random, argparse


parser = argparse.ArgumentParser(description="Kubi Industries Omegle spammer")
parser.add_argument('-u', '--URL', help='URL you want to send', type=str, dest='url', required=True)
parser.add_argument('-m', '--message', help='Message you want to send', type=str, dest='msg', required=True)
args = vars(parser.parse_args())
h = OmegleHandler(loop=True)
c = OmegleClient(h, wpm=47, lang='en')
c.start()
h.waiting()
print(args.get('url'))
time.sleep(8)

while 1:
    while True:
            c.write(args.get('msg'))
            time.sleep(8)
            c.write('Would you mind checking out my experiment?')
            c.send(args.get('url'))
            time.sleep(6)
            c.write('Thank you man')
            time.sleep(random.randint(2,7))
            c.next()
            break
