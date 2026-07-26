---
title: Record.Recording
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/record/recording-swift.struct
source_url: 'https://developer.apple.com/documentation/combine/record/recording-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/record/recording-swift.struct.json'
content_hash: 'sha256:fbecbc64aa7486b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Record](../record.md)

# Record.Recording

<sub>Structure</sub>

A recorded sequence of outputs, followed by a completion value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Recording
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md)

## Topics

### Creating a recording

- [init()](<recording-swift.struct/init().md>) — Set up a recording in a state ready to receive output.
- [init(output:completion:)](<recording-swift.struct/init(output_completion_).md>) — Set up a complete recording with the specified output and completion.

### Receiving elements

- [receive(_:)](<recording-swift.struct/receive(__).md>) — Add an output to the recording.

### Receiving life cycle events

- [receive(completion:)](<recording-swift.struct/receive(completion_).md>) — Add a completion to the recording.

### Encoding

- [encode(into:)](<recording-swift.struct/encode(into_).md>)

### Inspecting publisher properties

- [output](recording-swift.struct/output.md) — The output which will be sent to a `Subscriber`.
- [completion](recording-swift.struct/completion.md) — The completion which will be sent to a `Subscriber`.

### Declaring supporting types

- [Input](recording-swift.struct/input.md)

## See Also

### Inspecting publisher properties

- [recording](recording-swift.property.md) — The recorded output and completion.
