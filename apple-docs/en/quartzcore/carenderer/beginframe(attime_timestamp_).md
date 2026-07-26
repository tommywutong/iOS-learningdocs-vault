---
title: 'beginFrame(atTime:timeStamp:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/carenderer/beginframe(attime:timestamp:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/carenderer/beginframe(attime:timestamp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/carenderer/beginframe%28attime%3Atimestamp%3A%29.json'
content_hash: 'sha256:f46a12a8e44f9bd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CARenderer](../carenderer.md)

# beginFrame(atTime:timeStamp:)

<sub>Instance Method</sub>

Begin rendering a frame at the specified time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func beginFrame(atTime t: CFTimeInterval, timeStamp ts: UnsafeMutablePointer<CVTimeStamp>?)
```

## Parameters

- `t` — The layer time.

- `ts` — The display timestamp associated with timeInterval. Can be null.

## See Also

### Rendering a Frame

- [- updateBounds](<updatebounds().md>) — Returns the bounds of the update region that contains all pixels that will be rendered by the current frame.
- [- addUpdateRect:](<addupdate(__).md>) — Adds the rectangle to the update region of the current frame.
- [- render](<render().md>) — Render the update region of the current frame to the target context.
- [- nextFrameTime](<nextframetime().md>) — Returns the time at which the next update should happen.
- [- endFrame](<endframe().md>) — Release any data associated with the current frame.
