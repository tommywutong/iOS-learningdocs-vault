---
title: CGPatternTiling.constantSpacingMinimalDistortion
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpatterntiling/constantspacingminimaldistortion
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpatterntiling/constantspacingminimaldistortion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpatterntiling/constantspacingminimaldistortion.json'
content_hash: 'sha256:037f4733d64c7c52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPatternTiling](../cgpatterntiling.md)

# CGPatternTiling.constantSpacingMinimalDistortion

<sub>Case</sub>

Pattern cells are spaced consistently. Thepattern cell may be distorted by as much as 1 device pixel whenthe pattern is painted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case constantSpacingMinimalDistortion
```

## See Also

### Constants

- [kCGPatternTilingNoDistortion](nodistortion.md) — The pattern cell is not distorted when painted.The spacing between pattern cells may vary by as much as 1 devicepixel.
- [kCGPatternTilingConstantSpacing](constantspacing.md) — Pattern cells are spaced consistently, as with [kCGPatternTilingConstantSpacingMinimalDistortion](constantspacingminimaldistortion.md).The pattern cell may be distorted additionally to permit a moreefficient implementation.
