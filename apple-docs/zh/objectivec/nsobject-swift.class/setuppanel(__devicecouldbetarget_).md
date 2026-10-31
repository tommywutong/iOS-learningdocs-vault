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
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setupPanel(_:deviceCouldBeTarget:)

<sub>实例方法</sub>

允许委托确定设备是否可用作目标。

<sub>macOS</sub>

```swift
func setupPanel(_ aPanel: DRSetupPanel!, deviceCouldBeTarget device: DRDevice!) -> Bool
```

## 参数

- `aPanel` — 面板。

- `device` — 候选设备。

## 返回值

若设备可接受则为 `YES`，否则为 `NO`。

## 讨论

此方法用于将菜单限制为仅显示你希望出现的设备。例如，DVD 刻录应用可能用它将菜单限制为仅能写入 DVD-R 的设备。
