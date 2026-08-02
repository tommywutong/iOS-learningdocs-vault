---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/CoreMIDI.html
archived_at: '2026-07-18T02:56:32.239134Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreMIDI Changes for Objective-C

### CoreMIDI

#### MIDINetworkSession.h

Modified [+[MIDINetworkConnection connectionWithHost:]](https://developer.apple.com/documentation/coremidi/midinetworkconnection/1619340-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)connectionWithHost:(MIDINetworkHost *)host ``` |
| To | ``` + (instancetype _Nonnull)connectionWithHost:(MIDINetworkHost * _Nonnull)host ``` |

Modified [+[MIDINetworkHost hostWithName:address:port:]](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619365-hostwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (id)hostWithName:(NSString *)name address:(NSString *)address port:(NSUInteger)port ``` |
| To | ``` + (instancetype _Nonnull)hostWithName:(NSString * _Nonnull)name address:(NSString * _Nonnull)address port:(NSUInteger)port ``` |

Modified [+[MIDINetworkHost hostWithName:netService:]](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619371-hostwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (id)hostWithName:(NSString *)name netService:(NSNetService *)netService ``` |
| To | ``` + (instancetype _Nonnull)hostWithName:(NSString * _Nonnull)name netService:(NSNetService * _Nonnull)netService ``` |

Modified [+[MIDINetworkHost hostWithName:netServiceName:netServiceDomain:]](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619338-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)hostWithName:(NSString *)name netServiceName:(NSString *)netServiceName netServiceDomain:(NSString *)netServiceDomain ``` |
| To | ``` + (instancetype _Nonnull)hostWithName:(NSString * _Nonnull)name netServiceName:(NSString * _Nonnull)netServiceName netServiceDomain:(NSString * _Nonnull)netServiceDomain ``` |

Modified [-[MIDINetworkSession connections]](https://developer.apple.com/documentation/coremidi/midinetworksession/1619366-connections)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)connections ``` |
| To | ``` - (NSSet<MIDINetworkConnection *> * _Nonnull)connections ``` |

Modified [-[MIDINetworkSession contacts]](https://developer.apple.com/documentation/coremidi/midinetworksession/1619335-contacts)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)contacts ``` |
| To | ``` - (NSSet<MIDINetworkHost *> * _Nonnull)contacts ``` |

#### MIDIServices.h

Removed [kMIDIObjectType_ExternalMask](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_externalmask)Removed #def MIDIPacketNextAdded [kMIDIObjectType_ExternalMask](https://developer.apple.com/documentation/coremidi/kmidiobjecttype_externalmask)Added [MIDIClientCreateWithBlock()](https://developer.apple.com/documentation/coremidi/1495330-midiclientcreatewithblock)Added [MIDIDestinationCreateWithBlock()](https://developer.apple.com/documentation/coremidi/1495247-mididestinationcreatewithblock)Added [MIDIInputPortCreateWithBlock()](https://developer.apple.com/documentation/coremidi/1495333-midiinputportcreatewithblock)Added [MIDINotifyBlock](https://developer.apple.com/documentation/coremidi/midinotifyblock)Added [MIDIPacketNext()](https://developer.apple.com/documentation/coremidi/1495178-midipacketnext)Added [MIDIReadBlock](https://developer.apple.com/documentation/coremidi/midireadblock)Modified [MIDIObjectSetDictionaryProperty()](https://developer.apple.com/documentation/coremidi/1495160-midiobjectsetdictionaryproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MIDIObjectSetDictionaryProperty (     MIDIObjectRef obj,     CFStringRef propertyID,     CFDictionaryRef data ); ``` |
| To | ``` OSStatus MIDIObjectSetDictionaryProperty (     MIDIObjectRef obj,     CFStringRef _Nonnull propertyID,     CFDictionaryRef _Nonnull dict ); ``` |

#### MIDIThruConnection.h

Removed [#def MIDIThruConnectionParamsSize](https://developer.apple.com/documentation/coremidi/midi_thru_connection/midithruconnectionparamssize)Added [MIDIThruConnectionParamsSize()](https://developer.apple.com/documentation/coremidi/1508275-midithruconnectionparamssize)

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
