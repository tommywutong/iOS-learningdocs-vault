---
title: 'decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodedictionarywithkeysofclass:objectsofclass:forkey:'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodedictionarywithkeysofclass:objectsofclass:forkey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodedictionarywithkeysofclass%3Aobjectsofclass%3Aforkey%3A.json'
content_hash: 'sha256:5dbdc680eb2c89a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:

<sub>Instance Method</sub>

Decodes the \\c NSDictionary object for the given \\c key, which should be an \\c NSDictionary\<keyCls,objectCls\> , with keys of type given in \\c keyCls and objects of the given non-collection class \\c objectCls (no nested dictionaries or other dictionaries contained in the dictionary, etc) from the coder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSDictionary *) decodeDictionaryWithKeysOfClass:(Class) keyCls objectsOfClass:(Class) objectCls forKey:(NSString *) key;
```

## Discussion

Requires \\c NSSecureCoding otherwise an exception is thrown and sets the \\c decodingFailurePolicy to \\c NSDecodingFailurePolicySetErrorAndReturn.

Returns \\c nil if the object for \\c key is not of the expected types, or cannot be decoded, and sets the \\c error on the decoder.
