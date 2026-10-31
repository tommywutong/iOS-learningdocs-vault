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
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# compositionPickerView(_:didSelect:)

<sub>实例方法</sub>

当合成选择器视图中的所选合成更改时执行自定义任务。

> [!warning] 已废弃
> QuartzComposer API 已废弃。（定义 QC_SILENCE_DEPRECATION 可消除这些警告）

<sub>macOS</sub>

```swift
func compositionPickerView(_ pickerView: QCCompositionPickerView!, didSelect composition: QCComposition!)
```

## 参数

- `pickerView` — 选择发生更改的合成选择器视图。

- `composition` — 所选合成；若先前选定的合成不再被选中则为 `nil`。

## 讨论

当合成选择器视图中的所选合成更改时，Quartz Composer 会调用此方法。若要在此时执行自定义任务，请实现此方法。
