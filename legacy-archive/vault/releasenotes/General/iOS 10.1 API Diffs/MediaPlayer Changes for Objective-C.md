---
title: iOS 10.1 API Diffs
apple_id: TP40017545
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS101APIDiffs/Objective-C/MediaPlayer.html
archived_at: '2026-07-18T02:54:45.423802Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.1 API Diffs](iOS%2010.0%20to%20iOS%2010.1%20API%20Differences.md)


# MediaPlayer Changes for Objective-C

### MediaPlayer

#### MPError.h

Added [MPErrorCancelled](https://developer.apple.com/documentation/mediaplayer/mperror/code/cancelled)

#### MPMusicPlayerController.h

Added [-[MPMusicPlayerController prepareToPlayWithCompletionHandler:]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/2582424-preparetoplay)Added [-[MPMusicPlayerController setQueueWithDescriptor:]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/2582423-setqueuewithdescriptor)

#### MPMusicPlayerQueueDescriptor.h (Added)

Added [MPMusicPlayerMediaItemQueueDescriptor](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor)Added [-[MPMusicPlayerMediaItemQueueDescriptor initWithItemCollection:]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/2582437-init)Added [-[MPMusicPlayerMediaItemQueueDescriptor initWithQuery:]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/2582441-init)Added [MPMusicPlayerMediaItemQueueDescriptor.itemCollection](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/2582438-itemcollection)Added [MPMusicPlayerMediaItemQueueDescriptor.query](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/2582439-query)Added [-[MPMusicPlayerMediaItemQueueDescriptor setEndTime:forItem:]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/2582431-setendtime)Added [-[MPMusicPlayerMediaItemQueueDescriptor setStartTime:forItem:]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/2582428-setstarttime)Added [MPMusicPlayerMediaItemQueueDescriptor.startItem](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/2582433-startitem)Added [MPMusicPlayerQueueDescriptor](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerqueuedescriptor)Added [MPMusicPlayerStoreQueueDescriptor](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor)Added [-[MPMusicPlayerStoreQueueDescriptor initWithStoreIDs:]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor/2582435-init)Added [-[MPMusicPlayerStoreQueueDescriptor setEndTime:forItemWithStoreID:]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor/2582434-setendtime)Added [-[MPMusicPlayerStoreQueueDescriptor setStartTime:forItemWithStoreID:]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor/2582432-setstarttime)Added [MPMusicPlayerStoreQueueDescriptor.startItemID](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor/2582430-startitemid)Added [MPMusicPlayerStoreQueueDescriptor.storeIDs](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor/2582426-storeids)

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
