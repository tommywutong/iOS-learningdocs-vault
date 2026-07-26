---
title: objectEnumerator()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdictionary/objectenumerator()
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/objectenumerator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/objectenumerator%28%29.json'
content_hash: 'sha256:799fa104f2f31228'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# objectEnumerator()

<sub>Instance Method</sub>

Returns an enumerator object that lets you access each value in the dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objectEnumerator() -> NSEnumerator
```

## Return Value

An enumerator object that lets you access each value in the dictionary.

## Discussion

The following code fragment illustrates how you might use the method.

```objc
NSEnumerator *enumerator = [myDictionary objectEnumerator];
id value;
 
while ((value = [enumerator nextObject])) {
    /* code that acts on the dictionary’s values */
}
```

If you use this method with instances of mutable subclasses of `NSDictionary`, your code should not modify the entries during enumeration. If you intend to modify the entries, use the [allValues](allvalues.md) method to create a “snapshot” of the dictionary’s values. Work from this snapshot to modify the values.

### Special Considerations

It is more efficient to use the fast enumeration protocol (see [NSFastEnumeration](../nsfastenumeration.md)). Fast enumeration is available in macOS 10.5 and later and iOS 2.0 and later.

## See Also

### Related Documentation

- [- nextObject](<../nsenumerator/nextobject().md>) — Returns the next object from the collection being enumerated.

### Enumerating Dictionaries

- [- keyEnumerator](<keyenumerator().md>) — Provides an enumerator to access the keys in the dictionary.
- [- enumerateKeysAndObjectsUsingBlock:](<enumeratekeysandobjects(__).md>) — Applies a given block object to the entries of the dictionary.
- [- enumerateKeysAndObjectsWithOptions:usingBlock:](<enumeratekeysandobjects(options_using_).md>) — Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.
- [makeIterator()](<makeiterator().md>) — Returns an iterator over the elements of this sequence.
