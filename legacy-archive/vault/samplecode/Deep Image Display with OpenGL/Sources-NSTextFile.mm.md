---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_NSTextFile_mm.html
archived_at: '2026-07-18T03:06:08.677640Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-GLQuad.h.md)[Previous](Sources-NSBitmap.h.md)

# Sources/NSTextFile.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for loading a text file.
 */

#import <iostream>
#import <string>

#import "NSTextFile.h"

@implementation NSTextFile
{
@private
    std::string m_String;
}

- (BOOL) _newStringWithURL:(nullable NSURL *)url
{
    NSError* error = nil;

    NSString* string = [NSString stringWithContentsOfURL:url
                                                encoding:NSASCIIStringEncoding
                                                   error:&error];

    if(error)
    {
        NSLog(@">> %@", error.description);

        [error release];

        return NO;
    } // if
    else
    {
        m_String = string.UTF8String;
    } // else

    return YES;
} // _newStringWithURL

- (BOOL) _newStringWithFile:(nullable NSString *)path
{
    NSError* error = nil;

    NSString* string = [NSString stringWithContentsOfFile:path
                                                 encoding:NSASCIIStringEncoding
                                                    error:&error];

    if(error)
    {
        NSLog(@">> %@", error.description);

        [error release];

        return NO;
    } // if
    else
    {
        m_String = string.UTF8String;
    } // else

    return YES;
} // _newStringWithFile

- (BOOL) _newStringWithResource:(nullable NSString *)name
                            ext:(nullable NSString *)ext
{
    if(name && ext)
    {
        // Acquire the absolute pathname to the resource in application's bundle
        NSString* rsrc = [[NSBundle mainBundle] resourcePath];
        NSString* path = [NSString stringWithFormat:@"%@/%@.%@", rsrc, name, ext];

        return [self _newStringWithFile:path];
    } // if

    return NO;
} // _newStringWithResource

// Load a text file located at a URL
- (nullable instancetype) initWithURL:(nullable NSURL *)url;
{
    self = [super init];

    if(self)
    {
        if(![self _newStringWithURL:url])
        {
            NSLog(@">> ERROR: Failed acquiring sources from the url <%@>", url.absoluteString);
        } // if
    } // if

    return self;
} // initWithURL

+ (nullable instancetype) textWithURL:(nullable NSURL *)url
{
    return [[[NSTextFile allocWithZone:[self zone]] initWithURL:url] autorelease];
} // textWithURL

// Create a shader from a source file located at an absolute path
- (nullable instancetype) initWithFile:(nullable NSString *)path
{
    self = [super init];

    if(self)
    {
        if(![self _newStringWithFile:path])
        {
            NSLog(@">> ERROR: Failed acquiring sources from the file at pathname \"%@\"", path);
        } // if
    } // if

    return self;
} // initWithFile

+ (nullable instancetype) textWithFile:(nullable NSString *)path
{
    return [[[NSTextFile allocWithZone:[self zone]] initWithFile:path] autorelease];
} // NSTextFile

// Create a shader from a source file in application's bundle
- (nullable instancetype) initWithResource:(nullable NSString *)name
                                       ext:(nullable NSString *)ext
{
    self = [super init];

    if(self)
    {
        if(![self _newStringWithResource:name ext:ext])
        {
            NSLog(@">> ERROR: Failed acquiring sources from the \"%@.%@\' at application's bunble!", name, ext);
        } // if
    } // if

    return self;
} // initWithResource

+ (nullable instancetype) textWithResource:(nullable NSString *)name
                                       ext:(nullable NSString *)ext
{
    return [[[NSTextFile allocWithZone:[self zone]] initWithResource:name ext:ext] autorelease];
} // textWithResource

// Destructor
- (void) dealloc
{
    if(!m_String.empty())
    {
        m_String.clear();
    } // if

    [super dealloc];
} // dealloc

// Text file content
- (nullable const char *) source
{
    return m_String.c_str();
} // source

@end
```

[Next](Sources-GLQuad.h.md)[Previous](Sources-NSBitmap.h.md)

