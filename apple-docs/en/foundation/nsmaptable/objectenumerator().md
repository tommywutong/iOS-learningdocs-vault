---
title: objectEnumerator()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmaptable/objectenumerator()
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptable/objectenumerator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptable/objectenumerator%28%29.json'
content_hash: 'sha256:856d9508b4e558c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTable](../nsmaptable.md)

# objectEnumerator()

<sub>Instance Method</sub>

Returns an enumerator object that lets you access each value in the map table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objectEnumerator() -> NSEnumerator?
```

## Return Value

An enumerator object that lets you access each value in the map table.

## Discussion

The following code fragment illustrates how you might use the method.

```objc
NSEnumerator *enumerator = [myMapTable objectEnumerator];
id value;
 
while ((value = [enumerator nextObject])) {
    /* code that acts on the map table's values */
}
```

### Special Considerations

It is more efficient to use the fast enumeration protocol (see [NSFastEnumeration](../nsfastenumeration.md)).

## See Also

### Accessing Content

- [- objectForKey:](<object(forkey_).md>) — Returns a the value associated with a given key.
- [- keyEnumerator](<keyenumerator().md>) — Returns an enumerator object that lets you access each key in the map table.
- [count](count.md) — The number of key-value pairs in the map table.
