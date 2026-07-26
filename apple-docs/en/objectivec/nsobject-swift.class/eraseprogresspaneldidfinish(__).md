---
title: 'eraseProgressPanelDidFinish(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/eraseprogresspaneldidfinish(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/eraseprogresspaneldidfinish(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/eraseprogresspaneldidfinish%28_%3A%29.json'
content_hash: 'sha256:ab60b3f5e6dc0362'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# eraseProgressPanelDidFinish(_:)

<sub>Instance Method</sub>

Notification sent by the panel after ordering out.

<sub>macOS</sub>

```swift
func eraseProgressPanelDidFinish(_ aNotification: Notification!)
```

## Parameters

- `aNotification` — Always `DREraseProgressPanelDidFinishNotification` You can retrieve the `DREraseProgressPanel` object in question by sending [object](../../foundation/nsnotification/object.md) to `aNotification`.

## Discussion

If the delegate implements this method it will receive the message after the panel is removed from display.
