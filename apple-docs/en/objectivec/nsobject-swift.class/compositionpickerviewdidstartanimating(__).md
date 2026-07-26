---
title: 'compositionPickerViewDidStartAnimating(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/compositionpickerviewdidstartanimating(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/compositionpickerviewdidstartanimating(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/compositionpickerviewdidstartanimating%28_%3A%29.json'
content_hash: 'sha256:ee3ebec42a6dde02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# compositionPickerViewDidStartAnimating(_:)

<sub>Instance Method</sub>

Performs custom tasks when the composition picker view starts animating a composition.

> [!warning] Deprecated
> QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

<sub>macOS</sub>

```swift
func compositionPickerViewDidStartAnimating(_ pickerView: QCCompositionPickerView!)
```

## Parameters

- `pickerView` — The composition picker view in which the composition started animating.

## Discussion

Quartz Composer invokes  this method when  the composition picker view starts animating a composition. Implement this method if you want to perform custom tasks at that time.
