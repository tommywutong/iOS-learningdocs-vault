---
title: 'CFCharacterSetGetPredefined(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetgetpredefined(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetgetpredefined(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetgetpredefined%28_%3A%29.json'
content_hash: 'sha256:e878db84161b5d90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetGetPredefined(_:)

<sub>Function</sub>

Returns a predefined character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetGetPredefined(_ theSetIdentifier: CFCharacterSetPredefinedSet) -> CFCharacterSet!
```

## Parameters

- `theSetIdentifier` — A predefined character set. See [Predefined CFCharacterSet Selector Values](predefined_cfcharacterset_selector_values.md) for the list of available character sets.

## Return Value

A predefined character set. This instance is owned by Core Foundation.
