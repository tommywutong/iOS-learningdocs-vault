---
title: NSMachPort
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmachport
source_url: 'https://developer.apple.com/documentation/foundation/nsmachport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachport.json'
content_hash: 'sha256:6d062de28cbfda0a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMachPort

<sub>Class</sub>

A port that can be used as an endpoint for distributed object connections (or raw messaging).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMachPort
```

## Overview

[NSMachPort](nsmachport.md) is a subclass of [Port](port.md) that wraps a Mach port, the fundamental communication port in macOS. [NSMachPort](nsmachport.md) allows for local (on the same machine) communication only. A companion class, [SocketPort](socketport.md), allows for both local and remote distributed object communication, but may be more expensive than [NSMachPort](nsmachport.md) for the local case.

To use [NSMachPort](nsmachport.md) effectively, you should be familiar with Mach ports, port access rights, and Mach messages. See the Mach OS documentation for more information.

> [!note] Note
> [NSMachPort](nsmachport.md) conforms to the [NSCoding](nscoding.md) protocol, but only supports coding by an [NSPortCoder](nsportcoder.md). [Port](port.md) and its subclasses do not support archiving.

## Relationships

- **Inherits From**: [Port](port.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating and Initializing

- [+ portWithMachPort:](<nsmachport/port(withmachport_).md>) — Creates and returns a port object configured with the given Mach port.
- [+ portWithMachPort:options:](<nsmachport/port(withmachport_options_).md>) — Creates and returns a port object configured with the specified options and the given Mach port.
- [- initWithMachPort:](<nsmachport/init(machport_).md>) — Initializes a newly allocated `NSMachPort` object with a given Mach port.
- [- initWithMachPort:options:](<nsmachport/init(machport_options_).md>) — Initializes a newly allocated `NSMachPort` object with a given Mach port and the specified options.

### Getting the Mach Port

- [machPort](nsmachport/machport.md) — The Mach port used by the receiver, represented as an integer.

### Scheduling the Port on a Run Loop

- [- removeFromRunLoop:forMode:](<nsmachport/remove(from_formode_).md>) — Removes the receiver from the run loop mode `mode` of `runLoop`.
- [- scheduleInRunLoop:forMode:](<nsmachport/schedule(in_formode_).md>) — Schedules the receiver into the run loop mode `mode` of `runLoop`.

### Getting and Setting the Delegate

- [- delegate](<nsmachport/delegate().md>) — Returns the receiver’s delegate.
- [- setDelegate:](<nsmachport/setdelegate(__).md>) — Sets the receiver’s delegate to a given object.

### Constants

- [Options](nsmachport/options.md) — Used to remove access rights to a mach port when the `NSMachPort` object is invalidated or destroyed.

## See Also

### Legacy

- [NSMachPortDelegate](nsmachportdelegate.md) — An interface for handling incoming Mach messages.
- [MessagePort](messageport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [PortDelegate](portdelegate.md) — An interface for handling incoming messages.
- [PortMessage](portmessage.md) — A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [NSProtocolChecker](nsprotocolchecker.md) — An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
