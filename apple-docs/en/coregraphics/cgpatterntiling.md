---
title: CGPatternTiling
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpatterntiling
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpatterntiling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpatterntiling.json'
content_hash: 'sha256:1e3ec3c131b3ac4a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPatternTiling

<sub>Enumeration</sub>

Different methods for rendering a tiled pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGPatternTiling
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGPatternTilingNoDistortion](cgpatterntiling/nodistortion.md) — The pattern cell is not distorted when painted.The spacing between pattern cells may vary by as much as 1 devicepixel.
- [kCGPatternTilingConstantSpacingMinimalDistortion](cgpatterntiling/constantspacingminimaldistortion.md) — Pattern cells are spaced consistently. Thepattern cell may be distorted by as much as 1 device pixel whenthe pattern is painted.
- [kCGPatternTilingConstantSpacing](cgpatterntiling/constantspacing.md) — Pattern cells are spaced consistently, as with [kCGPatternTilingConstantSpacingMinimalDistortion](cgpatterntiling/constantspacingminimaldistortion.md).The pattern cell may be distorted additionally to permit a moreefficient implementation.

### Initializers

- [init(rawValue:)](<cgpatterntiling/init(rawvalue_).md>)
