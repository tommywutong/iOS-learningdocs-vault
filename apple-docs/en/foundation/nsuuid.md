---
title: NSUUID
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuuid
source_url: 'https://developer.apple.com/documentation/foundation/nsuuid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuuid.json'
content_hash: 'sha256:454c4f8ccdcc5ecc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUUID

<sub>Class</sub>

A universally unique value that can be used to identify types, interfaces, and other items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSUUID
```

## Overview

In Swift, this object bridges to [UUID](nsuuid/uuid.md); use [NSUUID](nsuuid.md) when you need reference semantics or other Foundation-specific behavior.

UUIDs (Universally Unique Identifiers), also known as GUIDs (Globally Unique Identifiers) or IIDs (Interface Identifiers), are 128-bit values. UUIDs created by `NSUUID` conform to RFC 4122 version 4 and are created with random bytes.

The standard format for UUIDs represented in ASCII is a string punctuated by hyphens, for example `68753A44-4D6F-1226-9C60-0050E4C00067`. The hex representation looks, as you might expect, like a list of numerical values preceded by 0x. For example, `0xD7`, `0x36`, `0x95`, `0x0A`, `0x4D`, `0x6E`, `0x12`, `0x26`, `0x80`, `0x3A`, `0x00`, `0x50`, `0xE4`, `0xC0`, `0x00`, `0x67`. Because a UUID is expressed simply as an array of bytes, there are no endianness considerations for different platforms.

The `NSUUID` class is _not_ toll-free bridged with CoreFoundation’s [CFUUID](../corefoundation/cfuuid.md). Use UUID strings to convert between `CFUUIDRef` and `NSUUID`, if needed. Two `NSUUID` objects are not guaranteed to be comparable by pointer value (as [CFUUID](../corefoundation/cfuuid.md) is); use [isEqual(_:)](<../objectivec/nsobjectprotocol/isequal(__).md>) to compare two `NSUUID` instances.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [UUID](nsuuid/uuid.md) structure, which bridges to the [NSUUID](nsuuid.md) class. For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating UUIDs

- [- init](<nsuuid/init().md>) — Initializes a new UUID with RFC 4122 version 4 random bytes.
- [- initWithUUIDString:](<nsuuid/init(uuidstring_)-8t9n3.md>) — Initializes a new UUID with the formatted string.
- [- initWithUUIDBytes:](<nsuuid/init(uuidbytes_)-2p4d5.md>) — Initializes a new UUID with the given bytes.

### Get UUID Values

- [- getUUIDBytes:](<nsuuid/getbytes(__).md>) — Returns the UUID as bytes.
- [UUIDString](nsuuid/uuidstring.md) — The UUID as a string.

### Initializers

- [init(UUIDBytes:)](<nsuuid/init(uuidbytes_)-4fntq.md>)
- [init(UUIDString:)](<nsuuid/init(uuidstring_)-8kcx.md>)
- [init(coder:)](<nsuuid/init(coder_).md>)

### Instance Methods

- [- compare:](<nsuuid/compare(__).md>) — Compares the receiver to another NSUUID in constant time.
