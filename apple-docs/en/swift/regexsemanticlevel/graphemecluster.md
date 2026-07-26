---
title: graphemeCluster
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regexsemanticlevel/graphemecluster
source_url: 'https://developer.apple.com/documentation/swift/regexsemanticlevel/graphemecluster'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexsemanticlevel/graphemecluster.json'
content_hash: 'sha256:4db309900f316aba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexSemanticLevel](../regexsemanticlevel.md)

# graphemeCluster

<sub>Type Property</sub>

Match at the character level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var graphemeCluster: RegexSemanticLevel { get }
```

## Discussion

At this semantic level, each matched element is a `Character` value. This is the default semantic level.
