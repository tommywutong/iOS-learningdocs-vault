---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Objective-C/MediaPlayer.html
archived_at: '2026-07-18T02:57:26.950496Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# MediaPlayer Changes for Objective-C

### MediaPlayer

#### MPContentItem.h

Added [MPContentItem.explicitContent](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1771744-explicitcontent)Added [MPContentItem.streamingContent](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1771745-isstreamingcontent)

#### MPMediaItem.h

Added [MPMediaItemArtwork](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork)Added [MPMediaItemArtwork.bounds](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621723-bounds)Added [MPMediaItemArtwork.imageCropRect](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621760-imagecroprect)Added [-[MPMediaItemArtwork imageWithSize:]](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621736-imagewithsize)Added [-[MPMediaItemArtwork initWithBoundsSize:requestHandler:]](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1649704-initwithboundssize)Added [-[MPMediaItemArtwork initWithImage:]](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621747-initwithimage)Added [MPMediaItemPropertyDateAdded](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertydateadded)Added [MPMediaItemPropertyIsExplicit](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertyisexplicit)

#### MPNowPlayingInfoCenter.h

Added [MPNowPlayingInfoCollectionIdentifier](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocollectionidentifier)Added [MPNowPlayingInfoMediaType](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfomediatype)Added [MPNowPlayingInfoMediaTypeAudio](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfomediatype/mpnowplayinginfomediatypeaudio)Added [MPNowPlayingInfoMediaTypeNone](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfomediatype/none)Added [MPNowPlayingInfoMediaTypeVideo](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfomediatype/video)Added [MPNowPlayingInfoPropertyExternalContentIdentifier](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyexternalcontentidentifier)Added [MPNowPlayingInfoPropertyExternalUserProfileIdentifier](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyexternaluserprofileidentifier)Added [MPNowPlayingInfoPropertyIsLiveStream](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyislivestream)Added [MPNowPlayingInfoPropertyMediaType](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertymediatype)Added [MPNowPlayingInfoPropertyPlaybackProgress](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyplaybackprogress)

#### MPRemoteCommand.h

Added [MPChangeRepeatModeCommand](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommand)Added [MPChangeRepeatModeCommand.currentRepeatType](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommand/1648342-currentrepeattype)Added [MPChangeShuffleModeCommand](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommand)Added [MPChangeShuffleModeCommand.currentShuffleType](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommand/1648341-currentshuffletype)Modified [MPSkipIntervalCommand.preferredIntervals](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommand/1622899-preferredintervals)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *preferredIntervals ``` |
| To | ``` @property(nonatomic, copy) NSArray<NSNumber *> *preferredIntervals ``` |

#### MPRemoteCommandCenter.h

Added [MPRemoteCommandCenter.changeRepeatModeCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1649694-changerepeatmodecommand)Added [MPRemoteCommandCenter.changeShuffleModeCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1649692-changeshufflemodecommand)Modified [MPRemoteCommandCenter.changePlaybackPositionCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618997-changeplaybackpositioncommand)

|  | Introduction |
| --- | --- |
| From | tvOS 9.0 |
| To | tvOS 9.1 |

#### MPRemoteCommandEvent.h

Added [MPChangeLanguageOptionCommandEvent.setting](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptioncommandevent/1649697-setting)Added [MPChangeRepeatModeCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommandevent)Added [MPChangeRepeatModeCommandEvent.preservesRepeatMode](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommandevent/2097553-preservesrepeatmode)Added [MPChangeRepeatModeCommandEvent.repeatType](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommandevent/1649689-repeattype)Added [MPChangeShuffleModeCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommandevent)Added [MPChangeShuffleModeCommandEvent.preservesShuffleMode](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommandevent/2097552-preservesshufflemode)Added [MPChangeShuffleModeCommandEvent.shuffleType](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommandevent/1649696-shuffletype)

#### MPRemoteControlTypes.h (Added)

Added [MPChangeLanguageOptionSetting](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptionsetting)Added [MPChangeLanguageOptionSettingNone](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptionsetting/none)Added [MPChangeLanguageOptionSettingNowPlayingItemOnly](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptionsetting/nowplayingitemonly)Added [MPChangeLanguageOptionSettingPermanent](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptionsetting/mpchangelanguageoptionsettingpermanent)Added [MPRepeatType](https://developer.apple.com/documentation/mediaplayer/mprepeattype)Added [MPRepeatTypeAll](https://developer.apple.com/documentation/mediaplayer/mprepeattype/mprepeattypeall)Added [MPRepeatTypeOff](https://developer.apple.com/documentation/mediaplayer/mprepeattype/mprepeattypeoff)Added [MPRepeatTypeOne](https://developer.apple.com/documentation/mediaplayer/mprepeattype/one)Added [MPShuffleType](https://developer.apple.com/documentation/mediaplayer/mpshuffletype)Added [MPShuffleTypeCollections](https://developer.apple.com/documentation/mediaplayer/mpshuffletype/collections)Added [MPShuffleTypeItems](https://developer.apple.com/documentation/mediaplayer/mpshuffletype/items)Added [MPShuffleTypeOff](https://developer.apple.com/documentation/mediaplayer/mpshuffletype/off)

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
