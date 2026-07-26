---
title: 'annotationTitles(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontent/annotationtitles(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontent/annotationtitles(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontent/annotationtitles%28_%3A%29.json'
content_hash: 'sha256:7c7239df716337b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContent](../mapcontent.md)

# annotationTitles(_:)

<sub>Instance Method</sub>

Sets the visibility of titles for markers and annotations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func annotationTitles(_ visibility: Visibility) -> some MapContent

```

## Parameters

- `visibility` — One of the [Visibility](../../swiftui/visibility.md) settings. The default is [Visibility.automatic](../../swiftui/visibility/automatic.md) visibility, that results in the title always being visible.

## Return Value

Returns [MapContent](../mapcontent.md) whose titles have the visibility setting you specified.

## See Also

### Supplying annotation titles

- [annotationSubtitles(_:)](<annotationsubtitles(__).md>) — Sets the visibility of subtitles for markers and annotations.
