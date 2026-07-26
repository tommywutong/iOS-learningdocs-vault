---
title: sampleHasDependentSamples
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplecursordependencyinfo/samplehasdependentsamples
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursordependencyinfo/samplehasdependentsamples'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursordependencyinfo/samplehasdependentsamples.json'
content_hash: 'sha256:169f5184b37e3e94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursorDependencyInfo](../avsamplecursordependencyinfo.md)

# sampleHasDependentSamples

<sub>Instance Property</sub>

A Boolean value that determines whether the sample has dependent samples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sampleHasDependentSamples: ObjCBool
```

## Discussion

This value indicates the sample has dependent samples when [sampleIndicatesWhetherItHasDependentSamples](sampleindicateswhetherithasdependentsamples.md) is [true](../../swift/true.md).

## See Also

### Dependency information

- [sampleIndicatesWhetherItHasDependentSamples](sampleindicateswhetherithasdependentsamples.md) — A Boolean value that determines whether the sample indicates if other samples depend on it.
- [sampleIndicatesWhetherItDependsOnOthers](sampleindicateswhetheritdependsonothers.md) — A Boolean value that determines whether the sample indicates that it depends on other samples.
- [sampleDependsOnOthers](sampledependsonothers.md) — A Boolean value that determines whether the sample depends on other samples.
- [sampleIndicatesWhetherItHasRedundantCoding](sampleindicateswhetherithasredundantcoding.md) — A Boolean value that determines whether the sample indicates that it has redundant coding.
- [sampleHasRedundantCoding](samplehasredundantcoding.md) — A Boolean value that determines whether the sample has redundant coding.
