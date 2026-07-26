---
title: 'decodeTopLevelObjectOfClasses:forKey:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodetoplevelobjectofclasses:forkey:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodetoplevelobjectofclasses:forkey:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodetoplevelobjectofclasses%3Aforkey%3Aerror%3A.json'
content_hash: 'sha256:0cc6061138ed738e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeTopLevelObjectOfClasses:forKey:error:

<sub>Instance Method</sub>

Decode an object as one of several expected types, failing if the archived type does not match.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (id) decodeTopLevelObjectOfClasses:(NSSet<Class> *) classes forKey:(NSString *) key error:(NSError **) error;
```

## Parameters

- `classes` — A set of expected classes that the object being decoded should match at least one of.

- `key` — The archive key indicating the member to decode.

- `error` — On return, an [NSError](../nserror.md) indicating why decoding failed, or `nil` if no error occurred.

## Return Value

The decoded object, or `nil` if decoding fails.

## Discussion

This method is equivalent to [decodeObject(of:forKey:)](<decodeobject(of_forkey_)-roif.md>), but allows you to specify a set of classes that the decoded object can match. If [requiresSecureCoding](requiressecurecoding.md) is [true](../../swift/true.md), the decoded object’s class must be a member of the classes parameter, or a sublcass of a member.

## See Also

### Decoding Top-Level Objects

- [decodeTopLevelObjectOfClass:forKey:error:](decodetoplevelobjectofclass_forkey_error_.md) — Decode an object as an expected type, failing if the archived type does not match.
- [decodeTopLevelObjectAndReturnError:](decodetoplevelobjectandreturnerror_.md) — Decodes a previously-encoded object, populating an error if decoding fails.
- [decodeTopLevelObjectForKey:error:](decodetoplevelobjectforkey_error_.md) — Decodes the previously-encoded object associated by a key, populating an error if decoding fails.
