---
title: URL.FormatStyle.ComponentDisplayOption
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/formatstyle/componentdisplayoption
source_url: 'https://developer.apple.com/documentation/foundation/url/formatstyle/componentdisplayoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatstyle/componentdisplayoption.json'
content_hash: 'sha256:cc04bb54a9aa9406'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [FormatStyle](../formatstyle.md)

# URL.FormatStyle.ComponentDisplayOption

<sub>Structure</sub>

A type that indicates whether a formatted URL should include a component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ComponentDisplayOption
```

## Relationships

- **Conforms To**: [CustomStringConvertible](../../../swift/customstringconvertible.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Display options

- [always](componentdisplayoption/always.md) — A display option that always displays the component.
- [never](componentdisplayoption/never.md) — A display option that never displays the component.
- [omitIfHTTPFamily](componentdisplayoption/omitifhttpfamily.md) — A display option that omits the component if the URL scheme is any flavor of HTTP.
- [displayWhen(_:matches:)](<componentdisplayoption/displaywhen(__matches_).md>) — Returns a display option that displays the component when a specified component meets the specified requirements.
- [omitWhen(_:matches:)](<componentdisplayoption/omitwhen(__matches_).md>) — Returns a display option that omits the component when a specified component meets the specified requirements.
- [Component](component.md) — An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.

## See Also

### Creating a URL format style

- [init(scheme:user:password:host:port:path:query:fragment:)](<init(scheme_user_password_host_port_path_query_fragment_).md>) — Creates a URL format style with the given display options.
- [HostDisplayOption](hostdisplayoption.md) — A type that indicates whether a formatted URL should include the host component.
