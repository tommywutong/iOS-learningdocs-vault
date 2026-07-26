---
title: delegate
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametaldisplaylink/delegate
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldisplaylink/delegate.json'
content_hash: 'sha256:f13f27b127b46576'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalDisplayLink](../cametaldisplaylink.md)

# delegate

<sub>Instance Property</sub>

An instance of a type your app implements that responds to the system’s callbacks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
weak var delegate: (any CAMetalDisplayLinkDelegate)? { get set }
```

## See Also

### Configuring a Display Link

- [preferredFrameRateRange](preferredframeraterange.md) — A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [preferredFrameLatency](preferredframelatency.md) — The amount of time, in frames, your app requests to render a frame.
