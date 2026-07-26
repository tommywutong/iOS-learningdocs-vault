---
title: 'init(anchor:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/userannotation/init(anchor:)'
source_url: 'https://developer.apple.com/documentation/mapkit/userannotation/init(anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/userannotation/init%28anchor%3A%29.json'
content_hash: 'sha256:c854a10fce62467e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [UserAnnotation](../userannotation.md)

# init(anchor:)

<sub>Initializer</sub>

Creates an annotation that displays the person’s current location using the system styled user location indicator with the specified anchor point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(anchor: UnitPoint = .center) where Content == EmptyView
```

## Parameters

- `anchor` — How to anchor the user location indicator around the user’s location. The default is [center](../../swiftui/unitpoint/center.md).

## See Also

### Creating a user annotation

- [init()](<init().md>) — Creates an annotation that displays the person’s current location.
- [init(anchor:content:)](<init(anchor_content_)-8u3r4.md>) — Creates an annotation that displays a person’s current location using the system styled user location indicator with the specified anchor point using a custom view.
- [init(anchor:content:)](<init(anchor_content_)-3e78j.md>) — Create an annotation that displays the person’s current location of the user using a custom view.
