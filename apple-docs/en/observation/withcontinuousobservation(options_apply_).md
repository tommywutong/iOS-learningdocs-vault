---
title: 'withContinuousObservation(options:apply:)'
framework: Observation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/observation/withcontinuousobservation(options:apply:)'
source_url: 'https://developer.apple.com/documentation/observation/withcontinuousobservation(options:apply:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/withcontinuousobservation%28options%3Aapply%3A%29.json'
content_hash: 'sha256:92e0ba7aa7e093e7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Observation](../observation.md)

# withContinuousObservation(options:apply:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withContinuousObservation(options: ObservationTracking.Options, apply: @escaping @isolated(any) @Sendable (borrowing ObservationTracking.Event) -> Void) -> ObservationTracking.Token
```
