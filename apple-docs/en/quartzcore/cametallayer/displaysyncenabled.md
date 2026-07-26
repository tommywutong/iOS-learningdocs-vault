---
title: displaySyncEnabled
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+, macOS 10.13+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/displaysyncenabled
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/displaysyncenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/displaysyncenabled.json'
content_hash: 'sha256:38089058322fecc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# displaySyncEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether the layer synchronizes its updates to the display’s refresh rate.

<sub>Mac Catalyst, macOS</sub>

```swift
var displaySyncEnabled: Bool { get set }
```

## Discussion

Set this value to [true](../../swift/true.md) to synchronize the presentation of the layer’s contents with the display’s refresh, also known as _vsync_ or _vertical sync_. If [false](../../swift/false.md), the layer presents new content more quickly, but possibly with brief visual artifacts (_screen tearing_).

The default value is [true](../../swift/true.md).

## See Also

### Configuring Presentation Behavior

- [presentsWithTransaction](presentswithtransaction.md) — A Boolean value that determines whether the layer presents its content using a Core Animation transaction.
