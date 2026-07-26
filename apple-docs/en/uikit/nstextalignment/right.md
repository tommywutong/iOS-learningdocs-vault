---
title: NSTextAlignment.right
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextalignment/right
source_url: 'https://developer.apple.com/documentation/uikit/nstextalignment/right'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextalignment/right.json'
content_hash: 'sha256:2fbed4e48bdbfbd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAlignment](../nstextalignment.md)

# NSTextAlignment.right

<sub>Case</sub>

Text is right-aligned.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case right
```

## Discussion

The value of this enumeration case is `2` for binaries built for the `arm64` architecture, and running in iOS, macOS, or Simulator. The value is also `2` for binaries built for the `x86_64` architecture and running in Simulator for iOS. However, the value of this enumeration case is `1` for other binaries built for the `x86_64` architecture, including apps translated using Rosetta. If you persist this value manually, make sure to convert it for the appropriate environment when you read it.

For more information about Rosetta, see [About the Rosetta translation environment](../../apple-silicon/about-the-rosetta-translation-environment.md).

## See Also

### Constants

- [NSTextAlignmentLeft](left.md) — Text is left-aligned.
- [NSTextAlignmentCenter](center.md) — Text is center-aligned.
- [NSTextAlignmentJustified](justified.md) — Text is justified.
- [NSTextAlignmentNatural](natural.md) — Text uses the default alignment for the current localization of the app.
