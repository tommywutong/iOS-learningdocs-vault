---
title: 'archiver(_:willEncode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedarchiverdelegate/archiver(_:willencode:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/archiver(_:willencode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiverdelegate/archiver%28_%3Awillencode%3A%29.json'
content_hash: 'sha256:e15308f0bd750cac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiverDelegate](../nskeyedarchiverdelegate.md)

# archiver(_:willEncode:)

<sub>Instance Method</sub>

Informs the delegate that `object` is about to be encoded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func archiver(_ archiver: NSKeyedArchiver, willEncode object: Any) -> Any?
```

## Parameters

- `archiver` — The archiver that sent the message.

- `object` — The object that is about to be encoded. This value is never `nil`.

## Return Value

Either `object` or a different object to be encoded in its stead. The delegate can also modify the coder state. If the delegate returns `nil`, `nil` is encoded.

## Discussion

This method is called after the original object may have replaced itself with [replacementObject(for:)](<../../objectivec/nsobject-swift.class/replacementobject(for_)-60vwc.md>):.

This method is called whether or not the object is being encoded conditionally.

This method is not called for an object once a replacement mapping has been set up for that object (either explicitly, or because the object has previously been encoded). This method is also not called when `nil` is about to be encoded.

## See Also

### Encoding Data and Objects

- [- archiver:didEncodeObject:](<archiver(__didencode_).md>) — Informs the delegate that a given object has been encoded.
- [- archiverDidFinish:](<archiverdidfinish(__).md>) — Notifies the delegate that encoding has finished.
- [- archiverWillFinish:](<archiverwillfinish(__).md>) — Notifies the delegate that encoding is about to finish.
- [- archiver:willReplaceObject:withObject:](<archiver(__willreplace_with_).md>) — Informs the delegate that one given object is being substituted for another given object.
