---
title: 'archiver(_:didEncode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedarchiverdelegate/archiver(_:didencode:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/archiver(_:didencode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiverdelegate/archiver%28_%3Adidencode%3A%29.json'
content_hash: 'sha256:ede47e699ed1a004'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiverDelegate](../nskeyedarchiverdelegate.md)

# archiver(_:didEncode:)

<sub>Instance Method</sub>

Informs the delegate that a given object has been encoded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func archiver(_ archiver: NSKeyedArchiver, didEncode object: Any?)
```

## Parameters

- `archiver` — The archiver that sent the message.

- `object` — The object that has been encoded. `object` may be `nil`.

## Discussion

The delegate might restore some state it had modified previously, or use this opportunity to keep track of the objects that are encoded.

This method is not called for conditional objects until they are actually encoded (if ever).

## See Also

### Related Documentation

- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)

### Encoding Data and Objects

- [- archiverDidFinish:](<archiverdidfinish(__).md>) — Notifies the delegate that encoding has finished.
- [- archiver:willEncodeObject:](<archiver(__willencode_).md>) — Informs the delegate that `object` is about to be encoded.
- [- archiverWillFinish:](<archiverwillfinish(__).md>) — Notifies the delegate that encoding is about to finish.
- [- archiver:willReplaceObject:withObject:](<archiver(__willreplace_with_).md>) — Informs the delegate that one given object is being substituted for another given object.
