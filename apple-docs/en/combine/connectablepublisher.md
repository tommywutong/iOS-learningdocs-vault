---
title: ConnectablePublisher
framework: Combine
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/connectablepublisher
source_url: 'https://developer.apple.com/documentation/combine/connectablepublisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/connectablepublisher.json'
content_hash: 'sha256:52dde7cbfbbae4d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# ConnectablePublisher

<sub>Protocol</sub>

A publisher that provides an explicit means of connecting and canceling publication.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ConnectablePublisher<Output, Failure> : Publisher
```

## Overview

Use a [ConnectablePublisher](connectablepublisher.md) when you need to perform additional configuration or setup prior to producing any elements.

This publisher doesn’t produce any elements until you call its [connect()](<connectablepublisher/connect().md>) method.

Use [makeConnectable()](<publisher/makeconnectable().md>) to create a [ConnectablePublisher](connectablepublisher.md) from any publisher whose failure type is [Never](../swift/never.md).

## Relationships

- **Inherits From**: [Publisher](publisher.md)

- **Conforming Types**: [MakeConnectable](publishers/makeconnectable.md), [Multicast](publishers/multicast.md)

## Topics

### Performing explicit connections

- [connect()](<connectablepublisher/connect().md>) — Connects to the publisher, allowing it to produce elements, and returns an instance with which to cancel publishing.

### Connecting automatically

- [autoconnect()](<connectablepublisher/autoconnect().md>) — Automates the process of connecting or disconnecting from this connectable publisher.

## See Also

### Connectable Publishers

- [Controlling Publishing with Connectable Publishers](controlling-publishing-with-connectable-publishers.md) — Coordinate when publishers start sending elements to subscribers.
