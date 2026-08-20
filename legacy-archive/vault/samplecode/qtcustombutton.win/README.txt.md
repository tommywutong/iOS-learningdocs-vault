---
title: qtcustombutton.win
apple_id: DTS10000856
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtcustombutton.win/Listings/README_txt.html
archived_at: '2026-07-26T19:52:46.214151Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtcustombutton.win](qtcustombutton.win.md)


[Next](QTCustomButton.c.md)[Previous](qtcustombutton.win.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# README.txt

```
README - QTCustomButton

This code snippet shows one way to display a pop-up menu when the user clicks on the custom button in the movie controller bar (just like the QuickTime web browser plug-in does for its custom button). The basic idea is very simple: just call PopUpMenuSelect when the user clicks the custom button. Before we do that, however, we need to obtain a MenuHandle to the desired pop-up menu. Here we use NewMenu and MacAppendMenu to create the menu on the fly; we do this mainly so that we don't need to drag a resource file around. A real application would just call MacGetMenu to read the menu from its resource file.

Enjoy,
QuickTime Team
```

[Next](QTCustomButton.c.md)[Previous](qtcustombutton.win.md)

