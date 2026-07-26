---
title: wasAdded
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.13+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevicenotificationname/wasadded
source_url: 'https://developer.apple.com/documentation/metal/mtldevicenotificationname/wasadded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevicenotificationname/wasadded.json'
content_hash: 'sha256:a836a86ab4511ed3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDeviceNotificationName](../mtldevicenotificationname.md)

# wasAdded

<sub>Type Property</sub>

A notification that Metal sends to observers when the system adds a GPU device.

> [!warning] Deprecated
> Device notifications are not applicable on Apple Silicon

<sub>macOS</sub>

```swift
static let wasAdded: MTLDeviceNotificationName
```

## See Also

### Creating a notification name

- [MTLDeviceRemovalRequestedNotification](removalrequested.md) — A notification that Metal sends to observers when a person requests to remove a GPU device from the system. _(deprecated)_
- [MTLDeviceWasRemovedNotification](wasremoved.md) — A notification that Metal sends to observers when the system removes a GPU device. _(deprecated)_
- [init(rawValue:)](<init(rawvalue_).md>) — Creates a Metal device notification name from a string. _(deprecated)_
