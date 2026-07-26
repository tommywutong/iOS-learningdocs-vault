---
title: targetPresentationTimestamp
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametaldisplaylink/update/targetpresentationtimestamp
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/update/targetpresentationtimestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldisplaylink/update/targetpresentationtimestamp.json'
content_hash: 'sha256:f3b328b4ef691602'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Animation](../../../quartzcore.md) · [CAMetalDisplayLink](../../cametaldisplaylink.md) · [Update](../update.md)

# targetPresentationTimestamp

<sub>Instance Property</sub>

The time the system estimates until the display of the next frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var targetPresentationTimestamp: CFTimeInterval { get }
```

## Discussion

Update your animations based on the time difference between this timestamp and the previous timestamp.
