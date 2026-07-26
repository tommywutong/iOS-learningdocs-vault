---
title: 'description(withLocale:indent:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/description(withlocale:indent:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/description(withlocale:indent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/description%28withlocale%3Aindent%3A%29.json'
content_hash: 'sha256:ef1e9b5086e08233'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# description(withLocale:indent:)

<sub>Instance Method</sub>

Returns a string that represents the contents of the array, formatted as a property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func description(withLocale locale: Any?, indent level: Int) -> String
```

## Parameters

- `locale` — An `NSLocale` object or an `NSDictionary` object that specifies options used for formatting each of the array’s elements (where recognized). Specify `nil` if you don’t want the elements formatted.

- `level` — A level of indent, to make the output more readable: set `level` to `0` to use four spaces to indent, or `1` to indent the output with a tab character.

## Return Value

A string that represents the contents of the array, formatted as a property list.

## Discussion

The returned `NSString` object contains the string representations of each of the array’s elements, in order, from first to last. To obtain the string representation of a given element, [- descriptionWithLocale:indent:](<description(withlocale_indent_).md>) proceeds as follows:

- If the element is an `NSString` object, it is used as is.
- If the element responds to [- descriptionWithLocale:indent:](<description(withlocale_indent_).md>), that method is invoked to obtain the element’s string representation.
- If the element responds to [- descriptionWithLocale:](<description(withlocale_).md>), that method is invoked to obtain the element’s string representation.
- If none of the above conditions is met, the element’s string representation is obtained by invoking its [description](description.md) method.

## See Also

### Creating a Description

- [description](description.md) — A string that represents the contents of the array, formatted as a property list.
- [- descriptionWithLocale:](<description(withlocale_).md>) — Returns a string that represents the contents of the array, formatted as a property list.
