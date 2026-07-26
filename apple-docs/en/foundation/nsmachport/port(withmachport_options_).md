---
title: 'port(withMachPort:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmachport/port(withmachport:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmachport/port(withmachport:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachport/port%28withmachport%3Aoptions%3A%29.json'
content_hash: 'sha256:0f331899641df3f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachPort](../nsmachport.md)

# port(withMachPort:options:)

<sub>Type Method</sub>

Creates and returns a port object configured with the specified options and the given Mach port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func port(withMachPort machPort: UInt32, options f: NSMachPort.Options = []) -> Port
```

## Parameters

- `machPort` — The Mach port for the new port. This parameter should originally be of type mach_port_t.

- `f` — Specifies options for what to do with the underlying port rights when the `NSMachPort` object is invalidated or destroyed. For a list of constants, see `Mach Port Rights`.

## Return Value

An `NSMachPort` object that uses `machPort` to send or receive messages.

## Discussion

Creates the port object if necessary. Depending on the access rights associated with `machPort`, the new port object may be usable only for sending messages.

## See Also

### Creating and Initializing

- [+ portWithMachPort:](<port(withmachport_).md>) — Creates and returns a port object configured with the given Mach port.
- [- initWithMachPort:](<init(machport_).md>) — Initializes a newly allocated `NSMachPort` object with a given Mach port.
- [- initWithMachPort:options:](<init(machport_options_).md>) — Initializes a newly allocated `NSMachPort` object with a given Mach port and the specified options.
