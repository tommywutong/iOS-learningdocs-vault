---
title: sampleHasRedundantCoding
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplecursordependencyinfo/samplehasredundantcoding
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursordependencyinfo/samplehasredundantcoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursordependencyinfo/samplehasredundantcoding.json'
content_hash: 'sha256:64bafd1c9530da08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursorDependencyInfo](../avsamplecursordependencyinfo.md)

# sampleHasRedundantCoding

<sub>Instance Property</sub>

A Boolean value that determines whether the sample has redundant coding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sampleHasRedundantCoding: ObjCBool
```

## Discussion

This value indicates the sample has redundant coding when [sampleIndicatesWhetherItHasRedundantCoding](sampleindicateswhetherithasredundantcoding.md) is `true`.

## See Also

### Dependency information

- [sampleIndicatesWhetherItHasDependentSamples](sampleindicateswhetherithasdependentsamples.md) — A Boolean value that determines whether the sample indicates if other samples depend on it.
- [sampleHasDependentSamples](samplehasdependentsamples.md) — A Boolean value that determines whether the sample has dependent samples.
- [sampleIndicatesWhetherItDependsOnOthers](sampleindicateswhetheritdependsonothers.md) — A Boolean value that determines whether the sample indicates that it depends on other samples.
- [sampleDependsOnOthers](sampledependsonothers.md) — A Boolean value that determines whether the sample depends on other samples.
- [sampleIndicatesWhetherItHasRedundantCoding](sampleindicateswhetherithasredundantcoding.md) — A Boolean value that determines whether the sample indicates that it has redundant coding.
