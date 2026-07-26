---
title: amount
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersionchangecontext/amount
source_url: 'https://developer.apple.com/documentation/swiftui/immersionchangecontext/amount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersionchangecontext/amount.json'
content_hash: 'sha256:f890440155377439'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersionChangeContext](../immersionchangecontext.md)

# amount

<sub>Instance Property</sub>

The current amount of immersion.

<sub>macOS, visionOS</sub>

```swift
let amount: Double?
```

## Discussion

Your app can display virtual content using [ImmersiveSpace](../immersivespace.md) and the different immersion styles to create immersive experiences. Depending on the immersion style, none of it, parts of it, or a all of video pass-through are occluded by your app while having an Immersive Space opened, and the amount of it is represented by this value.

Some immersion styles allow changing the amount interactively by turning the Digital Crown.

This value is `nil`, if your app currently does not provide any immersive experience at all.
