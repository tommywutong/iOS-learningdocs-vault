---
title: 'value(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/value(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/value(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/value%28forkey%3A%29.json'
content_hash: 'sha256:611351a8bddccc08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# value(forKey:)

<sub>Instance Method</sub>

Returns an array containing the results of invoking [- valueForKey:](<value(forkey_).md>) using `key` on each of the array’s objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(forKey key: String) -> Any
```

## Parameters

- `key` — The key to retrieve.

## Return Value

The value of the retrieved key.

## Discussion

The returned array contains `NSNull` elements for each object that returns `nil`.

## See Also

### Key-Value Coding

- [- setValue:forKey:](<setvalue(__forkey_).md>) — Invokes [- setValue:forKey:](<setvalue(__forkey_).md>) on each of the array’s items using the specified `value` and `key`.
