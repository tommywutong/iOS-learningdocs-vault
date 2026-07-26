---
title: title
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotation/title
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotation/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotation/title.json'
content_hash: 'sha256:d2b3422502bcdbbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotation](../mkannotation.md)

# title

<sub>Instance Property</sub>

The string containing the annotation’s title.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional var title: String? { get }
```

## Discussion

Use this optional property to supply a string that the annotation displays in the callout for the associated annotation view. If you specify a [detailCalloutAccessoryView](../mkannotationview/detailcalloutaccessoryview.md) object, setting the title isn’t required.

## See Also

### Title attributes

- [subtitle](subtitle.md) — The string containing the annotation’s subtitle.
