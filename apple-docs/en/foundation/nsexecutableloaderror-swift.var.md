---
title: NSExecutableLoadError
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexecutableloaderror-swift.var
source_url: 'https://developer.apple.com/documentation/foundation/nsexecutableloaderror-swift.var'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexecutableloaderror-swift.var.json'
content_hash: 'sha256:f5678e75740997d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSExecutableLoadError

<sub>Global Variable</sub>

Executable cannot be loaded for an otherwise-unspecified reason.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSExecutableLoadError: Int { get }
```

## Discussion

This error covers situations such as an error caused by a library the executable depends on.

## See Also

### Errors

- [NSExecutableErrorMinimum](nsexecutableerrorminimum-swift.var.md) — The beginning of the range of error codes reserved for errors related to executable files.
- [NSExecutableNotLoadableError](nsexecutablenotloadableerror-swift.var.md) — The executable type isn’t loadable in the current process.
- [NSExecutableArchitectureMismatchError](nsexecutablearchitecturemismatcherror-swift.var.md) — The executable doesn’t provide an architecture compatible with the current process.
- [NSExecutableRuntimeMismatchError](nsexecutableruntimemismatcherror-swift.var.md) — The executable has Objective-C runtime information that’s incompatible with the current process.
- [NSExecutableLinkError](nsexecutablelinkerror-swift.var.md) — The executable failed due to linking issues.
- [NSExecutableErrorMaximum](nsexecutableerrormaximum-swift.var.md) — The end of the range of error codes reserved for errors related to executable files.
