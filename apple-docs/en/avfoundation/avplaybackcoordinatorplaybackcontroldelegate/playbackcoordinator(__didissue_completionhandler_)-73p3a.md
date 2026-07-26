---
title: 'playbackCoordinator(_:didIssue:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-73p3a'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-73p3a'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator%28_%3Adidissue%3Acompletionhandler%3A%29-73p3a.json'
content_hash: 'sha256:c66e94a72fbd607b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlaybackCoordinatorPlaybackControlDelegate](../avplaybackcoordinatorplaybackcontroldelegate.md)

# playbackCoordinator(_:didIssue:completionHandler:)

<sub>Instance Method</sub>

Tells the delegate to match the playback rate to that of the group when the rate is nonzero.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func playbackCoordinator(_ coordinator: AVDelegatingPlaybackCoordinator, didIssue playCommand: AVDelegatingPlaybackCoordinatorPlayCommand, completionHandler: @escaping @Sendable () -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func playbackCoordinator(_ coordinator: AVDelegatingPlaybackCoordinator, didIssue playCommand: AVDelegatingPlaybackCoordinatorPlayCommand) async
```

## Parameters

- `coordinator` — The playback coordinator that issues the command.

- `playCommand` — The command to execute. Before performing it, verify that its [expectedCurrentItemIdentifier](../avdelegatingplaybackcoordinatorplaybackcontrolcommand/expectedcurrentitemidentifier.md) property value matches the item that you’re currently playing. If the command isn’t valid for the current item, ignore it and call the completion handler.

- `completionHandler` — A completion handler that your app must call when it finishes handling the command, either successfully or after beginning a suspension if it can’t handle the command currently.

## See Also

### Responding to commands

- [- playbackCoordinator:didIssuePauseCommand:completionHandler:](<playbackcoordinator(__didissue_completionhandler_)-56t01.md>) — Tells the delegate to pause playback.
- [- playbackCoordinator:didIssueSeekCommand:completionHandler:](<playbackcoordinator(__didissue_completionhandler_)-4fk8y.md>) — Tells the delegate to seek to a new time.
- [- playbackCoordinator:didIssueBufferingCommand:completionHandler:](<playbackcoordinator(__didissue_completionhandler_)-btle.md>) — Tells the delegate to expect playback soon and to start buffering media data in preparation.
