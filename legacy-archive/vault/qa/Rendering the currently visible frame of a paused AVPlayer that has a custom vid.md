---
title: Rendering the currently visible frame of a paused AVPlayer that has a custom
  video compositor
apple_id: DTS40017698
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-12-04'
source_url: https://developer.apple.com/library/archive/qa/qa1966/_index.html
archived_at: '2026-07-18T02:38:00.924427Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1966

# Rendering the currently visible frame of a paused AVPlayer that has a custom video compositor

## Q:  How can I re-render the currently visible frame of a paused `AVPlayer` that has a custom video compositor? I would like to update values that affect the rendered video while it is paused, and have those changes reflected in the currently visible frame.

A: To re-render a frame, you must set a new instance of `AVVideoComposition` to the player's current player item as shown in Listing 1.

__Listing 1__  Setting the video composition for a paused player to re-render the currently visible frame.

```swift
let asset:AVAsset = <#An asset#>
let playerItem:AVPlayerItem = <#A player's current player item#>

var applyComposition: ((AVAsynchronousCIImageFilteringRequest) -> Void)? = nil
applyComposition = { request in
      ...
}

let composition = AVVideoComposition(asset: asset,
          applyingCIFiltersWithHandler: applyComposition)
playerItem.videoComposition = composition   // Set the player item video composition.
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-12-04 | New document that shows how to re-render the currently visible frame of a paused AVPlayer that has a custom video compositor |

