---
title: 'playerViewController(_:timeToSeekAfterUserNavigatedFrom:to:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 10.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:timetoseekafterusernavigatedfrom:to:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:timetoseekafterusernavigatedfrom:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%28_%3Atimetoseekafterusernavigatedfrom%3Ato%3A%29.json'
content_hash: 'sha256:116db7218330f136'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController(_:timeToSeekAfterUserNavigatedFrom:to:)

<sub>Instance Method</sub>

Tells the delegate when the user skips, scrubs, or otherwise navigates to a new time and wants to resume playback at the target time.

<sub>tvOS</sub>

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, timeToSeekAfterUserNavigatedFrom oldTime: CMTime, to targetTime: CMTime) -> CMTime
```

## Parameters

- `playerViewController` — The player view controller.

- `oldTime` — The current playback time before the user began navigating.

- `targetTime` — The time to which the user navigated.

## Return Value

The time at which to begin playback.

## Discussion

The framework calls this method prior to beginning playback after a user-initiated scrubbing request. You can return a time value other than the specified target time if needed to enforce certain business rules. For instance, you may want to return a different time to prevent users from skipping past ad breaks in your program.

## See Also

### Responding to Navigation Events

- [- playerViewController:willResumePlaybackAfterUserNavigatedFromTime:toTime:](<playerviewcontroller(__willresumeplaybackafterusernavigatedfrom_to_).md>) — Tells the delegate when the user navigates to a new time and playback is about to begin.
- [- skipToPreviousItemForPlayerViewController:](<skiptopreviousitem(for_).md>) — Tells the delegate when the user requests skipping to the previous item in the timeline.
- [- skipToNextItemForPlayerViewController:](<skiptonextitem(for_).md>) — Tells the delegate when the user requests skipping to the next item in the timeline.
