---
title: 'init(anchor:content:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/userannotation/init(anchor:content:)-8u3r4'
source_url: 'https://developer.apple.com/documentation/mapkit/userannotation/init(anchor:content:)-8u3r4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/userannotation/init%28anchor%3Acontent%3A%29-8u3r4.json'
content_hash: 'sha256:fc167d48e698c735'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [UserAnnotation](../userannotation.md)

# init(anchor:content:)

<sub>Initializer</sub>

Creates an annotation that displays a person’s current location using the system styled user location indicator with the specified anchor point using a custom view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(anchor: UnitPoint = .center, @ViewBuilder content: @escaping (UserLocation) -> Content)
```

## Parameters

- `anchor` — A UnitPoint value that describes how to anchor the user location indicator to the person’s location. The default is [center](../../swiftui/unitpoint/center.md).

- `content` — The custom view to show at the person’s location.

## Return Value

Returns  a [UserAnnotation](../userannotation.md) that displays a persons current location using the specified anchor location.

## See Also

### Creating a user annotation

- [init()](<init().md>) — Creates an annotation that displays the person’s current location.
- [init(anchor:)](<init(anchor_).md>) — Creates an annotation that displays the person’s current location using the system styled user location indicator with the specified anchor point.
- [init(anchor:content:)](<init(anchor_content_)-3e78j.md>) — Create an annotation that displays the person’s current location of the user using a custom view.
