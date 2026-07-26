---
title: 'archiver(_:willReplace:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedarchiverdelegate/archiver(_:willreplace:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/archiver(_:willreplace:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiverdelegate/archiver%28_%3Awillreplace%3Awith%3A%29.json'
content_hash: 'sha256:a58d154e569f19b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiverDelegate](../nskeyedarchiverdelegate.md)

# archiver(_:willReplace:with:)

<sub>Instance Method</sub>

Informs the delegate that one given object is being substituted for another given object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func archiver(_ archiver: NSKeyedArchiver, willReplace object: Any?, with newObject: Any?)
```

## Parameters

- `archiver` — The archiver that sent the message.

- `object` — The object being replaced in the archive.

- `newObject` — The object replacing `object` in the archive.

## Discussion

This method is called even when the delegate itself is doing, or has done, the substitution. The delegate may use this method if it is keeping track of the encoded or decoded objects.

## See Also

### Encoding Data and Objects

- [- archiver:didEncodeObject:](<archiver(__didencode_).md>) — Informs the delegate that a given object has been encoded.
- [- archiverDidFinish:](<archiverdidfinish(__).md>) — Notifies the delegate that encoding has finished.
- [- archiver:willEncodeObject:](<archiver(__willencode_).md>) — Informs the delegate that `object` is about to be encoded.
- [- archiverWillFinish:](<archiverwillfinish(__).md>) — Notifies the delegate that encoding is about to finish.
