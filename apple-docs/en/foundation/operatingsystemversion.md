---
title: OperatingSystemVersion
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operatingsystemversion
source_url: 'https://developer.apple.com/documentation/foundation/operatingsystemversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operatingsystemversion.json'
content_hash: 'sha256:d5931e880996d4dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# OperatingSystemVersion

<sub>Structure</sub>

A structure that contains version information about the currently executing operating system, including major, minor, and patch version numbers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct OperatingSystemVersion
```

## Overview

Use the [ProcessInfo](processinfo.md) property [operatingSystemVersion](processinfo/operatingsystemversion.md) to fetch an instance of this type. You can also pass this type to [- isOperatingSystemAtLeastVersion:](<processinfo/isoperatingsystematleast(__).md>) to determine whether the current operating system version is the same or later than the given value.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an Operating System Version

- [init()](<operatingsystemversion/init().md>) — Creates an empty operating system version.
- [init(majorVersion:minorVersion:patchVersion:)](<operatingsystemversion/init(majorversion_minorversion_patchversion_).md>) — Creates an operating system version with the provided values.

### Version Components

- [majorVersion](operatingsystemversion/majorversion.md) — The major release number, such as 10 in version 10.9.3.
- [minorVersion](operatingsystemversion/minorversion.md) — The minor release number, such as 9 in version 10.9.3.
- [patchVersion](operatingsystemversion/patchversion.md) — The update release number, such as 3 in version 10.9.3.
- [majorVersion](operatingsystemversion/majorversion.md) — The major release number, such as 10 in version 10.9.3.
- [minorVersion](operatingsystemversion/minorversion.md) — The minor release number, such as 9 in version 10.9.3.
- [patchVersion](operatingsystemversion/patchversion.md) — The update release number, such as 3 in version 10.9.3.

## See Also

### Getting host information

- [hostName](processinfo/hostname.md) — The name of the host computer on which the process is executing.
- [operatingSystemVersionString](processinfo/operatingsystemversionstring.md) — A string containing the version of the operating system on which the process is executing.
- [operatingSystemVersion](processinfo/operatingsystemversion.md) — The version of the operating system on which the process is executing.
- [- isOperatingSystemAtLeastVersion:](<processinfo/isoperatingsystematleast(__).md>) — Returns a Boolean value indicating whether the version of the operating system on which the process is executing is the same or later than the given version.
- [- operatingSystem](<processinfo/operatingsystem().md>) — Returns a constant to indicate the operating system on which the process is executing. _(deprecated)_
- [Anonymous](1552984-anonymous.md) — The following constants are provided by the `NSProcessInfo` class as return values for [- operatingSystem](<processinfo/operatingsystem().md>).
- [- operatingSystemName](<processinfo/operatingsystemname().md>) — Returns a string containing the name of the operating system on which the process is executing. _(deprecated)_
