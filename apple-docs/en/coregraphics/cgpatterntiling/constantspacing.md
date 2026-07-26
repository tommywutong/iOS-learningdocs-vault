---
title: CGPatternTiling.constantSpacing
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpatterntiling/constantspacing
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpatterntiling/constantspacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpatterntiling/constantspacing.json'
content_hash: 'sha256:59289d913d3611b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPatternTiling](../cgpatterntiling.md)

# CGPatternTiling.constantSpacing

<sub>Case</sub>

Pattern cells are spaced consistently, as with [kCGPatternTilingConstantSpacingMinimalDistortion](constantspacingminimaldistortion.md).The pattern cell may be distorted additionally to permit a moreefficient implementation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case constantSpacing
```

## See Also

### Constants

- [kCGPatternTilingNoDistortion](nodistortion.md) — The pattern cell is not distorted when painted.The spacing between pattern cells may vary by as much as 1 devicepixel.
- [kCGPatternTilingConstantSpacingMinimalDistortion](constantspacingminimaldistortion.md) — Pattern cells are spaced consistently. Thepattern cell may be distorted by as much as 1 device pixel whenthe pattern is painted.
