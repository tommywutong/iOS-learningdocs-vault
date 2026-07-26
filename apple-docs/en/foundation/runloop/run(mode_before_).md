---
title: 'run(mode:before:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/runloop/run(mode:before:)'
source_url: 'https://developer.apple.com/documentation/foundation/runloop/run(mode:before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/run%28mode%3Abefore%3A%29.json'
content_hash: 'sha256:ab953bd734e600e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# run(mode:before:)

<sub>Instance Method</sub>

Runs the loop once, blocking for input in the specified mode until a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func run(mode: RunLoop.Mode, before limitDate: Date) -> Bool
```

## Parameters

- `mode` — The mode in which to run. You may specify custom modes or use one of the modes listed in `Run Loop Modes`.

- `limitDate` — The date until which to block.

## Return Value

[true](../../swift/true.md) if the run loop ran and processed an input source or if the specified timeout value was reached; otherwise, [false](../../swift/false.md) if the run loop could not be started.

## Discussion

If no input sources or timers are attached to the run loop, this method exits immediately and returns [false](../../swift/false.md); otherwise, it returns after either the first input source is processed or `limitDate` is reached. Manually removing all known input sources and timers from the run loop does not guarantee that the run loop will exit immediately. macOS may install and remove additional input sources as needed to process requests targeted at the receiver’s thread. Those sources could therefore prevent the run loop from exiting.

> [!note] Note
> A timer is not considered an input source and may fire multiple times while waiting for this method to return

## See Also

### Running a Loop

- [- run](<run().md>) — Puts the receiver into a permanent loop, during which time it processes data from all attached input sources.
- [- runUntilDate:](<run(until_).md>) — Runs the loop until the specified date, during which time it processes data from all attached input sources.
- [- acceptInputForMode:beforeDate:](<acceptinput(formode_before_).md>) — Runs the loop once or until the specified date, accepting input only for the specified mode.
