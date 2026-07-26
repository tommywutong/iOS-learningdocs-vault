---
title: decodingFailurePolicy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyedunarchiver/decodingfailurepolicy
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/decodingfailurepolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/decodingfailurepolicy.json'
content_hash: 'sha256:61ad1504fd45c750'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# decodingFailurePolicy

<sub>Instance Property</sub>

The action to take when this unarchiver fails to decode an entry.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var decodingFailurePolicy: NSCoder.DecodingFailurePolicy { get set }
```

## Discussion

The unarchiver may fail to decode an entry for the following reasons:

- The keyed archive data is corrupt or missing.
- A type mismatch occurs, such as expecting a class by calling [decodeObject(of:forKey:)](<../nscoder/decodeobject(of_forkey_)-7tmft.md>), but the unarchiver encounters a numeric value for that key instead. This also occurs when [decodeIntForKey:](decodeintforkey_.md) encounters a value encoded as floating-point, or vice versa.
- A secure coding violation occurs. This happens when attempting to decode an object that doesn’t conform to [NSSecureCoding](../nssecurecoding.md). This also happens when the encoded type doesn’t match any of the classes passed to [+ unarchivedObjectOfClasses:fromData:error:](<unarchivedobject(ofclasses_from_)-b9t5.md>).

## See Also

### Decoding Data

- [- containsValueForKey:](<containsvalue(forkey_).md>) — Returns a Boolean value that indicates whether the archive contains a value for a given key within the current decoding scope.
- [decodeDecodable(_:forKey:)](<decodedecodable(__forkey_).md>) — Decodes a decodable value associated with a given key.
- [decodeTopLevelDecodable(_:forKey:)](<decodetopleveldecodable(__forkey_).md>) — Decodes a top-level decodable value associated with a given key.
- [- decodeBoolForKey:](<decodebool(forkey_).md>) — Decodes a Boolean value associated with a given key.
- [- decodeBytesForKey:returnedLength:](<decodebytes(forkey_returnedlength_).md>) — Decodes a stream of bytes associated with a given key.
- [- decodeDoubleForKey:](<decodedouble(forkey_).md>) — Decodes a double-precision floating-point value associated with a given key.
- [- decodeFloatForKey:](<decodefloat(forkey_).md>) — Decodes a single-precision floating-point value associated with a given key.
- [- decodeInt32ForKey:](<decodeint32(forkey_).md>) — Decodes a 32-bit integer value associated with a given key.
- [- decodeInt64ForKey:](<decodeint64(forkey_).md>) — Decodes a 64-bit integer value associated with a given key.
- [- decodeObjectForKey:](<decodeobject(forkey_).md>) — Decodes and returns an object associated with a given key.
- [- finishDecoding](<finishdecoding().md>) — Tells the receiver that you are finished decoding objects.
