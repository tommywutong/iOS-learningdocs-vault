---
title: DevicePicker
framework: DeviceDiscoveryUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 16.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/devicediscoveryui/devicepicker
source_url: 'https://developer.apple.com/documentation/devicediscoveryui/devicepicker'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/devicediscoveryui/devicepicker.json'
content_hash: 'sha256:afca6ef5e520885a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [DeviceDiscoveryUI](../devicediscoveryui.md)

# DevicePicker

<sub>Structure</sub>

A SwiftUI view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
@MainActor @preconcurrency struct DevicePicker<Label, Fallback> where Label : View, Fallback : View
```

## Overview

Always display the picker as a full-screen, modal view. If the user selects a device, the system calls the closure you passed as the `onSelect` parameter. If the user cancels the picker, it silently closes.

```swift
DevicePicker(
    .applicationService(name: "MyAppService")) { endpoint in
        myDeviceManager.connectTo(endpoint: endpoint)
    } label: {
        Text("Connect to a local device.")
    } fallback: {
        Text("Not supported.")
    } parameters: {
        // This example uses the default application services parameters;
        // however, you can add a NWProtocolFramer to provide application-level
        // messaging.
        .applicationService
    }
```

If the current device doesn’t support device discovery, the system displays the fallback view instead of the device picker. Use the DevicePickerSupportedAction environment value to check whether the current device supports device discovery.

```swift
struct SettingsView: View {

    @Environment{\.devicePickerSupports} var myDevicePickerSupports
    @Binding var showDevicePicker: Bool

    var body: some View {
        if myDevicePickerSupports(.applicationService("MyAppService"),
                                  parameters: { .applicationService }) {
            Button("Select A Device") {
                // Display a device picker.
                showDevicePicker = true
            }
        }
    }
}
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a device picker

- [init(_:onSelect:label:fallback:parameters:)](<devicepicker/init(__onselect_label_fallback_parameters_).md>) — Creates a view that displays available devices.
- [init(_:access:onSelect:label:fallback:parameters:)](<devicepicker/init(__access_onselect_label_fallback_parameters_).md>) — Creates a view that displays the available devices with the access level, section handler, and other parameters you supply.

## See Also

### Pairing with nearby devices

- [DDDevicePickerViewController](dddevicepickerviewcontroller.md) — A UIKit view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.
- [DevicePickerSupportedAction](devicepickersupportedaction.md) — An environment value that indicates whether the current device supports device discovery.
- [Connecting a tvOS app to other devices over the local network](connecting-a-tvos-app-to-other-devices-over-the-local-network.md) — Display a view in your tvOS app that lists available iOS, iPadOS, and watchOS devices that the user can connect to over their local network.
