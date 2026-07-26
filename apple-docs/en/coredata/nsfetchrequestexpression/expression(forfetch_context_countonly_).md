---
title: 'expression(forFetch:context:countOnly:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsfetchrequestexpression/expression(forfetch:context:countonly:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/expression(forfetch:context:countonly:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequestexpression/expression%28forfetch%3Acontext%3Acountonly%3A%29.json'
content_hash: 'sha256:6cf8c7b46b9ad43c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequestExpression](../nsfetchrequestexpression.md)

# expression(forFetch:context:countOnly:)

<sub>Type Method</sub>

Returns an expression which will evaluate to the result of executing a fetch request on a context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func expression(forFetch fetch: NSExpression, context: NSExpression, countOnly countFlag: Bool) -> NSExpression
```

## Parameters

- `fetch` — An expression that evaluates to an instance of `NSFetchRequest`.

- `context` — An expression that evaluates to an instance of `NSManagedObjectContext`.

- `countFlag` — If [true](../../swift/true.md), when the new expression is evaluated the managed object context (from `context`) will perform [- countForFetchRequest:error:](<../nsmanagedobjectcontext/count(for_)-93zbm.md>) with the fetch request (from `fetch`). If [false](../../swift/false.md), when the new expression is evaluated the managed object context will perform [fetch(_:)](<../nsmanagedobjectcontext/fetch(__)-38ys1.md>) with the fetch request.

## Return Value

An expression which will evaluate to the result of executing a fetch request (from `fetch`) on a managed object context (from `context`).

## See Also

### Related Documentation

- [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)
- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
