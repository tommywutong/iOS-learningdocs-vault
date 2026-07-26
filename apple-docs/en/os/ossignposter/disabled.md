---
title: disabled
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/ossignposter/disabled
source_url: 'https://developer.apple.com/documentation/os/ossignposter/disabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/disabled.json'
content_hash: 'sha256:5d7ad894641df36e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# disabled

<sub>Type Property</sub>

A shared signposter that doesn’t emit signposts at runtime.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var disabled: OSSignposter { get }
```

## Discussion

You can use the signposter this property returns to disable signposts in your production builds without having to refactor your code, as the following example demonstrates:

```swift
let signposter: OSSignposter
#if DEBUG
signposter = OSSignposter()
#else
signposter = OSSignposter.disabled
#endif
```

To determine if a signposter can emit signposts, use the [isEnabled](isenabled.md) property.

## See Also

### Creating a Signposter

- [init()](<init().md>) — Creates a signposter that uses the default subsystem.
- [init(subsystem:category:)](<init(subsystem_category_)-94xpb.md>) — Creates a signposter that uses the specified subsystem and category.
- [init(subsystem:category:)](<init(subsystem_category_)-4vdri.md>) — Creates a signposter that uses the specified subsystem and system-defined log category.
- [init(logger:)](<init(logger_).md>) — Creates a signposter that uses the subsystem and category of an existing logger.
- [init(logHandle:)](<init(loghandle_).md>) — Creates a signposter that uses the subsystem and category of an existing log.
