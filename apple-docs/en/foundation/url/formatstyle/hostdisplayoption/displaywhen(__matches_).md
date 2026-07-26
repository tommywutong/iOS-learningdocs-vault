---
title: 'displayWhen(_:matches:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/formatstyle/hostdisplayoption/displaywhen(_:matches:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/formatstyle/hostdisplayoption/displaywhen(_:matches:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatstyle/hostdisplayoption/displaywhen%28_%3Amatches%3A%29.json'
content_hash: 'sha256:409c82df092d5e40'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [URL](../../../url.md) · [FormatStyle](../../formatstyle.md) · [HostDisplayOption](../hostdisplayoption.md)

# displayWhen(_:matches:)

<sub>Type Method</sub>

Returns a display option that displays the host component when a specified component matches against a set of requirement values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func displayWhen(_ component: URL.FormatStyle.Component, matches requirements: Set<String>) -> URL.FormatStyle.HostDisplayOption
```

## Parameters

- `component` — A component to compare. This may or may not be the host component itself.

- `requirements` — A set of string values to match against. Matching any member of the set allows the format style to display the component.

## Return Value

A display option that displays the host component when a specified component meets the specified requirements.

## See Also

### Display options

- [always](always.md) — A display option that always displays the host component.
- [never](never.md) — A display option that never displays the host component.
- [omitIfHTTPFamily](omitifhttpfamily.md) — A display option that omits the host component if the URL scheme is HTTP or HTTPS.
- [omitWhen(_:matches:)](<omitwhen(__matches_).md>) — Returns a display option that displays the host component when a specified component matches against a set of requirement values.
- [omitSpecificSubdomains(_:includeMultiLevelSubdomains:)](<omitspecificsubdomains(__includemultilevelsubdomains_).md>) — Returns a display option that omits the host component if it matches a set of subdomains.
- [omitSpecificSubdomains(_:includeMultiLevelSubdomains:when:matches:)](<omitspecificsubdomains(__includemultilevelsubdomains_when_matches_).md>) — Returns a display option that omits the host component if it matches a set of subdomains and a specified component matches a set of requirements.
- [Component](../component.md) — An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.
