---
title: 'inputPickerInteractionWillBeginDismissing(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractionwillbegindismissing(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractionwillbegindismissing(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractionwillbegindismissing%28_%3A%29.json'
content_hash: 'sha256:c2d39b93784895c2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVInputPickerInteraction](../../avinputpickerinteraction.md) · [Delegate](../delegate-swift.protocol.md)

# inputPickerInteractionWillBeginDismissing(_:)

<sub>Instance Method</sub>

Tells the delegate that the input picker view is about to dismiss devices.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func inputPickerInteractionWillBeginDismissing(_ inputPickerInteraction: AVInputPickerInteraction)
```

## Parameters

- `inputPickerInteraction` — The current AVInputPickerInteraction.

## See Also

### Responding to life cycle events

- [- inputPickerInteractionWillBeginPresenting:](<inputpickerinteractionwillbeginpresenting(__).md>) — Tells the delegate that the input picker view is about to present devices.
- [- inputPickerInteractionDidEndPresenting:](<inputpickerinteractiondidendpresenting(__).md>) — Tells the delegate that the input picker view has finished presenting devices
- [- inputPickerInteractionDidEndDismissing:](<inputpickerinteractiondidenddismissing(__).md>) — Tells the delegate that the input picker view has finished dismissing devices.
