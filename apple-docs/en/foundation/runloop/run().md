---
title: run()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/run()
source_url: 'https://developer.apple.com/documentation/foundation/runloop/run()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/run%28%29.json'
content_hash: 'sha256:b3896b03f5c38f7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# run()

<sub>Instance Method</sub>

Puts the receiver into a permanent loop, during which time it processes data from all attached input sources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func run()
```

## Discussion

If no input sources or timers are attached to the run loop, this method exits immediately; otherwise, it runs the receiver in the `NSDefaultRunLoopMode` by repeatedly invoking [- runMode:beforeDate:](<run(mode_before_).md>). In other words, this method effectively begins an infinite loop that processes data from the run loop’s input sources and timers.

Manually removing all known input sources and timers from the run loop is not a guarantee that the run loop will exit. macOS can install and remove additional input sources as needed to process requests targeted at the receiver’s thread. Those sources could therefore prevent the run loop from exiting.

If you want the run loop to terminate, you shouldn’t use this method. Instead, use one of the other run methods and also check other arbitrary conditions of your own, in a loop. A simple example would be:

```objc
BOOL shouldKeepRunning = YES; // global
NSRunLoop *theRL = [NSRunLoop currentRunLoop];
while (shouldKeepRunning && [theRL runMode:NSDefaultRunLoopMode beforeDate:[NSDate distantFuture]]);
```

where `shouldKeepRunning` is set to [false](../../swift/false.md) somewhere else in the program.

## See Also

### Running a Loop

- [- runMode:beforeDate:](<run(mode_before_).md>) — Runs the loop once, blocking for input in the specified mode until a given date.
- [- runUntilDate:](<run(until_).md>) — Runs the loop until the specified date, during which time it processes data from all attached input sources.
- [- acceptInputForMode:beforeDate:](<acceptinput(formode_before_).md>) — Runs the loop once or until the specified date, accepting input only for the specified mode.
