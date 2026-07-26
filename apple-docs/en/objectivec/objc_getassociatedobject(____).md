---
title: 'objc_getAssociatedObject(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_getassociatedobject(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_getassociatedobject(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_getassociatedobject%28_%3A_%3A%29.json'
content_hash: 'sha256:5b94e5ac2fd3ee6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_getAssociatedObject(_:_:)

<sub>Function</sub>

Returns the value associated with a given object for a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_getAssociatedObject(_ object: Any, _ key: UnsafeRawPointer) -> Any?
```

## Parameters

- `object` — The source object for the association.

- `key` — The key for the association.

## Return Value

The value associated with the key `key` for `object`.

## See Also

### Associative References

- [objc_setAssociatedObject](<objc_setassociatedobject(________).md>) — Sets an associated value for a given object using a given key and association policy.
- [objc_removeAssociatedObjects](<objc_removeassociatedobjects(__).md>) — Removes all associations for a given object.
