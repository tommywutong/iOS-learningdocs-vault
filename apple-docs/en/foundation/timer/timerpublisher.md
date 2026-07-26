---
title: Timer.TimerPublisher
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/timer/timerpublisher
source_url: 'https://developer.apple.com/documentation/foundation/timer/timerpublisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/timerpublisher.json'
content_hash: 'sha256:d2ad184ac63581cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Timer](../timer.md)

# Timer.TimerPublisher

<sub>Class</sub>

A publisher that repeatedly emits the current date on a given interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class TimerPublisher
```

## Relationships

- **Conforms To**: [ConnectablePublisher](../../combine/connectablepublisher.md), [Publisher](../../combine/publisher.md)

## Topics

### Initializers

- [init(interval:tolerance:runLoop:mode:options:)](<timerpublisher/init(interval_tolerance_runloop_mode_options_).md>) — Creates a publisher that repeatedly emits the current date on the given interval.

### Instance Properties

- [interval](timerpublisher/interval.md)
- [mode](timerpublisher/mode.md)
- [options](timerpublisher/options.md)
- [runLoop](timerpublisher/runloop.md)
- [tolerance](timerpublisher/tolerance.md)

## See Also

### Firing Messages as a Combine Publisher

- [publish(every:tolerance:on:in:options:)](<publish(every_tolerance_on_in_options_).md>) — Returns a publisher that repeatedly emits the current date on the given interval.
