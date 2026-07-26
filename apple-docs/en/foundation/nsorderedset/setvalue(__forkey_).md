---
title: 'setValue(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/setvalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/setvalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/setvalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:8422a11abf885ee9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# setValue(_:forKey:)

<sub>Instance Method</sub>

Invokes `setValue:forKey:` on each of the receiver’s members using the specified value and key

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: Any?, forKey key: String)
```

## Parameters

- `value` — The object value.

- `key` — The key to store the value.

## See Also

### Key-Value Coding Support

- [- valueForKey:](<value(forkey_).md>) — Returns an ordered set containing the results of invoking `valueForKey:` using key on each of the ordered set’s objects.
