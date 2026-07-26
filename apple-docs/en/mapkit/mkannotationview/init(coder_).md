---
title: 'init(coder:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkannotationview/init(coder:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/init%28coder%3A%29.json'
content_hash: 'sha256:eb2173292a647101'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# init(coder:)

<sub>Initializer</sub>

Creates an annotation view using data from the specified unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(coder aDecoder: NSCoder)
```

## Parameters

- `aDecoder` — The unarchiver to read data from.

## See Also

### Creating and preparing an annotation view

- [- initWithAnnotation:reuseIdentifier:](<init(annotation_reuseidentifier_).md>) — Creates and returns a new annotation view.
- [- prepareForReuse](<prepareforreuse().md>) — Calls this method when removing the view from the reuse queue.
- [- prepareForDisplay](<preparefordisplay().md>) — Notifies the annotation view that the map view is about to display it.
