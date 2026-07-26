---
title: 'compositionPickerView(_:didSelect:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/compositionpickerview(_:didselect:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/compositionpickerview(_:didselect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/compositionpickerview%28_%3Adidselect%3A%29.json'
content_hash: 'sha256:7ff69269d8125d38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# compositionPickerView(_:didSelect:)

<sub>Instance Method</sub>

Performs custom tasks when the selected composition in the composition picker view changes.

> [!warning] Deprecated
> QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

<sub>macOS</sub>

```swift
func compositionPickerView(_ pickerView: QCCompositionPickerView!, didSelect composition: QCComposition!)
```

## Parameters

- `pickerView` — The composition picker view in which the selection changed.

- `composition` — The selected composition or `nil` if the previously selected composition is no longer selected.

## Discussion

Quartz Composer invokes this method when the selected composition in the composition picker view changes. Implement this method if you want to perform custom tasks at that time.
