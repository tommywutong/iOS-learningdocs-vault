---
title: 'setSelected(_:animated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkannotationview/setselected(_:animated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/setselected(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/setselected%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:839672e7a47b487d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# setSelected(_:animated:)

<sub>Instance Method</sub>

Sets the selection state of the annotation view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setSelected(_ selected: Bool, animated: Bool)
```

## Parameters

- `selected` — Contains the value [true](../../swift/true.md) if the view displays in a selected state.

- `animated` — Set to [true](../../swift/true.md) if the map view animates the change in selection state.

## Discussion

Dont call this method directly. An [MKMapView](../mkmapview.md) object calls this method in response to user interactions with the annotation.

## See Also

### Related Documentation

- [- selectAnnotation:animated:](<../mkmapview/selectannotation(__animated_).md>) — Selects the specified annotation and displays a callout view for it.

### Managing the selection state

- [selected](isselected.md) — A Boolean value that indicates whether the annotation view is in a selected state.
