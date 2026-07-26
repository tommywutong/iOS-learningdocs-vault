---
title: alternativeInterpretations
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.1+, iPadOS 5.1+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidictationphrase/alternativeinterpretations
source_url: 'https://developer.apple.com/documentation/uikit/uidictationphrase/alternativeinterpretations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidictationphrase/alternativeinterpretations.json'
content_hash: 'sha256:518a2f8221b0d95c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDictationPhrase](../uidictationphrase.md)

# alternativeInterpretations

<sub>Instance Property</sub>

An array of alternative textual interpretations of a dictated phrase.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var alternativeInterpretations: [String]? { get }
```

## Discussion

If the system determines only one textual interpretation of a dictated phrase, the value of this property is `nil`. If there’s more than one interpretation, this property contains an array of strings, with the first being most likely interpretation and the last being the least likely.

## See Also

### Obtaining textual interpretations of spoken text

- [text](text.md) — The most likely textual interpretation of a dictated phrase.
