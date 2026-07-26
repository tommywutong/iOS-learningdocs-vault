---
title: objectWillChange
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/imagerenderer/objectwillchange
source_url: 'https://developer.apple.com/documentation/swiftui/imagerenderer/objectwillchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/imagerenderer/objectwillchange.json'
content_hash: 'sha256:1a6060804ac2108e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImageRenderer](../imagerenderer.md)

# objectWillChange

<sub>Instance Property</sub>

A publisher that informs subscribers of changes to the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final let objectWillChange: PassthroughSubject<Void, Never>
```

## Discussion

The renderer’s [ObjectWillChangePublisher](../../combine/observableobject/objectwillchangepublisher.md) publishes `Void` elements. Subscribers should interpret any event as indicating that the contents of the image may have changed.

## See Also

### Producing a stream of images

- [isObservationEnabled](isobservationenabled.md) — If observers of this observed object should be notified when the produced image changes.
