---
title: iOS 2.2 API Diffs
apple_id: TP40008092
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2008-11-20'
source_url: https://developer.apple.com/library/archive/releasenotes/Miscellaneous/iPhone22APIDiffs/iPhone21_iPhone22_APIDiffs.html
archived_at: '2026-07-18T02:58:58.942675Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


# iOS 2.1 to iOS 2.2 API Differences

## Added frameworks:

- AVFoundation

## AVFoundation

AVAudioPlayer.hAdded [AVAudioPlayer](https://developer.apple.com/documentation/avfoundation/avaudioplayer)Added [-[AVAudioPlayer averagePowerForChannel:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1390838-averagepowerforchannel)Added [AVAudioPlayer.currentTime](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387297-currenttime)Added [AVAudioPlayer.data](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389437-data)Added [AVAudioPlayer.delegate](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387134-delegate)Added [AVAudioPlayer.duration](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388395-duration)Added [-[AVAudioPlayer initWithContentsOfURL:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387281-initwithcontentsofurl)Added [-[AVAudioPlayer initWithData:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388809-init)Added [AVAudioPlayer.meteringEnabled](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387935-meteringenabled)Added [AVAudioPlayer.numberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388992-numberofchannels)Added [AVAudioPlayer.numberOfLoops](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1386071-numberofloops)Added [-[AVAudioPlayer pause]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389363-pause)Added [-[AVAudioPlayer peakPowerForChannel:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388509-peakpower)Added [-[AVAudioPlayer play]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387388-play)Added [AVAudioPlayer.playing](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1390139-playing)Added [-[AVAudioPlayer prepareToPlay]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1386886-preparetoplay)Added [-[AVAudioPlayer stop]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1386018-stop)Added [-[AVAudioPlayer updateMeters]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388565-updatemeters)Added [AVAudioPlayer.url](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387448-url)Added [AVAudioPlayer.volume](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389330-volume)Added [AVAudioPlayerDelegate](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate)Added [-[AVAudioPlayerDelegate audioPlayerBeginInterruption:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624037-audioplayerbegininterruption) (no architecture available)Added [-[AVAudioPlayerDelegate audioPlayerDecodeErrorDidOccur:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1387676-audioplayerdecodeerrordidoccur)Added [-[AVAudioPlayerDelegate audioPlayerDidFinishPlaying:successfully:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1389160-audioplayerdidfinishplaying)Added [-[AVAudioPlayerDelegate audioPlayerEndInterruption:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624039-audioplayerendinterruption) (no architecture available)

## AddressBook

No changes

## AddressBookUI

No changes

## AudioToolbox

AudioFile.hAdded [AudioFileReadPacketData()](https://developer.apple.com/documentation/audiotoolbox/1502788-audiofilereadpacketdata)AudioFormat.hAdded [kAudioFormatProperty_FirstPlayableFormatFromList](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_firstplayableformatfromlist)Added [kAudioFormatProperty_ID3TagSize](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_id3tagsize)Added [kAudioFormatProperty_ID3TagToDictionary](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_id3tagtodictionary)AudioQueue.hAdded [kAudioQueueErr_PrimeTimedOut](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_primetimedout)AudioServices.hAdded [kAudioSessionCategory_SoloAmbientSound](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_soloambientsound)Added [kAudioSessionProperty_AudioInputAvailable](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_audioinputavailable)

## AudioUnit

No changes

## CFNetwork

No changes

## CoreAudio

No changes

## CoreFoundation

CFBase.hAdded [#def kCFCoreFoundationVersionNumber10_5_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_5_2)Added [#def kCFCoreFoundationVersionNumber10_5_3](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_5_3)Added [#def kCFCoreFoundationVersionNumber10_5_4](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_5_4)Added #def kCFCoreFoundationVersionNumber_iOS_2_0Added #def kCFCoreFoundationVersionNumber_iOS_2_1

## CoreGraphics

No changes

## CoreLocation

CLLocation.hAdded [CLLocation.course](https://developer.apple.com/documentation/corelocation/cllocation/1423832-course)Added [CLLocation.speed](https://developer.apple.com/documentation/corelocation/cllocation/1423798-speed)Added [CLLocationDirection](https://developer.apple.com/documentation/corelocation/cllocationdirection)Added [CLLocationSpeed](https://developer.apple.com/documentation/corelocation/cllocationspeed)

## Foundation

NSDateFormatter.hModified [NSDateFormatterBehavior10_0](https://developer.apple.com/documentation/foundation/nsdateformatterbehavior/nsdateformatterbehavior10_0)

|  | Architectures |
| --- | --- |
| Old | arm |
| New | none? |

NSHTTPCookie.hAdded [-[NSHTTPCookie isHTTPOnly]](https://developer.apple.com/documentation/foundation/nshttpcookie/1392969-httponly)NSNumberFormatter.hModified [NSNumberFormatterBehavior10_0](https://developer.apple.com/documentation/foundation/numberformatter/behavior/behavior10_0)

|  | Architectures |
| --- | --- |
| Old | arm |
| New | none? |

NSObjCRuntime.hAdded [#def NSFoundationVersionNumber10_5_2](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_5_2)Added [#def NSFoundationVersionNumber10_5_3](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_5_3)Added [#def NSFoundationVersionNumber10_5_4](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_5_4)Added #def NSFoundationVersionNumber_iOS_2_0Added #def NSFoundationVersionNumber_iOS_2_1

## MediaPlayer

No changes

## OpenAL

No changes

## OpenGLES

No changes

## QuartzCore

No changes

## Security

No changes

## SystemConfiguration

No changes

## UIKit

UIViewController.hModified [UIViewController.nibName](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621487-nibname)

|  | Declaration |
| --- | --- |
| Old | @property(readonly, copy) NSString \*nibName |
| New | @property(nonatomic, readonly, copy) NSString \*nibName |

Modified [UIViewController.nibBundle](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621489-nibbundle)

|  | Declaration |
| --- | --- |
| Old | @property(readonly, retain) NSBundle \*nibBundle |
| New | @property(nonatomic, readonly, retain) NSBundle \*nibBundle |

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
