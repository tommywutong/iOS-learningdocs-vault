---
title: completionDueDate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinatorbufferingcommand/completionduedate
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorbufferingcommand/completionduedate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinatorbufferingcommand/completionduedate.json'
content_hash: 'sha256:3ff35383abd5b2d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinatorBufferingCommand](../avdelegatingplaybackcoordinatorbufferingcommand.md)

# completionDueDate

<sub>Instance Property</sub>

The deadline by which the coordinator expects the delegate to complete execution of a command.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var completionDueDate: Date? { get }
```

## Discussion

A command that expects buffering in preparation for playback requires that the delegate call the command’s completion handler by the deadline. The delegate needs to complete the command by this date to keep up with the group. Alternatively, have the delegate begin a stall recovery suspension, and communicate that state to the other participants.

Completing the command after this date means that the coordinator likely sends a play command that isn’t for the current state.

## See Also

### Accessing command details

- [anticipatedPlaybackRate](anticipatedplaybackrate.md) — The rate at which the coordinator expects the current item to play.
