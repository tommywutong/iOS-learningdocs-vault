---
title: NSObjectProtocol
framework: Objective-C Runtime
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobjectprotocol
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol.json'
content_hash: 'sha256:1f6e7dd8fa85bbb9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# NSObjectProtocol

<sub>Protocol</sub>

The group of methods that are fundamental to all Objective-C objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSObjectProtocol
```

## Overview

> [!note] Note
> This protocol is imported into Swift with the name `NSObjectProtocol`.

An object that conforms to this protocol can be considered a first-class object. Such an object can be asked about its:

- Class, and the place of its class in the inheritance hierarchy.
- Conformance to protocols.
- Ability to respond to a particular message.

The Cocoa root class [NSObject](nsobject-swift.class.md) adopts this protocol, so all objects inheriting from [NSObject](nsobject-swift.class.md) have the features described by this protocol.

## Relationships

- **Conforming Types**: [NSObject](nsobject-swift.class.md)

## Topics

### Identifying Classes

- [superclass](nsobjectprotocol/superclass.md) — Returns the class object for the receiver’s superclass.

### Identifying and Comparing Objects

- [- isEqual:](<nsobjectprotocol/isequal(__).md>) — Returns a Boolean value that indicates whether the receiver and a given object are equal.
- [hash](nsobjectprotocol/hash.md) — Returns an integer that can be used as a table address in a hash table structure.
- [- self](<nsobjectprotocol/self().md>) — Returns the receiver.

### Testing Object Inheritance, Behavior, and Conformance

- [- isKindOfClass:](<nsobjectprotocol/iskind(of_).md>) — Returns a Boolean value that indicates whether the receiver is an instance of given class or an instance of any class that inherits from that class.
- [- isMemberOfClass:](<nsobjectprotocol/ismember(of_).md>) — Returns a Boolean value that indicates whether the receiver is an instance of a given class.
- [- respondsToSelector:](<nsobjectprotocol/responds(to_).md>) — Returns a Boolean value that indicates whether the receiver implements or inherits a method that can respond to a specified message.
- [- conformsToProtocol:](<nsobjectprotocol/conforms(to_).md>) — Returns a Boolean value that indicates whether the receiver conforms to a given protocol.

### Describing Objects

- [description](nsobjectprotocol/description.md) — A textual representation of the receiver.
- [debugDescription](nsobjectprotocol/debugdescription.md) — A textual representation of the receiver to use with a debugger.

### Sending Messages

- [- performSelector:](<nsobjectprotocol/perform(__).md>) — Sends a specified message to the receiver and returns the result of the message.
- [- performSelector:withObject:](<nsobjectprotocol/perform(__with_).md>) — Sends a message to the receiver with an object as the argument.
- [- performSelector:withObject:withObject:](<nsobjectprotocol/perform(__with_with_).md>) — Sends a message to the receiver with two objects as arguments.

### Identifying Proxies

- [- isProxy](<nsobjectprotocol/isproxy().md>) — Returns a Boolean value that indicates whether the receiver does not descend from [NSObject](nsobject-swift.class.md).
