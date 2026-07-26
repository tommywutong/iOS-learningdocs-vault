---
title: 'init(machPort:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmachport/init(machport:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmachport/init(machport:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachport/init%28machport%3Aoptions%3A%29.json'
content_hash: 'sha256:74cd7c6fc4171334'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachPort](../nsmachport.md)

# init(machPort:options:)

<sub>Initializer</sub>

Initializes a newly allocated `NSMachPort` object with a given Mach port and the specified options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(machPort: UInt32, options f: NSMachPort.Options = [])
```

## Parameters

- `machPort` — The Mach port for the new port. This parameter should originally be of type mach_port_t.

- `f` — Specifies options for what to do with the underlying port rights when the `NSMachPort` object is invalidated or destroyed. For a list of constants, see `Mach Port Rights`.

## Return Value

Returns an initialized `NSMachPort` object that uses `machPort` to send or receive messages. The returned object might be different than the original receiver

## Discussion

Depending on the access rights for `machPort`, the new port may be able to only send messages. If a port with `machPort` already exists, this method deallocates the receiver, then retains and returns the existing port.

## See Also

### Creating and Initializing

- [+ portWithMachPort:](<port(withmachport_).md>) — Creates and returns a port object configured with the given Mach port.
- [+ portWithMachPort:options:](<port(withmachport_options_).md>) — Creates and returns a port object configured with the specified options and the given Mach port.
- [- initWithMachPort:](<init(machport_).md>) — Initializes a newly allocated `NSMachPort` object with a given Mach port.
