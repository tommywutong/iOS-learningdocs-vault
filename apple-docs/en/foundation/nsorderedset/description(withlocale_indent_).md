---
title: 'description(withLocale:indent:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/description(withlocale:indent:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/description(withlocale:indent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/description%28withlocale%3Aindent%3A%29.json'
content_hash: 'sha256:26ed0067dac12e3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# description(withLocale:indent:)

<sub>Instance Method</sub>

Returns a string that represents the contents of the ordered set, formatted as a property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func description(withLocale locale: Any?, indent level: Int) -> String
```

## Parameters

- `locale` — An [NSLocale](../nslocale.md) object or an `NSDictionary` object that specifies options used for formatting each of the array’s elements (where recognized). Specify `nil` if you don’t want the elements formatted.

- `level` — Specifies a level of indentation, to make the output more readable: the indentation is (4 spaces) * `level`.

## Return Value

A string that represents the contents of the ordered set, formatted as a property list.

## Discussion

The returned `NSString` object contains the string representations of each of the ordered set’s elements, in order, from first to last. To obtain the string representation of a given element, `descriptionWithLocale:indent:` proceeds as follows:

- If the element is an `NSString` object, it is used as is.
- If the element responds to `descriptionWithLocale:indent:`, that method is invoked to obtain the element’s string representation.
- If the element responds to `descriptionWithLocale:`, that method is invoked to obtain the element’s string representation.
- If none of the above conditions is met, the element’s string representation is obtained by invoking its `description` method

## See Also

### Describing a Set

- [description](description.md) — A string that represents the contents of the ordered set, formatted as a property list.
- [- descriptionWithLocale:](<description(withlocale_).md>) — Returns a string that represents the contents of the ordered set, formatted as a property list.
