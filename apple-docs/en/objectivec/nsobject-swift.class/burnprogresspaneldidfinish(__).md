---
title: 'burnProgressPanelDidFinish(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/burnprogresspaneldidfinish(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/burnprogresspaneldidfinish(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/burnprogresspaneldidfinish%28_%3A%29.json'
content_hash: 'sha256:4cd35337c1b64121'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# burnProgressPanelDidFinish(_:)

<sub>Instance Method</sub>

Notification sent by the panel after ordering out.

<sub>macOS</sub>

```swift
func burnProgressPanelDidFinish(_ aNotification: Notification!)
```

## Parameters

- `aNotification` — Always `DRBurnProgressPanelDidFinishNotification`

## Discussion

If the delegate implements this method it will receive the message after the panel is removed from display.
