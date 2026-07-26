---
title: CGPatternDrawPatternCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpatterndrawpatterncallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpatterndrawpatterncallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpatterndrawpatterncallback.json'
content_hash: 'sha256:726c8675180e17cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPatternDrawPatternCallback

<sub>Type Alias</sub>

Draws a pattern cell.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGPatternDrawPatternCallback = (UnsafeMutableRawPointer?, CGContext) -> Void
```

## Parameters

- `info` — A generic pointer to private data associated with the pattern. This is the same pointer you supplied to [CGPatternCreate](<cgpattern/init(info_bounds_matrix_xstep_ystep_tiling_iscolored_callbacks_).md>).

- `context` — The graphics context for drawing the pattern cell.

## Discussion

When a pattern is used to stroke or fill a graphics path,Quartz calls your custom drawing function at the appropriatetime to draw the pattern cell. The cell should be drawn exactly thesame way each time the drawing function is called.

In a drawing function associated with an uncolored pattern,you should not attempt to set a stroke or fill color or color space—ifyou do so, the result is undefined.

To learn how to associate your drawing function with a Quartzpattern, see [CGPatternCreate](<cgpattern/init(info_bounds_matrix_xstep_ystep_tiling_iscolored_callbacks_).md>) and [CGPatternCallbacks](cgpatterncallbacks.md).

## See Also

### Callbacks

- [CGPatternCallbacks](cgpatterncallbacks.md) — A structure that holds a version and two callback functions for drawing a custom pattern.
- [CGPatternReleaseInfoCallback](cgpatternreleaseinfocallback.md) — Release private data or resources associated with the pattern.
