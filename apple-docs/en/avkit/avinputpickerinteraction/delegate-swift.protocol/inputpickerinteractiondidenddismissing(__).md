---
title: 'inputPickerInteractionDidEndDismissing(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractiondidenddismissing(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractiondidenddismissing(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinputpickerinteraction/delegate-swift.protocol/inputpickerinteractiondidenddismissing%28_%3A%29.json'
content_hash: 'sha256:ca29da8d8f8eb900'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVInputPickerInteraction](../../avinputpickerinteraction.md) · [Delegate](../delegate-swift.protocol.md)

# inputPickerInteractionDidEndDismissing(_:)

<sub>Instance Method</sub>

Tells the delegate that the input picker view has finished dismissing devices.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func inputPickerInteractionDidEndDismissing(_ inputPickerInteraction: AVInputPickerInteraction)
```

## Parameters

- `inputPickerInteraction` — The current AVInputPickerInteraction.

## Discussion

The `isPresented` property is set to `NO` at this point, indicating that the dismissal is complete.

## See Also

### Responding to life cycle events

- [- inputPickerInteractionWillBeginPresenting:](<inputpickerinteractionwillbeginpresenting(__).md>) — Tells the delegate that the input picker view is about to present devices.
- [- inputPickerInteractionDidEndPresenting:](<inputpickerinteractiondidendpresenting(__).md>) — Tells the delegate that the input picker view has finished presenting devices
- [- inputPickerInteractionWillBeginDismissing:](<inputpickerinteractionwillbegindismissing(__).md>) — Tells the delegate that the input picker view is about to dismiss devices.
