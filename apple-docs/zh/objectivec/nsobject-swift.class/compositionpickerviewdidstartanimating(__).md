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
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# compositionPickerViewDidStartAnimating(_:)

<sub>实例方法</sub>

当合成选择器视图开始为合成设置动画时执行自定义任务。

> [!warning] 已废弃
> QuartzComposer API 已废弃。（定义 QC_SILENCE_DEPRECATION 可消除这些警告）

<sub>macOS</sub>

```swift
func compositionPickerViewDidStartAnimating(_ pickerView: QCCompositionPickerView!)
```

## 参数

- `pickerView` — 合成开始设置动画的合成选择器视图。

## 讨论

当合成选择器视图开始为合成设置动画时，Quartz Composer 会调用此方法。若要在此时执行自定义任务，请实现此方法。
