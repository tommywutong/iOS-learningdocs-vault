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
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setupPanel(_:determineBestDeviceOfA:orB:)

<sub>实例方法</sub>

允许委托指定其首选设备。

<sub>macOS</sub>

```swift
func setupPanel(_ aPanel: DRSetupPanel!, determineBestDeviceOfA deviceA: DRDevice!, orB device: DRDevice!) -> DRDevice!
```

## 参数

- `aPanel` — 面板。

- `deviceA` — 候选设备。可能为 nil。

- `device` — 候选设备。可能为 nil。

## 返回值

传入的两个设备对象之一。

## 讨论

当首次显示设置面板时，以及每次出现新设备时，设置面板都会要求委托比较两个设备，以确定哪个最适合刻录其内容。
