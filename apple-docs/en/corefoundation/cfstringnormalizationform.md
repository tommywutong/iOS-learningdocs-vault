---
title: CFStringNormalizationForm
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstringnormalizationform
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringnormalizationform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringnormalizationform.json'
content_hash: 'sha256:9c769e8c4c6bcf51'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringNormalizationForm

<sub>Enumeration</sub>

Unicode normalization forms as described in Unicode Technical Report #15.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFStringNormalizationForm
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFStringNormalizationFormD](cfstringnormalizationform/d.md) — Canonical decomposition.
- [kCFStringNormalizationFormKD](cfstringnormalizationform/kd.md) — Compatibility decomposition.
- [kCFStringNormalizationFormC](cfstringnormalizationform/c.md) — Canonical decomposition followed by canonical composition.
- [kCFStringNormalizationFormKC](cfstringnormalizationform/kc.md) — Compatibility decomposition followed by canonical composition.

### Initializers

- [init(rawValue:)](<cfstringnormalizationform/init(rawvalue_).md>)

## See Also

### Constants

- [Transform Identifiers for CFStringTransform](transform-identifiers-for-cfstringtransform.md) — Constants that identify transforms used with [CFStringTransform](<cfstringtransform(________).md>).
