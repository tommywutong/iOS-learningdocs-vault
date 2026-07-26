---
title: Publishers.MapKeyPath
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/mapkeypath
source_url: 'https://developer.apple.com/documentation/combine/publishers/mapkeypath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/mapkeypath.json'
content_hash: 'sha256:98736b2152653c0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.MapKeyPath

<sub>Structure</sub>

A publisher that publishes the value of a key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapKeyPath<Upstream, Output> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Declaring supporting types

- [Output](output.md) — A publisher that publishes elements specified by a range in the sequence of published elements.
- [Failure](mapkeypath/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](mapkeypath/upstream.md) — The publisher from which this publisher receives elements.
- [keyPath](mapkeypath/keypath.md) — The key path of a property to publish.

## See Also

### Identifying properties with key paths

- [MapKeyPath2](mapkeypath2.md) — A publisher that publishes the values of two key paths as a tuple.
- [MapKeyPath3](mapkeypath3.md) — A publisher that publishes the values of three key paths as a tuple.
