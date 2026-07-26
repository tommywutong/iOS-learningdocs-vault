---
title: 'decodeArrayOfObjectsOfClasses:forKey:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodearrayofobjectsofclasses:forkey:'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodearrayofobjectsofclasses:forkey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodearrayofobjectsofclasses%3Aforkey%3A.json'
content_hash: 'sha256:02000c274a645132'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeArrayOfObjectsOfClasses:forKey:

<sub>Instance Method</sub>

Decodes the \\c NSArray object for the given \\c key, which should be an \\c NSArray, containing the given non-collection classes (no nested arrays or arrays of dictionaries, etc) from the coder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSArray *) decodeArrayOfObjectsOfClasses:(NSSet<Class> *) classes forKey:(NSString *) key;
```

## Discussion

Requires \\c NSSecureCoding otherwise an exception is thrown and sets the \\c decodingFailurePolicy to \\c NSDecodingFailurePolicySetErrorAndReturn.

Returns \\c nil if the object for \\c key is not of the expected types, or cannot be decoded, and sets the \\c error on the decoder.
