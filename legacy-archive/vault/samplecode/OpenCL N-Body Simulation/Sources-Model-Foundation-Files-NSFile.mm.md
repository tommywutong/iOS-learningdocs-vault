---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_Foundation_Files_NSFile_mm.html
archived_at: '2026-07-18T03:17:36.856519Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-Foundation-Frame-CTFrame.h.md)[Previous](Sources-Model-Foundation-Files-CFFile.h.md)

# Sources/Model/Foundation/Files/NSFile.mm

```objc
/*
 <codex>
 <import>NSFile.h</import>
 </codex>
 */

#import "CFFile.h"
#import "NSFile.h"

typedef NSURL*          NSURLRef;
typedef NSMutableData*  NSMutableDataRef;

@implementation NSFile
{
@private
    CF::File* mpFile;
}

- (instancetype) initWithPathname:(NSString *)pathname
{
    self = [super init];

    if(self)
    {
        mpFile = new (std::nothrow) CF::File(CFStringRef(pathname));
    } // if

    return self;
} // initWithPathname

- (instancetype) initWithResourceInAppBundle:(NSString *)name
                                   extension:(NSString *)ext
{
    self = [super init];

    if(self)
    {
        mpFile = new (std::nothrow) CF::File(CFStringRef(name),
                                             CFStringRef(ext));
    } // if

    return self;
} // initWithResourceInAppBundle

- (instancetype) initWithDomain:(NSSearchPathDomainMask)domain
                         search:(NSSearchPathDirectory)directory
                      directory:(NSString *)dirName
                           file:(NSString *)fileName
                      extension:(NSString *)fileExt
{
    self = [super init];

    if(self)
    {
        mpFile = new (std::nothrow) CF::File(domain,
                                             directory,
                                             CFStringRef(dirName),
                                             CFStringRef(fileName),
                                             CFStringRef(fileExt));
    } // if

    return self;
} // initWithSearchPathDirectory

- (instancetype) initWithFile:(NSFile *)file
{
    self = [super init];

    if(self)
    {
        mpFile = new (std::nothrow) CF::File(CFURLRef(file.url));
    } // if

    return self;
} // initWithFile

- (instancetype) copyWithZone:(NSZone *)zone
{
    return [[NSFile allocWithZone:zone] initWithFile:self];
} // copyWithZone

+ (instancetype) fileWithPathname:(NSString *)pathname
{
    return [[[NSFile allocWithZone:[self zone]] initWithPathname:pathname] autorelease];
} // fileWithPathname

+ (instancetype) fileWithResourceInAppBundle:(NSString *)fileName
                                   extension:(NSString *)fileExt
{
    return [[[NSFile allocWithZone:[self zone]] initWithResourceInAppBundle:fileName
                                                                  extension:fileExt] autorelease];
} // fileWithResourceInAppBundle

+ (instancetype) fileWithDomain:(NSSearchPathDomainMask)domain
                         search:(NSSearchPathDirectory)directory
                      directory:(NSString *)dirName
                           file:(NSString *)fileName
                      extension:(NSString *)fileExt
{
    return [[[NSFile allocWithZone:[self zone]] initWithDomain:domain
                                                        search:directory
                                                     directory:dirName
                                                          file:fileName
                                                     extension:fileExt] autorelease];
} // fileWithDomain

+ (instancetype) fileWithFile:(NSFile *)file
{
    return [[[NSFile allocWithZone:[self zone]] initWithFile:file] autorelease];
} // fileWithFile

- (void) dealloc
{
    if(mpFile != nullptr)
    {
        delete mpFile;

        mpFile = nullptr;
    } // if

    [super dealloc];
} // dealloc

- (void) replace:(id)plist
{
    *mpFile = CFPropertyListRef(plist);
} // replace

- (NSSearchPathDirectory) directory
{
    return mpFile->directory();
} // directory

- (NSSearchPathDomainMask) domain
{
    return mpFile->domain();
} // domain

- (NSPropertyListFormat) format
{
    return NSPropertyListFormat(mpFile->format());
} // format

- (NSInteger) length
{
    return mpFile->length();
} // length

- (BOOL) isPList
{
    return mpFile->isPList();
} // isPlist

- (id) plist
{
    return id(mpFile->plist());
} // plist

- (NSURL *) url
{
    return NSURLRef(mpFile->url());
} // url

- (NSMutableData *) data
{
    return NSMutableDataRef(mpFile->data());
} // data

- (const uint8_t *) bytes
{
    return mpFile->bytes();
} // bytes

- (const char *) cstring
{
    return mpFile->cstring();
} // cstring

- (NSString *) string
{
    return [NSString stringWithCString:mpFile->cstring()
                              encoding:NSASCIIStringEncoding];
} // string

- (BOOL) write
{
    return mpFile->write();
} // write

- (BOOL) write:(NSString *)pathname
{
    return mpFile->write(CFStringRef(pathname));
} // write

- (BOOL) write:(NSString *)fileName
     extension:(NSString *)fileExt
{
    return mpFile->write(CFStringRef(fileName),
                         CFStringRef(fileExt));
} // write

@end
```

[Next](Sources-Model-Foundation-Frame-CTFrame.h.md)[Previous](Sources-Model-Foundation-Files-CFFile.h.md)

