---
title: 'playerViewController(_:willResumePlaybackAfterUserNavigatedFrom:to:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 9.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willresumeplaybackafterusernavigatedfrom:to:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willresumeplaybackafterusernavigatedfrom:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%28_%3Awillresumeplaybackafterusernavigatedfrom%3Ato%3A%29.json'
content_hash: 'sha256:242f4a6063254d6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController(_:willResumePlaybackAfterUserNavigatedFrom:to:)

<sub>Instance Method</sub>

Tells the delegate when the user navigates to a new time and playback is about to begin.

<sub>tvOS</sub>

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, willResumePlaybackAfterUserNavigatedFrom oldTime: CMTime, to targetTime: CMTime)
```

## Parameters

- `playerViewController` — The player view controller.

- `oldTime` — The current playback time before the user began navigating.

- `targetTime` — The new time where playback is about to resume.

## Discussion

Unlike the [timeJumpedNotification](../../avfoundation/avplayeritem/timejumpednotification.md) notification, this method fires only for complete, user-initiated navigation events. For example, if the user begins scrubbing through the media timeline and pauses several times before resuming playback, the player view controller calls this method only once.

You can use this method to present interstitial content before resuming playback, however, it’s recommended to use [- playerViewController:timeToSeekAfterUserNavigatedFromTime:toTime:](<playerviewcontroller(__timetoseekafterusernavigatedfrom_to_).md>) for this purpose.

## See Also

### Responding to Navigation Events

- [- playerViewController:timeToSeekAfterUserNavigatedFromTime:toTime:](<playerviewcontroller(__timetoseekafterusernavigatedfrom_to_).md>) — Tells the delegate when the user skips, scrubs, or otherwise navigates to a new time and wants to resume playback at the target time.
- [- skipToPreviousItemForPlayerViewController:](<skiptopreviousitem(for_).md>) — Tells the delegate when the user requests skipping to the previous item in the timeline.
- [- skipToNextItemForPlayerViewController:](<skiptonextitem(for_).md>) — Tells the delegate when the user requests skipping to the next item in the timeline.
