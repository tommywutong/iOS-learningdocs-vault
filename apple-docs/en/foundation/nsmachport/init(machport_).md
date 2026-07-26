---
title: 'init(machPort:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmachport/init(machport:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmachport/init(machport:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachport/init%28machport%3A%29.json'
content_hash: 'sha256:8ed5a94288c6fca9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachPort](../nsmachport.md)

# init(machPort:)

<sub>Initializer</sub>

Initializes a newly allocated `NSMachPort` object with a given Mach port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(machPort: UInt32)
```

## Parameters

- `machPort` — The Mach port for the new port. This parameter should originally be of type mach_port_t.

## Return Value

Returns an initialized `NSMachPort` object that uses `machPort` to send or receive messages. The returned object might be different than the original receiver

## Discussion

Depending on the access rights for `machPort`, the new port may be able to only send messages. If a port with `machPort` already exists, this method deallocates the receiver, then retains and returns the existing port.

This method is the designated initializer for the `NSMachPort` class.

## See Also

### Creating and Initializing

- [+ portWithMachPort:](<port(withmachport_).md>) — Creates and returns a port object configured with the given Mach port.
- [+ portWithMachPort:options:](<port(withmachport_options_).md>) — Creates and returns a port object configured with the specified options and the given Mach port.
- [- initWithMachPort:options:](<init(machport_options_).md>) — Initializes a newly allocated `NSMachPort` object with a given Mach port and the specified options.
