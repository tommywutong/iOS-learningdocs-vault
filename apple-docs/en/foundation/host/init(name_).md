---
title: 'init(name:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/host/init(name:)'
source_url: 'https://developer.apple.com/documentation/foundation/host/init(name:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/host/init%28name%3A%29.json'
content_hash: 'sha256:491913ebb660d482'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Host](../host.md)

# init(name:)

<sub>Initializer</sub>

Returns a host with a specific name.

> [!warning] Deprecated
> Use Network framework instead, see deprecation notice in \<Foundation/NSHost.h\>

<sub>macOS</sub>

```swift
convenience init(name: String?)
```

## Parameters

- `name` — Name of the host to look up. Can be either a simple hostname, such as `"sales"`, or a fully qualified domain name, such as `"sales.anycorp.com"`.

## Return Value

The host named `hostname`.

## See Also

### Creating Hosts

- [+ currentHost](<current().md>) — Returns an `NSHost` object representing the host the process is running on. _(deprecated)_
- [+ hostWithAddress:](<init(address_).md>) — Returns the `NSHost` with the Internet address `address`. _(deprecated)_
