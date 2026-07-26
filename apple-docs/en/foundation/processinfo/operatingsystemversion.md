---
title: operatingSystemVersion
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/operatingsystemversion
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/operatingsystemversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/operatingsystemversion.json'
content_hash: 'sha256:c2fa399ca9ffc7d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# operatingSystemVersion

<sub>Instance Property</sub>

The version of the operating system on which the process is executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var operatingSystemVersion: OperatingSystemVersion { get }
```

## See Also

### Getting host information

- [hostName](hostname.md) — The name of the host computer on which the process is executing.
- [operatingSystemVersionString](operatingsystemversionstring.md) — A string containing the version of the operating system on which the process is executing.
- [- isOperatingSystemAtLeastVersion:](<isoperatingsystematleast(__).md>) — Returns a Boolean value indicating whether the version of the operating system on which the process is executing is the same or later than the given version.
- [OperatingSystemVersion](../operatingsystemversion.md) — A structure that contains version information about the currently executing operating system, including major, minor, and patch version numbers.
- [- operatingSystem](<operatingsystem().md>) — Returns a constant to indicate the operating system on which the process is executing. _(deprecated)_
- [Anonymous](../1552984-anonymous.md) — The following constants are provided by the `NSProcessInfo` class as return values for [- operatingSystem](<operatingsystem().md>).
- [- operatingSystemName](<operatingsystemname().md>) — Returns a string containing the name of the operating system on which the process is executing. _(deprecated)_
