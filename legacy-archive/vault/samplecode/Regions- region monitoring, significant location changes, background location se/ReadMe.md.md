---
title: 'Regions: region monitoring, significant location changes, background location
  service, location service authorization'
apple_id: DTS40010726
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/Regions/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:22:05.164553Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Regions: region monitoring, significant location changes, background location service, location service authorization](Regions-%20region%20monitoring%2C%20significant%20location%20changes%2C%20background%20location%20se.md)


[Next](LICENSE.txt.md)[Previous](Regions-RegionsAppDelegate.h.md)

# ReadMe.md

```
# Regions

### Abstract:

This sample demonstrates proper use of region monitoring, significant location changes, and handling location events in the background on iOS.
The sample uses an MKMapView that allows the user to add and remove regions to monitor, as well as a UITableView to display the region enter/exit/fail events that occur.
When the application goes into the background, location updates are stopped and significant location changes are started. Likewise, when the application enters the foreground, location updates are started again and significant location changes are stopped.
When location updates occur in the background, a badge is added to the homescreen icon displaying the number of region enter/exit/fail events logged.

### Build Requirements:

iOS 8.4 or later

### Runtime Requirements:

iOS 8.4 or later. iPhone 4s, iPad 2 Wifi + 3G or later.

### Packaging List:

**RegionsAppDelegate**
The application delegate sets up the initial view and makes the window visible. It also handles events when the application goes into the background or enters the foreground.

**RegionsViewController**
This controller manages the CLLocationManager for location updates and switches the interface between showing the region map and the updates table list. This controller also manages adding and removing regions to be monitored by the application.

**RegionAnnotation**
This is a custom MKAnnotation with the addition of region and radius properties for ease of use when using region monitoring.

**RegionAnnotationView**
This is a custom MKAnnotationView that handles updating and removing the radius overlay to show where the region surrounding an annotation is.

### Changes from Previous Versions:

Version 2.0
- Updated for iOS 8.4, converted to use Storyboards, Auto Layout and Modern Objective-C.

Version 1.1
- Moved region re-adding logic into -viewDidAppear: due to timing issues.

Version 1.0
- First version.

Copyright (C) 2015 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](Regions-RegionsAppDelegate.h.md)

