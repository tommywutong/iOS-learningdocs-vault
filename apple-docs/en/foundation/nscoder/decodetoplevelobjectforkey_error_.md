---
title: 'decodeTopLevelObjectForKey:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodetoplevelobjectforkey:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodetoplevelobjectforkey:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodetoplevelobjectforkey%3Aerror%3A.json'
content_hash: 'sha256:4b2277a7f568b811'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeTopLevelObjectForKey:error:

<sub>Instance Method</sub>

Decodes the previously-encoded object associated by a key, populating an error if decoding fails.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (id) decodeTopLevelObjectForKey:(NSString *) key error:(NSError **) error;
```

## Parameters

- `key` — The key that identifies the object to decode.

- `error` — An [NSError](../nserror.md) reference. On return, if this value is not `nil`, it represents an error encountered while decoding.

## Return Value

The decoded object, or `nil` if decoding fails.

## See Also

### Decoding Top-Level Objects

- [decodeTopLevelObjectOfClass:forKey:error:](decodetoplevelobjectofclass_forkey_error_.md) — Decode an object as an expected type, failing if the archived type does not match.
- [decodeTopLevelObjectOfClasses:forKey:error:](decodetoplevelobjectofclasses_forkey_error_.md) — Decode an object as one of several expected types, failing if the archived type does not match.
- [decodeTopLevelObjectAndReturnError:](decodetoplevelobjectandreturnerror_.md) — Decodes a previously-encoded object, populating an error if decoding fails.
