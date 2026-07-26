---
title: Record
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/record
source_url: 'https://developer.apple.com/documentation/combine/record'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/record.json'
content_hash: 'sha256:1af7282ff90cb646'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# Record

<sub>Structure</sub>

A publisher that allows for recording a series of inputs and a completion, for later playback to each subscriber.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Record<Output, Failure> where Failure : Error
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Escapable](../swift/escapable.md), [Publisher](publisher.md)

## Topics

### Creating a record publisher

- [init(output:completion:)](<record/init(output_completion_).md>) — Creates a record publisher to publish the provided elements, followed by the provided completion value.
- [init(record:)](<record/init(record_).md>) — Creates a publisher to interactively record a series of outputs and a completion.
- [init(recording:)](<record/init(recording_).md>) — Creates a record publisher from an existing recording.

### Inspecting publisher properties

- [recording](record/recording-swift.property.md) — The recorded output and completion.
- [Recording](record/recording-swift.struct.md) — A recorded sequence of outputs, followed by a completion value.

## See Also

### Convenience Publishers

- [Future](future.md) — A publisher that eventually produces a single value and then finishes or fails.
- [Just](just.md) — A publisher that emits an output to each subscriber just once, and then finishes.
- [Deferred](deferred.md) — A publisher that awaits subscription before running the supplied closure to create a publisher for the new subscriber.
- [Empty](empty.md) — A publisher that never publishes any values, and optionally finishes immediately.
- [Fail](fail.md) — A publisher that immediately terminates with the specified error.
