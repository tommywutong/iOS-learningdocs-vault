---
title: MTLBinaryArchiveError.Code
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbinaryarchiveerror-swift.struct/code
source_url: 'https://developer.apple.com/documentation/metal/mtlbinaryarchiveerror-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinaryarchiveerror-swift.struct/code.json'
content_hash: 'sha256:f7ca62beb8372bcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBinaryArchiveError](../mtlbinaryarchiveerror-swift.struct.md)

# MTLBinaryArchiveError.Code

<sub>Enumeration</sub>

Error codes when creating binary archives of compiled shader code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Error codes

- [MTLBinaryArchiveErrorNone](code/none.md) — An error code that represents the absence of any problems.
- [MTLBinaryArchiveErrorInvalidFile](code/invalidfile.md) — An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [MTLBinaryArchiveErrorCompilationFailure](code/compilationfailure.md) — An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [MTLBinaryArchiveErrorUnexpectedElement](code/unexpectedelement.md) — An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.
- [MTLBinaryArchiveErrorInternalError](code/internalerror.md) — An error code that indicates the Metal framework has an internal problem.
- [MTLBinaryArchiveErrorNone](code/none.md) — An error code that represents the absence of any problems.
- [MTLBinaryArchiveErrorInvalidFile](code/invalidfile.md) — An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [MTLBinaryArchiveErrorCompilationFailure](code/compilationfailure.md) — An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [MTLBinaryArchiveErrorUnexpectedElement](code/unexpectedelement.md) — An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.
- [MTLBinaryArchiveErrorInternalError](code/internalerror.md) — An error code that indicates the Metal framework has an internal problem.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Error codes

- [none](none.md) — An error code that represents the absence of any problems.
- [invalidFile](invalidfile.md) — An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [compilationFailure](compilationfailure.md) — An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [unexpectedElement](unexpectedelement.md) — An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.
- [internalError](internalerror.md) — An error code that indicates the Metal framework has an internal problem.
