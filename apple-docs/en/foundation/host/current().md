---
title: current()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/host/current()
source_url: 'https://developer.apple.com/documentation/foundation/host/current()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/host/current%28%29.json'
content_hash: 'sha256:c8e4073f13806dd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Host](../host.md)

# current()

<sub>Type Method</sub>

Returns an `NSHost` object representing the host the process is running on.

> [!warning] Deprecated
> Use Network framework instead, see deprecation notice in \<Foundation/NSHost.h\>

<sub>macOS</sub>

```swift
class func current() -> Self
```

## Return Value

`NSHost` object for the process’s host.

## Discussion

This method executes synchronously. The execution time of this method can be highly variable, depending on the local network configuration, and may block for several seconds if the network is unreachable. To avoid blocking execution on the main thread, you should call this method in an [Operation](../operation.md) or _Grand Central Dispatch_ block that executes asynchronously in the background.

## See Also

### Creating Hosts

- [+ hostWithAddress:](<init(address_).md>) — Returns the `NSHost` with the Internet address `address`. _(deprecated)_
- [+ hostWithName:](<init(name_).md>) — Returns a host with a specific name. _(deprecated)_
