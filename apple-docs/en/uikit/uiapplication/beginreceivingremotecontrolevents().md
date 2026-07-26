---
title: beginReceivingRemoteControlEvents()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/beginreceivingremotecontrolevents()
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/beginreceivingremotecontrolevents()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/beginreceivingremotecontrolevents%28%29.json'
content_hash: 'sha256:75456848ca2df20e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# beginReceivingRemoteControlEvents()

<sub>Instance Method</sub>

Tells the app to begin receiving remote-control events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func beginReceivingRemoteControlEvents()
```

## Discussion

In iOS 7.1 and later, use the shared [MPRemoteCommandCenter](../../mediaplayer/mpremotecommandcenter.md) object to register for remote control events. You do not need to call this method when using the shared command center object.

This method starts the delivery of remote control events using the responder chain. Remote-control events originate as commands issued by headsets and external accessories that are intended to control multimedia presented by an app. To stop the reception of remote-control events, you must call [- endReceivingRemoteControlEvents](<endreceivingremotecontrolevents().md>).

## See Also

### Receiving remote control events

- [- endReceivingRemoteControlEvents](<endreceivingremotecontrolevents().md>) — Tells the app to stop receiving remote-control events.
