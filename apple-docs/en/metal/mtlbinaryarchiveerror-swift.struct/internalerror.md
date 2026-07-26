---
title: internalError
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbinaryarchiveerror-swift.struct/internalerror
source_url: 'https://developer.apple.com/documentation/metal/mtlbinaryarchiveerror-swift.struct/internalerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinaryarchiveerror-swift.struct/internalerror.json'
content_hash: 'sha256:42b65321ba7f349c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBinaryArchiveError](../mtlbinaryarchiveerror-swift.struct.md)

# internalError

<sub>Type Property</sub>

An error code that indicates the Metal framework has an internal problem.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var internalError: MTLBinaryArchiveError.Code { get }
```

## Discussion

You can report the scenario that generated this error code with [Feedback Assistant](https://feedbackassistant.apple.com).

## See Also

### Error codes

- [none](none.md) — An error code that represents the absence of any problems.
- [invalidFile](invalidfile.md) — An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [compilationFailure](compilationfailure.md) — An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [unexpectedElement](unexpectedelement.md) — An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.
- [Code](code.md) — Error codes when creating binary archives of compiled shader code.
