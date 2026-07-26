---
title: UISceneError.Code
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisceneerror/code
source_url: 'https://developer.apple.com/documentation/uikit/uisceneerror/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneerror/code.json'
content_hash: 'sha256:9abd479a5f85ece9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneError](../uisceneerror.md)

# UISceneError.Code

<sub>Enumeration</sub>

Error codes for issues with scenes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Error codes

- [UISceneErrorCodeMultipleScenesNotSupported](code/multiplescenesnotsupported.md) — An error that indicates multiple scenes aren’t supported.
- [UISceneErrorCodeRequestDenied](code/requestdenied.md) — An error that indicates the request was denied.
- [UISceneErrorCodeGeometryRequestUnsupported](code/geometryrequestunsupported.md) — An error that indicates the geometry request is invalid or unsupported.
- [UISceneErrorCodeGeometryRequestDenied](code/geometryrequestdenied.md) — An error that indicates the geometry request is valid but the system denied the request.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Errors

- [UISceneError](../uisceneerror.md) — Errors returned during the creation or management of a scene.
- [UISceneErrorDomain](../uisceneerrordomain.md) — The domain for scene-related errors.
