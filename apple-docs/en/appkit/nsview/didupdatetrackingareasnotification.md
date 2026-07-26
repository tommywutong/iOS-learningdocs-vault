---
title: didUpdateTrackingAreasNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.5+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsview/didupdatetrackingareasnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsview/didupdatetrackingareasnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsview/didupdatetrackingareasnotification.json'
content_hash: 'sha256:27a02c0d336e5f69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSView](../nsview.md)

# didUpdateTrackingAreasNotification

<sub>Type Property</sub>

Posted whenever a view recalculates its tracking areas.

<sub>macOS</sub>

```swift
class let didUpdateTrackingAreasNotification: NSNotification.Name
```

## Discussion

It is sent after the view receives [- updateTrackingAreas](<updatetrackingareas().md>).

## See Also

### Managing Tracking Areas

- [- addTrackingArea:](<addtrackingarea(__).md>) — Adds a given tracking area to the view.
- [- removeTrackingArea:](<removetrackingarea(__).md>) — Removes a given tracking area from the view.
- [trackingAreas](trackingareas.md) — An array of the view’s tracking areas.
- [- updateTrackingAreas](<updatetrackingareas().md>) — Invoked automatically when the view’s geometry changes such that its tracking areas need to be recalculated.
