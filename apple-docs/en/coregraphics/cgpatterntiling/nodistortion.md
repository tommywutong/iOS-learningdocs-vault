---
title: CGPatternTiling.noDistortion
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpatterntiling/nodistortion
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpatterntiling/nodistortion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpatterntiling/nodistortion.json'
content_hash: 'sha256:b3d35abafa1ee095'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPatternTiling](../cgpatterntiling.md)

# CGPatternTiling.noDistortion

<sub>Case</sub>

The pattern cell is not distorted when painted.The spacing between pattern cells may vary by as much as 1 devicepixel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case noDistortion
```

## See Also

### Constants

- [kCGPatternTilingConstantSpacingMinimalDistortion](constantspacingminimaldistortion.md) — Pattern cells are spaced consistently. Thepattern cell may be distorted by as much as 1 device pixel whenthe pattern is painted.
- [kCGPatternTilingConstantSpacing](constantspacing.md) — Pattern cells are spaced consistently, as with [kCGPatternTilingConstantSpacingMinimalDistortion](constantspacingminimaldistortion.md).The pattern cell may be distorted additionally to permit a moreefficient implementation.
