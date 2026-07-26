---
title: start()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataquery/start()
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquery/start()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquery/start%28%29.json'
content_hash: 'sha256:a368750fd6f4d290'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQuery](../nsmetadataquery.md)

# start()

<sub>Instance Method</sub>

Attempts to start the query.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func start() -> Bool
```

## Return Value

[true](../../swift/true.md) when successful; otherwise, [false](../../swift/false.md).

A query may fail to start if it does not specify a [predicate](predicate.md), or if the query has already been started.

## Discussion

A query can’t be started if the receiver is already running a query or no predicate has been specified.

This method must be called from the receiver’s [operationQueue](operationqueue.md) or on the main thread. For example:

**Swift**

```swift
let query: NSMetadataQuery = // Initialize and set up a query
    query.operationQueue?.addOperationWithBlock {
        query.startQuery()
}
```

**Objective-C**

```objc
NSMetadataQuery *query = // Initialize and set up a query
[query.operationQueue addOperationWithBlock:^{
    [query startQuery];
}];
```

## See Also

### Running queries

- [started](isstarted.md) — A Boolean value that indicates whether the query has started. (read-only)
- [gathering](isgathering.md) — A Boolean value that indicates whether the receiver is in the initial gathering phase of the query. (read-only)
- [stopped](isstopped.md) — A Boolean value that indicates whether the query has stopped.
- [- stopQuery](<stop().md>) — Stops the receiver’s current query from gathering any further results.
