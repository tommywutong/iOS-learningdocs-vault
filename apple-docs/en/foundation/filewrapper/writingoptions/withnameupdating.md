---
title: withNameUpdating
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/writingoptions/withnameupdating
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/writingoptions/withnameupdating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/writingoptions/withnameupdating.json'
content_hash: 'sha256:5974c337290e27f7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileWrapper](../../filewrapper.md) · [WritingOptions](../writingoptions.md)

# withNameUpdating

<sub>Type Property</sub>

Whether descendant file wrappers’[filename](../filename.md) properties are set if the writing succeeds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var withNameUpdating: FileWrapper.WritingOptions { get }
```

## Discussion

This option is necessary when your application passes a URL in the `originalContentsURL` parameter to the [- writeToURL:options:originalContentsURL:error:](<../write(to_options_originalcontentsurl_).md>) method. Without using this option (and reusing child file wrappers properly), subsequent invocations of [- writeToURL:options:originalContentsURL:error:](<../write(to_options_originalcontentsurl_).md>) would not be able to reliably create hard links in a new file package, because the record of names in the old file package would be out of date.

## See Also

### Constants

- [NSFileWrapperWritingAtomic](atomic.md) — Whether writing is done atomically.
