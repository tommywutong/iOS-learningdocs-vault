---
title: 'CFBagGetValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbaggetvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbaggetvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbaggetvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:ec7f34c96ab11e3d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagGetValue(_:_:)

<sub>Function</sub>

Returns a requested value from a bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagGetValue(_ theBag: CFBag!, _ value: UnsafeRawPointer!) -> UnsafeRawPointer!
```

## Parameters

- `theBag` — The bag to examine.

- `value` — The value for which to find matches in `theBag`. The equal callback provided when `theBag` was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `value`, or any other value in `theBag`, is not understood by the equal callback, the behavior is undefined.

## Return Value

A pointer to `value`, or `NULL` if `value` is not in `theBag`. If the value is a Core Foundation object, ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

Depending on the implementation of the equal callback specified when creating `theBag`, the value returned may not have the same pointer equality as `value`.

## See Also

### Examining a Bag

- [CFBagContainsValue](<cfbagcontainsvalue(____).md>) — Reports whether or not a value is in a bag.
- [CFBagGetCount](<cfbaggetcount(__).md>) — Returns the number of values currently in a bag.
- [CFBagGetCountOfValue](<cfbaggetcountofvalue(____).md>) — Returns the number of times a value occurs in a bag.
- [CFBagGetValueIfPresent](<cfbaggetvalueifpresent(______).md>) — Reports whether or not a value is in a bag, and returns that value indirectly if it exists.
- [CFBagGetValues](<cfbaggetvalues(____).md>) — Fills a buffer with values from a bag.
