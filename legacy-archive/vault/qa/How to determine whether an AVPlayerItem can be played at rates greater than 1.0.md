---
title: How to determine whether an AVPlayerItem can be played at rates greater than
  1.0
apple_id: DTS40016827
resource_type: QA
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-03-23'
source_url: https://developer.apple.com/library/archive/qa/qa1772/_index.html
archived_at: '2026-07-18T02:34:41.137663Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1772

# How to determine whether an AVPlayerItem can be played at rates greater than 1.0

## Q:  I’m using the `AVPlayerItem`.`canPlayFastForward` property to find out if an `AVPlayerItem` can be played at rates greater than 1.0, but it always returns NO. Under what conditions does `AVPlayerItem`.`canPlayFastForward` return YES?

A: An `AVPlayerItem` whose status property equals `AVPlayerItemStatusReadyToPlay` can be played at rates between 1.0 and 2.0, inclusive, even if `AVPlayerItem`.`canPlayFastForward` is NO. `AVPlayerItem`.`canPlayFastForward` indicates whether the item can be played at rates greater than 2.0.

The value of the `AVPlayerItem`.`canPlayFastForward` property is always reported as `NO` until the `AVPlayerItem.status` property changes to `AVPlayerItemStatusReadyToPlay`. If the `AVPlayerItem` isn’t prepared to play at all, it certainly can’t play fast.

If the test you are performing is similar to Listing 1 or Listing 2:

__Listing 1__  Obtaining the value of `AVPlayerItem`.`canPlayFastForward` (Swift).

```
import AVFoundation

let anAsset = AVAsset(URL: <#A URL#>)
let playerItem = AVPlayerItem(asset: anAsset)
let canPlayFastForward = playerItem.canPlayFastForward
```


__Listing 2__  Obtaining the value of `AVPlayerItem`.`canPlayFastForward` (Objective-C).

```objc
#import <AVFoundation/AVFoundation.h>

AVAsset *asset = [AVAsset assetWithURL:<#A URL>];
AVPlayerItem *playerItem = [AVPlayerItem playerItemWithAsset:asset];
BOOL canPlayFastForward = [playerItem canPlayFastForward];
```

then the `AVPlayerItem`.`canPlayFastForward` property will always be `NO`.

`AVPlayerItem` objects are dynamic. The value of `AVPlayerItem`.`canPlayFastForward` will change to `YES` for all file-based assets and some streaming based assets (if the source playlist offers media that allows it) at the time the item becomes ready to play. The way to get notified when the player item is ready to play is by observing the `AVPlayerItem.status` property via Key-Value Observing (KVO). See the [AV Foundation Programming Guide](https://developer.apple.com/library/ios/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html) for the details.

The `AVPlayerItem`.`canPlayFastForward` property is not designed to indicate that playback at arbitrarily high rates is possible with no loss of smoothness.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-03-23 | New document that discusses how to determine if an AVPlayerItem can be played at rates greater than 1.0. |

