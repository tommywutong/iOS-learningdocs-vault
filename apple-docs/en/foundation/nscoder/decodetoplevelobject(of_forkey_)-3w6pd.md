---
title: 'decodeTopLevelObject(of:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodetoplevelobject(of:forkey:)-3w6pd'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodetoplevelobject(of:forkey:)-3w6pd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodetoplevelobject%28of%3Aforkey%3A%29-3w6pd.json'
content_hash: 'sha256:9e916cf717e420c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeTopLevelObject(of:forKey:)

<sub>Instance Method</sub>

Decode an object as one of several expected types, failing if the archived type does not match.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decodeTopLevelObject<DecodedObjectType>(of cls: DecodedObjectType.Type, forKey key: String) throws -> DecodedObjectType? where DecodedObjectType : NSObject, DecodedObjectType : NSCoding
```

## Parameters

- `cls` — The expected class of the object being decoded.

- `key` — The key indicating the member to decode.

## Return Value

The decoded object, or `nil` if decoding fails.

## Discussion

If the coder responds [true](../../swift/true.md) to [requiresSecureCoding](requiressecurecoding.md), then the coder calls [- failWithError:](<failwitherror(__).md>) in either the following cases:

- The class indicated by `cls` does not implement [NSSecureCoding](../nssecurecoding.md).
- The unarchived class does not match `cls`, nor do any of its superclasses.

If the coder does not require secure coding, it ignores the `cls` parameter and does not check the decoded object.

## See Also

### Decoding Top-Level Objects

- [decodeObject(of:forKey:)](<decodeobject(of_forkey_)-7tmft.md>) — Decode an object as an expected type, failing if the archived type doesn’t match.
- [decodeObject(of:forKey:)](<decodeobject(of_forkey_)-roif.md>) — Decode an object as one of several expected types, failing if the archived type doesn’t match any of the types.
- [decodeTopLevelObject()](<decodetoplevelobject().md>) — Decodes a previously-encoded object. _(deprecated)_
- [decodeTopLevelObject(forKey:)](<decodetoplevelobject(forkey_).md>) — Decodes the previously-encoded object associated by a key.
- [decodeTopLevelObject(of:forKey:)](<decodetoplevelobject(of_forkey_)-5lnnn.md>) — Decode an object as one of several expected types, failing if the archived type does not match.
