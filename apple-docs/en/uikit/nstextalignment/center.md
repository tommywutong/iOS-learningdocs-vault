---
title: NSTextAlignment.center
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextalignment/center
source_url: 'https://developer.apple.com/documentation/uikit/nstextalignment/center'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextalignment/center.json'
content_hash: 'sha256:c4b3f26b4ace4819'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAlignment](../nstextalignment.md)

# NSTextAlignment.center

<sub>Case</sub>

Text is center-aligned.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case center
```

## Discussion

The value of this enumeration case is `1` for binaries built for the `arm64` architecture, and running in iOS, macOS, or Simulator. The value is also `1` for binaries built for the `x86_64` architecture and running in Simulator for iOS. However, the value of this enumeration case is `2` for other binaries built for the `x86_64` architecture, including apps translated using Rosetta. If you persist this value manually, make sure to convert it for the appropriate environment when you read it.

For more information about Rosetta, see [About the Rosetta translation environment](../../apple-silicon/about-the-rosetta-translation-environment.md).

## See Also

### Constants

- [NSTextAlignmentLeft](left.md) — Text is left-aligned.
- [NSTextAlignmentRight](right.md) — Text is right-aligned.
- [NSTextAlignmentJustified](justified.md) — Text is justified.
- [NSTextAlignmentNatural](natural.md) — Text uses the default alignment for the current localization of the app.
