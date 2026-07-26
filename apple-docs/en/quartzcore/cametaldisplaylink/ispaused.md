---
title: isPaused
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametaldisplaylink/ispaused
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/ispaused'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldisplaylink/ispaused.json'
content_hash: 'sha256:1aef60afaad04b63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalDisplayLink](../cametaldisplaylink.md)

# isPaused

<sub>Instance Property</sub>

A Boolean value that indicates whether the system suspends the display link’s notifications to the target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isPaused: Bool { get set }
```

## Discussion

You can instruct the display link to stop sending notifications to the delegate by setting the property to [true](../../swift/true.md). The property defaults to [false](../../swift/false.md).
