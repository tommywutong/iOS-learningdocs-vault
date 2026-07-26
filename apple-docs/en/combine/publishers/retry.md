---
title: Publishers.Retry
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/retry
source_url: 'https://developer.apple.com/documentation/combine/publishers/retry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/retry.json'
content_hash: 'sha256:d0d144912acf409f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Retry

<sub>Structure</sub>

A publisher that attempts to recreate its subscription to a failed upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Retry<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a retry publisher

- [init(upstream:retries:)](<retry/init(upstream_retries_).md>) — Creates a publisher that attempts to recreate its subscription to a failed upstream publisher.

### Declaring supporting types

- [Output](retry/output.md) — The kind of values published by this publisher.
- [Failure](retry/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](retry/upstream.md) — The publisher from which this publisher receives elements.
- [retries](retry/retries.md) — The maximum number of retry attempts to perform.

### Comparing publishers

- [==(_:_:)](<retry/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](retry/equatable-implementations.md)

## See Also

### Handling errors

- [AssertNoFailure](assertnofailure.md) — A publisher that raises a fatal error upon receiving any failure, and otherwise republishes all received input.
- [Catch](catch.md) — A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.
- [TryCatch](trycatch.md) — A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher or producing a new error.
