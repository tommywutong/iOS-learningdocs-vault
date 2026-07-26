---
title: 'keysOfEntries(options:passingTest:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/keysofentries(options:passingtest:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/keysofentries(options:passingtest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/keysofentries%28options%3Apassingtest%3A%29.json'
content_hash: 'sha256:a4b4eff8827c0aae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# keysOfEntries(options:passingTest:)

<sub>Instance Method</sub>

Returns the set of keys whose corresponding value satisfies a constraint described by a block object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func keysOfEntries(options opts: NSEnumerationOptions = [], passingTest predicate: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>
```

## Parameters

- `opts` — A bit mask of enumeration options.

- `predicate` — A block object that specifies constraints for values in the dictionary.

## Return Value

The set of keys whose corresponding value satisfies `predicate`.

## See Also

### Related Documentation

- [- enumerateKeysAndObjectsWithOptions:usingBlock:](<enumeratekeysandobjects(options_using_).md>) — Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.

### Filtering Dictionaries

- [- keysOfEntriesPassingTest:](<keysofentries(passingtest_).md>) — Returns the set of keys whose corresponding value satisfies a constraint described by a block object.
