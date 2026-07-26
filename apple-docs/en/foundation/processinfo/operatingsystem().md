---
title: operatingSystem()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/processinfo/operatingsystem()
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/operatingsystem()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/operatingsystem%28%29.json'
content_hash: 'sha256:76ff34f32971f15e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# operatingSystem()

<sub>Instance Method</sub>

Returns a constant to indicate the operating system on which the process is executing.

> [!warning] Deprecated
> Use [operatingSystemVersion](operatingsystemversion.md) or [- isOperatingSystemAtLeastVersion:](<isoperatingsystematleast(__).md>) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func operatingSystem() -> Int
```

## Return Value

Operating system identifier. See Constants for a list of possible values. In macOS, it’s `NSMACHOperatingSystem`.

## See Also

### Getting host information

- [hostName](hostname.md) — The name of the host computer on which the process is executing.
- [operatingSystemVersionString](operatingsystemversionstring.md) — A string containing the version of the operating system on which the process is executing.
- [operatingSystemVersion](operatingsystemversion.md) — The version of the operating system on which the process is executing.
- [- isOperatingSystemAtLeastVersion:](<isoperatingsystematleast(__).md>) — Returns a Boolean value indicating whether the version of the operating system on which the process is executing is the same or later than the given version.
- [OperatingSystemVersion](../operatingsystemversion.md) — A structure that contains version information about the currently executing operating system, including major, minor, and patch version numbers.
- [Anonymous](../1552984-anonymous.md) — The following constants are provided by the `NSProcessInfo` class as return values for [- operatingSystem](<operatingsystem().md>).
- [- operatingSystemName](<operatingsystemname().md>) — Returns a string containing the name of the operating system on which the process is executing. _(deprecated)_
