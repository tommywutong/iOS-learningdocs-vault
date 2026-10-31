---
title: 'setupPanelDeviceSelectionChanged(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setuppaneldeviceselectionchanged(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setuppaneldeviceselectionchanged(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setuppaneldeviceselectionchanged%28_%3A%29.json'
content_hash: 'sha256:58d00b13d9cdbdac'
translated: true
---
> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setupPanelDeviceSelectionChanged(_:)

<sub>实例方法</sub>

当面板中的设备选中项更改时，由默认通知中心发送。

<sub>macOS</sub>

```swift
func setupPanelDeviceSelectionChanged(_ aNotification: Notification!)
```

## 参数

- `aNotification` — 通知对象。始终为 `DRSetupPanelDeviceSelectionChangedNotification`。

## 讨论

你可以通过向 `aNotification` 发送 `NSNotification` 的 object 来检索相关的 `DRSetupPanel` 对象。userInfo 字典包含单一键 DRSetupPanelSelectedDeviceKey，其值为当前选中的 `DRDevice` 对象。
