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
doc_path: '/documentation/foundation/nscoder/decodeobject(of:forkey:)-roif'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodeobject(of:forkey:)-roif'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodeobject%28of%3Aforkey%3A%29-roif.json'
content_hash: 'sha256:d58d9c31d62d684c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeObject(of:forKey:)

<sub>Instance Method</sub>

Decode an object as one of several expected types, failing if the archived type doesn’t match any of the types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc func decodeObject(of classes: [AnyClass]?, forKey key: String) -> Any?
```

## Parameters

- `classes` — An array of expected classes that the object being decoded should match at least one of.

- `key` — The key indicating the member to decode.

## Return Value

The decoded object, or `nil` if decoding fails.

## Discussion

This method is equivalent to [decodeObject(of:forKey:)](<decodeobject(of_forkey_)-7tmft.md>), but accepts a set of classes that the decoded object can match. If [requiresSecureCoding](requiressecurecoding.md) is [true](../../swift/true.md), the decoded object’s class must be a member of the `classes` parameter, or a sublcass of a member.

## See Also

### Decoding Top-Level Objects

- [decodeObject(of:forKey:)](<decodeobject(of_forkey_)-7tmft.md>) — Decode an object as an expected type, failing if the archived type doesn’t match.
- [decodeTopLevelObject()](<decodetoplevelobject().md>) — Decodes a previously-encoded object. _(deprecated)_
- [decodeTopLevelObject(forKey:)](<decodetoplevelobject(forkey_).md>) — Decodes the previously-encoded object associated by a key.
- [decodeTopLevelObject(of:forKey:)](<decodetoplevelobject(of_forkey_)-3w6pd.md>) — Decode an object as one of several expected types, failing if the archived type does not match.
- [decodeTopLevelObject(of:forKey:)](<decodetoplevelobject(of_forkey_)-5lnnn.md>) — Decode an object as one of several expected types, failing if the archived type does not match.
