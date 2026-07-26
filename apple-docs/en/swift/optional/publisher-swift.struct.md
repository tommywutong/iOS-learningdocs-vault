---
title: Optional.Publisher
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/optional/publisher-swift.struct
source_url: 'https://developer.apple.com/documentation/swift/optional/publisher-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/publisher-swift.struct.json'
content_hash: 'sha256:ce5efcd1ee492e85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Optional](../optional.md)

# Optional.Publisher

<sub>Structure</sub>

The type of a Combine publisher that publishes the value of a Swift optional instance to each subscriber exactly once, if the instance has any value at all.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Publisher
```

## Overview

In contrast with the [Just](../../combine/just.md) publisher, which always produces a single value, this publisher might not send any values and instead finish normally, if [output](publisher-swift.struct/output-swift.property.md) is `nil`.

## Relationships

- **Conforms To**: [Equatable](../equatable.md), [Publisher](../../combine/publisher.md)

## Topics

### Declaring Publisher Topography

- [Output](publisher-swift.struct/output-swift.typealias.md) — The kind of value published by this publisher.
- [Failure](publisher-swift.struct/failure.md) — The kind of error this publisher might publish.

### Creating an Optional Publisher

- [init(_:)](<publisher-swift.struct/init(__).md>) — Creates a publisher to emit the value of the optional, or to finish immediately if the optional doesn’t have a value.

### Inpsecting Publisher Properties

- [output](publisher-swift.struct/output-swift.property.md) — The output to deliver to each subscriber.

### Working with Subscribers

- [receive(subscriber:)](<publisher-swift.struct/receive(subscriber_).md>) — Implements the Publisher protocol by accepting the subscriber and immediately publishing the optional’s value if it has one, or finishing normally if it doesn’t.

### Instance Methods

- [allSatisfy(_:)](<publisher-swift.struct/allsatisfy(__).md>)
- [collect()](<publisher-swift.struct/collect().md>)
- [compactMap(_:)](<publisher-swift.struct/compactmap(__).md>)
- [contains(_:)](<publisher-swift.struct/contains(__).md>)
- [contains(where:)](<publisher-swift.struct/contains(where_).md>)
- [count()](<publisher-swift.struct/count().md>)
- [drop(while:)](<publisher-swift.struct/drop(while_).md>)
- [dropFirst(_:)](<publisher-swift.struct/dropfirst(__).md>)
- [filter(_:)](<publisher-swift.struct/filter(__).md>)
- [first()](<publisher-swift.struct/first().md>)
- [first(where:)](<publisher-swift.struct/first(where_).md>)
- [ignoreOutput()](<publisher-swift.struct/ignoreoutput().md>)
- [last()](<publisher-swift.struct/last().md>)
- [last(where:)](<publisher-swift.struct/last(where_).md>)
- [map(_:)](<publisher-swift.struct/map(__).md>)
- [max()](<publisher-swift.struct/max().md>)
- [max(by:)](<publisher-swift.struct/max(by_).md>)
- [min()](<publisher-swift.struct/min().md>)
- [min(by:)](<publisher-swift.struct/min(by_).md>)
- [output(at:)](<publisher-swift.struct/output(at_).md>)
- [output(in:)](<publisher-swift.struct/output(in_).md>)
- [prefix(_:)](<publisher-swift.struct/prefix(__).md>)
- [prefix(while:)](<publisher-swift.struct/prefix(while_).md>)
- [reduce(_:_:)](<publisher-swift.struct/reduce(____).md>)
- [removeDuplicates()](<publisher-swift.struct/removeduplicates().md>)
- [removeDuplicates(by:)](<publisher-swift.struct/removeduplicates(by_).md>)
- [replaceEmpty(with:)](<publisher-swift.struct/replaceempty(with_).md>)
- [replaceError(with:)](<publisher-swift.struct/replaceerror(with_).md>)
- [retry(_:)](<publisher-swift.struct/retry(__).md>)
- [scan(_:_:)](<publisher-swift.struct/scan(____).md>)

## See Also

### Publishing an Optional

- [publisher](publisher-swift.property.md) — A Combine publisher that publishes this instance’s value to each subscriber exactly once, if it has any value at all.
