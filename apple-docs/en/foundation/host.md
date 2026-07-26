---
title: Host
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/host
source_url: 'https://developer.apple.com/documentation/foundation/host'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/host.json'
content_hash: 'sha256:932195a8f014fa91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Host

<sub>Class</sub>

A representation of an individual host on the network.

> [!warning] Deprecated
> Use Network framework instead, see deprecation notice in \<Foundation/NSHost.h\>

<sub>macOS</sub>

```swift
class Host
```

## Overview

The [Host](host.md) class provides methods to access the network name and address information for a host. Instances of the [Host](host.md) class represent individual _hosts_ on a network. Use [Host](host.md) objects  to get the current host’s names and addresses and to look up other hosts by name or by address.

To create an [Host](host.md) object, use the [+ currentHost](<host/current().md>), [+ hostWithAddress:](<host/init(address_).md>), or [+ hostWithName:](<host/init(name_).md>) class methods (don’t use `alloc` and `init`). These methods use available network administration services to discover all names and addresses for the host requested. They don’t attempt to contact the host itself, however. This approach avoids untimely delays due to a host being unavailable, but it may result in incomplete information about the host.

An [Host](host.md) object contains all of the network addresses and names discovered for a given host by the network administration services. Each [Host](host.md) object may contain several addresses and have more than one name. If an [Host](host.md) object has more than one name, the additional names are variations on the same name, typically the basic host name plus the fully qualified domain name. For example, with a host name `"sales"` in the domain `"anycorp.com"`, an [Host](host.md) object can hold both the names `"sales"` and `"sales.anycorp.com"`.

[Host](host.md) methods are thread-safe.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating Hosts

- [+ currentHost](<host/current().md>) — Returns an `NSHost` object representing the host the process is running on. _(deprecated)_
- [+ hostWithAddress:](<host/init(address_).md>) — Returns the `NSHost` with the Internet address `address`. _(deprecated)_
- [+ hostWithName:](<host/init(name_).md>) — Returns a host with a specific name. _(deprecated)_

### Getting Host Information

- [address](host/address.md) — Returns one of the network addresses of the receiver. _(deprecated)_
- [addresses](host/addresses.md) — Returns all the network addresses of the receiver. _(deprecated)_
- [name](host/name.md) — Returns one of the hostnames of the receiver. _(deprecated)_
- [localizedName](host/localizedname.md) — Returns the name used as by default when publishing `NSNetServices`. _(deprecated)_
- [names](host/names.md) — Returns all the hostnames of the receiver. _(deprecated)_

### Comparing Hosts

- [- isEqualToHost:](<host/isequal(to_).md>) — Indicates whether the receiver represents the same host as another `NSHost` object. _(deprecated)_

## See Also

### Sockets

- [Port](port.md) — An abstract class that represents a communication channel.
- [SocketPort](socketport.md) — A port that represents a BSD socket.
