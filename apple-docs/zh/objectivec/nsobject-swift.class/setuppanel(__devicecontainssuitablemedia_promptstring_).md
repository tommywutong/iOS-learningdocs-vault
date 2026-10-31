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
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setupPanel(_:deviceContainsSuitableMedia:promptString:)

<sub>实例方法</sub>

此委托方法允许委托确定设备中插入的介质是否适合要执行的操作。

<sub>macOS</sub>

```swift
func setupPanel(_ aPanel: DRSetupPanel!, deviceContainsSuitableMedia device: DRDevice!, promptString prompt: AutoreleasingUnsafeMutablePointer<NSString?>!) -> Bool
```

## 参数

- `aPanel` — 面板。

- `device` — 包含所询问介质的设备。

- `prompt` — 指向 NSString 存储的指针。回传一个描述介质状态的 NSString 对象。

## 返回值

返回 `NO` 以禁用默认按钮。
