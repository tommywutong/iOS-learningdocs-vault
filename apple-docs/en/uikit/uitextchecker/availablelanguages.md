---
title: availableLanguages
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextchecker/availablelanguages
source_url: 'https://developer.apple.com/documentation/uikit/uitextchecker/availablelanguages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextchecker/availablelanguages.json'
content_hash: 'sha256:b111f27e03f30165'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextChecker](../uitextchecker.md)

# availableLanguages

<sub>Type Property</sub>

Returns the languages that the text checker’s class can perform spell-checking for.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var availableLanguages: [String] { get }
```

## Return Value

An array of strings representing ISO 639-1 language codes or combined ISO 639-1 language codes and ISO 3166-1 regional codes (for example, `en_US`).

## Discussion

The languages represented by the strings in the returned array are in user-preference order.
