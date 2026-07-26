---
title: Publishers.AssertNoFailure
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/assertnofailure
source_url: 'https://developer.apple.com/documentation/combine/publishers/assertnofailure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/assertnofailure.json'
content_hash: 'sha256:81c4c70f3ecfd0c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.AssertNoFailure

<sub>Structure</sub>

A publisher that raises a fatal error upon receiving any failure, and otherwise republishes all received input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AssertNoFailure<Upstream> where Upstream : Publisher
```

## Overview

Use this function for internal integrity checks that are active during testing but don’t affect performance of shipping code.

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating an assert no failure publisher

- [init(upstream:prefix:file:line:)](<assertnofailure/init(upstream_prefix_file_line_).md>) — Creates a publisher that raises a fatal error upon receiving any failure, and otherwise republishes all received input.

### Declaring supporting types

- [Output](assertnofailure/output.md) — The kind of values published by this publisher.
- [Failure](assertnofailure/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](assertnofailure/upstream.md) — The publisher from which this publisher receives elements.
- [file](assertnofailure/file.md) — The filename used in the error message.
- [line](assertnofailure/line.md) — The line number used in the error message.
- [prefix](assertnofailure/prefix.md) — The string used at the beginning of the fatal error message.

## See Also

### Handling errors

- [Catch](catch.md) — A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.
- [TryCatch](trycatch.md) — A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher or producing a new error.
- [Retry](retry.md) — A publisher that attempts to recreate its subscription to a failed upstream publisher.
