---
title: 'unarchiveTopLevelObjectWithData(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+（12.0 起废弃）, iPadOS 9.0+（12.0 起废弃）, Mac Catalyst 9.0+（12.0 起废弃）, macOS 10.11+（10.14 起废弃）, tvOS 9.0+（12.0 起废弃）, visionOS 1.0+, watchOS 2.0+（5.0 起废弃）, Swift 4.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nskeyedunarchiver/unarchivetoplevelobjectwithdata(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchivetoplevelobjectwithdata(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/unarchivetoplevelobjectwithdata%28_%3A%29.json'
content_hash: 'sha256:af8e10d27c848d75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# unarchiveTopLevelObjectWithData(_:)

<sub>Type Method</sub>

Decodes a previously-archived object graph, and returns the root object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc class func unarchiveTopLevelObjectWithData(_ data: Data) throws -> Any?
```

## Parameters

- `data` — An object graph previously encoded by [NSKeyedArchiver](../nskeyedarchiver.md).

## Return Value

The unarchived object, or `nil` if an error occurred.

## Discussion

This method throws an error if `data` does not contain valid keyed data.

## See Also

### Unarchiving Data

- [unarchivedObject(ofClass:from:)](<unarchivedobject(ofclass_from_).md>) — Decodes a previously-archived object graph, and returns the root object as the specified type.
- [+ unarchivedObjectOfClasses:fromData:error:](<unarchivedobject(ofclasses_from_)-b9t5.md>) — Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [unarchivedObject(ofClasses:from:)](<unarchivedobject(ofclasses_from_)-3h32t.md>) — Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [requiresSecureCoding](requiressecurecoding.md) — Indicates whether the receiver requires all unarchived classes to conform to [NSSecureCoding](../nssecurecoding.md).
- [+ unarchiveObjectWithData:](<unarchiveobject(with_).md>) — Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object. _(deprecated)_
- [+ unarchiveObjectWithFile:](<unarchiveobject(withfile_).md>) — Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path. _(deprecated)_
