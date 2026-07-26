---
title: Observable
framework: Observation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/observation/observable
source_url: 'https://developer.apple.com/documentation/observation/observable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/observable.json'
content_hash: 'sha256:71c4480d40042f4e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Observation](../observation.md)

# Observable

<sub>Protocol</sub>

A type that emits notifications to observers when underlying data changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Observable
```

## Overview

Conforming to this protocol signals to other APIs that the type supports observation. However, applying the `Observable` protocol by itself to a type doesn’t add observation functionality to the type. Instead, always use the [Observable()](<observable().md>) macro when adding observation support to a type.

## See Also

### Observable conformance

- [Observable()](<observable().md>) — Defines and implements conformance of the Observable protocol.
