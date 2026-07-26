---
title: Publishers.Print
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/print
source_url: 'https://developer.apple.com/documentation/combine/publishers/print'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/print.json'
content_hash: 'sha256:65b0e8104edd14f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Print

<sub>Structure</sub>

A publisher that prints log messages for all publishing events, optionally prefixed with a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Print<Upstream> where Upstream : Publisher
```

## Overview

This publisher prints log messages when receiving the following events:

- subscription
- value
- normal completion
- failure
- cancellation

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a print publisher

- [init(upstream:prefix:to:)](<print/init(upstream_prefix_to_).md>) — Creates a publisher that prints log messages for all publishing events.

### Declaring supporting types

- [Output](print/output.md) — The kind of values published by this publisher.
- [Failure](print/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](print/upstream.md) — The publisher from which this publisher receives elements.
- [prefix](print/prefix.md) — A string with which to prefix all log messages.
- [stream](print/stream.md)

## See Also

### Debugging

- [Breakpoint](breakpoint.md) — A publisher that raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [HandleEvents](handleevents.md) — A publisher that performs the specified closures when publisher events occur.
