---
title: 'unarchiveTopLevelObjectWithData:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.11+（10.14 起废弃）, tvOS 9.0+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（5.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nskeyedunarchiver/unarchivetoplevelobjectwithdata:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchivetoplevelobjectwithdata:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/unarchivetoplevelobjectwithdata%3Aerror%3A.json'
content_hash: 'sha256:eb8bf275505047d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# unarchiveTopLevelObjectWithData:error:

<sub>Type Method</sub>

Decodes a previously-archived object graph, returning the root object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (id) unarchiveTopLevelObjectWithData:(NSData *) data error:(NSError **) error;
```

## Parameters

- `data` — An object graph previously encoded by [NSKeyedArchiver](../nskeyedarchiver.md).

- `error` — On output, an error encountered during decoding, or `nil` if no error occurred.

## Return Value

The unarchived object, or `nil` if an error occurred.

## Discussion

This method produces an error if `data` does not contain valid keyed data.

## See Also

### Unarchiving Data

- [unarchivedObjectOfClass:fromData:error:](unarchivedobjectofclass_fromdata_error_.md) — Decodes a previously-archived object graph, that returns the root object as the specified type.
- [+ unarchivedObjectOfClasses:fromData:error:](<unarchivedobject(ofclasses_from_)-b9t5.md>) — Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [requiresSecureCoding](requiressecurecoding.md) — Indicates whether the receiver requires all unarchived classes to conform to [NSSecureCoding](../nssecurecoding.md).
- [+ unarchiveObjectWithData:](<unarchiveobject(with_).md>) — Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object. _(deprecated)_
- [+ unarchiveObjectWithFile:](<unarchiveobject(withfile_).md>) — Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path. _(deprecated)_
