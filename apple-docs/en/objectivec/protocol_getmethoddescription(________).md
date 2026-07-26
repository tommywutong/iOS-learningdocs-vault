---
title: 'protocol_getMethodDescription(_:_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/protocol_getmethoddescription(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/protocol_getmethoddescription(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/protocol_getmethoddescription%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:2754e7285b4d73fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# protocol_getMethodDescription(_:_:_:_:)

<sub>Function</sub>

Returns a method description structure for a specified method of a given protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func protocol_getMethodDescription(_ proto: Protocol, _ aSel: Selector, _ isRequiredMethod: Bool, _ isInstanceMethod: Bool) -> objc_method_description
```

## Parameters

- `proto` — A protocol.

- `aSel` — A selector

- `isRequiredMethod` — A Boolean value that indicates whether `aSel` is a required method.

- `isInstanceMethod` — A Boolean value that indicates whether `aSel` is an instance method.

## Return Value

An `objc_method_description` structure that describes the method specified by `aSel`, `isRequiredMethod`, and `isInstanceMethod` for the protocol `p`.

## Discussion

If the protocol does not contain the specified method, returns an `objc_method_description` structure with the value `{NULL, NULL}`.

## See Also

### Working with Protocols

- [objc_getProtocol](<objc_getprotocol(__).md>) — Returns a specified protocol.
- [objc_copyProtocolList](<objc_copyprotocollist(__).md>) — Returns an array of all the protocols known to the runtime.
- [objc_allocateProtocol](<objc_allocateprotocol(__).md>) — Creates a new protocol instance.
- [objc_registerProtocol](<objc_registerprotocol(__).md>) — Registers a newly created protocol with the Objective-C runtime.
- [protocol_addMethodDescription](<protocol_addmethoddescription(__________).md>) — Adds a method to a protocol.
- [protocol_addProtocol](<protocol_addprotocol(____).md>) — Adds a registered protocol to another protocol that is under construction.
- [protocol_addProperty](<protocol_addproperty(____________).md>) — Adds a property to a protocol that is under construction.
- [protocol_getName](<protocol_getname(__).md>) — Returns the name of a protocol.
- [protocol_isEqual](<protocol_isequal(____).md>) — Returns a Boolean value that indicates whether two protocols are equal.
- [protocol_copyMethodDescriptionList](<protocol_copymethoddescriptionlist(________).md>) — Returns an array of method descriptions of methods meeting a given specification for a given protocol.
- [protocol_copyPropertyList](<protocol_copypropertylist(____).md>) — Returns an array of the properties declared by a protocol.
- [protocol_getProperty](<protocol_getproperty(________).md>) — Returns the specified property of a given protocol.
- [protocol_copyProtocolList](<protocol_copyprotocollist(____).md>) — Returns an array of the protocols adopted by a protocol.
- [protocol_conformsToProtocol](<protocol_conformstoprotocol(____).md>) — Returns a Boolean value that indicates whether one protocol conforms to another protocol.
