---
title: 'Scoreboard: A demonstration of RTL support on macOS using NSStackView and
  localizedStringWithFormat'
apple_id: TP40017507
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/Scoreboard/Listings/README_md.html
archived_at: '2026-07-18T03:23:25.845910Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Scoreboard: A demonstration of RTL support on macOS using NSStackView and localizedStringWithFormat](Scoreboard-%20A%20demonstration%20of%20RTL%20support%20on%20macOS%20using%20NSStackView%20and%20locali.md)


[Next](LICENSE.txt.md)[Previous](Scoreboard-PlayerInfo.swift.md)

# README.md

```
# Scoreboard: A demonstration of RTL support on macOS using NSStackView and localizedStringWithFormat

This sample project illustrates the usage of AppKit controls and Auto Layout constraints in a macOS project. By using standard AppKit controls such as NSTableView and NStackView and laying out the views with Auto Layout, the UI automatically adapt to Right-to-Left languages, without adding special logic to mirror the UI for these languages.
This sample also shows how to render bidirectional text (mixed directionality scripts) correctly without adding logic to your variables.

To test Right-to-left UI without adding a localization: 

1. Open the Scheme editor in Xcode
2. Select 'Run'
3. Select the tab 'Options'
4. Override the 'Applicaton Language' setting to use 'Right-to-left pseudolanguage'

To test bidirectional text behavior, you can run your app in your application language, add a new player and type the player name with an Arabic or Hebrew keyboard.  


## Requirements

### Build

Xcode 8.0 or later; macOS 10.12 SDK or later

### Runtime

macOS 10.12 or later

Copyright (C) 2016 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](Scoreboard-PlayerInfo.swift.md)

