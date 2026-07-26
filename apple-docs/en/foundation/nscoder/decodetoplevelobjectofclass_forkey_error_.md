---
title: 'decodeTopLevelObjectOfClass:forKey:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodetoplevelobjectofclass:forkey:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodetoplevelobjectofclass:forkey:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodetoplevelobjectofclass%3Aforkey%3Aerror%3A.json'
content_hash: 'sha256:f6f32172e21046af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeTopLevelObjectOfClass:forKey:error:

<sub>Instance Method</sub>

Decode an object as an expected type, failing if the archived type does not match.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (id) decodeTopLevelObjectOfClass:(Class) aClass forKey:(NSString *) key error:(NSError **) error;
```

## Parameters

- `aClass` — The expected class of the object being decoded.

- `key` — The archive key indicating the member to decode.

- `error` — On return, an [NSError](../nserror.md) indicating why decoding failed, or `nil` if no error occurred.

## Return Value

The decoded object, or `nil` if decoding fails.

## Discussion

If the coder responds [true](../../swift/true.md) to [requiresSecureCoding](requiressecurecoding.md), then the coder calls [- failWithError:](<failwitherror(__).md>) in either the following cases:

- The class indicated by `cls` does not implement [NSSecureCoding](../nssecurecoding.md).
- The unarchived class does not match `cls`, nor do any of its superclasses.

If the coder does not require secure coding, it ignores the `cls` parameter and does not check the decoded object.

## See Also

### Decoding Top-Level Objects

- [decodeTopLevelObjectOfClasses:forKey:error:](decodetoplevelobjectofclasses_forkey_error_.md) — Decode an object as one of several expected types, failing if the archived type does not match.
- [decodeTopLevelObjectAndReturnError:](decodetoplevelobjectandreturnerror_.md) — Decodes a previously-encoded object, populating an error if decoding fails.
- [decodeTopLevelObjectForKey:error:](decodetoplevelobjectforkey_error_.md) — Decodes the previously-encoded object associated by a key, populating an error if decoding fails.
