---
title: 'decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodedictionarywithkeysofclasses:objectsofclasses:forkey:'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodedictionarywithkeysofclasses:objectsofclasses:forkey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodedictionarywithkeysofclasses%3Aobjectsofclasses%3Aforkey%3A.json'
content_hash: 'sha256:7535cd8d8ed121bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:

<sub>Instance Method</sub>

Decodes the \\c NSDictionary object for the given \\c key, which should be an \\c NSDictionary, with keys of the types given in \\c keyClasses and objects of the given non-collection classes in \\c objectClasses (no nested dictionaries or other dictionaries contained in the dictionary, etc) from the given coder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSDictionary *) decodeDictionaryWithKeysOfClasses:(NSSet<Class> *) keyClasses objectsOfClasses:(NSSet<Class> *) objectClasses forKey:(NSString *) key;
```

## Discussion

Requires \\c NSSecureCoding otherwise an exception is thrown and sets the \\c decodingFailurePolicy to \\c NSDecodingFailurePolicySetErrorAndReturn.

Returns \\c nil if the object for \\c key is not of the expected types, or cannot be decoded, and sets the \\c error on the decoder.
