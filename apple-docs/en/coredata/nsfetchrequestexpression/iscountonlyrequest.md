---
title: isCountOnlyRequest
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequestexpression/iscountonlyrequest
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/iscountonlyrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequestexpression/iscountonlyrequest.json'
content_hash: 'sha256:9efa128498e45b44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequestExpression](../nsfetchrequestexpression.md)

# isCountOnlyRequest

<sub>Instance Property</sub>

Returns a Boolean value that indicates whether the receiver represents a count-only fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isCountOnlyRequest: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver represents a count-only fetch request, otherwise [false](../../swift/false.md). If this method returns [false](../../swift/false.md), the managed object context (from the [contextExpression](contextexpression.md)) will perform [fetch(_:)](<../nsmanagedobjectcontext/fetch(__)-38ys1.md>): with the [requestExpression](requestexpression.md); if this method returns [true](../../swift/true.md), the managed object context will perform [- countForFetchRequest:error:](<../nsmanagedobjectcontext/count(for_)-93zbm.md>) with the [requestExpression](requestexpression.md).

## See Also

### Examining a Fetch Request Expression

- [requestExpression](requestexpression.md) — The expression for the receiver’s fetch request.
- [contextExpression](contextexpression.md) — The expression for the receiver’s managed object context.
