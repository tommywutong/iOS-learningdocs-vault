---
title: CLTimeIntervalMax
framework: Core Location
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cltimeintervalmax
source_url: 'https://developer.apple.com/documentation/corelocation/cltimeintervalmax'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cltimeintervalmax.json'
content_hash: 'sha256:bd83d5f7e835cf0c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLTimeIntervalMax

<sub>Global Variable</sub>

A value representing an unlimited amount of time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let CLTimeIntervalMax: TimeInterval
```

## Discussion

When scheduling deferred updates, you can use this constant to indicate that a new update should be triggered only after a large time interval has passed.
