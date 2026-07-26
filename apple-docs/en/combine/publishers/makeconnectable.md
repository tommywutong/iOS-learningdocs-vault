---
title: Publishers.MakeConnectable
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/makeconnectable
source_url: 'https://developer.apple.com/documentation/combine/publishers/makeconnectable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/makeconnectable.json'
content_hash: 'sha256:86cc5724dbf12454'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.MakeConnectable

<sub>Structure</sub>

A publisher that provides explicit connectability to another publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MakeConnectable<Upstream> where Upstream : Publisher
```

## Overview

[MakeConnectable](makeconnectable.md) is a [ConnectablePublisher](../connectablepublisher.md), which allows you to perform configuration before publishing any elements. Call [connect()](<../connectablepublisher/connect().md>) on this publisher when you want to attach to its upstream publisher and start producing elements.

Use the [makeConnectable()](<../publisher/makeconnectable().md>) operator to wrap an upstream publisher with an instance of this publisher.

## Relationships

- **Conforms To**: [ConnectablePublisher](../connectablepublisher.md), [Publisher](../publisher.md)

## Topics

### Creating a connectable publisher

- [init(upstream:)](<makeconnectable/init(upstream_).md>) — Creates a connectable publisher, attached to the provide upstream publisher.

### Declaring supporting types

- [Output](makeconnectable/output.md) — The kind of values published by this publisher.
- [Failure](makeconnectable/failure.md) — The kind of errors this publisher might publish.

## See Also

### Using explicit publisher connections

- [Autoconnect](autoconnect.md) — A publisher that automatically connects to an upstream connectable publisher.
