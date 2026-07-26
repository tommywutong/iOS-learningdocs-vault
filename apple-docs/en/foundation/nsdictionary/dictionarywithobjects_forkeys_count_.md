---
title: 'dictionaryWithObjects:forKeys:count:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/dictionarywithobjects:forkeys:count:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/dictionarywithobjects:forkeys:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/dictionarywithobjects%3Aforkeys%3Acount%3A.json'
content_hash: 'sha256:9a728ebb4bb0ca11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# dictionaryWithObjects:forKeys:count:

<sub>Type Method</sub>

Creates a dictionary containing a specified number of objects from a C array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dictionaryWithObjects:(ObjectType const[]) objects forKeys:(id<NSCopying> const[]) keys count:(NSUInteger) cnt;
```

## Parameters

- `objects` — A C array of values for the new dictionary.

- `keys` — A C array of keys for the new dictionary. Each key is copied (using [- copyWithZone:](<../nscopying/copy(with_).md>); keys must conform to the `NSCopying` protocol), and the copy is added to the new dictionary.

- `cnt` — The number of elements to use from the `keys` and `objects` arrays. `cnt` must not exceed the number of elements in `objects` or `keys`.

## Discussion

This method steps through the `objects` and `keys` arrays, creating entries in the new dictionary as it goes. An `NSInvalidArgumentException` is raised if a key or value object is `nil`.

The following code fragment illustrates how to create a dictionary that associates the alphabetic characters with their ASCII values:

```objc
static const NSInteger N_ENTRIES = 26;
NSDictionary *asciiDict;
NSString *keyArray[N_ENTRIES];
NSNumber *valueArray[N_ENTRIES];
NSInteger i;
 
for (i = 0; i < N_ENTRIES; i++) {
 
    char charValue = 'a' + i;
    keyArray[i] = [NSString stringWithFormat:@"%c", charValue];
    valueArray[i] = [NSNumber numberWithChar:charValue];
}
 
asciiDict = [NSDictionary dictionaryWithObjects:(id *)valueArray
                          forKeys:(id *)keyArray count:N_ENTRIES];
```

## See Also

### Creating a Dictionary from Objects and Keys

- [dictionaryWithObjects:forKeys:](dictionarywithobjects_forkeys_.md) — Creates a dictionary containing entries constructed from the contents of an array of keys and an array of values.
- [- initWithObjects:forKeys:](<init(objects_forkeys_).md>) — Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.
- [- initWithObjects:forKeys:count:](<init(objects_forkeys_count_).md>) — Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.
- [dictionaryWithObjectsAndKeys:](dictionarywithobjectsandkeys_.md) — Creates a dictionary containing entries constructed from the specified set of values and keys.
- [initWithObjectsAndKeys:](initwithobjectsandkeys_.md) — Initializes a newly allocated dictionary with entries constructed from the specified set of values and keys.
- [+ dictionaryWithObject:forKey:](<init(object_forkey_).md>) — Creates a dictionary containing a given key and value.
