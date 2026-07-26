---
title: 'add(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscountedset/add(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscountedset/add(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscountedset/add%28_%3A%29.json'
content_hash: 'sha256:fd7ab0e51cef8de1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCountedSet](../nscountedset.md)

# add(_:)

<sub>Instance Method</sub>

Adds a given object to the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func add(_ object: Any)
```

## Parameters

- `object` — The object to add to the set.

## Discussion

If `object` is already a member, [- addObject:](<add(__).md>) increments the count associated with the object. If `object` is not already a member, it is sent a [retain](../../objectivec/nsobject-c.protocol/retain.md) message.

## See Also

### Adding and Removing Entries

- [- removeObject:](<remove(__).md>) — Removes a given object from the set.
