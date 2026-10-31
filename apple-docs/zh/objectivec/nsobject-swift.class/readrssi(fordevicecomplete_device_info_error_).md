---
title: 'readRSSI(forDeviceComplete:device:info:error:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/readrssi(fordevicecomplete:device:info:error:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/readrssi(fordevicecomplete:device:info:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/readrssi%28fordevicecomplete%3Adevice%3Ainfo%3Aerror%3A%29.json'
content_hash: 'sha256:641179ada7e976bd'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# readRSSI(forDeviceComplete:device:info:error:)

<sub>实例方法</sub>

<sub>macOS</sub>

```swift
func readRSSI(forDeviceComplete controller: Any!, device: IOBluetoothDevice!, info: UnsafeMutablePointer<BluetoothHCIRSSIInfo>!, error: IOReturn)
```

## 参数

- `controller` — 发送此委托消息的控制器对象。

- `device` — `IOBluetooth` 设备。

- `info` — 指向信息的指针。

## 讨论

当发生 RSSI 命令完成事件时会调用此委托。这可能是因为你发出了 `-readRSSIForDevice:` 命令，或者同一控制器上的其他应用也发出了该命令。
