---
title: 'run(until:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/runloop/run(until:)'
source_url: 'https://developer.apple.com/documentation/foundation/runloop/run(until:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/run%28until%3A%29.json'
content_hash: 'sha256:603da07c44db4e58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# run(until:)

<sub>Instance Method</sub>

Runs the loop until the specified date, during which time it processes data from all attached input sources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func run(until limitDate: Date)
```

## Parameters

- `limitDate` — The date up until which to run.

## Discussion

If no input sources or timers are attached to the run loop, this method exits immediately; otherwise, it runs the receiver in the `NSDefaultRunLoopMode` by repeatedly invoking [- runMode:beforeDate:](<run(mode_before_).md>) until the specified expiration date.

Manually removing all known input sources and timers from the run loop is not a guarantee that the run loop will exit. macOS can install and remove additional input sources as needed to process requests targeted at the receiver’s thread. Those sources could therefore prevent the run loop from exiting.

## See Also

### Running a Loop

- [- run](<run().md>) — Puts the receiver into a permanent loop, during which time it processes data from all attached input sources.
- [- runMode:beforeDate:](<run(mode_before_).md>) — Runs the loop once, blocking for input in the specified mode until a given date.
- [- acceptInputForMode:beforeDate:](<acceptinput(formode_before_).md>) — Runs the loop once or until the specified date, accepting input only for the specified mode.
