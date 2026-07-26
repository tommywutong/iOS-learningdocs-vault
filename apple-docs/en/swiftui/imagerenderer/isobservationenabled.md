---
title: isObservationEnabled
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+, macOS 14.2+, tvOS 17.2+, visionOS 1.0+, watchOS 10.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/imagerenderer/isobservationenabled
source_url: 'https://developer.apple.com/documentation/swiftui/imagerenderer/isobservationenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/imagerenderer/isobservationenabled.json'
content_hash: 'sha256:350379f669e52493'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImageRenderer](../imagerenderer.md)

# isObservationEnabled

<sub>Instance Property</sub>

If observers of this observed object should be notified when the produced image changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) final var isObservationEnabled: Bool { get set }
```

## See Also

### Producing a stream of images

- [objectWillChange](objectwillchange.md) — A publisher that informs subscribers of changes to the image.
