from __future__ import print_function
from datasift import Client
from termcolor import colored

ds = Client("hmaserrat", "2d2a336d5a7aefe2f197c815a3f6931a")

def print_pretty(msg):
    if not msg.has_key('twitter'):
        print(colored('Non twitter msg', 'cyan'))
        return

    tw = msg['twitter']
    user = tw['user']
    name = user['name'] if 'name' in user else 'Unknown'
    output = colored('Name: ', 'red') + colored(name, 'green')
    gender = msg['demographic']['gender'] if 'demographic' in msg else 'Unknown'
    output += colored(' Gender: ', 'red') + colored(gender, 'green')
    location = user['location'] if 'location' in user else 'Unknown'
    output += colored(' Location: ', 'red') + colored(location, 'green')
    print(output)
    print(tw['text'])
    lat = tw['geo']['latitude'] if 'geo' in tw else 'None'
    lon = tw['geo']['longitude'] if 'geo' in tw else 'None'
    if 'links' in msg:
        print(msg['links']['title'])
        print(msg['links']['url'])
    print(lat, lon, user['geo_enabled'])


@ds.on_delete
def on_delete(interaction):
    #print( 'Deleted interaction %s ' % interaction)
    print_pretty(interaction)


@ds.on_open
def on_open():
    print( 'Streaming ready, can start subscribing')
    #   interaction.content contains "burnaby" and
    #    demographic.location.city contains_any "Burnaby, Vancouver"
    csdl = '''
        interaction.type == "twitter" and
        (twitter.geo geo_polygon "49.290021, -122.893453:
                                     49.237147, -122.892766:
                                     49.200818, -122.959714:
                                     49.195210, -122.953191:
                                     49.182869, -122.979627:
                                     49.203062, -123.022886:
                                     49.292932, -123.023229" or
        demographic.location.country contains "burnaby" or
        demographic.location.city contains "burnaby" or
        twitter.user.location contains "burnaby")
    '''
    csdl = '''
        interaction.type == "twitter" and
        salience.content.topics contains "Politics" and
        (demographic.location.country contains_any "Canada" or
        twitter.user.location contains "Canada")
    '''
    stream = ds.compile(csdl)['hash']

    @ds.subscribe(stream)
    def subscribe_to_hash(msg):
        if 'text' in msg['twitter']:
            #print_pretty( msg['twitter']['text'])
            print_pretty( msg)


@ds.on_closed
def on_close(wasClean, code, reason):
    print( 'Streaming connection closed')


@ds.on_ds_message
def on_ds_message(msg):
    print_pretty( 'DS Message %s' % msg)

#must start stream subscriber
ds.start_stream_subscriber()

