---
title: AVInputPickerInteraction.Delegate
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinputpickerinteraction/delegate-swift.protocol
source_url: 'https://developer.apple.com/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol.json'
content_hash: 'sha256:a92e40a0fe0e1a73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInputPickerInteraction](../avinputpickerinteraction.md)

# AVInputPickerInteraction.Delegate

<sub>Protocol</sub>

The `AVInputPickerInteractionDelegate` protocol defines methods you use to receive notifications about transitions in an `AVInputPickerInteraction` object.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
protocol Delegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Responding to life cycle events

- [- inputPickerInteractionWillBeginPresenting:](<delegate-swift.protocol/inputpickerinteractionwillbeginpresenting(__).md>) — Tells the delegate that the input picker view is about to present devices.
- [- inputPickerInteractionDidEndPresenting:](<delegate-swift.protocol/inputpickerinteractiondidendpresenting(__).md>) — Tells the delegate that the input picker view has finished presenting devices
- [- inputPickerInteractionWillBeginDismissing:](<delegate-swift.protocol/inputpickerinteractionwillbegindismissing(__).md>) — Tells the delegate that the input picker view is about to dismiss devices.
- [- inputPickerInteractionDidEndDismissing:](<delegate-swift.protocol/inputpickerinteractiondidenddismissing(__).md>) — Tells the delegate that the input picker view has finished dismissing devices.

## See Also

### Setting the delegate

- [delegate](delegate-swift.property.md) — The input picker view’s delegate.
