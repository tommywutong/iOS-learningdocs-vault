---
title: 'unarchivedDictionaryWithKeysOfClass:objectsOfClass:fromData:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiver/unarchiveddictionarywithkeysofclass:objectsofclass:fromdata:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchiveddictionarywithkeysofclass:objectsofclass:fromdata:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/unarchiveddictionarywithkeysofclass%3Aobjectsofclass%3Afromdata%3Aerror%3A.json'
content_hash: 'sha256:23a65845eaed1f2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# unarchivedDictionaryWithKeysOfClass:objectsOfClass:fromData:error:

<sub>Type Method</sub>

Decodes the \\c NSDictionary root object from \\c data which should be an \\c NSDictionary\<keyCls,objectCls\>  with keys of type given in \\c keyCls and objects of the given non-collection class \\c objectCls (no nested dictionaries or other dictionaries contained in the dictionary, etc) from the given archive, previously encoded by \\c NSKeyedArchiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSDictionary *) unarchivedDictionaryWithKeysOfClass:(Class) keyCls objectsOfClass:(Class) valueCls fromData:(NSData *) data error:(NSError **) error;
```

## Discussion

Enables \\c requiresSecureCoding and sets the \\c decodingFailurePolicy to \\c NSDecodingFailurePolicySetErrorAndReturn.

Returns \\c nil if the given data is not valid or cannot be decoded, and sets the \\c error out parameter.
