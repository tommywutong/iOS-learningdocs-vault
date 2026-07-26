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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# readRSSI(forDeviceComplete:device:info:error:)

<sub>Instance Method</sub>

<sub>macOS</sub>

```swift
func readRSSI(forDeviceComplete controller: Any!, device: IOBluetoothDevice!, info: UnsafeMutablePointer<BluetoothHCIRSSIInfo>!, error: IOReturn)
```

## Parameters

- `controller` — Controller object that sent this delegate message.

- `device` — The `IOBluetooth` device.

- `info` — A pointer to the info.

## Discussion

This delegate gets invoked when an RSSI command complete event occurs. This could occur because you invoked it by issuing a `-readRSSIForDevice:` command, or someone else did from another app on the same controller.
