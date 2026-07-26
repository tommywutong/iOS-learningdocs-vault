---
title: uuidString
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuuid/uuidstring
source_url: 'https://developer.apple.com/documentation/foundation/nsuuid/uuidstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuuid/uuidstring.json'
content_hash: 'sha256:53d5960d9bad7a3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUUID](../nsuuid.md)

# uuidString

<sub>Instance Property</sub>

The UUID as a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var uuidString: String { get }
```

## Discussion

A string containing a formatted UUID for example `E621E1F8-C36C-495A-93FC-0C247A3E6E5F`.

Use this property when you need a string representation of the `NSUUID` object—for example, to compare with a [CFUUID](../../corefoundation/cfuuid.md) object.

## See Also

### Get UUID Values

- [- getUUIDBytes:](<getbytes(__).md>) — Returns the UUID as bytes.
