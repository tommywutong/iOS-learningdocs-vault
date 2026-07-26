---
title: 'keysOfEntries(passingTest:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/keysofentries(passingtest:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/keysofentries(passingtest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/keysofentries%28passingtest%3A%29.json'
content_hash: 'sha256:3093f6352a6d9eaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# keysOfEntries(passingTest:)

<sub>Instance Method</sub>

Returns the set of keys whose corresponding value satisfies a constraint described by a block object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func keysOfEntries(passingTest predicate: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>
```

## Parameters

- `predicate` — A block object that specifies constraints for values in the dictionary.

## Return Value

The set of keys whose corresponding value satisfies `predicate`.

## See Also

### Related Documentation

- [- enumerateKeysAndObjectsUsingBlock:](<enumeratekeysandobjects(__).md>) — Applies a given block object to the entries of the dictionary.

### Filtering Dictionaries

- [- keysOfEntriesWithOptions:passingTest:](<keysofentries(options_passingtest_).md>) — Returns the set of keys whose corresponding value satisfies a constraint described by a block object.
