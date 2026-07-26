---
title: 'init(log:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/os/ossignpostid/init(log:)'
source_url: 'https://developer.apple.com/documentation/os/ossignpostid/init(log:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostid/init%28log%3A%29.json'
content_hash: 'sha256:fca87e507ab2e3bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignpostID](../ossignpostid.md)

# init(log:)

<sub>Initializer</sub>

Creates a signpost ID for the specified log.

> [!warning] Deprecated
> Use [makeSignpostID()](<../ossignposter/makesignpostid().md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(log: OSLog)
```

## Parameters

- `log` — The log that you’re writing signposted events to.

## See Also

### Creating a Signpost Identifier

- [init(_:)](<init(__).md>) — Creates a signpost ID from an arbitrary 64-bit integer value.
- [init(log:object:)](<init(log_object_).md>) — Creates a signpost ID and associates it with the specified object. _(deprecated)_
