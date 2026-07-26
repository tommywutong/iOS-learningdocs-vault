---
title: 'unarchivedDictionaryWithKeysOfClasses:objectsOfClasses:fromData:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiver/unarchiveddictionarywithkeysofclasses:objectsofclasses:fromdata:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchiveddictionarywithkeysofclasses:objectsofclasses:fromdata:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/unarchiveddictionarywithkeysofclasses%3Aobjectsofclasses%3Afromdata%3Aerror%3A.json'
content_hash: 'sha256:4f7c7a90d9b1bb26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# unarchivedDictionaryWithKeysOfClasses:objectsOfClasses:fromData:error:

<sub>Type Method</sub>

Decodes the \\c NSDictionary root object from \\c data which should be an \\c NSDictionary, with keys of the types given in \\c keyClasses and objects of the given non-collection classes in \\c objectClasses (no nested dictionaries or other dictionaries contained in the dictionary, etc) from the given archive, previously encoded by \\c NSKeyedArchiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSDictionary *) unarchivedDictionaryWithKeysOfClasses:(NSSet<Class> *) keyClasses objectsOfClasses:(NSSet<Class> *) valueClasses fromData:(NSData *) data error:(NSError **) error;
```

## Discussion

Enables \\c requiresSecureCoding and sets the \\c decodingFailurePolicy to \\c NSDecodingFailurePolicySetErrorAndReturn.

Returns \\c nil if the given data is not valid or cannot be decoded, and sets the \\c error out parameter.
