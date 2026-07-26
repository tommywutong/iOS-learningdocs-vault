---
title: 'init(x:y:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/annotationoverflowresolution/init(x:y:)'
source_url: 'https://developer.apple.com/documentation/charts/annotationoverflowresolution/init(x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/annotationoverflowresolution/init%28x%3Ay%3A%29.json'
content_hash: 'sha256:f30c60f80cc1f9de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AnnotationOverflowResolution](../annotationoverflowresolution.md)

# init(x:y:)

<sub>Initializer</sub>

Creates an AnnotationOverflowResolution with strategies for the X and Y dimensions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(x: AnnotationOverflowResolution.Strategy = .automatic, y: AnnotationOverflowResolution.Strategy = .automatic)
```

## Discussion

Parameters:

- x: The strategy to resolve X overflow.
- y: The strategy to resolve Y overflow.
