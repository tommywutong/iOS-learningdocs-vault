---
title: init()
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/operatingsystemversion/init()
source_url: 'https://developer.apple.com/documentation/foundation/operatingsystemversion/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operatingsystemversion/init%28%29.json'
content_hash: 'sha256:8c83d278b1ed2c99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OperatingSystemVersion](../operatingsystemversion.md)

# init()

<sub>Initializer</sub>

Creates an empty operating system version.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

After initialization, the [majorVersion](majorversion.md), [minorVersion](minorversion.md), and [patchVersion](patchversion.md) are all `0`.

## See Also

### Creating an Operating System Version

- [init(majorVersion:minorVersion:patchVersion:)](<init(majorversion_minorversion_patchversion_).md>) — Creates an operating system version with the provided values.
