---
title: 'setValue(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/setvalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/setvalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/setvalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:1be9120471c0ea5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# setValue(_:forKey:)

<sub>Instance Method</sub>

Invokes [- setValue:forKey:](<setvalue(__forkey_).md>) on each of the array’s items using the specified `value` and `key`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: Any?, forKey key: String)
```

## Parameters

- `value` — The object value.

- `key` — The key to store the value.

## See Also

### Key-Value Coding

- [- valueForKey:](<value(forkey_).md>) — Returns an array containing the results of invoking [- valueForKey:](<value(forkey_).md>) using `key` on each of the array’s objects.
