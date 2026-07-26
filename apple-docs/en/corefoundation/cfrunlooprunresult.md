---
title: CFRunLoopRunResult
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunlooprunresult
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooprunresult.json'
content_hash: 'sha256:c18a84ed0f598218'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopRunResult

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFRunLoopRunResult
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFRunLoopRunFinished](cfrunlooprunresult/finished.md) — The running run loop mode has no sources or timers to process.
- [kCFRunLoopRunHandledSource](cfrunlooprunresult/handledsource.md) — A source has been processed. This value is returned only if the run loop was told to run only until a source was processed.
- [kCFRunLoopRunStopped](cfrunlooprunresult/stopped.md) — [CFRunLoopStop](<cfrunloopstop(__).md>) was called on the run loop.
- [kCFRunLoopRunTimedOut](cfrunlooprunresult/timedout.md) — The specified time interval for running the run loop has passed.

### Initializers

- [init(rawValue:)](<cfrunlooprunresult/init(rawvalue_).md>)

## See Also

### Enumerations

- [CFFileSecurityClearOptions](cffilesecurityclearoptions.md)
- [CFISO8601DateFormatOptions](cfiso8601dateformatoptions.md)
- [CFURLEnumeratorOptions](cfurlenumeratoroptions.md) — Options for controlling enumerator behavior.
- [CFURLEnumeratorResult](cfurlenumeratorresult.md) — Result codes from the [CFURLEnumeratorGetNextURL](<cfurlenumeratorgetnexturl(______).md>) function.
- [CGRectEdge](cgrectedge.md)
