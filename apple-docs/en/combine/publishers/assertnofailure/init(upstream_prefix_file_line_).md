---
title: 'init(upstream:prefix:file:line:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/assertnofailure/init(upstream:prefix:file:line:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/assertnofailure/init(upstream:prefix:file:line:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/assertnofailure/init%28upstream%3Aprefix%3Afile%3Aline%3A%29.json'
content_hash: 'sha256:0949a44398a7fd42'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [AssertNoFailure](../assertnofailure.md)

# init(upstream:prefix:file:line:)

<sub>Initializer</sub>

Creates a publisher that raises a fatal error upon receiving any failure, and otherwise republishes all received input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, prefix: String, file: StaticString, line: UInt)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `prefix` — The string used at the beginning of the fatal error message.

- `file` — The filename used in the error message.

- `line` — The line number used in the error message.
