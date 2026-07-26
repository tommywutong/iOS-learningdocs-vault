---
title: preferredFrameLatency
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametaldisplaylink/preferredframelatency
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/preferredframelatency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldisplaylink/preferredframelatency.json'
content_hash: 'sha256:3919e4d482c62d3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalDisplayLink](../cametaldisplaylink.md)

# preferredFrameLatency

<sub>Instance Property</sub>

The amount of time, in frames, your app requests to render a frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preferredFrameLatency: Float { get set }
```

## Discussion

The final latency may be bigger if the system needs more time, such as for windowed modes on macOS.

> [!important] Important
> The only acceptable values are `1.0` and `2.0`.

## See Also

### Configuring a Display Link

- [preferredFrameRateRange](preferredframeraterange.md) — A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [delegate](delegate.md) — An instance of a type your app implements that responds to the system’s callbacks.
