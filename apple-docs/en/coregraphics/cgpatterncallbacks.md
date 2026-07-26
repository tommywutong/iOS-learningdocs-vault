---
title: CGPatternCallbacks
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpatterncallbacks
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpatterncallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpatterncallbacks.json'
content_hash: 'sha256:814474f2ae5b2559'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPatternCallbacks

<sub>Structure</sub>

A structure that holds a version and two callback functions for drawing a custom pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CGPatternCallbacks
```

## Overview

You supply a [CGPatternCallbacks](cgpatterncallbacks.md) structure to the function [CGPatternCreate](<cgpattern/init(info_bounds_matrix_xstep_ystep_tiling_iscolored_callbacks_).md>) to create a data provider for direct access. The functions specified by the [CGPatternCallbacks](cgpatterncallbacks.md) structure are responsible for drawing the pattern and for handling the pattern’s memory management.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cgpatterncallbacks/init().md>)
- [init(version:drawPattern:releaseInfo:)](<cgpatterncallbacks/init(version_drawpattern_releaseinfo_).md>)

### Instance Properties

- [drawPattern](cgpatterncallbacks/drawpattern.md) — A pointer to a custom function that draws thepattern. For information about this callback function, see [CGPatternDrawPatternCallback](cgpatterndrawpatterncallback.md).
- [releaseInfo](cgpatterncallbacks/releaseinfo.md) — An optional pointer to a custom function that’sinvoked when the pattern is released. [CGPatternReleaseInfoCallback](cgpatternreleaseinfocallback.md).
- [version](cgpatterncallbacks/version.md) — The version of the structure passed in as a parameterto the [CGPatternCreate](<cgpattern/init(info_bounds_matrix_xstep_ystep_tiling_iscolored_callbacks_).md>). Forthis version of the structure, you should set this value to zero.

## See Also

### Callbacks

- [CGPatternDrawPatternCallback](cgpatterndrawpatterncallback.md) — Draws a pattern cell.
- [CGPatternReleaseInfoCallback](cgpatternreleaseinfocallback.md) — Release private data or resources associated with the pattern.
