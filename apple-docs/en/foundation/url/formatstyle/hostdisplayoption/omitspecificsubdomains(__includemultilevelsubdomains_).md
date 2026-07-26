---
title: 'omitSpecificSubdomains(_:includeMultiLevelSubdomains:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/formatstyle/hostdisplayoption/omitspecificsubdomains(_:includemultilevelsubdomains:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/formatstyle/hostdisplayoption/omitspecificsubdomains(_:includemultilevelsubdomains:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatstyle/hostdisplayoption/omitspecificsubdomains%28_%3Aincludemultilevelsubdomains%3A%29.json'
content_hash: 'sha256:aa5e41193604d8f6'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [URL](../../../url.md) · [FormatStyle](../../formatstyle.md) · [HostDisplayOption](../hostdisplayoption.md)

# omitSpecificSubdomains(_:includeMultiLevelSubdomains:)

<sub>Type Method</sub>

Returns a display option that omits the host component if it matches a set of subdomains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func omitSpecificSubdomains(_ subdomainsToOmit: Set<String> = Set(), includeMultiLevelSubdomains omitMultiLevelSubdomains: Bool = false) -> URL.FormatStyle.HostDisplayOption
```

## Parameters

- `subdomainsToOmit` — A set of subdomains to omit, such as `[”www”, “mobile”, “m”]`. Matching any member of this set omits the host from the formatted output.

- `omitMultiLevelSubdomains` — A Boolean value to manage display of multi-level subdomains. If `true`, format style omits additional subdomains if there are more than two in addition to the top-level domain (TLD). For example, when this value is `true`, `api.code.developer.example.com` becomes `developer.example.com`, because the TLD is `“com”`. By comparison, `api.code.developer.example.com.cn` has a TLD of `“com.cn”`, so it becomes `developer.example.com.cn`.

## Return Value

A display option that omits the host component if it matches a set of subdomains.

## See Also

### Display options

- [always](always.md) — A display option that always displays the host component.
- [never](never.md) — A display option that never displays the host component.
- [omitIfHTTPFamily](omitifhttpfamily.md) — A display option that omits the host component if the URL scheme is HTTP or HTTPS.
- [displayWhen(_:matches:)](<displaywhen(__matches_).md>) — Returns a display option that displays the host component when a specified component matches against a set of requirement values.
- [omitWhen(_:matches:)](<omitwhen(__matches_).md>) — Returns a display option that displays the host component when a specified component matches against a set of requirement values.
- [omitSpecificSubdomains(_:includeMultiLevelSubdomains:when:matches:)](<omitspecificsubdomains(__includemultilevelsubdomains_when_matches_).md>) — Returns a display option that omits the host component if it matches a set of subdomains and a specified component matches a set of requirements.
- [Component](../component.md) — An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.
