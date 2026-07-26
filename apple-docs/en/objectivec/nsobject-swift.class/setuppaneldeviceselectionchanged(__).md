---
title: 'setupPanelDeviceSelectionChanged(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setuppaneldeviceselectionchanged(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setuppaneldeviceselectionchanged(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setuppaneldeviceselectionchanged%28_%3A%29.json'
content_hash: 'sha256:58d00b13d9cdbdac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setupPanelDeviceSelectionChanged(_:)

<sub>Instance Method</sub>

Sent by the default notification center when the device selection in the panel has changed.

<sub>macOS</sub>

```swift
func setupPanelDeviceSelectionChanged(_ aNotification: Notification!)
```

## Parameters

- `aNotification` — Notification object. This is always `DRSetupPanelDeviceSelectionChangedNotification`.

## Discussion

You can retrieve the `DRSetupPanel` object in question by sending `NSNotification` object to `aNotification`. The userInfo dictionary contains the single key DRSetupPanelSelectedDeviceKey whose value is the `DRDevice` object that is currently selected.
