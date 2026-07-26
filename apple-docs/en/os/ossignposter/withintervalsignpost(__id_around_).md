---
title: 'withIntervalSignpost(_:id:around:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/withintervalsignpost(_:id:around:)'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/withintervalsignpost(_:id:around:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/withintervalsignpost%28_%3Aid%3Aaround%3A%29.json'
content_hash: 'sha256:65ba4b4a6e4e90c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# withIntervalSignpost(_:id:around:)

<sub>Instance Method</sub>

Measures the execution of the specified closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withIntervalSignpost<T>(_ name: StaticString, id: OSSignpostID = .exclusive, around task: () throws -> T) rethrows -> T
```

## Parameters

- `name` — The signpost’s name.

- `id` — The signpost’s ID. The default value is [exclusive](../ossignpostid/exclusive.md).

- `task` — The closure around which to create the signposted interval.

## Discussion

The signposter uses a signpost ID to pair the beginning and the end of a signposted interval, which is necessary because multiple intervals with the same configuration and scope can be in-flight simultaneously. If only one interval with a specific configuration can execute at any particular time, pass [exclusive](../ossignpostid/exclusive.md) as the `id` parameter. Otherwise, use the [makeSignpostID()](<makesignpostid().md>) and [makeSignpostID(from:)](<makesignpostid(from_).md>) methods to generate a signpost identifier, as the following example shows:

```swift
// Create a signposter using the default subsystem.
let signposter = OSSignposter()
        
// Generate a signpost ID to associate with the signpost.
let signpostID = signposter.makeSignpostID()
        
// Signpost the interval of a closure that encapsulates 
// one or more related tasks.
signposter.withIntervalSignpost("Example Signpost", id: signpostID) {
    // Perform one or more related tasks.
}
```

## See Also

### Measuring a Closure

- [withIntervalSignpost(_:id:_:around:)](<withintervalsignpost(__id___around_).md>) — Measures the execution of a closure and attaches the specified message.
