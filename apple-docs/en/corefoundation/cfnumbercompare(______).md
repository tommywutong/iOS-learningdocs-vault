---
title: 'CFNumberCompare(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumbercompare(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumbercompare(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumbercompare%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d6d4691f742b83d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberCompare(_:_:_:)

<sub>Function</sub>

Compares two CFNumber objects and returns a comparison result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberCompare(_ number: CFNumber!, _ otherNumber: CFNumber!, _ context: UnsafeMutableRawPointer!) -> CFComparisonResult
```

## Parameters

- `number` — The first CFNumber object to compare.

- `otherNumber` — The second CFNumber object to compare.

- `context` — Pass `NULL`.

## Return Value

A [CFComparisonResult](cfcomparisonresult.md) constant that indicates whether `number` is equal to, less than, or greater than `otherNumber`.

## Discussion

When comparing two CFNumber objects using this function, one or both objects can represent a special-case number such as signed 0, signed infinity, or NaN.

The following rules apply:

- Negative 0 compares less than positive 0.
- Positive infinity compares greater than everything except itself, to which it compares equal.
- Negative infinity compares less than everything except itself, to which it compares equal.
- If both numbers are NaN, then they compare equal.
- If only one of the numbers is NaN, then the NaN compares greater than the other number if it is negative, and smaller than the other number if it is positive.
