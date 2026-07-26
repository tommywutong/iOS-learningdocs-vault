---
title: updateBounds()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/carenderer/updatebounds()
source_url: 'https://developer.apple.com/documentation/quartzcore/carenderer/updatebounds()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/carenderer/updatebounds%28%29.json'
content_hash: 'sha256:63091fc43dabb154'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CARenderer](../carenderer.md)

# updateBounds()

<sub>Instance Method</sub>

Returns the bounds of the update region that contains all pixels that will be rendered by the current frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func updateBounds() -> CGRect
```

## Return Value

The bounds of the update region..

## Discussion

Initially `updateBounds` will include all differences between the current frame and the previously rendered frame.

## See Also

### Rendering a Frame

- [- beginFrameAtTime:timeStamp:](<beginframe(attime_timestamp_).md>) — Begin rendering a frame at the specified time.
- [- addUpdateRect:](<addupdate(__).md>) — Adds the rectangle to the update region of the current frame.
- [- render](<render().md>) — Render the update region of the current frame to the target context.
- [- nextFrameTime](<nextframetime().md>) — Returns the time at which the next update should happen.
- [- endFrame](<endframe().md>) — Release any data associated with the current frame.
