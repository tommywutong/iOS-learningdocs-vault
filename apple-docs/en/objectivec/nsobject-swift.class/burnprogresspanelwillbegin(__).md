---
title: 'burnProgressPanelWillBegin(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/burnprogresspanelwillbegin(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/burnprogresspanelwillbegin(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/burnprogresspanelwillbegin%28_%3A%29.json'
content_hash: 'sha256:ab8f0c7e78e7e1f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# burnProgressPanelWillBegin(_:)

<sub>Instance Method</sub>

Notification sent by the panel before display.

<sub>macOS</sub>

```swift
func burnProgressPanelWillBegin(_ aNotification: Notification!)
```

## Parameters

- `aNotification` — Always `DRBurnProgressPanelDidFinishNotification`

## Discussion

If the delegate implements this method it will receive the message immediately before the panel is displayed.
