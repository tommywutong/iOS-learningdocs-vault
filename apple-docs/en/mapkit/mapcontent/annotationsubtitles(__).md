---
title: 'annotationSubtitles(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontent/annotationsubtitles(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontent/annotationsubtitles(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontent/annotationsubtitles%28_%3A%29.json'
content_hash: 'sha256:0dbf45df2a1c765b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContent](../mapcontent.md)

# annotationSubtitles(_:)

<sub>Instance Method</sub>

Sets the visibility of subtitles for markers and annotations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func annotationSubtitles(_ visibility: Visibility) -> some MapContent

```

## Parameters

- `visibility` — One of the `Visibility` settings. The default is [Visibility.automatic](../../swiftui/visibility/automatic.md), which results in the subtitle being visible only when the annotation is in a selected state.

## Return Value

Returns [MapContent](../mapcontent.md) whose subtitles have the visibility setting you specified.

## See Also

### Supplying annotation titles

- [annotationTitles(_:)](<annotationtitles(__).md>) — Sets the visibility of titles for markers and annotations.
