---
title: NSStringDrawingOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsstringdrawingoptions
source_url: 'https://developer.apple.com/documentation/uikit/nsstringdrawingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringdrawingoptions.json'
content_hash: 'sha256:534afd5b4a61cb43'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSStringDrawingOptions

<sub>Structure</sub>

Constants that specify the rendering options for drawing a string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct NSStringDrawingOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [NSStringDrawingUsesLineFragmentOrigin](nsstringdrawingoptions/useslinefragmentorigin.md) — Uses the line fragment origin instead of the baseline origin.
- [NSStringDrawingUsesFontLeading](nsstringdrawingoptions/usesfontleading.md) — Uses the font leading for calculating line heights.
- [NSStringDrawingUsesDeviceMetrics](nsstringdrawingoptions/usesdevicemetrics.md) — Uses image glyph bounds instead of typographic bounds.
- [NSStringDrawingTruncatesLastVisibleLine](nsstringdrawingoptions/truncateslastvisibleline.md) — Truncates and adds the ellipsis character to the last visible line if the text doesn’t fit into the specified bounds.

### Initializer

- [init(rawValue:)](<nsstringdrawingoptions/init(rawvalue_).md>) — Creates a structure that specifies the rendering options for drawing a string.

### Type Properties

- [NSStringDrawingOptionsResolvesNaturalAlignmentWithBaseWritingDirection](nsstringdrawingoptions/optionsresolvesnaturalalignmentwithbasewritingdirection.md) — Specifies the behavior for resolving [NSTextAlignmentNatural](nstextalignment/natural.md) to the visual alignment.

## See Also

### Strings

- [NSStringDrawingContext](nsstringdrawingcontext.md) — An object that manages metrics for drawing attributed strings.
- [UIBaselineAdjustment](uibaselineadjustment.md) — Vertical adjustment options.
