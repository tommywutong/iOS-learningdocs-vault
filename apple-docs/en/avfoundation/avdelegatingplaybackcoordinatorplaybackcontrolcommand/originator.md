---
title: originator
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinatorplaybackcontrolcommand/originator
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorplaybackcontrolcommand/originator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinatorplaybackcontrolcommand/originator.json'
content_hash: 'sha256:b2aa15b31fffb411'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinatorPlaybackControlCommand](../avdelegatingplaybackcoordinatorplaybackcontrolcommand.md)

# originator

<sub>Instance Property</sub>

The participant that causes the coordinator to issue the command.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var originator: AVCoordinatedPlaybackParticipant? { get }
```

## Discussion

Only commands that the system issues on behalf of another participant contain an originator. Local commands to coordinate rate change, or those that originate from a call to [- reapplyCurrentItemStateToPlaybackControlDelegate](<../avdelegatingplaybackcoordinator/reapplycurrentitemstatetoplaybackcontroldelegate().md>), don’t.

> [!note] Note
> You can use the existance of an originator value to show a user interface that indicates another partipant’s action.

## See Also

### Accessing command details

- [expectedCurrentItemIdentifier](expectedcurrentitemidentifier.md) — An item identifier the coordinator issues the command for.
