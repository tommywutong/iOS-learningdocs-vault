---
title: 'skipToPreviousItem(for:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 10.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/skiptopreviousitem(for:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/skiptopreviousitem(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/skiptopreviousitem%28for%3A%29.json'
content_hash: 'sha256:36b19a0852b5e155'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# skipToPreviousItem(for:)

<sub>Instance Method</sub>

Tells the delegate when the user requests skipping to the previous item in the timeline.

<sub>tvOS</sub>

```swift
optional func skipToPreviousItem(for playerViewController: AVPlayerViewController)
```

## Parameters

- `playerViewController` — The player view controller.

## Discussion

The framework calls this method when you set the player view controller’s skipping behavior to [AVPlayerViewControllerSkippingBehaviorSkipItem](../avplayerviewcontrollerskippingbehavior/skipitem.md) and a user performs a backward skip gesture (by pressing the left side of the Siri Remote’s Touch surface). Implement this method to update the player view controller’s [player](../avplayerviewcontroller/player.md) to play the previous player item.

## See Also

### Responding to Navigation Events

- [- playerViewController:timeToSeekAfterUserNavigatedFromTime:toTime:](<playerviewcontroller(__timetoseekafterusernavigatedfrom_to_).md>) — Tells the delegate when the user skips, scrubs, or otherwise navigates to a new time and wants to resume playback at the target time.
- [- playerViewController:willResumePlaybackAfterUserNavigatedFromTime:toTime:](<playerviewcontroller(__willresumeplaybackafterusernavigatedfrom_to_).md>) — Tells the delegate when the user navigates to a new time and playback is about to begin.
- [- skipToNextItemForPlayerViewController:](<skiptonextitem(for_).md>) — Tells the delegate when the user requests skipping to the next item in the timeline.
