---
title: Polygons
apple_id: DTS10000399
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Polygons/Listings/theHardWay_m.html
archived_at: '2026-07-18T03:19:21.541294Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Polygons](Polygons.md)


[Next](Document%20Revision%20History.md)[Previous](StringArtView.m.md)

# theHardWay.m

```
//
//  theHardWay.m
//  Polygons
//
//  Created by John C. Randolph on Wed May 01 2002.
//  Copyright (c) 2002 __MyCompanyName__. All rights reserved.
//

 {
    // note that few of the variables used for this calculation are ivars of StringArtView.  I don't *need* their values to persist, since the NSBezierPath keeps all the state I need to redraw the view.
  int index = numPoints;
  float theta = M_PI * 2;  //M_PI is defined in the standard C headers.  Math.h, I believe.
  float sliceAngle = theta / numPoints;

  float radius = MIN(NSWidth(_frame), NSHeight(_frame)) * scaleFactor;
  NSPoint centerPoint, *perimeterPoints;

  perimeterPoints = alloca (numPoints * sizeof(NSPoint));  

  centerPoint = NSMakePoint(NSMidX(_frame), NSMidY(_frame));

  [path removeAllPoints];  // start with an empty path.

  theta += thetaOrigin;  // get the initial rotation.
  while (index--)
    {
    theta -= sliceAngle;
    perimeterPoints[index].x = centerPoint.x + radius * cos(theta);
    perimeterPoints[index].y = centerPoint.y + radius * sin(theta);
    }

  index = numPoints;
  while (index--)
    {
    int subIndex = index;
      while (subIndex--)
        {
        [path moveToPoint:perimeterPoints[index]];
        [path lineToPoint:perimeterPoints[subIndex]];
        }
    }
  [self display];
  }
*/
```

[Next](Document%20Revision%20History.md)[Previous](StringArtView.m.md)

