---
title: 'ShapeEdit: Building a Simple iCloud Document App'
apple_id: TP40016100
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/ShapeEdit/Listings/ShapeEdit_ShapeEditError_swift.html
archived_at: '2026-07-18T03:23:44.057311Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ShapeEdit: Building a Simple iCloud Document App](ShapeEdit-%20Building%20a%20Simple%20iCloud%20Document%20App.md)


[Next](ShapeEdit-DocumentEditor-DocumentViewController.swift.md)[Previous](LICENSE.txt.md)

# ShapeEdit/ShapeEditError.swift

```
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This file contains the list of error codes that ShapeEdit can throw.
*/

/// These represent the possible errors thrown in our project.
enum ShapeEditError: ErrorType {
    case ThumbnailLoadFailed
    case BookmarkResolveFailed
    case NoShape
    case PlistReadFailed
    case SignedOutOfiCloud
}
```

[Next](ShapeEdit-DocumentEditor-DocumentViewController.swift.md)[Previous](LICENSE.txt.md)

