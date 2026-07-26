---
title: 'objc_allocateProtocol(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_allocateprotocol(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_allocateprotocol(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_allocateprotocol%28_%3A%29.json'
content_hash: 'sha256:33b7e96c838027ea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_allocateProtocol(_:)

<sub>Function</sub>

Creates a new protocol instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_allocateProtocol(_ name: UnsafePointer<CChar>) -> Protocol?
```

## Parameters

- `name` — The name of the protocol you want to create.

## Return Value

A new protocol instance or `nil` if a protocol with the same name as `name` already exists.

## Discussion

You must register the returned protocol instance with the [objc_registerProtocol](<objc_registerprotocol(__).md>) function before you can use it.

There is no dispose method associated with this function.

## See Also

### Working with Protocols

- [objc_getProtocol](<objc_getprotocol(__).md>) — Returns a specified protocol.
- [objc_copyProtocolList](<objc_copyprotocollist(__).md>) — Returns an array of all the protocols known to the runtime.
- [objc_registerProtocol](<objc_registerprotocol(__).md>) — Registers a newly created protocol with the Objective-C runtime.
- [protocol_addMethodDescription](<protocol_addmethoddescription(__________).md>) — Adds a method to a protocol.
- [protocol_addProtocol](<protocol_addprotocol(____).md>) — Adds a registered protocol to another protocol that is under construction.
- [protocol_addProperty](<protocol_addproperty(____________).md>) — Adds a property to a protocol that is under construction.
- [protocol_getName](<protocol_getname(__).md>) — Returns the name of a protocol.
- [protocol_isEqual](<protocol_isequal(____).md>) — Returns a Boolean value that indicates whether two protocols are equal.
- [protocol_copyMethodDescriptionList](<protocol_copymethoddescriptionlist(________).md>) — Returns an array of method descriptions of methods meeting a given specification for a given protocol.
- [protocol_getMethodDescription](<protocol_getmethoddescription(________).md>) — Returns a method description structure for a specified method of a given protocol.
- [protocol_copyPropertyList](<protocol_copypropertylist(____).md>) — Returns an array of the properties declared by a protocol.
- [protocol_getProperty](<protocol_getproperty(________).md>) — Returns the specified property of a given protocol.
- [protocol_copyProtocolList](<protocol_copyprotocollist(____).md>) — Returns an array of the protocols adopted by a protocol.
- [protocol_conformsToProtocol](<protocol_conformstoprotocol(____).md>) — Returns a Boolean value that indicates whether one protocol conforms to another protocol.
