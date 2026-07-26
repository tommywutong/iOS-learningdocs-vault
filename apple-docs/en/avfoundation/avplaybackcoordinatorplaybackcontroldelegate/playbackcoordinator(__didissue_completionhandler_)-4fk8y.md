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
doc_path: '/documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-4fk8y'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-4fk8y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator%28_%3Adidissue%3Acompletionhandler%3A%29-4fk8y.json'
content_hash: 'sha256:b16c57db6be3988a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlaybackCoordinatorPlaybackControlDelegate](../avplaybackcoordinatorplaybackcontroldelegate.md)

# playbackCoordinator(_:didIssue:completionHandler:)

<sub>Instance Method</sub>

Tells the delegate to seek to a new time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func playbackCoordinator(_ coordinator: AVDelegatingPlaybackCoordinator, didIssue seekCommand: AVDelegatingPlaybackCoordinatorSeekCommand, completionHandler: @escaping @Sendable () -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func playbackCoordinator(_ coordinator: AVDelegatingPlaybackCoordinator, didIssue seekCommand: AVDelegatingPlaybackCoordinatorSeekCommand) async
```

## Parameters

- `coordinator` — The playback coordinator that issues the command.

- `seekCommand` — The command to execute. Before performing it, verify that its [expectedCurrentItemIdentifier](../avdelegatingplaybackcoordinatorplaybackcontrolcommand/expectedcurrentitemidentifier.md) property value matches the item that you’re currently playing. If the command isn’t valid for the current item, ignore it and call the completion handler.

- `completionHandler` — A completion handler that your app must call when it finishes handling the command, either successfully or after beginning a suspension if it can’t handle the command currently. If the value of the command’s [shouldBufferInAnticipationOfPlayback](../avdelegatingplaybackcoordinatorpausecommand/shouldbufferinanticipationofplayback.md) property is [true](../../swift/true.md), call the completion handler only after the player is ready for playback.

## Discussion

The coordinator issues this command to perform a seek in the item timeline, potentially pausing playback in the process.

## See Also

### Responding to commands

- [- playbackCoordinator:didIssuePlayCommand:completionHandler:](<playbackcoordinator(__didissue_completionhandler_)-73p3a.md>) — Tells the delegate to match the playback rate to that of the group when the rate is nonzero.
- [- playbackCoordinator:didIssuePauseCommand:completionHandler:](<playbackcoordinator(__didissue_completionhandler_)-56t01.md>) — Tells the delegate to pause playback.
- [- playbackCoordinator:didIssueBufferingCommand:completionHandler:](<playbackcoordinator(__didissue_completionhandler_)-btle.md>) — Tells the delegate to expect playback soon and to start buffering media data in preparation.
