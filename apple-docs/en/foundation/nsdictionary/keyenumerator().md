---
title: keyEnumerator()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdictionary/keyenumerator()
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/keyenumerator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/keyenumerator%28%29.json'
content_hash: 'sha256:85c4ed140cf97320'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# keyEnumerator()

<sub>Instance Method</sub>

Provides an enumerator to access the keys in the dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func keyEnumerator() -> NSEnumerator
```

## Return Value

An enumerator object that lets you access each key in the dictionary.

## Discussion

Here’s how you might use this method.

**Swift**

```swift
let enumerator = myDictionary.keyEnumerator()

while let key = enumerator.nextObject() {
    /* code that uses the returned key */
}

```

**Objective-C**

```objc
NSEnumerator *enumerator = [myDictionary keyEnumerator];
id key;
 
while ((key = [enumerator nextObject])) {
    /* code that uses the returned key */
}
```

If you use this method with instances of mutable subclasses of [NSDictionary](../nsdictionary.md), your code should not modify the entries during enumeration. If you intend to modify the entries, use the [allKeys](allkeys.md) property to create a snapshot of the dictionary’s keys. Then use this snapshot to traverse the entries, modifying them along the way.

If you want to enumerate the dictionary’s values rather than its keys, use the [- objectEnumerator](<objectenumerator().md>) method.

### Special Considerations

It is more efficient to use the fast enumeration protocol (see [NSFastEnumeration](../nsfastenumeration.md)) than this method. Fast enumeration is available in macOS 10.5 and later and iOS 2.0 and later.

## See Also

### Enumerating Dictionaries

- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each value in the dictionary.
- [- enumerateKeysAndObjectsUsingBlock:](<enumeratekeysandobjects(__).md>) — Applies a given block object to the entries of the dictionary.
- [- enumerateKeysAndObjectsWithOptions:usingBlock:](<enumeratekeysandobjects(options_using_).md>) — Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.
- [makeIterator()](<makeiterator().md>) — Returns an iterator over the elements of this sequence.
