---
title: 'unarchiveObject(withFile:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.14 起废弃）, tvOS 9.0+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（5.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nskeyedunarchiver/unarchiveobject(withfile:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchiveobject(withfile:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/unarchiveobject%28withfile%3A%29.json'
content_hash: 'sha256:4d0a1998c456a50c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# unarchiveObject(withFile:)

<sub>Type Method</sub>

Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path.

> [!warning] Deprecated
> Use +unarchivedObjectOfClass:fromData:error: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func unarchiveObject(withFile path: String) -> Any?
```

## Parameters

- `path` — A path to a file that contains an object graph previously encoded by `NSKeyedArchiver`.

## Return Value

The object graph previously encoded by `NSKeyedArchiver` written to the file `path`. Returns `nil` if there is no file at `path`.

## Discussion

This method raises an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md) if the file at `path` does not contain a valid archive.

## See Also

### Unarchiving Data

- [unarchiveTopLevelObjectWithData(_:)](<unarchivetoplevelobjectwithdata(__).md>) — Decodes a previously-archived object graph, and returns the root object.
- [unarchivedObject(ofClass:from:)](<unarchivedobject(ofclass_from_).md>) — Decodes a previously-archived object graph, and returns the root object as the specified type.
- [+ unarchivedObjectOfClasses:fromData:error:](<unarchivedobject(ofclasses_from_)-b9t5.md>) — Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [unarchivedObject(ofClasses:from:)](<unarchivedobject(ofclasses_from_)-3h32t.md>) — Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [requiresSecureCoding](requiressecurecoding.md) — Indicates whether the receiver requires all unarchived classes to conform to [NSSecureCoding](../nssecurecoding.md).
- [+ unarchiveObjectWithData:](<unarchiveobject(with_).md>) — Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object. _(deprecated)_
