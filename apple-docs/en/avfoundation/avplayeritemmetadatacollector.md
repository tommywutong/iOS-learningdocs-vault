---
title: AVPlayerItemMetadataCollector
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.3+, tvOS 9.2+, visionOS 1.0+, watchOS 2.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemmetadatacollector
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemmetadatacollector.json'
content_hash: 'sha256:35a0f61cef2ac74a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemMetadataCollector

<sub>Class</sub>

An object used to capture the date range metadata defined for an HTTP Live Streaming asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerItemMetadataCollector
```

## Overview

You can use the HLS `#EXT-X-DATERANGE` tag to define date range metadata in a media playlist. This tag is useful for defining timed metadata for interstitial regions such as advertisements, but can be used to define any timed metadata needed by your stream. To access this metadata when the stream is played using an [AVPlayer](avplayer.md), you create an instance of `AVPlayerItemMetadataCollector`, configure its delegate object (see [AVPlayerItemMetadataCollectorPushDelegate](avplayeritemmetadatacollectorpushdelegate.md)), and add it as a media data collector to the [AVPlayerItem](avplayeritem.md) (see example).

**Swift**

```swift
class PlaybackController: NSObject, AVPlayerItemMetadataCollectorPushDelegate {
    
    let player = AVPlayer()
    var playerItem: AVPlayerItem!
    var metadataCollector: AVPlayerItemMetadataCollector!
    
    func prepareToPlay(url: URL) {
        metadataCollector = AVPlayerItemMetadataCollector()
        metadataCollector.setDelegate(self, queue: DispatchQueue.main)
        
        playerItem = AVPlayerItem(url: url)
        playerItem.add(metadataCollector)
        
        player.replaceCurrentItem(with: playerItem)
    }
    
    func metadataCollector(_ metadataCollector: AVPlayerItemMetadataCollector,
                           didCollect metadataGroups: [AVDateRangeMetadataGroup],
                           indexesOfNewGroups: IndexSet,
                           indexesOfModifiedGroups: IndexSet) {
        // Process metadata
    }
}
```

**Objective-C**

```objc
// Adopts AVPlayerItemMetadataCollectorPushDelegate
@implementation PlaybackController
 
- (void)prepareToPlay:(NSURL *)url {
    self.metadataCollector = [[AVPlayerItemMetadataCollector alloc] init];
    [self.metadataCollector setDelegate:self queue:dispatch_get_main_queue()];
 
    self.playerItem = [AVPlayerItem playerItemWithURL:url];
    [self.playerItem addMediaDataCollector:self.metadataCollector];
 
    self.player = [AVPlayer playerWithPlayerItem:self.playerItem];
}
 
- (void)metadataCollector:(AVPlayerItemMetadataCollector *)metadataCollector
didCollectDateRangeMetadataGroups:(NSArray<AVDateRangeMetadataGroup *> *)metadataGroups
       indexesOfNewGroups:(NSIndexSet *)indexesOfNewGroups
  indexesOfModifiedGroups:(NSIndexSet *)indexesOfModifiedGroups {
    // Process metadata
}
 
@end
```

Creating an `AVPlayerItemMetadataCollector` as shown in the example, will capture all `#EXT-X-DATERANGE` metadata defined in your stream. If you would like to filter the output to only the metadata of interest, you can create an instance to filter by identifier and/or classifying labels using the [- initWithIdentifiers:classifyingLabels:](<avplayeritemmetadatacollector/init(identifiers_classifyinglabels_).md>) initializer.

## Relationships

- **Inherits From**: [AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a metadata collector

- [- initWithIdentifiers:classifyingLabels:](<avplayeritemmetadatacollector/init(identifiers_classifyinglabels_).md>) — Creates a metadata collector to access a stream’s metadata groups matching the specified array of identifiers and classifying labels.

### Accessing the delegate and callback queue

- [- setDelegate:queue:](<avplayeritemmetadatacollector/setdelegate(__queue_).md>) — Sets the delegate and a dispatch queue on which the delegate will be called.
- [delegate](avplayeritemmetadatacollector/delegate.md) — Accesses the metadata collector’s delegate object.
- [AVPlayerItemMetadataCollectorPushDelegate](avplayeritemmetadatacollectorpushdelegate.md) — A protocol you implement to receive metadata callbacks from a player item metadata collector.
- [delegateQueue](avplayeritemmetadatacollector/delegatequeue.md) — The dispatch queue on which the delegate’s methods are called.

## See Also

### Timed metadata

- [Presenting chapter markers](presenting-chapter-markers.md) — Add chapter markers to enable users to quickly navigate your content.
- [AVMetadataGroup](avmetadatagroup.md) — A collection of metadata items associated with a timeline segment.
- [AVTimedMetadataGroup](avtimedmetadatagroup.md) — A collection of metadata items that are valid for use during a specific time range.
- [AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md) — A mutable collection of metadata items that are valid for use during a specific time range.
- [AVDateRangeMetadataGroup](avdaterangemetadatagroup.md) — A collection of metadata items that are valid for use within a specific date range.
- [AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md) — A mutable collection of metadata items that are valid for use within a specific range of dates.
- [AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md) — The abstract base for media data collectors.
