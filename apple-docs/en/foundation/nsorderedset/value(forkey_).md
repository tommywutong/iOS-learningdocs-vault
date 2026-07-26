---
title: 'value(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/value(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/value(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/value%28forkey%3A%29.json'
content_hash: 'sha256:79c090e847fe17d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# value(forKey:)

<sub>Instance Method</sub>

Returns an ordered set containing the results of invoking `valueForKey:` using key on each of the ordered set’s objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(forKey key: String) -> Any
```

## Parameters

- `key` — The key to retrieve.

## Return Value

The ordered set of the values for the retrieved key. The returned ordered set might not have the same number of members as the receiver.

## Discussion

The returned ordered set will not contain any elements corresponding to instances of `valueForKey:` returning `nil`, nor will it contain duplicates.

## See Also

### Key-Value Coding Support

- [- setValue:forKey:](<setvalue(__forkey_).md>) — Invokes `setValue:forKey:` on each of the receiver’s members using the specified value and key
