---
title: 'string(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/listformatter/string(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/listformatter/string(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/listformatter/string%28for%3A%29.json'
content_hash: 'sha256:87326d9347dd22d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ListFormatter](../listformatter.md)

# string(for:)

<sub>Instance Method</sub>

Creates a formatted string for an array of items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(for obj: Any?) -> String?
```

## Parameters

- `obj` — An array of objects to format as a list.

## Return Value

A formatted string representing the list of objects in an array. Returns `nil` if the formatter can’t generate a description for all objects in the array, or if `obj` is `nil`.

## Discussion

The list formatter uses [itemFormatter](itemformatter.md) to format each item in the array. If [itemFormatter](itemformatter.md) doesn’t apply to a particular item, the list formatter falls back to the item’s [- descriptionWithLocale:](<../nsarray/description(withlocale_).md>) or [localizedDescription](../progress/localizeddescription.md) if implemented. If those methods aren’t implemented, the formatter uses [description](../../objectivec/nsobjectprotocol/description.md) instead.

## See Also

### Converting Arrays to Formatted Lists

- [- stringFromItems:](<string(from_).md>) — Creates a formatted string for an array of items.
- [+ localizedStringByJoiningStrings:](<localizedstring(byjoining_).md>) — Constructs a formatted string from an array of strings that uses the list format specific to the current locale.
