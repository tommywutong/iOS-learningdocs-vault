---
title: wasRemoved
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.13+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevicenotificationname/wasremoved
source_url: 'https://developer.apple.com/documentation/metal/mtldevicenotificationname/wasremoved'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevicenotificationname/wasremoved.json'
content_hash: 'sha256:e84d29392da9b2e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDeviceNotificationName](../mtldevicenotificationname.md)

# wasRemoved

<sub>Type Property</sub>

A notification that Metal sends to observers when the system removes a GPU device.

> [!warning] Deprecated
> Device notifications are not applicable on Apple Silicon

<sub>macOS</sub>

```swift
static let wasRemoved: MTLDeviceNotificationName
```

## Discussion

This notification tells your app that an [MTLDevice](../mtldevice.md) instance and its methods are no longer valid to avoid runtime failures.

> [!important] Important
> If a person removes a GPU without warning, this notification may be posted without a prior [MTLDeviceRemovalRequestedNotification](removalrequested.md) notification.

## See Also

### Creating a notification name

- [MTLDeviceWasAddedNotification](wasadded.md) — A notification that Metal sends to observers when the system adds a GPU device. _(deprecated)_
- [MTLDeviceRemovalRequestedNotification](removalrequested.md) — A notification that Metal sends to observers when a person requests to remove a GPU device from the system. _(deprecated)_
- [init(rawValue:)](<init(rawvalue_).md>) — Creates a Metal device notification name from a string. _(deprecated)_
