---
title: byStateReportingDomain
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: /documentation/swift/array/bystatereportingdomain-8k1ux
source_url: 'https://developer.apple.com/documentation/swift/array/bystatereportingdomain-8k1ux'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/bystatereportingdomain-8k1ux.json'
content_hash: 'sha256:3239ef7248529f35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# byStateReportingDomain

<sub>Instance Property</sub>

State entries grouped by their StateReporting domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var byStateReportingDomain: [StateReportingDomain : [MetricReport.StateEntry]] { get }
```

## Discussion

State entries with active StateReporting context are grouped by their domain.
