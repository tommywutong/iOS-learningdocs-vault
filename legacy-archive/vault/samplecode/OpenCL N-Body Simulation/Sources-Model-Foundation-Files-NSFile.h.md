---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_Foundation_Files_NSFile_h.html
archived_at: '2026-07-18T03:17:36.814909Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-Foundation-Files-CFDataFile.mm.md)[Previous](Sources-Model-Foundation-Files-CFDataFile.h.md)

# Sources/Model/Foundation/Files/NSFile.h

```objc
/*
 <codex>
 <abstract>
 Objective-C language binding for CFFile utilities.
 </abstract>
 </codex>
 */

#import <Cocoa/Cocoa.h>

@interface NSFile : NSObject <NSCopying>

@property (nonatomic, readonly) id plist;

@property (nonatomic, readonly) NSURL*          url;
@property (nonatomic, readonly) NSMutableData*  data;
@property (nonatomic, readonly) NSString*       string;

@property (nonatomic, readonly) const char*    cstring;
@property (nonatomic, readonly) const uint8_t* bytes;

@property (nonatomic, readonly) BOOL                   isPList;
@property (nonatomic, readonly) NSInteger              length;
@property (nonatomic, readonly) NSPropertyListFormat   format;
@property (nonatomic, readonly) NSSearchPathDirectory  directory;
@property (nonatomic, readonly) NSSearchPathDomainMask domain;

- (instancetype) initWithPathname:(NSString *)pathname;

- (instancetype) initWithResourceInAppBundle:(NSString *)fileName
                                   extension:(NSString *)fileExt;

- (instancetype) initWithDomain:(NSSearchPathDomainMask)domain
                         search:(NSSearchPathDirectory)directory
                      directory:(NSString *)dirName
                           file:(NSString *)fileName
                      extension:(NSString *)fileExt;

- (instancetype) initWithFile:(NSFile *)file;

+ (instancetype) fileWithPathname:(NSString *)pathname;

+ (instancetype) fileWithResourceInAppBundle:(NSString *)fileName
                                   extension:(NSString *)fileExt;

+ (instancetype) fileWithDomain:(NSSearchPathDomainMask)domain
                         search:(NSSearchPathDirectory)directory
                      directory:(NSString *)dirName
                           file:(NSString *)fileName
                      extension:(NSString *)fileExt;

+ (instancetype) fileWithFile:(NSFile *)file;

- (void) replace:(id)plist;

- (BOOL) write;

- (BOOL) write:(NSString *)pathname;

- (BOOL) write:(NSString *)fileName
     extension:(NSString *)fileExt;

@end
```

[Next](Sources-Model-Foundation-Files-CFDataFile.mm.md)[Previous](Sources-Model-Foundation-Files-CFDataFile.h.md)

