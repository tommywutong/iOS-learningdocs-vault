---
title: UISceneError
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisceneerror
source_url: 'https://developer.apple.com/documentation/uikit/uisceneerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneerror.json'
content_hash: 'sha256:dc10a0101e6a6705'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISceneError

<sub>Structure</sub>

Errors returned during the creation or management of a scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UISceneError
```

## Relationships

- **Conforms To**: [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying an error cause

- [multipleScenesNotSupported](uisceneerror/multiplescenesnotsupported.md) — An error that indicates multiple scenes aren’t supported.
- [requestDenied](uisceneerror/requestdenied.md) — An error that indicates the request was denied.
- [geometryRequestUnsupported](uisceneerror/geometryrequestunsupported.md) — An error that indicates the geometry request is invalid or unsupported.
- [geometryRequestDenied](uisceneerror/geometryrequestdenied.md) — An error that indicates the geometry request is valid but the system denied the request.
- [Code](uisceneerror/code.md) — Error codes for issues with scenes.

### Inspecting error information

- [errorDomain](uisceneerror/errordomain.md) — The domain for scene-related errors.

## See Also

### Errors

- [Code](uisceneerror/code.md) — Error codes for issues with scenes.
- [UISceneErrorDomain](uisceneerrordomain.md) — The domain for scene-related errors.
