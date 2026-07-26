---
title: Publishers.TryCatch
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/trycatch
source_url: 'https://developer.apple.com/documentation/combine/publishers/trycatch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trycatch.json'
content_hash: 'sha256:f3b4848051aa0f5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.TryCatch

<sub>Structure</sub>

A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher or producing a new error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TryCatch<Upstream, NewPublisher> where Upstream : Publisher, NewPublisher : Publisher, Upstream.Output == NewPublisher.Output
```

## Overview

Because this publisher’s handler can throw an error, [TryCatch](trycatch.md) defines its [Failure](../publisher/failure.md) type as `Error`. This is different from [Catch](catch.md), which gets its failure type from the replacement publisher.

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a try-catch publisher

- [init(upstream:handler:)](<trycatch/init(upstream_handler_).md>) — Creates a publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher or by throwing an error.

### Declaring supporting types

- [Output](trycatch/output.md) — The kind of values published by this publisher.
- [Failure](trycatch/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](trycatch/upstream.md) — The publisher from which this publisher receives its elements.
- [handler](trycatch/handler.md) — A closure that accepts the upstream failure as input and either returns a publisher to replace the upstream publisher or throws an error.

## See Also

### Handling errors

- [AssertNoFailure](assertnofailure.md) — A publisher that raises a fatal error upon receiving any failure, and otherwise republishes all received input.
- [Catch](catch.md) — A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.
- [Retry](retry.md) — A publisher that attempts to recreate its subscription to a failed upstream publisher.
