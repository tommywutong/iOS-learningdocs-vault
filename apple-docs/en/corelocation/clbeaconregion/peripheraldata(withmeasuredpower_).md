---
title: 'peripheralData(withMeasuredPower:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clbeaconregion/peripheraldata(withmeasuredpower:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconregion/peripheraldata(withmeasuredpower:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconregion/peripheraldata%28withmeasuredpower%3A%29.json'
content_hash: 'sha256:2fac4bb9eaac4944'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeaconRegion](../clbeaconregion.md)

# peripheralData(withMeasuredPower:)

<sub>Instance Method</sub>

Retrieves data that you can use to advertise the current device as a beacon.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func peripheralData(withMeasuredPower measuredPower: NSNumber?) -> NSMutableDictionary
```

## Parameters

- `measuredPower` — The received signal strength indicator (RSSI) value, measured in decibels, for the device. This value represents the measured strength of the beacon from one meter away that Core Location uses during ranging. Specify `nil` to use the default value for the device.

## Return Value

A dictionary of data that you can use in conjunction with a [CBPeripheralManager](../../corebluetooth/cbperipheralmanager.md) to advertise the current device as a beacon.

## Discussion

The returned dictionary encodes the beacon’s identifying information, along with other information needed to advertise the beacon. You don’t need to access the dictionary contents directly. Pass the dictionary to the [startAdvertising(_:)](<../../corebluetooth/cbperipheralmanager/startadvertising(__).md>) method of a [CBPeripheralManager](../../corebluetooth/cbperipheralmanager.md) to begin advertising the beacon.
