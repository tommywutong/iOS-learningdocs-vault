---
title: 'beginInterval(_:id:_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/begininterval(_:id:_:)'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/begininterval(_:id:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/begininterval%28_%3Aid%3A_%3A%29.json'
content_hash: 'sha256:fbff939dcb0efc9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# beginInterval(_:id:_:)

<sub>Instance Method</sub>

Begins a signposted interval and attaches the specified message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func beginInterval(_ name: StaticString, id: OSSignpostID = .exclusive, _ message: SignpostMetadata) -> OSSignpostIntervalState
```

## Parameters

- `name` — The signpost’s name.

- `id` — The signpost’s identifier. The default value is [exclusive](../ossignpostid/exclusive.md).

- `message` — The interpolated string that the signposter attaches to the signpost. Each of the message’s interpolations can specify individual formatting and privacy options. For more information, see [Message Argument Formatters](../message-argument-formatters.md).

## Return Value

The interval state that the signposter derives from the specified `id` parameter.

## Discussion

> [!important] Important
> Don’t create an instance of [SignpostMetadata](../signpostmetadata.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

The signposter uses a signpost ID to pair the beginning and the end of a signposted interval, which is necessary because multiple intervals with the same configuration and scope can be in-flight simultaneously. If only one interval with a specific configuration can execute at any particular time, use [exclusive](../ossignpostid/exclusive.md) for the `id` parameter. Otherwise, use the [makeSignpostID()](<makesignpostid().md>) and [makeSignpostID(from:)](<makesignpostid(from_).md>) methods to generate a signpost identifier.

To end a signposted interval, pass the return value to one of the [endInterval(_:_:)](<endinterval(____).md>) or [endInterval(_:_:_:)](<endinterval(______).md>) methods. If you don’t have access to the returned interval state when you want to end the signposted interval, recreate it by passing the same signpost ID to the [beginState(id:)](<../ossignpostintervalstate/beginstate(id_).md>) method.

If you need to pass the returned interval state across process boundaries, you must encode it first. For more information, see [OSSignpostIntervalState](../ossignpostintervalstate.md).

The following example shows how to use a signpost ID and interval state to signpost the beginning and the end of an interval, and also demonstrates the use of message interpolation:

```swift
let accountNumber = "12345678"
        
// Create a signposter that uses the default subsystem.
let signposter = OSSignposter()
        
// Generate a signpost ID to associate with the signposted interval.
let signpostID = signposter.makeSignpostID()
        
// Create a name that the signposter uses, along with the 
// signpost ID, to disambiguate the begin call and end call. 
// The type must be StaticString.
let name: StaticString = "Account Reconciliation"
        
// Begin a signposted interval and attach a message that securely
// interpolates sensitive data.
let state = signposter.beginInterval(name, id: signpostID,
    "Account: \(accountNumber, privacy: .sensitive(mask: .hash))")
        
// Perform the related tasks you want to measure.
processTransactions()
updateBalance()
        
// Use the interval state from the begin call to end the
// corresponding signposted interval.
signposter.endInterval(name, state)
```

## See Also

### Starting a Signposted Interval

- [beginInterval(_:id:)](<begininterval(__id_).md>) — Begins a signposted interval.
- [beginAnimationInterval(_:id:)](<beginanimationinterval(__id_).md>) — Begins a signposted interval for measuring an animation.
- [beginAnimationInterval(_:id:_:)](<beginanimationinterval(__id___).md>) — Begins a signposted interval for measuring an animation, and attaches a message.
- [OSSignpostIntervalState](../ossignpostintervalstate.md) — An object that tracks the state of a signposted interval.
- [SignpostMetadata](../signpostmetadata.md) — The type that represents a message you attach to a signpost.
