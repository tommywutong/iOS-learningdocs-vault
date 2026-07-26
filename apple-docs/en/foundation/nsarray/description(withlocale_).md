---
title: 'description(withLocale:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/description(withlocale:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/description(withlocale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/description%28withlocale%3A%29.json'
content_hash: 'sha256:c341336b42573e21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# description(withLocale:)

<sub>Instance Method</sub>

Returns a string that represents the contents of the array, formatted as a property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func description(withLocale locale: Any?) -> String
```

## Parameters

- `locale` — An `NSLocale` object or an `NSDictionary` object that specifies options used for formatting each of the array’s elements (where recognized). Specify `nil` if you don’t want the elements formatted.

## Return Value

A string that represents the contents of the array, formatted as a property list.

## Discussion

For a description of how `locale` is applied to each element in the receiving array, see [- descriptionWithLocale:indent:](<description(withlocale_indent_).md>).

## See Also

### Creating a Description

- [description](description.md) — A string that represents the contents of the array, formatted as a property list.
- [- descriptionWithLocale:indent:](<description(withlocale_indent_).md>) — Returns a string that represents the contents of the array, formatted as a property list.
