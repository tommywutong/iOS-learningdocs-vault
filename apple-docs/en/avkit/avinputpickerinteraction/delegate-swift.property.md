---
title: delegate
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinputpickerinteraction/delegate-swift.property
source_url: 'https://developer.apple.com/documentation/avkit/avinputpickerinteraction/delegate-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinputpickerinteraction/delegate-swift.property.json'
content_hash: 'sha256:c1d0190417e8be25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInputPickerInteraction](../avinputpickerinteraction.md)

# delegate

<sub>Instance Property</sub>

The input picker view’s delegate.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
weak var delegate: (any AVInputPickerInteraction.Delegate)? { get set }
```

## See Also

### Setting the delegate

- [Delegate](delegate-swift.protocol.md) — The `AVInputPickerInteractionDelegate` protocol defines methods you use to receive notifications about transitions in an `AVInputPickerInteraction` object.
