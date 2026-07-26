---
title: Publishers.Autoconnect
framework: Combine
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/autoconnect
source_url: 'https://developer.apple.com/documentation/combine/publishers/autoconnect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/autoconnect.json'
content_hash: 'sha256:df3c4f5c865b0de0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Autoconnect

<sub>Class</sub>

A publisher that automatically connects to an upstream connectable publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Autoconnect<Upstream> where Upstream : ConnectablePublisher
```

## Overview

This publisher calls [connect()](<../connectablepublisher/connect().md>) on the upstream [ConnectablePublisher](../connectablepublisher.md) when first attached to by a subscriber.

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating an autoconnect publisher

- [init(upstream:)](<autoconnect/init(upstream_).md>) — Creates a publisher that automatically connects to an upstream connectable publisher.

### Declaring supporting types

- [Output](autoconnect/output.md) — The kind of values published by this publisher.
- [Failure](autoconnect/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](autoconnect/upstream.md) — The publisher from which this publisher receives elements.

## See Also

### Using explicit publisher connections

- [MakeConnectable](makeconnectable.md) — A publisher that provides explicit connectability to another publisher.
