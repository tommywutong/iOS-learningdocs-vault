---
title: sampleDependsOnOthers
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplecursordependencyinfo/sampledependsonothers
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursordependencyinfo/sampledependsonothers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursordependencyinfo/sampledependsonothers.json'
content_hash: 'sha256:5a110277c656ffde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursorDependencyInfo](../avsamplecursordependencyinfo.md)

# sampleDependsOnOthers

<sub>Instance Property</sub>

A Boolean value that determines whether the sample depends on other samples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sampleDependsOnOthers: ObjCBool
```

## Discussion

This value indicates whether the sample depends on other media samples when [sampleIndicatesWhetherItDependsOnOthers](sampleindicateswhetheritdependsonothers.md) is [true](../../swift/true.md).

## See Also

### Dependency information

- [sampleIndicatesWhetherItHasDependentSamples](sampleindicateswhetherithasdependentsamples.md) — A Boolean value that determines whether the sample indicates if other samples depend on it.
- [sampleHasDependentSamples](samplehasdependentsamples.md) — A Boolean value that determines whether the sample has dependent samples.
- [sampleIndicatesWhetherItDependsOnOthers](sampleindicateswhetheritdependsonothers.md) — A Boolean value that determines whether the sample indicates that it depends on other samples.
- [sampleIndicatesWhetherItHasRedundantCoding](sampleindicateswhetherithasredundantcoding.md) — A Boolean value that determines whether the sample indicates that it has redundant coding.
- [sampleHasRedundantCoding](samplehasredundantcoding.md) — A Boolean value that determines whether the sample has redundant coding.
