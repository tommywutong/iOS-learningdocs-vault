---
title: qtfullscreen
apple_id: DTS10000861
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtfullscreen/Listings/README_txt.html
archived_at: '2026-07-26T19:52:46.394231Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtfullscreen](qtfullscreen.md)


[Next](QTFullScreen.c.md)[Previous](qtfullscreen.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

Relevant replacement documents include:

- Sample Code Project _[FullScreenWindow](../FullScreenWindow/FullScreenWindow.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmjyha)_

# README.txt

```
README - QTFullScreen

QTFullScreen.c defines functions that illustrate how to play QuickTime movies full screen. The key elements to displaying full screen movies are the calls BeginFullScreen and EndFullScreen, introduced in QuickTime 2.5. Here we open a QuickTime movie, configure it to play full screen, associate a movie controller, and then let the controller handle events. Your application should call the function QTFullScreen_EventLoopAction in its event loop (on MacOS) or when it gets idle events (on Windows).

Enjoy,
QuickTime Team
```

[Next](QTFullScreen.c.md)[Previous](qtfullscreen.md)

