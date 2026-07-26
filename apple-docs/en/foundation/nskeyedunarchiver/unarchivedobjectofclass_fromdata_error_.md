---
title: 'unarchivedObjectOfClass:fromData:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiver/unarchivedobjectofclass:fromdata:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchivedobjectofclass:fromdata:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/unarchivedobjectofclass%3Afromdata%3Aerror%3A.json'
content_hash: 'sha256:8cb37c75144d5b52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# unarchivedObjectOfClass:fromData:error:

<sub>Type Method</sub>

Decodes a previously-archived object graph, that returns the root object as the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (id) unarchivedObjectOfClass:(Class) cls fromData:(NSData *) data error:(NSError **) error;
```

## Parameters

- `cls` — The expected class of the root object.

- `data` — An object graph previously encoded by [NSKeyedArchiver](../nskeyedarchiver.md).

- `error` — If the return value is `nil`, an [NSError](../nserror.md) indicating why the unarchive operation failed.

## Return Value

The decoded root of the object graph, or `nil` if an error occurred.

## Discussion

This method produces an error if `data` does not contain valid keyed data.

> [!important] Important
> Make sure you have adopted [NSSecureCoding](../nssecurecoding.md) in the types you decode. If any call to a `decode`-prefixed method fails, the default [decodingFailurePolicy](decodingfailurepolicy.md) sets the error rather than throwing an exception. In this case, the current and all subsequent decode calls return `0` or `nil`.

## See Also

### Unarchiving Data

- [+ unarchivedObjectOfClasses:fromData:error:](<unarchivedobject(ofclasses_from_)-b9t5.md>) — Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [requiresSecureCoding](requiressecurecoding.md) — Indicates whether the receiver requires all unarchived classes to conform to [NSSecureCoding](../nssecurecoding.md).
- [+ unarchiveObjectWithData:](<unarchiveobject(with_).md>) — Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object. _(deprecated)_
- [unarchiveTopLevelObjectWithData:error:](unarchivetoplevelobjectwithdata_error_.md) — Decodes a previously-archived object graph, returning the root object. _(deprecated)_
- [+ unarchiveObjectWithFile:](<unarchiveobject(withfile_).md>) — Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path. _(deprecated)_
