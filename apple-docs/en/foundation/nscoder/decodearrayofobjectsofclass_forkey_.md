---
title: 'decodeArrayOfObjectsOfClass:forKey:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodearrayofobjectsofclass:forkey:'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodearrayofobjectsofclass:forkey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodearrayofobjectsofclass%3Aforkey%3A.json'
content_hash: 'sha256:39f0b524e9901e75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeArrayOfObjectsOfClass:forKey:

<sub>Instance Method</sub>

Decodes the \\c NSArray object for the given  \\c key, which should be an \\c NSArray, containing the given non-collection class (no nested arrays or arrays of dictionaries, etc) from the coder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSArray *) decodeArrayOfObjectsOfClass:(Class) cls forKey:(NSString *) key;
```

## Discussion

Requires \\c NSSecureCoding otherwise an exception is thrown and sets the \\c decodingFailurePolicy to \\c NSDecodingFailurePolicySetErrorAndReturn.

Returns \\c nil if the object for \\c key is not of the expected types, or cannot be decoded, and sets the \\c error on the decoder.
