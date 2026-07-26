---
title: 'init(rawValue:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.13+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtldevicenotificationname/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevicenotificationname/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevicenotificationname/init%28rawvalue%3A%29.json'
content_hash: 'sha256:3db8d63c4eaa7d08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDeviceNotificationName](../mtldevicenotificationname.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a Metal device notification name from a string.

> [!warning] Deprecated
> Device notifications are not applicable on Apple Silicon

<sub>macOS</sub>

```swift
init(rawValue: String)
```

## Parameters

- `rawValue` — A string of the notification’s name.

## Discussion

Use this type’s static properties instead of this initializer.

## See Also

### Creating a notification name

- [MTLDeviceWasAddedNotification](wasadded.md) — A notification that Metal sends to observers when the system adds a GPU device. _(deprecated)_
- [MTLDeviceRemovalRequestedNotification](removalrequested.md) — A notification that Metal sends to observers when a person requests to remove a GPU device from the system. _(deprecated)_
- [MTLDeviceWasRemovedNotification](wasremoved.md) — A notification that Metal sends to observers when the system removes a GPU device. _(deprecated)_
