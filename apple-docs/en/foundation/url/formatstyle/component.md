---
title: URL.FormatStyle.Component
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/formatstyle/component
source_url: 'https://developer.apple.com/documentation/foundation/url/formatstyle/component'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatstyle/component.json'
content_hash: 'sha256:a7cf34e903e6ba3b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [FormatStyle](../formatstyle.md)

# URL.FormatStyle.Component

<sub>Enumeration</sub>

An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Component
```

## Overview

You use this type with style-modifying methods like [displayWhen(_:matches:)](<componentdisplayoption/displaywhen(__matches_).md>) in [ComponentDisplayOption](componentdisplayoption.md) and [omitWhen(_:matches:)](<hostdisplayoption/omitwhen(__matches_).md>) in [HostDisplayOption](hostdisplayoption.md).

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [CustomStringConvertible](../../../swift/customstringconvertible.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### URL format style components

- [URL.FormatStyle.Component.scheme](component/scheme.md) — The URL format style scheme component.
- [URL.FormatStyle.Component.host](component/host.md) — The URL format style host component.
- [URL.FormatStyle.Component.port](component/port.md) — The URL format style port component.
- [URL.FormatStyle.Component.user](component/user.md) — The URL format style user component.
- [URL.FormatStyle.Component.password](component/password.md) — The URL format style password component.
- [URL.FormatStyle.Component.path](component/path.md) — The URL format style path component.
- [URL.FormatStyle.Component.query](component/query.md) — The URL format style query component.
- [URL.FormatStyle.Component.fragment](component/fragment.md) — The URL format style fragment component.

## See Also

### Display options

- [always](componentdisplayoption/always.md) — A display option that always displays the component.
- [never](componentdisplayoption/never.md) — A display option that never displays the component.
- [omitIfHTTPFamily](componentdisplayoption/omitifhttpfamily.md) — A display option that omits the component if the URL scheme is any flavor of HTTP.
- [displayWhen(_:matches:)](<componentdisplayoption/displaywhen(__matches_).md>) — Returns a display option that displays the component when a specified component meets the specified requirements.
- [omitWhen(_:matches:)](<componentdisplayoption/omitwhen(__matches_).md>) — Returns a display option that omits the component when a specified component meets the specified requirements.
