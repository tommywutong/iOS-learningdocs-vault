---
title: 'unarchivedObject(ofClass:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiver/unarchivedobject(ofclass:from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchivedobject(ofclass:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/unarchivedobject%28ofclass%3Afrom%3A%29.json'
content_hash: 'sha256:38b41344ed215159'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# unarchivedObject(ofClass:from:)

<sub>Type Method</sub>

Decodes a previously-archived object graph, and returns the root object as the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc static func unarchivedObject<DecodedObjectType>(ofClass cls: DecodedObjectType.Type, from data: Data) throws -> DecodedObjectType? where DecodedObjectType : NSObject, DecodedObjectType : NSCoding
```

## Parameters

- `cls` — The expected class of the root object.

- `data` — An object graph previously encoded by [NSKeyedArchiver](../nskeyedarchiver.md).

## Return Value

The decoded root of the object graph, or `nil` if an error occurred.

## Discussion

This method produces an error if `data` does not contain valid keyed data.

> [!important] Important
> Make sure you have adopted [NSSecureCoding](../nssecurecoding.md) in the types you decode. If any call to a `decode`-prefixed method fails, the default [decodingFailurePolicy](decodingfailurepolicy.md) sets the error rather than throwing an exception. In this case, the current and all subsequent decode calls return `0` or `nil`.

## See Also

### Unarchiving Data

- [unarchiveTopLevelObjectWithData(_:)](<unarchivetoplevelobjectwithdata(__).md>) — Decodes a previously-archived object graph, and returns the root object.
- [+ unarchivedObjectOfClasses:fromData:error:](<unarchivedobject(ofclasses_from_)-b9t5.md>) — Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [unarchivedObject(ofClasses:from:)](<unarchivedobject(ofclasses_from_)-3h32t.md>) — Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [requiresSecureCoding](requiressecurecoding.md) — Indicates whether the receiver requires all unarchived classes to conform to [NSSecureCoding](../nssecurecoding.md).
- [+ unarchiveObjectWithData:](<unarchiveobject(with_).md>) — Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object. _(deprecated)_
- [+ unarchiveObjectWithFile:](<unarchiveobject(withfile_).md>) — Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path. _(deprecated)_
