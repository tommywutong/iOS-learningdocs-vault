---
title: 'archiverDidFinish(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedarchiverdelegate/archiverdidfinish(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/archiverdidfinish(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiverdelegate/archiverdidfinish%28_%3A%29.json'
content_hash: 'sha256:9fcd448c802edd99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiverDelegate](../nskeyedarchiverdelegate.md)

# archiverDidFinish(_:)

<sub>Instance Method</sub>

Notifies the delegate that encoding has finished.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func archiverDidFinish(_ archiver: NSKeyedArchiver)
```

## Parameters

- `archiver` — The archiver that sent the message.

## See Also

### Encoding Data and Objects

- [- archiver:didEncodeObject:](<archiver(__didencode_).md>) — Informs the delegate that a given object has been encoded.
- [- archiver:willEncodeObject:](<archiver(__willencode_).md>) — Informs the delegate that `object` is about to be encoded.
- [- archiverWillFinish:](<archiverwillfinish(__).md>) — Notifies the delegate that encoding is about to finish.
- [- archiver:willReplaceObject:withObject:](<archiver(__willreplace_with_).md>) — Informs the delegate that one given object is being substituted for another given object.
