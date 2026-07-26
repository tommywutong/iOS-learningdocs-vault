---
title: Swift updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/updates/swift
source_url: 'https://developer.apple.com/documentation/updates/swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/swift.json'
content_hash: 'sha256:a40b407bdf8fe5a6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# Swift updates

<sub>Article</sub>

Learn about important changes to Swift.

## Overview

Browse notable changes in [Swift](../swift.md). For information about Swift language changes, refer to [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/revisionhistory).

## June 2025

### Swift standard library

- Safely access contiguous regions of memory, like a container’s underlying storage, using [Span](../swift/span.md) and [RawSpan](../swift/rawspan.md). Safely modify that memory using [MutableSpan](../swift/mutablespan.md) and [MutableRawSpan](../swift/mutablerawspan.md).

  Many collections in the standard library now have a `span` property that provides access to their underlying storage. `Span` has a [bytes](../swift/span/bytes-8rxg.md) property to access the raw storage when the element type supports it.
- Process Unicode strings efficiently and safely, using [UTF8Span](../swift/utf8span.md) to access a contiguous region of memory.
- Create fixed-size arrays that have contiguous underlying storage using [InlineArray](../swift/inlinearray.md).
- To identify a task during debugging, you can set a name for a detached task using [init(name:priority:operation:)](<../swift/task/init(name_priority_operation_)-43wmk.md>), and for a task in a task group using [addTask(name:priority:operation:)](<../swift/taskgroup/addtask(name_priority_operation_).md>). Access the current task’s name using [name](../swift/task/name-swift.property.md).
- Start a task immediately using [immediate(name:priority:executorPreference:operation:)](<../swift/task/immediate(name_priority_executorpreference_operation_)-9bghc.md>).

## June 2024

### Swift standard library

- Operate on noncontiguous ranges in collections using [RangeSet](../swift/rangeset.md) and [DiscontiguousSlice](../swift/discontiguousslice.md).
- Control which executor runs a task using [TaskExecutor](../swift/taskexecutor.md).
- Validate that C strings contain well-formed Unicode text when converting to them to `String` with [init(validatingCString:)](<../swift/string/init(validatingcstring_)-992vo.md>) and [init(validating:as:)](<../swift/string/init(validating_as_)-84qr9.md>).
- Preserve more information about thrown errors from [AsyncSequence](../swift/asyncsequence.md) and [AsyncIteratorProtocol](../swift/asynciteratorprotocol.md) using their `Failure` associated type.

## See Also

### Technology and frameworks

- [Accelerate updates](accelerate.md) — Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md) — Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md) — Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md) — Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md) — Learn about important changes in App Clips.
- [App Intents updates](appintents.md) — Learn about important changes in App Intents.
- [AppKit updates](appkit.md) — Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md) — Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md) — Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md) — Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md) — Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md) — Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md) — Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md) — Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md) — Learn about important changes to AVFoundation.
