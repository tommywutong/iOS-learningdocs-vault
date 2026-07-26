---
title: 'compositionPickerViewWillStopAnimating(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/compositionpickerviewwillstopanimating(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/compositionpickerviewwillstopanimating(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/compositionpickerviewwillstopanimating%28_%3A%29.json'
content_hash: 'sha256:b323ffe90515911b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# compositionPickerViewWillStopAnimating(_:)

<sub>Instance Method</sub>

Performs custom tasks when the composition picker view stops animating a composition.

> [!warning] Deprecated
> QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

<sub>macOS</sub>

```swift
func compositionPickerViewWillStopAnimating(_ pickerView: QCCompositionPickerView!)
```

## Parameters

- `pickerView` — The composition picker view in which the composition stopped animating.

## Discussion

Quartz Composer invokes  this method whenever the composition picker view stops animating a composition. Implement this method if you want to perform custom tasks at that time.
