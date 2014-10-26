from hashlib import sha1

TOPICS = [
    'com.apple.ess',
    'com.apple.gamed',
    'com.apple.icloud-container.com.apple.callhistory.sync-helper',
    'com.apple.itunesstored',
    'com.apple.itunesu',
    'com.apple.jalisco',
    'com.apple.madrid',  # iMessage
    'com.apple.maps.icloud',
    'com.apple.maspushagent',
    'com.apple.mediastream.subscription.push',
    'com.apple.mobileme.fmf1',  # Find My Friends
    'com.apple.mobileme.fmf3',
    'com.apple.mobileme.fmip',  # Find My iPhone/Mac
    'com.apple.private.ac',
    'com.apple.private.alloy.callhistorysync',
    'com.apple.private.alloy.continuity.activity',
    'com.apple.private.alloy.continuity.activity.public',
    'com.apple.private.alloy.continuity.auth',
    'com.apple.private.alloy.continuity.encryption',
    'com.apple.private.alloy.continuity.tethering',
    'com.apple.private.alloy.icloudpairing',
    'com.apple.private.alloy.idsremoteurlconnection',
    'com.apple.private.alloy.maps',
    'com.apple.private.alloy.phonecontinuity',
    'com.apple.private.alloy.screensharing',
    'com.apple.private.alloy.sms',
    'com.apple.private.ids',
    'com.apple.sagad',
    'com.apple.sharedstreams',
    'com.apple.store.Jolly',
    'com.icloud.askpermission',
    'com.icloud.family',
    'com.me.bookmarks',
    'com.me.btmm',  # Back To My Mac
    'com.me.cal',
    'com.me.contacts',
    'com.me.keyvalueservice',
    'com.me.setupservice',
    'com.me.ubiquity',
    'com.me.ubiquity.system',
]

TOPIC_HASHES = dict([(sha1(topic).digest(), topic) for topic in TOPICS])


def topicForHash(hash):
    return TOPIC_HASHES.get(hash, hash.encode('hex'))
