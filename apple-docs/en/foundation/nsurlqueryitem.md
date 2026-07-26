---
title: NSURLQueryItem
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlqueryitem
source_url: 'https://developer.apple.com/documentation/foundation/nsurlqueryitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlqueryitem.json'
content_hash: 'sha256:1d3661de3a85941e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLQueryItem

<sub>Class</sub>

An object representing a single name/value pair for an item in the query portion of a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSURLQueryItem
```

## Overview

In Swift, this object bridges to [URLQueryItem](urlqueryitem.md); use [NSURLQueryItem](nsurlqueryitem.md) when you need reference semantics or other Foundation-specific behavior.

You use query items with the [queryItems](nsurlcomponents/queryitems.md) property of an [NSURLComponents](nsurlcomponents.md) object.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [URLQueryItem](urlqueryitem.md) structure, which bridges to the [NSURLQueryItem](nsurlqueryitem.md) class. For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Query Item

- [- initWithName:value:](<nsurlqueryitem/init(name_value_).md>) — Initializes a newly allocated query item with the specified name and value.

### Reading a Query Item’s Name and Value

- [name](nsurlqueryitem/name.md) — The name of the query item.
- [value](nsurlqueryitem/value.md) — The value for the query item.

### Initializers

- [init(coder:)](<nsurlqueryitem/init(coder_).md>)
