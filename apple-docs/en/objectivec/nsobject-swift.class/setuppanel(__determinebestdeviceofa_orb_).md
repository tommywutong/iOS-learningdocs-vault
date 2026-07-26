---
title: 'setupPanel(_:determineBestDeviceOfA:orB:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setuppanel(_:determinebestdeviceofa:orb:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setuppanel(_:determinebestdeviceofa:orb:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setuppanel%28_%3Adeterminebestdeviceofa%3Aorb%3A%29.json'
content_hash: 'sha256:4edf911f190f7827'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setupPanel(_:determineBestDeviceOfA:orB:)

<sub>Instance Method</sub>

Allows the delegate to specify which device is its preferred.

<sub>macOS</sub>

```swift
func setupPanel(_ aPanel: DRSetupPanel!, determineBestDeviceOfA deviceA: DRDevice!, orB device: DRDevice!) -> DRDevice!
```

## Parameters

- `aPanel` — The panel.

- `deviceA` — A candidate device. May be nil.

- `device` — A candidate device. May be nil.

## Return Value

One of the two device objects passed in.

## Discussion

When the setup panel is first displayed and again, each time a new device appears, the setup panel will ask the delegate to compare two devices to determine which is most suitable for their content to burn.
