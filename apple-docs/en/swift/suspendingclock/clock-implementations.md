---
title: Clock Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/suspendingclock/clock-implementations
source_url: 'https://developer.apple.com/documentation/swift/suspendingclock/clock-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/suspendingclock/clock-implementations.json'
content_hash: 'sha256:20d543ea68c683ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Time](../time-and-duration.md) · [SuspendingClock](../suspendingclock.md)

# Clock Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [minimumResolution](minimumresolution.md) — The minimum non-zero resolution between any two calls to `now`.
- [now](now-swift.property.md) — The current instant accounting for machine suspension.

### Instance Methods

- [measure(_:)](<measure(__)-1zuvn.md>) — Measure the elapsed time to execute an asynchronous closure.
- [measure(_:)](<measure(__)-6nlcy.md>) — Measure the elapsed time to execute a closure.
- [measure(isolation:_:)](<measure(isolation___).md>) _(deprecated)_
- [sleep(for:tolerance:)](<sleep(for_tolerance_).md>) — Suspends for the given duration.
- [sleep(until:tolerance:)](<sleep(until_tolerance_).md>) — Suspend task execution until a given deadline within a tolerance. If no tolerance is specified then the system may adjust the deadline to coalesce CPU wake-ups to more efficiently process the wake-ups in a more power efficient manner.

### Type Aliases

- [Duration](duration.md)

### Type Properties

- [suspending](suspending.md) — A clock that measures time that always increments but stops incrementing while the system is asleep.
