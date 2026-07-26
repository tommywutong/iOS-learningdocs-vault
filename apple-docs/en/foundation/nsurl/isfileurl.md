---
title: isFileURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/isfileurl
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/isfileurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/isfileurl.json'
content_hash: 'sha256:d09124dcf5523812'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# isFileURL

<sub>Instance Property</sub>

A boolean value that determines whether the receiver is a file URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isFileURL: Bool { get }
```

## Discussion

The property’s value is  [true](../../swift/true.md) if the receiver uses the file scheme, [false](../../swift/false.md) otherwise. Both file path and file reference URLs are considered to be file URLs.

If this property’s value is [true](../../swift/true.md), then the receiver’s [path](path.md) property contains a suitable value for input into [FileManager](../filemanager.md) or `NSPathUtilities`.

## See Also

### Querying an NSURL

- [- checkResourceIsReachableAndReturnError:](<checkresourceisreachableandreturnerror(__).md>) — Returns whether the resource pointed to by a file URL can be reached.
- [- isFileReferenceURL](<isfilereferenceurl().md>) — Returns whether the URL is a file reference URL.
