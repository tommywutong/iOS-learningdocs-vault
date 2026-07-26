---
title: 'CFBagContainsValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbagcontainsvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagcontainsvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagcontainsvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:961a09406ee490f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagContainsValue(_:_:)

<sub>Function</sub>

Reports whether or not a value is in a bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagContainsValue(_ theBag: CFBag!, _ value: UnsafeRawPointer!) -> Bool
```

## Parameters

- `theBag` — The bag to examine.

- `value` — The value to match in `theBag`. The equal callback provided when `theBag` was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `value`, or any other value in `theBag`, is not understood by the equal callback, the behavior is undefined.

## Return Value

`true` if `value` is contained in `theBag`, otherwise `false`.

## See Also

### Examining a Bag

- [CFBagGetCount](<cfbaggetcount(__).md>) — Returns the number of values currently in a bag.
- [CFBagGetCountOfValue](<cfbaggetcountofvalue(____).md>) — Returns the number of times a value occurs in a bag.
- [CFBagGetValue](<cfbaggetvalue(____).md>) — Returns a requested value from a bag.
- [CFBagGetValueIfPresent](<cfbaggetvalueifpresent(______).md>) — Reports whether or not a value is in a bag, and returns that value indirectly if it exists.
- [CFBagGetValues](<cfbaggetvalues(____).md>) — Fills a buffer with values from a bag.
