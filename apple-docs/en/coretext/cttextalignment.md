---
title: CTTextAlignment
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/cttextalignment
source_url: 'https://developer.apple.com/documentation/coretext/cttextalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttextalignment.json'
content_hash: 'sha256:67334276ac286d16'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTTextAlignment

<sub>Enumeration</sub>

Constants that specify text alignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTTextAlignment
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCTTextAlignmentLeft](cttextalignment/left.md) — Text is visually left-aligned.
- [kCTTextAlignmentRight](cttextalignment/right.md) — Text is visually right-aligned.
- [kCTTextAlignmentCenter](cttextalignment/center.md) — Text is visually center-aligned.
- [kCTTextAlignmentJustified](cttextalignment/justified.md) — Text is fully justified.
- [kCTTextAlignmentNatural](cttextalignment/natural.md) — Text uses the natural alignment of the text’s script.

### Initializers

- [init(_:)](<cttextalignment/init(__).md>) — Converts a UIKit text alignment constant value to the matching constant value that Core Text uses.
- [init(rawValue:)](<cttextalignment/init(rawvalue_).md>)

### Deprecated

- [kCTLeftTextAlignment](cttextalignment/kctlefttextalignment.md) — Text is visually left-aligned. _(deprecated)_
- [kCTRightTextAlignment](cttextalignment/kctrighttextalignment.md) — Text is visually right-aligned. _(deprecated)_
- [kCTCenterTextAlignment](cttextalignment/kctcentertextalignment.md) — Text is visually center-aligned. _(deprecated)_
- [kCTJustifiedTextAlignment](cttextalignment/kctjustifiedtextalignment.md) — Text is fully justified. _(deprecated)_
- [kCTNaturalTextAlignment](cttextalignment/kctnaturaltextalignment.md) — Text uses the natural alignment of the text’s script. _(deprecated)_

## See Also

### Constants

- [CTLineBreakMode](ctlinebreakmode.md) — These constants specify what happens when a line is too long for its frame.
- [CTWritingDirection](ctwritingdirection.md) — These constants specify the writing direction.
- [CTParagraphStyleSpecifier](ctparagraphstylespecifier.md) — Constants used to query and modify a paragraph style object.
