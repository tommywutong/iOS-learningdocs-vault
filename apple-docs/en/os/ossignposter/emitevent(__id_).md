---
title: 'emitEvent(_:id:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/emitevent(_:id:)'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/emitevent(_:id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/emitevent%28_%3Aid%3A%29.json'
content_hash: 'sha256:b1e38f436c99f25c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# emitEvent(_:id:)

<sub>Instance Method</sub>

Marks a point of interest in time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func emitEvent(_ name: StaticString, id: OSSignpostID = .exclusive)
```

## Parameters

- `name` — The event’s name.

- `id` — The event’s identifier. The default value is [exclusive](../ossignpostid/exclusive.md).

## Discussion

You can use the [makeSignpostID()](<makesignpostid().md>) and [makeSignpostID(from:)](<makesignpostid(from_).md>) methods to generate an identifier for the event, as the following example shows:

```swift
// Create a signposter using the default subsystem.
let signposter = OSSignposter()
        
// Generate a signpost ID to associate with the event.
let signpostID = signposter.makeSignpostID()
        
// Emit a named event using the signpost ID.
signposter.emitEvent("Example Event", id: signpostID)
```

## See Also

### Emitting Individual Signposts

- [emitEvent(_:id:_:)](<emitevent(__id___).md>) — Marks a point of interest in time and attaches the specified message.
