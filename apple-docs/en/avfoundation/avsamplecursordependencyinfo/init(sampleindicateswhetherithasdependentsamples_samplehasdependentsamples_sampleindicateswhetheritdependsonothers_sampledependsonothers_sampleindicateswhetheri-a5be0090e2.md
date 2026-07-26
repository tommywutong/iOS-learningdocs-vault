---
title: 'init(sampleIndicatesWhetherItHasDependentSamples:sampleHasDependentSamples:sampleIndicatesWhetherItDependsOnOthers:sampleDependsOnOthers:sampleIndicatesWhetherItHasRedundantCoding:sampleHasRedundantCoding:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplecursordependencyinfo/init(sampleindicateswhetherithasdependentsamples:samplehasdependentsamples:sampleindicateswhetheritdependsonothers:sampledependsonothers:sampleindicateswhetherithasredundantcoding:samplehasredundantcoding:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursordependencyinfo/init(sampleindicateswhetherithasdependentsamples:samplehasdependentsamples:sampleindicateswhetheritdependsonothers:sampledependsonothers:sampleindicateswhetherithasredundantcoding:samplehasredundantcoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursordependencyinfo/init%28sampleindicateswhetherithasdependentsamples%3Asamplehasdependentsamples%3Asampleindicateswhetheritdependsonothers%3Asampledependsonothers%3Asampleindicateswhetherithasredundantcoding%3Asamplehasredundantcoding%3A%29.json'
content_hash: 'sha256:f47ee96584bb5e2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursorDependencyInfo](../avsamplecursordependencyinfo.md)

# init(sampleIndicatesWhetherItHasDependentSamples:sampleHasDependentSamples:sampleIndicatesWhetherItDependsOnOthers:sampleDependsOnOthers:sampleIndicatesWhetherItHasRedundantCoding:sampleHasRedundantCoding:)

<sub>Initializer</sub>

Creates a sample cursor dependency information structure with sample information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(sampleIndicatesWhetherItHasDependentSamples: ObjCBool, sampleHasDependentSamples: ObjCBool, sampleIndicatesWhetherItDependsOnOthers: ObjCBool, sampleDependsOnOthers: ObjCBool, sampleIndicatesWhetherItHasRedundantCoding: ObjCBool, sampleHasRedundantCoding: ObjCBool)
```

## Parameters

- `sampleIndicatesWhetherItHasDependentSamples` — A Boolean value that determines whether the sample indicates if other samples depend on it.

- `sampleHasDependentSamples` — A Boolean value that determines whether the sample has dependent samples.

- `sampleIndicatesWhetherItDependsOnOthers` — A Boolean value that determines whether the sample indicates that it depends on other samples.

- `sampleDependsOnOthers` — A Boolean value that determines whether the sample depends on other samples.

- `sampleIndicatesWhetherItHasRedundantCoding` — A Boolean value that determines whether the sample indicates that it has redundant coding.

- `sampleHasRedundantCoding` — A Boolean value that determines whether the sample has redundant coding.
