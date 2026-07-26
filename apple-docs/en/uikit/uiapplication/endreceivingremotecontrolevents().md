---
title: endReceivingRemoteControlEvents()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/endreceivingremotecontrolevents()
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/endreceivingremotecontrolevents()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/endreceivingremotecontrolevents%28%29.json'
content_hash: 'sha256:6296938a7a4ae6a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# endReceivingRemoteControlEvents()

<sub>Instance Method</sub>

Tells the app to stop receiving remote-control events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func endReceivingRemoteControlEvents()
```

## Discussion

In iOS 7.1 and later, use the shared [MPRemoteCommandCenter](../../mediaplayer/mpremotecommandcenter.md) object to unregister for remote control events. You do not need to call this method when using the shared command center object.

This method stops the delivery of remote control events using the responder chain. Remote-control events originate as commands issued by headsets and external accessories that are intended to control multimedia presented by an app.

## See Also

### Receiving remote control events

- [- beginReceivingRemoteControlEvents](<beginreceivingremotecontrolevents().md>) — Tells the app to begin receiving remote-control events.
