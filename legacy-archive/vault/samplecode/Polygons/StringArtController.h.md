---
title: Polygons
apple_id: DTS10000399
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Polygons/Listings/StringArtController_h.html
archived_at: '2026-07-18T03:19:21.300954Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Polygons](Polygons.md)


[Next](StringArtController.m.md)[Previous](PolygonAppController.m.md)

# StringArtController.h

```objc
//
//  StringArtController.h
//  StringArtPath
//
//  Created by John C. Randolph on Thu May 02 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>


@interface StringArtController : NSObject 
  {
  IBOutlet id stringArtView;
  IBOutlet id sidesSlider;
  IBOutlet id sidesField;
  IBOutlet id rotationSlider;
  IBOutlet id rotationField;
  IBOutlet id radiusSlider;
  IBOutlet id radiusField;
  IBOutlet id fgColorWell;
  IBOutlet id bgColorWell;
  }

- (void) updateUI;


@end
```

[Next](StringArtController.m.md)[Previous](PolygonAppController.m.md)

