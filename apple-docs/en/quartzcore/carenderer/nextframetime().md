---
title: nextFrameTime()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/carenderer/nextframetime()
source_url: 'https://developer.apple.com/documentation/quartzcore/carenderer/nextframetime()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/carenderer/nextframetime%28%29.json'
content_hash: 'sha256:3e76b4b59dc098b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CARenderer](../carenderer.md)

# nextFrameTime()

<sub>Instance Method</sub>

Returns the time at which the next update should happen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func nextFrameTime() -> CFTimeInterval
```

## Return Value

The time at which the next update should happen.

## Discussion

If infinite, no update needs to be scheduled yet. If `nextFrameTime` is the current frame time, a continuous animation is running and an update should be scheduled after an appropriate delay.

## See Also

### Rendering a Frame

- [- beginFrameAtTime:timeStamp:](<beginframe(attime_timestamp_).md>) — Begin rendering a frame at the specified time.
- [- updateBounds](<updatebounds().md>) — Returns the bounds of the update region that contains all pixels that will be rendered by the current frame.
- [- addUpdateRect:](<addupdate(__).md>) — Adds the rectangle to the update region of the current frame.
- [- render](<render().md>) — Render the update region of the current frame to the target context.
- [- endFrame](<endframe().md>) — Release any data associated with the current frame.
