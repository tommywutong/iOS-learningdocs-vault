---
title: 'port(withMachPort:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmachport/port(withmachport:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmachport/port(withmachport:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachport/port%28withmachport%3A%29.json'
content_hash: 'sha256:91140b6e221ace37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachPort](../nsmachport.md)

# port(withMachPort:)

<sub>Type Method</sub>

Creates and returns a port object configured with the given Mach port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func port(withMachPort machPort: UInt32) -> Port
```

## Parameters

- `machPort` — The Mach port for the new port. This parameter should originally be of type mach_port_t.

## Return Value

An `NSMachPort` object that uses `machPort` to send or receive messages.

## Discussion

Creates the port object if necessary. Depending on the access rights associated with `machPort`, the new port object may be usable only for sending messages.

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)

### Creating and Initializing

- [+ portWithMachPort:options:](<port(withmachport_options_).md>) — Creates and returns a port object configured with the specified options and the given Mach port.
- [- initWithMachPort:](<init(machport_).md>) — Initializes a newly allocated `NSMachPort` object with a given Mach port.
- [- initWithMachPort:options:](<init(machport_options_).md>) — Initializes a newly allocated `NSMachPort` object with a given Mach port and the specified options.
