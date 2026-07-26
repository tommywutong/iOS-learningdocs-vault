---
title: 'localizedString(byJoining:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/listformatter/localizedstring(byjoining:)'
source_url: 'https://developer.apple.com/documentation/foundation/listformatter/localizedstring(byjoining:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/listformatter/localizedstring%28byjoining%3A%29.json'
content_hash: 'sha256:989c7884c37dbd3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ListFormatter](../listformatter.md)

# localizedString(byJoining:)

<sub>Type Method</sub>

Constructs a formatted string from an array of strings that uses the list format specific to the current locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func localizedString(byJoining strings: [String]) -> String
```

## Parameters

- `strings` — An array of strings to join together in a list.

## Return Value

A formatted string that joins together a list of strings using a locale-specific list format.

## Discussion

> [!tip] Tip
> Use this method to join strings that are ready to be displayed in a bullet-point list. Sentences, phrases with punctuations, and appositions may not work well when joined together.

## See Also

### Converting Arrays to Formatted Lists

- [- stringFromItems:](<string(from_).md>) — Creates a formatted string for an array of items.
- [- stringForObjectValue:](<string(for_).md>) — Creates a formatted string for an array of items.
