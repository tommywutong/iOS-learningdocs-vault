---
title: localizedName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.6+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/host/localizedname
source_url: 'https://developer.apple.com/documentation/foundation/host/localizedname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/host/localizedname.json'
content_hash: 'sha256:257a01700d24bd72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Host](../host.md)

# localizedName

<sub>Instance Property</sub>

Returns the name used as by default when publishing `NSNetServices`.

<sub>macOS</sub>

```swift
var localizedName: String? { get }
```

## Return Value

A string containing the computer name.

## Discussion

This is the name displayed in the Finder sidebar, as well as in the Sharing preference panel.

This method only returns an `NSString` when sent to the [+ currentHost](<current().md>) instance, all other instances currently return `nil`.

This property is key-value observable.

## See Also

### Getting Host Information

- [address](address.md) — Returns one of the network addresses of the receiver. _(deprecated)_
- [addresses](addresses.md) — Returns all the network addresses of the receiver. _(deprecated)_
- [name](name.md) — Returns one of the hostnames of the receiver. _(deprecated)_
- [names](names.md) — Returns all the hostnames of the receiver. _(deprecated)_
