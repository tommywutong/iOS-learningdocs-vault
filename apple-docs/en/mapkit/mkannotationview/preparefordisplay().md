---
title: prepareForDisplay()
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/preparefordisplay()
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/preparefordisplay()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/preparefordisplay%28%29.json'
content_hash: 'sha256:58ce4c200511a85a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# prepareForDisplay()

<sub>Instance Method</sub>

Notifies the annotation view that the map view is about to display it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func prepareForDisplay()
```

## Discussion

Use this method to prepare the content of your annotation view.

## See Also

### Creating and preparing an annotation view

- [- initWithAnnotation:reuseIdentifier:](<init(annotation_reuseidentifier_).md>) — Creates and returns a new annotation view.
- [- initWithCoder:](<init(coder_).md>) — Creates an annotation view using data from the specified unarchiver.
- [- prepareForReuse](<prepareforreuse().md>) — Calls this method when removing the view from the reuse queue.
