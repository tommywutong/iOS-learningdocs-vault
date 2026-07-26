---
title: 'withObservationTracking(options:_:onChange:)'
framework: Observation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/observation/withobservationtracking(options:_:onchange:)'
source_url: 'https://developer.apple.com/documentation/observation/withobservationtracking(options:_:onchange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/withobservationtracking%28options%3A_%3Aonchange%3A%29.json'
content_hash: 'sha256:7d532257009fdc2f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Observation](../observation.md)

# withObservationTracking(options:_:onChange:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withObservationTracking<Result, Failure>(options: ObservationTracking.Options, _ apply: () throws(Failure) -> Result, onChange: @escaping @Sendable (borrowing ObservationTracking.Event) -> Void) throws(Failure) -> Result where Failure : Error, Result : ~Copyable
```
