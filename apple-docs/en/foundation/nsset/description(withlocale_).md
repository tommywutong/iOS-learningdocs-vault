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
doc_path: '/documentation/foundation/nsset/description(withlocale:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/description(withlocale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/description%28withlocale%3A%29.json'
content_hash: 'sha256:9086d20d47139332'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# description(withLocale:)

<sub>Instance Method</sub>

Returns a string that represents the contents of the set, formatted as a property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func description(withLocale locale: Any?) -> String
```

## Parameters

- `locale` — On iOS and macOS 10.5 and later, either an instance of `NSDictionary` or an `NSLocale` object may be used for `locale`.In OS X v10.4 and earlier it must be an instance of `NSDictionary`.

## Return Value

A string that represents the contents of the set, formatted as a property list.

## Discussion

This method sends each of the set’s members  `descriptionWithLocale:` with `locale` passed as the sole parameter. If the set’s members do not respond to `descriptionWithLocale:`, this method sends [description](../../objectivec/nsobjectprotocol/description.md) instead.

## See Also

### Describing a Set

- [description](description.md) — A string that represents the contents of the set, formatted as a property list.
