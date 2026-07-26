---
title: 'CFBagGetValueIfPresent(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbaggetvalueifpresent(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbaggetvalueifpresent(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbaggetvalueifpresent%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:023881f3a477da8b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagGetValueIfPresent(_:_:_:)

<sub>Function</sub>

Reports whether or not a value is in a bag, and returns that value indirectly if it exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagGetValueIfPresent(_ theBag: CFBag!, _ candidate: UnsafeRawPointer!, _ value: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool
```

## Parameters

- `theBag` — The bag to be searched.

- `candidate` — The value for which to find matches in `theBag`. The equal callback provided when `theBag` was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `candidate`, or any other value in `theBag`, is not understood by the equal callback, the behavior is undefined.

- `value` — A pointer to a value object. Set to the matching value if it exists in the bag, otherwise `NULL`. If the value is a Core Foundation object, ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Return Value

`true` if `value` is present in `theBag`, otherwise `false`.

## Discussion

Depending on the implementation of the equal callback specified when creating `theBag`, the value returned in `value` may not have the same pointer equality as `candidate`.

## See Also

### Examining a Bag

- [CFBagContainsValue](<cfbagcontainsvalue(____).md>) — Reports whether or not a value is in a bag.
- [CFBagGetCount](<cfbaggetcount(__).md>) — Returns the number of values currently in a bag.
- [CFBagGetCountOfValue](<cfbaggetcountofvalue(____).md>) — Returns the number of times a value occurs in a bag.
- [CFBagGetValue](<cfbaggetvalue(____).md>) — Returns a requested value from a bag.
- [CFBagGetValues](<cfbaggetvalues(____).md>) — Fills a buffer with values from a bag.
