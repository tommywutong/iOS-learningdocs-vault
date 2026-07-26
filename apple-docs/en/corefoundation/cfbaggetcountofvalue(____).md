---
title: 'CFBagGetCountOfValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbaggetcountofvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbaggetcountofvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbaggetcountofvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:bfd5a7cb556c2cc7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagGetCountOfValue(_:_:)

<sub>Function</sub>

Returns the number of times a value occurs in a bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagGetCountOfValue(_ theBag: CFBag!, _ value: UnsafeRawPointer!) -> CFIndex
```

## Parameters

- `theBag` — The bag to examine.

- `value` — The value for which to find matches in `theBag`. The equal callback provided when `theBag` was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `value`, or any other value in `theBag`, is not understood by the equal callback, the behavior is undefined.

## Return Value

The number of times `value` occurs in `theBag`.

## See Also

### Examining a Bag

- [CFBagContainsValue](<cfbagcontainsvalue(____).md>) — Reports whether or not a value is in a bag.
- [CFBagGetCount](<cfbaggetcount(__).md>) — Returns the number of values currently in a bag.
- [CFBagGetValue](<cfbaggetvalue(____).md>) — Returns a requested value from a bag.
- [CFBagGetValueIfPresent](<cfbaggetvalueifpresent(______).md>) — Reports whether or not a value is in a bag, and returns that value indirectly if it exists.
- [CFBagGetValues](<cfbaggetvalues(____).md>) — Fills a buffer with values from a bag.
