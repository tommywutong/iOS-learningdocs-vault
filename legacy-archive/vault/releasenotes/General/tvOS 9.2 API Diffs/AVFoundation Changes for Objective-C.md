---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Objective-C/AVFoundation.html
archived_at: '2026-07-18T02:58:04.035254Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# AVFoundation Changes for Objective-C

### AVFoundation

#### AVMetadataFormat.h

Added [AVMetadataKeySpaceHLSDateRange](https://developer.apple.com/documentation/avfoundation/avmetadatakeyspacehlsdaterange)

#### AVPlayerItem.h

Added [-[AVPlayerItem addMediaDataCollector:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1624164-add)Added [AVPlayerItem.mediaDataCollectors](https://developer.apple.com/documentation/avfoundation/avplayeritem/1624161-mediadatacollectors)Added [-[AVPlayerItem removeMediaDataCollector:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1624163-remove)Added AVPlayerItem(AVPlayerItemMediaDataCollectors)

#### AVPlayerItemMediaDataCollector.h (Added)

Added [AVPlayerItemMediaDataCollector](https://developer.apple.com/documentation/avfoundation/avplayeritemmediadatacollector)Added [AVPlayerItemMetadataCollector](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector)Added [AVPlayerItemMetadataCollector.delegate](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/1617196-delegate)Added [AVPlayerItemMetadataCollector.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/1617192-delegatequeue)Added [-[AVPlayerItemMetadataCollector initWithIdentifiers:classifyingLabels:]](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/1617191-init)Added [-[AVPlayerItemMetadataCollector setDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/1617195-setdelegate)Added [AVPlayerItemMetadataCollectorPushDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate)Added [-[AVPlayerItemMetadataCollectorPushDelegate metadataCollector:didCollectDateRangeMetadataGroups:indexesOfNewGroups:indexesOfModifiedGroups:]](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate/1617190-metadatacollector)

#### AVTimedMetadataGroup.h

Added [AVMetadataGroup.classifyingLabel](https://developer.apple.com/documentation/avfoundation/avmetadatagroup/1620087-classifyinglabel)Added [AVMetadataGroup.uniqueID](https://developer.apple.com/documentation/avfoundation/avmetadatagroup/1620088-uniqueid)Added AVMetadataGroup(AVMetadataGroupIdentification)

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
