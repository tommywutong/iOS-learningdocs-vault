---
title: init()
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/userannotation/init()
source_url: 'https://developer.apple.com/documentation/mapkit/userannotation/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/userannotation/init%28%29.json'
content_hash: 'sha256:d43a0c8bc1e05675'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [UserAnnotation](../userannotation.md)

# init()

<sub>Initializer</sub>

Creates an annotation that displays the person’s current location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init() where Content == DefaultUserAnnotationContent
```

## See Also

### Creating a user annotation

- [init(anchor:)](<init(anchor_).md>) — Creates an annotation that displays the person’s current location using the system styled user location indicator with the specified anchor point.
- [init(anchor:content:)](<init(anchor_content_)-8u3r4.md>) — Creates an annotation that displays a person’s current location using the system styled user location indicator with the specified anchor point using a custom view.
- [init(anchor:content:)](<init(anchor_content_)-3e78j.md>) — Create an annotation that displays the person’s current location of the user using a custom view.
