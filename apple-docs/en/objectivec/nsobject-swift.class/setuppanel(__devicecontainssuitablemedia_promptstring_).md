---
title: 'setupPanel(_:deviceContainsSuitableMedia:promptString:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setuppanel(_:devicecontainssuitablemedia:promptstring:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setuppanel(_:devicecontainssuitablemedia:promptstring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setuppanel%28_%3Adevicecontainssuitablemedia%3Apromptstring%3A%29.json'
content_hash: 'sha256:c956ef584fba3a58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setupPanel(_:deviceContainsSuitableMedia:promptString:)

<sub>Instance Method</sub>

This delegate method allows the delegate to determine if the media inserted in the device is suitable for whatever operation is to be performed.

<sub>macOS</sub>

```swift
func setupPanel(_ aPanel: DRSetupPanel!, deviceContainsSuitableMedia device: DRDevice!, promptString prompt: AutoreleasingUnsafeMutablePointer<NSString?>!) -> Bool
```

## Parameters

- `aPanel` — The panel.

- `device` — The device that contains the media being asked about.

- `prompt` — A pointer to storage for an NSString. Pass back an NSString object describing the media state.

## Return Value

Return `NO` to disable the default button.
