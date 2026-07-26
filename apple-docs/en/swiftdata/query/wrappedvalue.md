---
title: wrappedValue
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/query/wrappedvalue
source_url: 'https://developer.apple.com/documentation/swiftdata/query/wrappedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query/wrappedvalue.json'
content_hash: 'sha256:0f52259a79c67d40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Query](../query.md)

# wrappedValue

<sub>Instance Property</sub>

The most recent fetched result from the Query.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var wrappedValue: Result { get }
```

## Discussion

> [!note] Note
> When an fetch error occurs, `wrappedValue` retains results from the last successful fetch. Its value will update once a new fetch succeeds.
