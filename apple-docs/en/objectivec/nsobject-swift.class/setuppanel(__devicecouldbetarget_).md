---
title: 'setupPanel(_:deviceCouldBeTarget:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setuppanel(_:devicecouldbetarget:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setuppanel(_:devicecouldbetarget:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setuppanel%28_%3Adevicecouldbetarget%3A%29.json'
content_hash: 'sha256:1edf6e9bfa8bf791'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setupPanel(_:deviceCouldBeTarget:)

<sub>Instance Method</sub>

Allows the delegate to determine if device can be used as a target.

<sub>macOS</sub>

```swift
func setupPanel(_ aPanel: DRSetupPanel!, deviceCouldBeTarget device: DRDevice!) -> Bool
```

## Parameters

- `aPanel` — The panel.

- `device` — The candidate device.

## Return Value

`YES` if the device is acceptable, `NO` if not.

## Discussion

This method is used to limit the menu to only those devices that you want to appear.  For example, a DVD burning application might use this to limit the menu to only devices that are capable of writing DVD-Rs.
