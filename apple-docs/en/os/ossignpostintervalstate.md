---
title: OSSignpostIntervalState
framework: os
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/ossignpostintervalstate
source_url: 'https://developer.apple.com/documentation/os/ossignpostintervalstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostintervalstate.json'
content_hash: 'sha256:ed81d11d98383083'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OSSignpostIntervalState

<sub>Class</sub>

An object that tracks the state of a signposted interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class OSSignpostIntervalState
```

## Overview

[OSSignposter](ossignposter.md) uses interval state to enforce the following runtime assertions:

- Multiple end calls don’t consume the same interval state.
- The begin call and end call use the same name.
- The begin call and end call emit signposts to the same underlying log.
- You don’t use the [exclusive](ossignpostid/exclusive.md) signpost ID for intervals that cross process boundaries.

In debug builds, any assertion failures result in a crash. In production builds, your app continues to run and, instead, the signposter attaches an error message to the interval’s closing signpost.

[OSSignpostIntervalState](ossignpostintervalstate.md) adopts the [Codable](../swift/codable.md) protocol, which means you can serialize state and safely share it across processes, as the following example shows:

```swift
// A closure that represents a process in the context of this example.
let processA: () throws -> Data = {
    // Create a signposter that uses the default subsystem.
    let signposter = OSSignposter()
            
    // Generate a signpost ID to associate with the signposted interval.
    let signpostID = signposter.makeSignpostID()
            
    // Begin a signposted interval.
    let state = signposter.beginInterval("Example", id: signpostID)
            
    // Encode the state into JSON and return to the caller.
    return try JSONEncoder().encode(state)
}
        
// A closure that represents a different process.
let processB: (Data) throws -> Void = { data in
    // Decode the provided JSON data into an instance of 
    // OSSignpostIntervalState.
    let state = try JSONDecoder().decode(OSSignpostIntervalState.self, 
        from: data)
            
    // Create a signposter that uses the same subsystem as
    // the original, which, in this case, is the default.
    let signposter = OSSignposter()
            
    // End the signposted interval using the decoded state.
    signposter.endInterval("Example", state)
}
        
// Execute the two closures.
do {
    let data = try processA()
    try processB(data)
} catch {
    // Handle any thrown errors accordingly.
}
```

If you don’t have access to the returned interval state from the call that begins the signposted interval, or the cost you incur when serializing the state to pass between processes is unacceptable, recreate the interval state by passing the interval’s signpost ID to the [beginState(id:)](<ossignpostintervalstate/beginstate(id_).md>) method.

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Interval State

- [init(from:)](<ossignpostintervalstate/init(from_).md>) — Decodes the interval state from the provided decoder.

### Recreating Interval State

- [beginState(id:)](<ossignpostintervalstate/beginstate(id_).md>) — Recreates interval state from the specified signpost ID.

### Encoding Interval State

- [encode(to:)](<ossignpostintervalstate/encode(to_).md>) — Encodes the interval state into the provided encoder.

## See Also

### Starting a Signposted Interval

- [beginInterval(_:id:)](<ossignposter/begininterval(__id_).md>) — Begins a signposted interval.
- [beginInterval(_:id:_:)](<ossignposter/begininterval(__id___).md>) — Begins a signposted interval and attaches the specified message.
- [beginAnimationInterval(_:id:)](<ossignposter/beginanimationinterval(__id_).md>) — Begins a signposted interval for measuring an animation.
- [beginAnimationInterval(_:id:_:)](<ossignposter/beginanimationinterval(__id___).md>) — Begins a signposted interval for measuring an animation, and attaches a message.
- [SignpostMetadata](signpostmetadata.md) — The type that represents a message you attach to a signpost.
