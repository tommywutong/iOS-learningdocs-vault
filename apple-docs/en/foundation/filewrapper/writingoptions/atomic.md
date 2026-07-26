---
title: atomic
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/writingoptions/atomic
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/writingoptions/atomic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/writingoptions/atomic.json'
content_hash: 'sha256:21373f1b18f9956c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileWrapper](../../filewrapper.md) · [WritingOptions](../writingoptions.md)

# atomic

<sub>Type Property</sub>

Whether writing is done atomically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var atomic: FileWrapper.WritingOptions { get }
```

## Discussion

You can use this option to ensure that, when overwriting a file package, the overwriting either completely succeeds or completely fails, with no possibility of leaving the file package in an inconsistent state. Because this option causes additional I/O, you shouldn’t use it unnecessarily. For example, don’t use this option in an override of `-[NSDocument` [write(to:ofType:)](<../../../appkit/nsdocument/write(to_oftype_).md>)`]`, because `NSDocument` safe-saving is already done atomically.

## See Also

### Constants

- [NSFileWrapperWritingWithNameUpdating](withnameupdating.md) — Whether descendant file wrappers’[filename](../filename.md) properties are set if the writing succeeds.
