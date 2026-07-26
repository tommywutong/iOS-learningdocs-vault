---
title: 'withIntervalSignpost(_:id:_:around:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/withintervalsignpost(_:id:_:around:)'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/withintervalsignpost(_:id:_:around:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/withintervalsignpost%28_%3Aid%3A_%3Aaround%3A%29.json'
content_hash: 'sha256:fda9e1832fa52415'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# withIntervalSignpost(_:id:_:around:)

<sub>Instance Method</sub>

Measures the execution of a closure and attaches the specified message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withIntervalSignpost<T>(_ name: StaticString, id: OSSignpostID = .exclusive, _ message: SignpostMetadata, around task: () throws -> T) rethrows -> T
```

## Parameters

- `name` — The signpost’s name.

- `id` — The signpost’s ID. The default value is [exclusive](../ossignpostid/exclusive.md).

- `message` — The interpolated string that the signposter attaches to the signpost. Each of the message’s interpolations can specify individual formatting and privacy options. For more information, see [Message Argument Formatters](../message-argument-formatters.md).

- `task` — The closure around which to create the signposted interval.

## Discussion

> [!important] Important
> Don’t create an instance of [SignpostMetadata](../signpostmetadata.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

The signposter uses a signpost ID to pair the beginning and the end of a signposted interval, which is necessary because multiple intervals with the same configuration and scope can be in-flight simultaneously. If only one interval with a specific configuration can execute at any particular time, pass [exclusive](../ossignpostid/exclusive.md) as the `id` parameter. Otherwise, use the [makeSignpostID()](<makesignpostid().md>) and [makeSignpostID(from:)](<makesignpostid(from_).md>) methods to generate a signpost identifier, as the following example shows:

```swift
let accountNumber = "12345678"
                
// Create a signposter using the default subsystem.
let signposter = OSSignposter()
        
// Generate a signpost ID to associate with the signpost.
let signpostID = signposter.makeSignpostID()
        
// Signpost the interval of a closure that encapsulates
// one or more related tasks, and attach a message that
// securely interpolates sensitive data.
signposter.withIntervalSignpost("Account Reconciliation", id: signpostID,
    "Account: \(accountNumber, privacy: .sensitive(mask: .hash))") {
    
    // Perform the related tasks.
    processTransactions()
    updateBalance()
}
```

## See Also

### Measuring a Closure

- [withIntervalSignpost(_:id:around:)](<withintervalsignpost(__id_around_).md>) — Measures the execution of the specified closure.
