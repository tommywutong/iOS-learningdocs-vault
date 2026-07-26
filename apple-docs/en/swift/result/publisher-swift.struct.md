---
title: Result.Publisher
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/result/publisher-swift.struct
source_url: 'https://developer.apple.com/documentation/swift/result/publisher-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/publisher-swift.struct.json'
content_hash: 'sha256:e72f0f077c045b54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Result](../result.md)

# Result.Publisher

<sub>Structure</sub>

The type of a Combine publisher that publishes this instance’s result to each subscriber exactly once, or fails immediately if the result indicates failure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Publisher
```

## Overview

If the result is `Swift/Result/success`, then the publisher waits until it receives a request for at least one value, then sends the output to all subscribers and finishes normally. If the result is `/Swift/Result/failure`, then the publisher sends the failure immediately upon subscription. This latter behavior is a contrast with [Just](../../combine/just.md), which always publishes a single value.

## Relationships

- **Conforms To**: [Equatable](../equatable.md), [Publisher](../../combine/publisher.md)

## Topics

### Creating a Result Publisher

- [init(_:)](<publisher-swift.struct/init(__)-516t.md>) — Creates a publisher that delivers the specified result.
- [init(_:)](<publisher-swift.struct/init(__)-69fv4.md>) — Creates a publisher that immediately terminates upon subscription with the given failure.
- [init(_:)](<publisher-swift.struct/init(__)-7t2tt.md>) — Creates a publisher that sends the specified output to all subscribers and finishes normally.

### Inspecting Publisher Properties

- [result](publisher-swift.struct/result.md) — The result to deliver to each subscriber.

### Instance Methods

- [allSatisfy(_:)](<publisher-swift.struct/allsatisfy(__).md>)
- [collect()](<publisher-swift.struct/collect().md>)
- [contains(_:)](<publisher-swift.struct/contains(__).md>)
- [contains(where:)](<publisher-swift.struct/contains(where_).md>)
- [count()](<publisher-swift.struct/count().md>)
- [first()](<publisher-swift.struct/first().md>)
- [ignoreOutput()](<publisher-swift.struct/ignoreoutput().md>)
- [last()](<publisher-swift.struct/last().md>)
- [map(_:)](<publisher-swift.struct/map(__).md>)
- [mapError(_:)](<publisher-swift.struct/maperror(__).md>)
- [max()](<publisher-swift.struct/max().md>)
- [max(by:)](<publisher-swift.struct/max(by_).md>)
- [min()](<publisher-swift.struct/min().md>)
- [min(by:)](<publisher-swift.struct/min(by_).md>)
- [reduce(_:_:)](<publisher-swift.struct/reduce(____).md>)
- [removeDuplicates()](<publisher-swift.struct/removeduplicates().md>)
- [removeDuplicates(by:)](<publisher-swift.struct/removeduplicates(by_).md>)
- [replaceEmpty(with:)](<publisher-swift.struct/replaceempty(with_).md>)
- [replaceError(with:)](<publisher-swift.struct/replaceerror(with_).md>)
- [retry(_:)](<publisher-swift.struct/retry(__).md>)
- [scan(_:_:)](<publisher-swift.struct/scan(____).md>)
- [setFailureType(to:)](<publisher-swift.struct/setfailuretype(to_).md>)
- [tryAllSatisfy(_:)](<publisher-swift.struct/tryallsatisfy(__).md>)
- [tryContains(where:)](<publisher-swift.struct/trycontains(where_).md>)
- [tryMap(_:)](<publisher-swift.struct/trymap(__).md>)
- [tryMax(by:)](<publisher-swift.struct/trymax(by_).md>)
- [tryMin(by:)](<publisher-swift.struct/trymin(by_).md>)
- [tryReduce(_:_:)](<publisher-swift.struct/tryreduce(____).md>)
- [tryRemoveDuplicates(by:)](<publisher-swift.struct/tryremoveduplicates(by_).md>)
- [tryScan(_:_:)](<publisher-swift.struct/tryscan(____).md>)

## See Also

### Publishing a Result

- [publisher](publisher-swift.property.md) — A Combine publisher that publishes this instance’s result to each subscriber exactly once, or fails immediately if the result indicates failure.
