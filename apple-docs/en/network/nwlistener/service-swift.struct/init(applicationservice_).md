---
title: 'init(applicationService:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwlistener/service-swift.struct/init(applicationservice:)'
source_url: 'https://developer.apple.com/documentation/network/nwlistener/service-swift.struct/init(applicationservice:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/service-swift.struct/init%28applicationservice%3A%29.json'
content_hash: 'sha256:2fa696ba00c3dc1a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWListener](../../nwlistener.md) · [Service](../service-swift.struct.md)

# init(applicationService:)

<sub>Initializer</sub>

Creates a listener for apps that listen for connections from a network device picker.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(applicationService: String)
```

## Parameters

- `applicationService` — The name of the application service. This must match the name passed to the network device picker.

## Discussion

Use this initializer to setup a listener for application services.

Apps that register as advertising an application service should always have a listener waiting for a local connection. The system launches your app when the user selects the current device in a [DevicePicker](../../../devicediscoveryui/devicepicker.md) or [DDDevicePickerViewController](../../../devicediscoveryui/dddevicepickerviewcontroller.md). Create the listener as soon as your app launches, so that your app can connect with the requesting device.
