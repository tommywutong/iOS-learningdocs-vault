---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Objective-C/MediaPlayer.html
archived_at: '2026-07-18T02:58:04.442705Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# MediaPlayer Changes for Objective-C

### MediaPlayer

#### MPContentItem.h

Added [MPContentItem](https://developer.apple.com/documentation/mediaplayer/mpcontentitem)Added [MPContentItem.artwork](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620160-artwork)Added [MPContentItem.container](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620154-iscontainer)Added [MPContentItem.identifier](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620157-identifier)Added [-[MPContentItem initWithIdentifier:]](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620152-initwithidentifier)Added [MPContentItem.playable](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620158-isplayable)Added [MPContentItem.playbackProgress](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620153-playbackprogress)Added [MPContentItem.subtitle](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620155-subtitle)Added [MPContentItem.title](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620156-title)

#### MPError.h (Added)

Added [MPErrorCloudServiceCapabilityMissing](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrorcloudservicecapabilitymissing)Added [MPErrorCode](https://developer.apple.com/documentation/mediaplayer/mperror/code)Added [MPErrorDomain](https://developer.apple.com/documentation/mediaplayer/mperrordomain)Added [MPErrorNetworkConnectionFailed](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrornetworkconnectionfailed)Added [MPErrorNotFound](https://developer.apple.com/documentation/mediaplayer/mperror/code/notfound)Added [MPErrorNotSupported](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrornotsupported)Added [MPErrorPermissionDenied](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrorpermissiondenied)Added [MPErrorUnknown](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrorunknown)

#### MPMediaItem.h

Modified [MPMediaItemPropertyHasProtectedAsset](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertyhasprotectedasset)

|  | Introduction |
| --- | --- |
| From | tvOS 9.1 |
| To | tvOS 9.2 |

#### MPMediaLibrary.h

Added [MPMediaLibraryAuthorizationStatus](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus)Added [MPMediaLibraryAuthorizationStatusAuthorized](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/mpmedialibraryauthorizationstatusauthorized)Added [MPMediaLibraryAuthorizationStatusDenied](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/denied)Added [MPMediaLibraryAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/notdetermined)Added [MPMediaLibraryAuthorizationStatusRestricted](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/restricted)

#### MPMediaPlaylist.h

Added [MPMediaPlaylistPropertyAuthorDisplayName](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistpropertyauthordisplayname)Added [MPMediaPlaylistPropertyDescriptionText](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistpropertydescriptiontext)

#### MPMusicPlayerController.h

Added [-[MPMusicPlayerController setQueueWithStoreIDs:]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624253-setqueue)

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
