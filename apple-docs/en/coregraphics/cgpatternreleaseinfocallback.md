---
title: CGPatternReleaseInfoCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpatternreleaseinfocallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpatternreleaseinfocallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpatternreleaseinfocallback.json'
content_hash: 'sha256:4b6ff05c4ccbb596'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPatternReleaseInfoCallback

<sub>Type Alias</sub>

Release private data or resources associated with the pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGPatternReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [CGPatternCreate](<cgpattern/init(info_bounds_matrix_xstep_ystep_tiling_iscolored_callbacks_).md>).

## Discussion

Quartz calls your release function when it frees your pattern object.

To learn how to associate your release function with a Quartz pattern, see [CGPatternCreate](<cgpattern/init(info_bounds_matrix_xstep_ystep_tiling_iscolored_callbacks_).md>) and [CGPatternCallbacks](cgpatterncallbacks.md).

## See Also

### Callbacks

- [CGPatternCallbacks](cgpatterncallbacks.md) — A structure that holds a version and two callback functions for drawing a custom pattern.
- [CGPatternDrawPatternCallback](cgpatterndrawpatterncallback.md) — Draws a pattern cell.
