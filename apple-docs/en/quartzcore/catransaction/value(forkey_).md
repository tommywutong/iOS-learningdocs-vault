---
title: 'value(forKey:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransaction/value(forkey:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/value(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/value%28forkey%3A%29.json'
content_hash: 'sha256:434ea99aa76e3c79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# value(forKey:)

<sub>Type Method</sub>

Returns the arbitrary keyed-data specified by the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func value(forKey key: String) -> Any?
```

## Parameters

- `key` — The name of one of the receiver’s properties.

## Return Value

The value for the data specified by the key.

## Discussion

Nested transactions have nested data scope. Requesting a value for a key first searches the innermost scope, then the enclosing transactions.

## See Also

### Getting and Setting Transaction Properties

- [+ setValue:forKey:](<setvalue(__forkey_).md>) — Sets the arbitrary keyed-data for the specified key.
