---
title: 'emitEvent(_:id:_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/emitevent(_:id:_:)'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/emitevent(_:id:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/emitevent%28_%3Aid%3A_%3A%29.json'
content_hash: 'sha256:4988a8b15b923727'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# emitEvent(_:id:_:)

<sub>Instance Method</sub>

Marks a point of interest in time and attaches the specified message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func emitEvent(_ name: StaticString, id: OSSignpostID = .exclusive, _ message: SignpostMetadata)
```

## Parameters

- `name` — The event’s name.

- `id` — The event’s identifier. The default value is [exclusive](../ossignpostid/exclusive.md).

- `message` — The interpolated string that the signposter attaches to the event. Each of the message’s interpolations can specify individual formatting and privacy options. For more information, see [Message Argument Formatters](../message-argument-formatters.md).

## Discussion

> [!important] Important
> Don’t create an instance of [SignpostMetadata](../signpostmetadata.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

You can use the [makeSignpostID()](<makesignpostid().md>) and [makeSignpostID(from:)](<makesignpostid(from_).md>) methods to generate an identifier for the event, as the following example shows:

```swift
let accountNumber = "12345678"

// Create a signposter using the default subsystem.
let signposter = OSSignposter()
        
// Generate a signpost ID to associate with the event.
let signpostID = signposter.makeSignpostID()
        
// Emit a named event using the signpost ID and attach a message
// that securely interpolates sensitive data.
signposter.emitEvent("New Account Created", id: signpostID,
    "Account: \(accountNumber, privacy: .sensitive(mask: .hash))")
```

## See Also

### Emitting Individual Signposts

- [emitEvent(_:id:)](<emitevent(__id_).md>) — Marks a point of interest in time.
