---
title: 'protocol_addProperty(_:_:_:_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/protocol_addproperty(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/protocol_addproperty(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/protocol_addproperty%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c65701c9db682e83'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# protocol_addProperty(_:_:_:_:_:_:)

<sub>Function</sub>

Adds a property to a protocol that is under construction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func protocol_addProperty(_ proto: Protocol, _ name: UnsafePointer<CChar>, _ attributes: UnsafePointer<objc_property_attribute_t>?, _ attributeCount: UInt32, _ isRequiredProperty: Bool, _ isInstanceProperty: Bool)
```

## Parameters

- `proto` — The protocol you want to add a property to.

- `name` — The name of the property you want to add.

- `attributes` — An array of property attributes.

- `attributeCount` — The number of properties in `attributes`.

- `isRequiredProperty` — A Boolean indicating whether the property’s accessor methods are required methods of the `proto` protocol. If [YES](yes.md), the property’s accessor methods are required methods; if [NO](no.md), the property’s accessor methods are optional methods.

- `isInstanceProperty` — A Boolean indicating whether the property’s accessor methods are instance methods. If [YES](yes.md), the property’s accessor methods are instance methods. [YES](yes.md) is the only value allowed for a property. As a result, if you set this value to [NO](no.md), the property will not be added to the protocol.

## Discussion

The protocol you want to add the property to must be under construction—allocated but not yet registered with the Objective-C runtime (via the [objc_registerProtocol](<objc_registerprotocol(__).md>) function).

## See Also

### Working with Protocols

- [objc_getProtocol](<objc_getprotocol(__).md>) — Returns a specified protocol.
- [objc_copyProtocolList](<objc_copyprotocollist(__).md>) — Returns an array of all the protocols known to the runtime.
- [objc_allocateProtocol](<objc_allocateprotocol(__).md>) — Creates a new protocol instance.
- [objc_registerProtocol](<objc_registerprotocol(__).md>) — Registers a newly created protocol with the Objective-C runtime.
- [protocol_addMethodDescription](<protocol_addmethoddescription(__________).md>) — Adds a method to a protocol.
- [protocol_addProtocol](<protocol_addprotocol(____).md>) — Adds a registered protocol to another protocol that is under construction.
- [protocol_getName](<protocol_getname(__).md>) — Returns the name of a protocol.
- [protocol_isEqual](<protocol_isequal(____).md>) — Returns a Boolean value that indicates whether two protocols are equal.
- [protocol_copyMethodDescriptionList](<protocol_copymethoddescriptionlist(________).md>) — Returns an array of method descriptions of methods meeting a given specification for a given protocol.
- [protocol_getMethodDescription](<protocol_getmethoddescription(________).md>) — Returns a method description structure for a specified method of a given protocol.
- [protocol_copyPropertyList](<protocol_copypropertylist(____).md>) — Returns an array of the properties declared by a protocol.
- [protocol_getProperty](<protocol_getproperty(________).md>) — Returns the specified property of a given protocol.
- [protocol_copyProtocolList](<protocol_copyprotocollist(____).md>) — Returns an array of the protocols adopted by a protocol.
- [protocol_conformsToProtocol](<protocol_conformstoprotocol(____).md>) — Returns a Boolean value that indicates whether one protocol conforms to another protocol.
