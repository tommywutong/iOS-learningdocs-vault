---
title: 'objc_setAssociatedObject(_:_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_setassociatedobject(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_setassociatedobject(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_setassociatedobject%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ec8a92c4a7db7a75'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_setAssociatedObject(_:_:_:_:)

<sub>Function</sub>

Sets an associated value for a given object using a given key and association policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_setAssociatedObject(_ object: Any, _ key: UnsafeRawPointer, _ value: Any?, _ policy: objc_AssociationPolicy)
```

## Parameters

- `object` — The source object for the association.

- `key` — The key for the association.

- `value` — The value to associate with the key `key` for `object`. Pass `nil` to clear an existing association.

- `policy` — The policy for the association. For possible values, see [objc_AssociationPolicy](objc_associationpolicy.md).

## See Also

### Associative References

- [objc_getAssociatedObject](<objc_getassociatedobject(____).md>) — Returns the value associated with a given object for a given key.
- [objc_removeAssociatedObjects](<objc_removeassociatedobjects(__).md>) — Removes all associations for a given object.
