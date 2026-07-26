---
title: 'description(withLocale:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/description(withlocale:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/description(withlocale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/description%28withlocale%3A%29.json'
content_hash: 'sha256:1d4d20ef77da0ca1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# description(withLocale:)

<sub>Instance Method</sub>

Returns a string that represents the contents of the ordered set, formatted as a property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func description(withLocale locale: Any?) -> String
```

## Parameters

- `locale` — An [NSLocale](../nslocale.md) object or an `NSDictionary` object that specifies options used for formatting each of the ordered set’s elements (where recognized). Specify `nil` if you don’t want the elements formatted.

## Return Value

A string that represents the contents of the ordered set, formatted as a property list.

## Discussion

For a description of how locale is applied to each element in the receiving ordered set, see [- descriptionWithLocale:indent:](<description(withlocale_indent_).md>).

## See Also

### Describing a Set

- [description](description.md) — A string that represents the contents of the ordered set, formatted as a property list.
- [- descriptionWithLocale:indent:](<description(withlocale_indent_).md>) — Returns a string that represents the contents of the ordered set, formatted as a property list.
