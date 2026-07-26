---
title: ObservationIgnored()
framework: Observation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/observation/observationignored()
source_url: 'https://developer.apple.com/documentation/observation/observationignored()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/observationignored%28%29.json'
content_hash: 'sha256:b8c6f1f9e29eacac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Observation](../observation.md)

# ObservationIgnored()

<sub>Macro</sub>

Disables observation tracking of a property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(accessor) macro ObservationIgnored()
```

## Overview

By default, an object can observe any property of an observable type that is accessible to the observing object. To prevent observation of an accessible property, attach the `ObservationIgnored` macro to the property.
