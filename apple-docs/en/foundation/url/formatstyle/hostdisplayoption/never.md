---
title: never
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/formatstyle/hostdisplayoption/never
source_url: 'https://developer.apple.com/documentation/foundation/url/formatstyle/hostdisplayoption/never'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatstyle/hostdisplayoption/never.json'
content_hash: 'sha256:5f6dcf9115b003a0'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [URL](../../../url.md) · [FormatStyle](../../formatstyle.md) · [HostDisplayOption](../hostdisplayoption.md)

# never

<sub>Type Property</sub>

A display option that never displays the host component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var never: URL.FormatStyle.HostDisplayOption { get }
```

## See Also

### Display options

- [always](always.md) — A display option that always displays the host component.
- [omitIfHTTPFamily](omitifhttpfamily.md) — A display option that omits the host component if the URL scheme is HTTP or HTTPS.
- [displayWhen(_:matches:)](<displaywhen(__matches_).md>) — Returns a display option that displays the host component when a specified component matches against a set of requirement values.
- [omitWhen(_:matches:)](<omitwhen(__matches_).md>) — Returns a display option that displays the host component when a specified component matches against a set of requirement values.
- [omitSpecificSubdomains(_:includeMultiLevelSubdomains:)](<omitspecificsubdomains(__includemultilevelsubdomains_).md>) — Returns a display option that omits the host component if it matches a set of subdomains.
- [omitSpecificSubdomains(_:includeMultiLevelSubdomains:when:matches:)](<omitspecificsubdomains(__includemultilevelsubdomains_when_matches_).md>) — Returns a display option that omits the host component if it matches a set of subdomains and a specified component matches a set of requirements.
- [Component](../component.md) — An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.
