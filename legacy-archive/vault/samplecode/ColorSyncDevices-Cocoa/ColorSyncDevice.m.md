---
title: ColorSyncDevices-Cocoa
apple_id: DTS10000387
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ColorSyncDevices-Cocoa/Listings/ColorSyncDevice_m.html
archived_at: '2026-07-18T03:04:00.494191Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ColorSyncDevices-Cocoa](ColorSyncDevices-Cocoa.md)


[Next](MyDataSource.h.md)[Previous](ColorSyncDevice.h.md)

# ColorSyncDevice.m

```objc
//
//  ColorSyncDevice.m
//  ColorSyncDevices-Cocoa
//
//  Created by Scott Kuechle on Sun Sep 08 2002.
//  Copyright (c) 2001 __MyCompanyName__. All rights reserved.
//

#import "ColorSyncDevice.h"
#import "Root.h"

#define IsALeafNode ((id)-1)

@implementation ColorSyncDevice

//static ColorSyncDevice *rootItem = nil;
#if 0
    + (ColorSyncDevice *)rootItem 
    {
//        if (rootItem == nil) rootItem = [[ColorSyncDevice alloc] initWithPath:@"Devices" parent:nil];
        if (rootItem == nil) rootItem = [[Root alloc] init];

        return rootItem;       
    }
#endif




    - (id)initWithPath:(NSString *)path parent:(ColorSyncDevice *)obj 
    {
        if (self = [super init]) {
            relativePath = [[path lastPathComponent] copy];
            parent = obj;
        }
        return self;
    }


    - (int)numberOfChildren 
    {
//        id tmp = [self children];
//        return (tmp == IsALeafNode) ? (-1) : [tmp count];

    }

//////////
//
// IterateDeviceInfo
//
// The caller-supplied iterator function for CMIterateColorDevices
//
//////////
#if 0
OSErr IterateDeviceInfo (const CMDeviceInfo *deviceInfo, void *refCon)
{
#pragma unused (refCon)

    return noErr;
}
#endif

    - (NSArray *)children 
    {
        if (children == NULL) 
        {
            UInt32          seed = 0;
            UInt32          count = 0;
            OSErr           err = noErr;

            seed = count = 0;
            /* display all ColorSync devices */
//            err = CMIterateColorDevices(&IterateDeviceInfo, &seed, &count, 0);

        }
#if 0
        if (children == NULL) 
        {
            NSFileManager *fileManager = [NSFileManager defaultManager];
            NSString *fullPath = [self fullPath];
            BOOL isDir, valid = [fileManager fileExistsAtPath:fullPath isDirectory:&isDir];
            if (valid && isDir) 
            {
                NSArray *array = [fileManager directoryContentsAtPath:fullPath];
                int cnt, numChildren = [array count];
                children = [[NSMutableArray alloc] initWithCapacity:numChildren];
                for (cnt = 0; cnt < numChildren; cnt++) 
                {
                    [children addObject:[[FileSystemItem alloc] initWithPath:[array objectAtIndex:cnt] parent:self]];
                }
            } 
            else
            {
                children = IsALeafNode;
            }
        }
#endif
        return children;
    }

- (NSString *)relativePath {
    return relativePath;
}

@end
```

[Next](MyDataSource.h.md)[Previous](ColorSyncDevice.h.md)

