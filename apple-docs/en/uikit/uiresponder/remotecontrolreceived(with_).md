---
title: 'remoteControlReceived(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/remotecontrolreceived(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/remotecontrolreceived(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/remotecontrolreceived%28with%3A%29.json'
content_hash: 'sha256:ddb368e2896206ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# remoteControlReceived(with:)

<sub>Instance Method</sub>

Tells the object when a remote-control event is received.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func remoteControlReceived(with event: UIEvent?)
```

## Parameters

- `event` — An event object encapsulating a remote-control command. Remote-control events have a type of [UIEventTypeRemoteControl](../uievent/eventtype/remotecontrol.md).

## Discussion

Remote-control events originate as commands from external accessories, including headsets. An app responds to these commands by controlling audio or video media presented to the user. The receiving responder object should examine the [subtype](../uievent/subtype.md) of `event` to determine the intended command — for example, _play_ ([UIEventSubtypeRemoteControlPlay](../uievent/eventsubtype/remotecontrolplay.md)) — and then proceed accordingly.

To allow delivery of remote-control events, you must call the [- beginReceivingRemoteControlEvents](<../uiapplication/beginreceivingremotecontrolevents().md>) method of [UIApplication](../uiapplication.md). To turn off delivery of remote-control events, call the [- endReceivingRemoteControlEvents](<../uiapplication/endreceivingremotecontrolevents().md>) method.
