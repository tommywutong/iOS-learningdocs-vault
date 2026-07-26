---
title: 'removeObject(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledictionary/removeobject(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledictionary/removeobject(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledictionary/removeobject%28forkey%3A%29.json'
content_hash: 'sha256:a1a602e386c6f317'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableDictionary](../nsmutabledictionary.md)

# removeObject(forKey:)

<sub>Instance Method</sub>

Removes a given key and its associated value from the dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObject(forKey aKey: Any)
```

## Parameters

- `aKey` — The key to remove. > [!important] Important > Raises an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md) if `aKey` is `nil`.

## Discussion

Does nothing if `aKey` does not exist.

For example, assume you have an archived dictionary that records the call letters and associated frequencies of radio stations. To remove an entry for a defunct station, you could write code similar to the following:

```objc
NSMutableDictionary *stations = nil;
 
stations = [[NSMutableDictionary alloc]
        initWithContentsOfFile: pathToArchive];
[stations removeObjectForKey:@"KIKT"];
```

## See Also

### Removing Entries From a Mutable Dictionary

- [- removeAllObjects](<removeallobjects().md>) — Empties the dictionary of its entries.
- [- removeObjectsForKeys:](<removeobjects(forkeys_).md>) — Removes from the dictionary entries specified by elements in a given array.
