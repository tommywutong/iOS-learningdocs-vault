---
title: unexpectedElement
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbinaryarchiveerror-swift.struct/unexpectedelement
source_url: 'https://developer.apple.com/documentation/metal/mtlbinaryarchiveerror-swift.struct/unexpectedelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinaryarchiveerror-swift.struct/unexpectedelement.json'
content_hash: 'sha256:3c73a7643ab2c6d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBinaryArchiveError](../mtlbinaryarchiveerror-swift.struct.md)

# unexpectedElement

<sub>Type Property</sub>

An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var unexpectedElement: MTLBinaryArchiveError.Code { get }
```

## See Also

### Error codes

- [none](none.md) — An error code that represents the absence of any problems.
- [invalidFile](invalidfile.md) — An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [compilationFailure](compilationfailure.md) — An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [internalError](internalerror.md) — An error code that indicates the Metal framework has an internal problem.
- [Code](code.md) — Error codes when creating binary archives of compiled shader code.
