---
title: MTKTextureLoader.Error
framework: MetalKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metalkit/mtktextureloader/error
source_url: 'https://developer.apple.com/documentation/metalkit/mtktextureloader/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtktextureloader/error.json'
content_hash: 'sha256:fd3639dd469ea6a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MetalKit](../../metalkit.md) · [MTKTextureLoader](../mtktextureloader.md)

# MTKTextureLoader.Error

<sub>Structure</sub>

Errors returned by the texture loader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct Error
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<error/init(rawvalue_).md>)

### Keys

- [MTKTextureLoaderErrorDomain](error/domain.md) — The error domain used by `MetalKit` when returning texture loading errors.
- [MTKTextureLoaderErrorKey](error/key.md) — The key used to retrieve an error string from an error object’s [userInfo](../../foundation/nserror/userinfo.md) dictionary.
