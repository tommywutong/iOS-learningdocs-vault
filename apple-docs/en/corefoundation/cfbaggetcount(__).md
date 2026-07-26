---
title: 'CFBagGetCount(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbaggetcount(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbaggetcount(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbaggetcount%28_%3A%29.json'
content_hash: 'sha256:2333a2b8640a6cc2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagGetCount(_:)

<sub>Function</sub>

Returns the number of values currently in a bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagGetCount(_ theBag: CFBag!) -> CFIndex
```

## Parameters

- `theBag` — The bag to examine.

## Return Value

The number of values in `theBag`.

## See Also

### Examining a Bag

- [CFBagContainsValue](<cfbagcontainsvalue(____).md>) — Reports whether or not a value is in a bag.
- [CFBagGetCountOfValue](<cfbaggetcountofvalue(____).md>) — Returns the number of times a value occurs in a bag.
- [CFBagGetValue](<cfbaggetvalue(____).md>) — Returns a requested value from a bag.
- [CFBagGetValueIfPresent](<cfbaggetvalueifpresent(______).md>) — Reports whether or not a value is in a bag, and returns that value indirectly if it exists.
- [CFBagGetValues](<cfbaggetvalues(____).md>) — Fills a buffer with values from a bag.
