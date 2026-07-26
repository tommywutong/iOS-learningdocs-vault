---
title: 'isOperatingSystemAtLeast(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/processinfo/isoperatingsystematleast(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/isoperatingsystematleast(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/isoperatingsystematleast%28_%3A%29.json'
content_hash: 'sha256:7918a149327955dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# isOperatingSystemAtLeast(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the version of the operating system on which the process is executing is the same or later than the given version.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isOperatingSystemAtLeast(_ version: OperatingSystemVersion) -> Bool
```

## Parameters

- `version` — The operating system version to test against.

## Return Value

[true](../../swift/true.md) if the operating system on which the process is executing is the same or later than the given version; otherwise [false](../../swift/false.md).

## Discussion

This method accounts for major, minor, and update versions of the operating system.

## See Also

### Getting host information

- [hostName](hostname.md) — The name of the host computer on which the process is executing.
- [operatingSystemVersionString](operatingsystemversionstring.md) — A string containing the version of the operating system on which the process is executing.
- [operatingSystemVersion](operatingsystemversion.md) — The version of the operating system on which the process is executing.
- [OperatingSystemVersion](../operatingsystemversion.md) — A structure that contains version information about the currently executing operating system, including major, minor, and patch version numbers.
- [- operatingSystem](<operatingsystem().md>) — Returns a constant to indicate the operating system on which the process is executing. _(deprecated)_
- [Anonymous](../1552984-anonymous.md) — The following constants are provided by the `NSProcessInfo` class as return values for [- operatingSystem](<operatingsystem().md>).
- [- operatingSystemName](<operatingsystemname().md>) — Returns a string containing the name of the operating system on which the process is executing. _(deprecated)_
