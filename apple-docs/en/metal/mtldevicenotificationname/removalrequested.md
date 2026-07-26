---
title: removalRequested
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.13+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevicenotificationname/removalrequested
source_url: 'https://developer.apple.com/documentation/metal/mtldevicenotificationname/removalrequested'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevicenotificationname/removalrequested.json'
content_hash: 'sha256:76ddc10f55891abb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDeviceNotificationName](../mtldevicenotificationname.md)

# removalRequested

<sub>Type Property</sub>

A notification that Metal sends to observers when a person requests to remove a GPU device from the system.

> [!warning] Deprecated
> Device notifications are not applicable on Apple Silicon

<sub>macOS</sub>

```swift
static let removalRequested: MTLDeviceNotificationName
```

## Discussion

This notification tells your app to stop using an [MTLDevice](../mtldevice.md) instance by releasing any objects and resources your app created with it.

> [!note] Note
> Metal removes the device instance from the array it returns with its methods — such as [MTLCopyAllDevices](<../mtlcopyalldevices().md>) — before sending this notification.

## See Also

### Creating a notification name

- [MTLDeviceWasAddedNotification](wasadded.md) — A notification that Metal sends to observers when the system adds a GPU device. _(deprecated)_
- [MTLDeviceWasRemovedNotification](wasremoved.md) — A notification that Metal sends to observers when the system removes a GPU device. _(deprecated)_
- [init(rawValue:)](<init(rawvalue_).md>) — Creates a Metal device notification name from a string. _(deprecated)_
