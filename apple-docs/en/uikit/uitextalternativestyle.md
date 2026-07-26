---
title: UITextAlternativeStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextalternativestyle
source_url: 'https://developer.apple.com/documentation/uikit/uitextalternativestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextalternativestyle.json'
content_hash: 'sha256:26c9b0ddec2473e7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextAlternativeStyle

<sub>Enumeration</sub>

A constant that determines if the system highlights alternative phrases during text input.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UITextAlternativeStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UITextAlternativeStyleLowConfidence](uitextalternativestyle/lowconfidence.md) — A constant that indicates that the text input should highlight alternatives because the input text may be incorrect.
- [UITextAlternativeStyleNone](uitextalternativestyle/none.md) — A constant that indicates that the text input shouldn’t highlight alternatives because the input text is expected to be correct.

### Initializers

- [init(rawValue:)](<uitextalternativestyle/init(rawvalue_).md>)

## See Also

### Supporting text-phrase alternatives

- [- insertText:alternatives:style:](<uitextinput/inserttext(__alternatives_style_).md>)
