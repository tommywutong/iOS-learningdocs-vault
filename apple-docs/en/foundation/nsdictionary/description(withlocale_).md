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
doc_path: '/documentation/foundation/nsdictionary/description(withlocale:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/description(withlocale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/description%28withlocale%3A%29.json'
content_hash: 'sha256:be16d85b649ae4d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# description(withLocale:)

<sub>Instance Method</sub>

Returns a string object that represents the contents of the dictionary, formatted as a property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func description(withLocale locale: Any?) -> String
```

## Parameters

- `locale` — An object that specifies options used for formatting each of the dictionary’s keys and values; pass `nil` if you don’t want them formatted. On iOS and macOS 10.5 and later, either an instance of `NSDictionary` or an `NSLocale` object may be used for `locale`. In OS X v10.4 and earlier it must be an instance of `NSDictionary`.

## Discussion

For a description of how `locale` is applied to each element in the dictionary, see [- descriptionWithLocale:indent:](<description(withlocale_indent_).md>).

If each key in the dictionary responds to `compare:`, the entries are listed in ascending order by key, otherwise the order in which the entries are listed is undefined.

## See Also

### Describing a Dictionary

- [description](description.md) — A string that represents the contents of the dictionary, formatted as a property list.
- [descriptionInStringsFileFormat](descriptioninstringsfileformat.md) — A string that represents the contents of the dictionary, formatted in `.strings` file format.
- [- descriptionWithLocale:indent:](<description(withlocale_indent_).md>) — Returns a string object that represents the contents of the dictionary, formatted as a property list.
