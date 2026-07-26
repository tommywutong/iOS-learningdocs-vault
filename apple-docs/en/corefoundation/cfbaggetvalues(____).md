---
title: 'CFBagGetValues(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbaggetvalues(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbaggetvalues(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbaggetvalues%28_%3A_%3A%29.json'
content_hash: 'sha256:40d6fb00c731d19e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagGetValues(_:_:)

<sub>Function</sub>

Fills a buffer with values from a bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagGetValues(_ theBag: CFBag!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!)
```

## Parameters

- `theBag` — The bag to examine.

- `values` — A C array of pointer-sized values to be filled with values from `theBag`. The value must be a valid C array of the appropriate type and size (that is, a size equal to the count of `theBag`).

## See Also

### Examining a Bag

- [CFBagContainsValue](<cfbagcontainsvalue(____).md>) — Reports whether or not a value is in a bag.
- [CFBagGetCount](<cfbaggetcount(__).md>) — Returns the number of values currently in a bag.
- [CFBagGetCountOfValue](<cfbaggetcountofvalue(____).md>) — Returns the number of times a value occurs in a bag.
- [CFBagGetValue](<cfbaggetvalue(____).md>) — Returns a requested value from a bag.
- [CFBagGetValueIfPresent](<cfbaggetvalueifpresent(______).md>) — Reports whether or not a value is in a bag, and returns that value indirectly if it exists.
