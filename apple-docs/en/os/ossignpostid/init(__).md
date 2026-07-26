---
title: 'init(_:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignpostid/init(_:)'
source_url: 'https://developer.apple.com/documentation/os/ossignpostid/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostid/init%28_%3A%29.json'
content_hash: 'sha256:4bf5085b74c72ddd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignpostID](../ossignpostid.md)

# init(_:)

<sub>Initializer</sub>

Creates a signpost ID from an arbitrary 64-bit integer value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ value: UInt64)
```

## Parameters

- `value` — The value to use when generating the signpost ID.

## See Also

### Creating a Signpost Identifier

- [init(log:)](<init(log_).md>) — Creates a signpost ID for the specified log. _(deprecated)_
- [init(log:object:)](<init(log_object_).md>) — Creates a signpost ID and associates it with the specified object. _(deprecated)_
