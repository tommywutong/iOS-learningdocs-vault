---
title: 'addUpdate(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/carenderer/addupdate(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/carenderer/addupdate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/carenderer/addupdate%28_%3A%29.json'
content_hash: 'sha256:8d5d4ee9ad3eed4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CARenderer](../carenderer.md)

# addUpdate(_:)

<sub>Instance Method</sub>

Adds the rectangle to the update region of the current frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addUpdate(_ r: CGRect)
```

## Parameters

- `r` — A rectangle defining the region to be added to the update region.

## See Also

### Rendering a Frame

- [- beginFrameAtTime:timeStamp:](<beginframe(attime_timestamp_).md>) — Begin rendering a frame at the specified time.
- [- updateBounds](<updatebounds().md>) — Returns the bounds of the update region that contains all pixels that will be rendered by the current frame.
- [- render](<render().md>) — Render the update region of the current frame to the target context.
- [- nextFrameTime](<nextframetime().md>) — Returns the time at which the next update should happen.
- [- endFrame](<endframe().md>) — Release any data associated with the current frame.
