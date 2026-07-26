---
title: 'eraseProgressPanelWillBegin(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/eraseprogresspanelwillbegin(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/eraseprogresspanelwillbegin(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/eraseprogresspanelwillbegin%28_%3A%29.json'
content_hash: 'sha256:2e6f68b0f683e10a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# eraseProgressPanelWillBegin(_:)

<sub>Instance Method</sub>

Notification sent by the panel before display.

<sub>macOS</sub>

```swift
func eraseProgressPanelWillBegin(_ aNotification: Notification!)
```

## Parameters

- `aNotification` — Always `DREraseProgressPanelWillBeginNotification` You can retrieve the `DREraseProgressPanel` object in question by sending [object](../../foundation/nsnotification/object.md) to `aNotification`.

## Discussion

If the delegate implements this method it will receive the message immediately before the panel is displayed.
