---
title: 'objc_removeAssociatedObjects(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_removeassociatedobjects(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_removeassociatedobjects(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_removeassociatedobjects%28_%3A%29.json'
content_hash: 'sha256:91c881c40de788ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_removeAssociatedObjects(_:)

<sub>Function</sub>

Removes all associations for a given object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_removeAssociatedObjects(_ object: Any)
```

## Parameters

- `object` — An object that maintains associated objects.

## Discussion

The main purpose of this function is to make it easy to return an object to a “pristine state”. You should not use this function for general removal of associations from objects, since it also removes associations that other clients may have added to the object. Typically you should use [objc_setAssociatedObject](<objc_setassociatedobject(________).md>) with a `nil` value to clear an association.

## See Also

### Associative References

- [objc_setAssociatedObject](<objc_setassociatedobject(________).md>) — Sets an associated value for a given object using a given key and association policy.
- [objc_getAssociatedObject](<objc_getassociatedobject(____).md>) — Returns the value associated with a given object for a given key.
