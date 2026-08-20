---
title: 'PIVToken: Using CryptoTokenKit to add support for new types of tokens'
apple_id: TP40017285
resource_type: Sample Code
platform: macOS
topic: null
technology: CryptoTokenKit
published: '2016-09-22'
source_url: https://developer.apple.com/library/archive/samplecode/PIVToken/Listings/PIVToken_NSData_Zip_m.html
archived_at: '2026-07-18T03:18:35.196370Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PIVToken: Using CryptoTokenKit to add support for new types of tokens](PIVToken-%20Using%20CryptoTokenKit%20to%20add%20support%20for%20new%20types%20of%20tokens.md)


[Next](PIVToken-Token.m.md)[Previous](LICENSE.txt.md)

# PIVToken/NSData_Zip.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Implements ZIP functionality for PIV standard
 */


#import <Foundation/Foundation.h>
#import <zlib.h>
#import <zconf.h>

#import "Token.h"

NS_ASSUME_NONNULL_BEGIN

@implementation NSData(Zip)

- (int)getWindowSize {
    int windowSize = MAX_WBITS;
    uint8_t *bytes = (uint8_t *)self.bytes;

    if (self.length > 2 && bytes[0] == 0x1F && bytes[1] == 0x8B) //gzip
        windowSize += 0x10;
    else
        windowSize += 0x20;

    return windowSize;
}

- (nullable NSData *)inflate {
    z_stream dstream;
    int windowSize = [self getWindowSize];

    dstream.zalloc = (alloc_func)0;
    dstream.zfree = (free_func)0;
    dstream.opaque = (voidpf)0;
    /* Input not altered , so de-const-casting ok*/
    dstream.next_in  = (Bytef*)self.bytes;
    dstream.avail_in = (uInt)self.length;
    int err = inflateInit2(&dstream, windowSize);
    if (err != Z_OK)
        return nil;

    NSUInteger offset = 0;
    NSMutableData *data = [NSMutableData dataWithLength:1024];
    for (;;) {
        dstream.next_out = [data mutableBytes] + offset;
        dstream.avail_out = (uInt)(data.length - offset);
        err = inflate(&dstream, Z_NO_FLUSH);

        if (err == Z_OK) {
            offset = data.length;
            [data setLength:data.length + data.length / 2];
        }
        else if (err == Z_STREAM_END) {
            break;
        }
        else {
            inflateEnd(&dstream);
            return nil;
        }
    }

    [data setLength:dstream.total_out];
    inflateEnd(&dstream);
    return data;
}

@end

NS_ASSUME_NONNULL_END
```

[Next](PIVToken-Token.m.md)[Previous](LICENSE.txt.md)

