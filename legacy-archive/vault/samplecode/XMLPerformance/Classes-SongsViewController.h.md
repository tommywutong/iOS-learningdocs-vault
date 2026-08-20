---
title: XMLPerformance
apple_id: DTS40008094
resource_type: Sample Code
platform: iOS
topic: Performance
technology: Foundation
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/XMLPerformance/Listings/Classes_SongsViewController_h.html
archived_at: '2026-07-18T03:28:29.875496Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [XMLPerformance](XMLPerformance.md)


[Next](ReadMe.md.md)[Previous](Classes-CocoaXMLParser.h.md)

# Classes/SongsViewController.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Creates and runs an instance of the parser type chosen by the user, and displays the parsed songs in a table. Selecting a row in the table navigates to a detail view for that song.
*/


@import UIKit;
#import "iTunesRSSParser.h"

@interface SongsViewController : UITableViewController <iTunesRSSParserDelegate>

// called by the ParserChoiceViewController based on the selected parser type
- (void)parseWithParserType:(XMLParserType)parserType;

@end
```

[Next](ReadMe.md.md)[Previous](Classes-CocoaXMLParser.h.md)

