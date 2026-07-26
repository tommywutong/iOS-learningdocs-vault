---
title: 'decodeObject(of:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodeobject(of:forkey:)-7tmft'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodeobject(of:forkey:)-7tmft'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodeobject%28of%3Aforkey%3A%29-7tmft.json'
content_hash: 'sha256:d1d99400c09ab81c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeObject(of:forKey:)

<sub>Instance Method</sub>

Decode an object as an expected type, failing if the archived type doesn’t match.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decodeObject<DecodedObjectType>(of cls: DecodedObjectType.Type, forKey key: String) -> DecodedObjectType? where DecodedObjectType : NSObject, DecodedObjectType : NSCoding
```

## Parameters

- `cls` — The expected class of the object being decoded.

- `key` — The key indicating the member to decode.

## Return Value

The decoded object, or `nil` if decoding fails.

## Discussion

If the coder responds [true](../../swift/true.md) to [requiresSecureCoding](requiressecurecoding.md), then the coder calls [- failWithError:](<failwitherror(__).md>) in either of the following cases:

- The class indicated by `cls` doesn’t implement [NSSecureCoding](../nssecurecoding.md).
- The unarchived class doesn’t match `cls`, nor do any of its superclasses.

If the coder doesn’t require secure coding, it ignores the `cls` parameter and does not check the decoded object.

## See Also

### Decoding Top-Level Objects

- [decodeObject(of:forKey:)](<decodeobject(of_forkey_)-roif.md>) — Decode an object as one of several expected types, failing if the archived type doesn’t match any of the types.
- [decodeTopLevelObject()](<decodetoplevelobject().md>) — Decodes a previously-encoded object. _(deprecated)_
- [decodeTopLevelObject(forKey:)](<decodetoplevelobject(forkey_).md>) — Decodes the previously-encoded object associated by a key.
- [decodeTopLevelObject(of:forKey:)](<decodetoplevelobject(of_forkey_)-3w6pd.md>) — Decode an object as one of several expected types, failing if the archived type does not match.
- [decodeTopLevelObject(of:forKey:)](<decodetoplevelobject(of_forkey_)-5lnnn.md>) — Decode an object as one of several expected types, failing if the archived type does not match.
