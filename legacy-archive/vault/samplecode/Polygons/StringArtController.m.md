---
title: Polygons
apple_id: DTS10000399
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Polygons/Listings/StringArtController_m.html
archived_at: '2026-07-18T03:19:21.327801Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Polygons](Polygons.md)


[Next](StringArtView.h.md)[Previous](StringArtController.h.md)

# StringArtController.m

```objc
//
//  StringArtController.m
//  StringArtPath
//
//  Created by John C. Randolph on Thu May 02 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

#import "StringArtController.h"
#import "StringArtView.h"

@implementation StringArtController

- (void) awakeFromNib
  {
  [self updateUI];
  }

- (void) updateUI
  {
  [sidesSlider setIntValue:[stringArtView sides]];
  [sidesField setIntValue:[stringArtView sides]];

  [rotationSlider setFloatValue:[stringArtView rotation]];
  [rotationField setFloatValue:[stringArtView rotation]];

  [radiusSlider setFloatValue:[stringArtView radius]];
  [radiusField setFloatValue:[stringArtView radius]];

  [fgColorWell setColor:[stringArtView foregroundColor]];
  [bgColorWell setColor:[stringArtView backgroundColor]];
  }

@end
```

[Next](StringArtView.h.md)[Previous](StringArtController.h.md)

