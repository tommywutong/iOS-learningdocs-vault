---
title: 'init(address:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/host/init(address:)'
source_url: 'https://developer.apple.com/documentation/foundation/host/init(address:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/host/init%28address%3A%29.json'
content_hash: 'sha256:12c0dd7fe9a57cef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Host](../host.md)

# init(address:)

<sub>Initializer</sub>

Returns the `NSHost` with the Internet address `address`.

> [!warning] Deprecated
> Use Network framework instead, see deprecation notice in \<Foundation/NSHost.h\>

<sub>macOS</sub>

```swift
convenience init(address: String)
```

## Parameters

- `address` — Network address to look up. For example, `"127.0.0.1"` or `"fe80::1"`.

## Return Value

The host for `address`.

## See Also

### Creating Hosts

- [+ currentHost](<current().md>) — Returns an `NSHost` object representing the host the process is running on. _(deprecated)_
- [+ hostWithName:](<init(name_).md>) — Returns a host with a specific name. _(deprecated)_
