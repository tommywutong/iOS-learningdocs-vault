---
title: 'Flags: A demonstration of automatic RTL support in Asset Catalogs and UIStackViews'
apple_id: TP40017471
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/Flags/Listings/README_md.html
archived_at: '2026-07-18T03:08:46.675625Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Flags: A demonstration of automatic RTL support in Asset Catalogs and UIStackViews](Flags-%20A%20demonstration%20of%20automatic%20RTL%20support%20in%20Asset%20Catalogs%20and%20UIStackVie.md)


[Next](Flags-RootViewController.swift.md)[Previous](Flags-%20A%20demonstration%20of%20automatic%20RTL%20support%20in%20Asset%20Catalogs%20and%20UIStackVie.md)

# README.md

```
# Flags: A demonstration of automatic RTL support in Asset Catalogs and UIStackViews

This sample project illustrates the usage of Directional Image Assets in an iOS project. By using Directional Image Assets, images shown on-screen can automatically adapt to different layout directions (e.g. right-to-left contexts when running in Arabic or Hebrew), without requiring special code for loading different image variations at runtime.

This can be seen in the project by:

1. Running the application
2. Tapping on 'Start'

The 'Back' and 'Forward' arrows have been marked as mirrored images in the Xcode project's asset catalog. Therefore, when running in a right-to-left context, these images will automatically mirror themselves horizontally. This can be seen by:

1. Opening up the Scheme editor in Xcode
2. Select 'Run' on the left of the drop-down
3. With the 'Options' tab selected, override the 'Application Language' setting to 'Right-to-left pseudolanguage'

When running in the environment above, both the forward and back arrows will be pointing in the opposite direction, to reflect their new positions relative to English UI.

## Requirements

### Build

Xcode 8.0 or later; iOS 10.0 SDK or later

### Runtime

iOS 10.0 or later

Copyright (C) 2016 Apple Inc. All rights reserved.
```

[Next](Flags-RootViewController.swift.md)[Previous](Flags-%20A%20demonstration%20of%20automatic%20RTL%20support%20in%20Asset%20Catalogs%20and%20UIStackVie.md)

