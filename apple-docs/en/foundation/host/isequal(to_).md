---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/host/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/host/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/host/isequal%28to%3A%29.json'
content_hash: 'sha256:1ddc69c1243403f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Host](../host.md)

# isEqual(to:)

<sub>Instance Method</sub>

Indicates whether the receiver represents the same host as another `NSHost` object.

> [!warning] Deprecated
> Use Network framework instead, see deprecation notice in \<Foundation/NSHost.h\>

<sub>macOS</sub>

```swift
func isEqual(to aHost: Host) -> Bool
```

## Parameters

- `aHost` — Host to compare the receiver to.

## Return Value

[true](../../swift/true.md) when the receiver and `host` share at least one network address; [false](../../swift/false.md) otherwise.

## See Also

### Related Documentation

- [addresses](addresses.md) — Returns all the network addresses of the receiver. _(deprecated)_
