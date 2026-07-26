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
doc_path: '/documentation/foundation/nscoder/decodetoplevelobject(of:forkey:)-5lnnn'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodetoplevelobject(of:forkey:)-5lnnn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodetoplevelobject%28of%3Aforkey%3A%29-5lnnn.json'
content_hash: 'sha256:5956e9f50e045fa6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeTopLevelObject(of:forKey:)

<sub>Instance Method</sub>

Decode an object as one of several expected types, failing if the archived type does not match.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc func decodeTopLevelObject(of classes: [AnyClass]?, forKey key: String) throws -> Any?
```

## Parameters

- `classes` — An array of expected classes that the object being decoded should match at least one of.

- `key` — The key indicating the member to decode.

## Return Value

The decoded object, or `nil` if decoding fails.

## Discussion

This method is equivalent to [decodeObject(of:forKey:)](<decodeobject(of_forkey_)-7tmft.md>), but allows you to specify a set of classes that the decoded object can match. If [requiresSecureCoding](requiressecurecoding.md) is `true`, the decoded object’s class must be a member of the classes parameter, or a sublcass of a member.

## See Also

### Decoding Top-Level Objects

- [decodeObject(of:forKey:)](<decodeobject(of_forkey_)-7tmft.md>) — Decode an object as an expected type, failing if the archived type doesn’t match.
- [decodeObject(of:forKey:)](<decodeobject(of_forkey_)-roif.md>) — Decode an object as one of several expected types, failing if the archived type doesn’t match any of the types.
- [decodeTopLevelObject()](<decodetoplevelobject().md>) — Decodes a previously-encoded object. _(deprecated)_
- [decodeTopLevelObject(forKey:)](<decodetoplevelobject(forkey_).md>) — Decodes the previously-encoded object associated by a key.
- [decodeTopLevelObject(of:forKey:)](<decodetoplevelobject(of_forkey_)-3w6pd.md>) — Decode an object as one of several expected types, failing if the archived type does not match.
