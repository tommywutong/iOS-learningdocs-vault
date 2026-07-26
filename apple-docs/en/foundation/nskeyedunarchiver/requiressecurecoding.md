---
title: requiresSecureCoding
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyedunarchiver/requiressecurecoding
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/requiressecurecoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/requiressecurecoding.json'
content_hash: 'sha256:acf36cd69575a20f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# requiresSecureCoding

<sub>Instance Property</sub>

Indicates whether the receiver requires all unarchived classes to conform to [NSSecureCoding](../nssecurecoding.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var requiresSecureCoding: Bool { get set }
```

## Parameters

- `flag` — [true](../../swift/true.md) if the receiver requires [NSSecureCoding](../nssecurecoding.md); [false](../../swift/false.md) if not.

## Discussion

If you set the receiver to require secure coding, it will throw an exception if you attempt to unarchive a class which does not conform to [NSSecureCoding](../nssecurecoding.md).

The secure coding requirement for [NSKeyedUnarchiver](../nskeyedunarchiver.md) is designed to be set once at the top level and remain on. Once enabled, attempting to call `setRequiresSecureCoding:` with a value of [false](../../swift/false.md) will throw an exception. This is to prevent classes from selectively turning secure coding off.

Note that the getter is on the superclass, [NSCoder](../nscoder.md). See [NSCoder](../nscoder.md) for more information about secure coding.

## See Also

### Unarchiving Data

- [unarchiveTopLevelObjectWithData(_:)](<unarchivetoplevelobjectwithdata(__).md>) — Decodes a previously-archived object graph, and returns the root object.
- [unarchivedObject(ofClass:from:)](<unarchivedobject(ofclass_from_).md>) — Decodes a previously-archived object graph, and returns the root object as the specified type.
- [+ unarchivedObjectOfClasses:fromData:error:](<unarchivedobject(ofclasses_from_)-b9t5.md>) — Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [unarchivedObject(ofClasses:from:)](<unarchivedobject(ofclasses_from_)-3h32t.md>) — Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [+ unarchiveObjectWithData:](<unarchiveobject(with_).md>) — Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object. _(deprecated)_
- [+ unarchiveObjectWithFile:](<unarchiveobject(withfile_).md>) — Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path. _(deprecated)_
