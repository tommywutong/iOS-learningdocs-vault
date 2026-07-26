---
title: 'init(log:object:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/os/ossignpostid/init(log:object:)'
source_url: 'https://developer.apple.com/documentation/os/ossignpostid/init(log:object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostid/init%28log%3Aobject%3A%29.json'
content_hash: 'sha256:22801f7a8f09500e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignpostID](../ossignpostid.md)

# init(log:object:)

<sub>Initializer</sub>

Creates a signpost ID and associates it with the specified object.

> [!warning] Deprecated
> Use [makeSignpostID(from:)](<../ossignposter/makesignpostid(from_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(log: OSLog, object: AnyObject)
```

## Parameters

- `log` — The log that you’re writing signposted events to.

- `object` — The object to associate with this signpost ID.

## Discussion

> [!important] Important
> Don’t use this method if your signpost IDs cross process boundaries.

## See Also

### Creating a Signpost Identifier

- [init(_:)](<init(__).md>) — Creates a signpost ID from an arbitrary 64-bit integer value.
- [init(log:)](<init(log_).md>) — Creates a signpost ID for the specified log. _(deprecated)_
