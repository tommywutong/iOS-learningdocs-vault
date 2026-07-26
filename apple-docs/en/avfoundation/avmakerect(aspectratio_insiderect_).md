---
title: 'AVMakeRect(aspectRatio:insideRect:)'
framework: AVFoundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmakerect(aspectratio:insiderect:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmakerect(aspectratio:insiderect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmakerect%28aspectratio%3Ainsiderect%3A%29.json'
content_hash: 'sha256:b49ea93edf7cf1c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMakeRect(aspectRatio:insideRect:)

<sub>Function</sub>

Returns a scaled rectangle that maintains the specified aspect ratio within a bounding rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func AVMakeRect(aspectRatio: CGSize, insideRect boundingRect: CGRect) -> CGRect
```

## Parameters

- `aspectRatio` — The width and height ratio (aspect ratio) you want to maintain.

- `boundingRect` — The bounding rectangle you want to fit into.

## Return Value

Returns a scaled `CGRect` that maintains the aspect ratio specified by `aspectRatio` that fits within `boundingRect`.

## Discussion

Use this function when attempting to fit the presentation size of a player item object’s content within the bounds of another [CALayer](../quartzcore/calayer.md). Use the returned [CGRect](../corefoundation/cgrect.md) as the player layer’s [frame](../quartzcore/calayer/frame.md) property value. For example:

**Swift**

```swift
let aspectRatio = CGSize(width: 1920, height: 1080)
playerLayer.frame = AVMakeRect(aspectRatio: aspectRatio, insideRect: superLayer.bounds)
```

**Objective-C**

```objc
CGSize aspectRatio = CGSizeMake(1920, 1080);
self.playerLayer.frame = AVMakeRectWithAspectRatioInsideRect(aspectRatio, self.superLayer.bounds);
```
