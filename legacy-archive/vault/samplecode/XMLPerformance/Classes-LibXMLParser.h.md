---
title: XMLPerformance
apple_id: DTS40008094
resource_type: Sample Code
platform: iOS
topic: Performance
technology: Foundation
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/XMLPerformance/Listings/Classes_LibXMLParser_h.html
archived_at: '2026-07-18T03:28:29.584701Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [XMLPerformance](XMLPerformance.md)


[Next](Classes-LibXMLParser.m.md)[Previous](Classes-DetailController.h.md)

# Classes/LibXMLParser.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Subclass of iTunesRSSParser that uses libxml2 for parsing the XML data.
*/

@import UIKit;
#import "iTunesRSSParser.h"


// This approach to parsing uses NSURLSession to asychronously retrieve the XML data. libxml's SAX parsing supports chunked parsing, with no requirement for the chunks to be discrete blocks of well formed XML. The primary purpose of this class is to start the download, configure the parser with a set of C callback functions, and pass downloaded data to it. In addition, the class maintains a number of state variables for the parsing.
@interface LibXMLParser : iTunesRSSParser

@end
```

[Next](Classes-LibXMLParser.m.md)[Previous](Classes-DetailController.h.md)

