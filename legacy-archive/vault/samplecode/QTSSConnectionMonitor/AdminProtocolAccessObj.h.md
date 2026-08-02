---
title: QTSSConnectionMonitor
apple_id: DTS10001049
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSSConnectionMonitor/Listings/AdminProtocolAccessObj_h.html
archived_at: '2026-07-18T03:21:18.400946Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSSConnectionMonitor](QTSSConnectionMonitor.md)


[Next](AdminProtocolAccessObj.m.md)[Previous](main.m.md)

# AdminProtocolAccessObj.h

```objc
//
//  AdminProtocolAccessObj.h
//  QTSSStatusView
//
//  Created by John Anderson on Fri Mar 08 2002.
//  Copyright (c) 2002 Apple. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <MOKit/MORegularExpression.h>


@interface AdminProtocolAccessObj : NSObject {
    NSString *authString;
    NSString *myHost;
}

- (id)initWithUsername:(NSString *)username password:(NSString *)password host:(NSString *)host;
- (int)getAllValuesAtPath:(NSString *)path withResult:(NSMutableDictionary *)result;
- (int)getValue:(NSString *)value withResult:(NSMutableArray *)result;
- (int)makeRequest:(NSString *)request withResult:(NSMutableArray *)result;
- (void)setAuthString:(NSString *)newString;

@end
```

[Next](AdminProtocolAccessObj.m.md)[Previous](main.m.md)

