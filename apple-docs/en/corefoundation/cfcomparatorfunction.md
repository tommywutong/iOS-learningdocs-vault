---
title: CFComparatorFunction
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfcomparatorfunction
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcomparatorfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcomparatorfunction.json'
content_hash: 'sha256:a1bfed56d2d05691'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFComparatorFunction

<sub>Type Alias</sub>

Callback function that compares two values. You provide a pointer to this callback in certain Core Foundation sorting functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFComparatorFunction = (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult
```

## Parameters

- `val1` — The first value to compare.

- `val2` — The second value to compare.

- `context` — An untyped pointer to the context of the evaluation. The meaning of this value and its use are defined by each comparator function. This value is usually passed to a sort function, such as [CFArraySortValues](<cfarraysortvalues(________).md>), which then passes it, unchanged, to the comparator function.

## Return Value

A `CFComparisonResult` value that indicates whether the `val1` is equal to, less than, or greater than `val2`. See [CFComparisonResult](cfcomparisonresult.md) for a list of possible values.

## Discussion

If you need to sort the elements in a collection using special criteria, you can implement a comparator function with the signature defined by this prototype. You pass a pointer to this function in one of the “sort” functions, such as CFArray’s [CFArraySortValues](<cfarraysortvalues(________).md>).

You can also pass pointers to standard Core Foundation comparator functions such as [CFStringCompare](<cfstringcompare(______).md>) and [CFDateCompare](<cfdatecompare(______).md>).
