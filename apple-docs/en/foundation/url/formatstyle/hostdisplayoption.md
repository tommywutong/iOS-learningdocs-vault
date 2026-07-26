---
title: URL.FormatStyle.HostDisplayOption
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/formatstyle/hostdisplayoption
source_url: 'https://developer.apple.com/documentation/foundation/url/formatstyle/hostdisplayoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatstyle/hostdisplayoption.json'
content_hash: 'sha256:e3b42a462a538935'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [FormatStyle](../formatstyle.md)

# URL.FormatStyle.HostDisplayOption

<sub>Structure</sub>

A type that indicates whether a formatted URL should include the host component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct HostDisplayOption
```

## Relationships

- **Conforms To**: [CustomStringConvertible](../../../swift/customstringconvertible.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Display options

- [always](hostdisplayoption/always.md) — A display option that always displays the host component.
- [never](hostdisplayoption/never.md) — A display option that never displays the host component.
- [omitIfHTTPFamily](hostdisplayoption/omitifhttpfamily.md) — A display option that omits the host component if the URL scheme is HTTP or HTTPS.
- [displayWhen(_:matches:)](<hostdisplayoption/displaywhen(__matches_).md>) — Returns a display option that displays the host component when a specified component matches against a set of requirement values.
- [omitWhen(_:matches:)](<hostdisplayoption/omitwhen(__matches_).md>) — Returns a display option that displays the host component when a specified component matches against a set of requirement values.
- [omitSpecificSubdomains(_:includeMultiLevelSubdomains:)](<hostdisplayoption/omitspecificsubdomains(__includemultilevelsubdomains_).md>) — Returns a display option that omits the host component if it matches a set of subdomains.
- [omitSpecificSubdomains(_:includeMultiLevelSubdomains:when:matches:)](<hostdisplayoption/omitspecificsubdomains(__includemultilevelsubdomains_when_matches_).md>) — Returns a display option that omits the host component if it matches a set of subdomains and a specified component matches a set of requirements.
- [Component](component.md) — An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.

## See Also

### Creating a URL format style

- [init(scheme:user:password:host:port:path:query:fragment:)](<init(scheme_user_password_host_port_path_query_fragment_).md>) — Creates a URL format style with the given display options.
- [ComponentDisplayOption](componentdisplayoption.md) — A type that indicates whether a formatted URL should include a component.
