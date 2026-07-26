---
title: CFRunLoopSourceContext1
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopsourcecontext1
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopsourcecontext1.json'
content_hash: 'sha256:ac69768f96c3e95d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopSourceContext1

<sub>Structure</sub>

A structure that contains program-defined data and callbacks with which you can configure a version 1 CFRunLoopSource’s behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFRunLoopSourceContext1
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfrunloopsourcecontext1/init().md>)
- [init(version:info:retain:release:copyDescription:equal:hash:getPort:perform:)](<cfrunloopsourcecontext1/init(version_info_retain_release_copydescription_equal_hash_getport_perform_).md>)

### Instance Properties

- [copyDescription](cfrunloopsourcecontext1/copydescription.md) — A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [equal](cfrunloopsourcecontext1/equal.md) — An equality test callback for your program-defined `info` pointer. Can be `NULL`.
- [getPort](cfrunloopsourcecontext1/getport.md) — A callback to retrieve the native Mach port represented by the source. This callback is called when the source is either added to or removed from a run loop mode.
- [hash](cfrunloopsourcecontext1/hash.md) — A hash calculation callback for your program-defined `info` pointer. Can be `NULL`.
- [info](cfrunloopsourcecontext1/info.md) — An arbitrary pointer to program-defined data, which can be associated with the run loop source at creation time. This pointer is passed to all the callbacks defined in the context.
- [perform](cfrunloopsourcecontext1/perform.md) — A perform callback for the run loop source. This callback is called when the source has fired.
- [release](cfrunloopsourcecontext1/release.md) — A release callback for your program-defined `info` pointer. Can be `NULL`.
- [retain](cfrunloopsourcecontext1/retain.md) — A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [version](cfrunloopsourcecontext1/version.md) — Version number of the structure. Must be 1.

## See Also

### Data Types

- [CFRunLoopSourceContext](cfrunloopsourcecontext.md) — A structure that contains program-defined data and callbacks with which you can configure a version 0 CFRunLoopSource’s behavior.
