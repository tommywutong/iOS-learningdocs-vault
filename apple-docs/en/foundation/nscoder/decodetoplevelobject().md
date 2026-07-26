---
title: decodeTopLevelObject()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 9.0+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nscoder/decodetoplevelobject()
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodetoplevelobject()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodetoplevelobject%28%29.json'
content_hash: 'sha256:5cca575f2c96859c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeTopLevelObject()

<sub>Instance Method</sub>

Decodes a previously-encoded object.

> [!warning] Deprecated
> Use decodeTopLevelObject(of:forKey:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc func decodeTopLevelObject() throws -> Any?
```

## Return Value

The decoded object, or `nil` if decoding fails.

## See Also

### Decoding Top-Level Objects

- [decodeObject(of:forKey:)](<decodeobject(of_forkey_)-7tmft.md>) — Decode an object as an expected type, failing if the archived type doesn’t match.
- [decodeObject(of:forKey:)](<decodeobject(of_forkey_)-roif.md>) — Decode an object as one of several expected types, failing if the archived type doesn’t match any of the types.
- [decodeTopLevelObject(forKey:)](<decodetoplevelobject(forkey_).md>) — Decodes the previously-encoded object associated by a key.
- [decodeTopLevelObject(of:forKey:)](<decodetoplevelobject(of_forkey_)-3w6pd.md>) — Decode an object as one of several expected types, failing if the archived type does not match.
- [decodeTopLevelObject(of:forKey:)](<decodetoplevelobject(of_forkey_)-5lnnn.md>) — Decode an object as one of several expected types, failing if the archived type does not match.
