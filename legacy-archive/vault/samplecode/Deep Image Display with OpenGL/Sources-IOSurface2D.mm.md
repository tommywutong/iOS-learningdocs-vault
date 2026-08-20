---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_IOSurface2D_mm.html
archived_at: '2026-07-18T03:06:08.304731Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-GLShader.h.md)[Previous](Sources-CGImageCopy.mm.md)

# Sources/IOSurface2D.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating a 2D I/O surface with immutable properties.
 */

#import <CoreVideo/CVPixelBuffer.h>

#import "CGImageCopy.h"
#import "NSBitmap.h"
#import "IOSurface2D.h"

enum : long
{
    kCVPixelFormatType_24RGB_BPP      = 3,
    kCVPixelFormatType_32RGBA_BPP     = 4,
    kCVPixelFormatType_48RGB_BPP      = 6,
    kCVPixelFormatType_64RGBAHalf_BPP = 8
};

static const size_t kIOSurface2DCount = 6;

static const void* kIOSurface2DKeys[kIOSurface2DCount] =
{
    kIOSurfaceWidth,
    kIOSurfaceHeight,
    kIOSurfacePixelFormat,
    kIOSurfaceBytesPerElement,
    kIOSurfaceBytesPerRow,
    kIOSurfaceAllocSize
};

#define CGBitmapIsRGBA(bpp,bpc)    (((bpp / bpc) % 2) == 0)
#define CGBitmapCheckBPP(bpp)      ((bpp == 24) || (bpp == 32) || (bpp == 48) || (bpp == 64))
#define CGBitmapHasAlpha(bpp)      ((bpp == 32) || (bpp == 64))
#define CGBitmapIs8BPC(bpp)        ((bpp == 24) || (bpp == 32))
#define CGBitmapGetChannels(bpp)   (((bpp == 24) || (bpp == 48)) ? 3 : 4)
#define CGBitmapGetByteOrder(bpp)  (CGBitmapIs8BPC(bpp) ? kCGBitmapByteOrder32Host : kCGBitmapByteOrder16Host)

@implementation IOSurface2D
{
@private
    BOOL  _isRGBA;
    BOOL  _avoidSync;

    size_t  _bytesPerPixel;
    size_t  _width;
    size_t  _height;
    size_t  _samplesPerPixel;
    size_t  _bitsPerComponent;
    size_t  _bitsPerPixel;
    size_t  _bytesPerRow;
    size_t  _size;

    uint32_t  _byteOrder;
    uint32_t  _bitmapInfo;

    OSType            _format;
    IOSurfaceRef      _surface;
    CGImageAlphaInfo  _alphaInfo;

    BOOL                  isFinalized;
    uint32_t              seed;
    IOSurfaceLockOptions  options;
}

//-----------------------------------------------------------------------------
//
// FIXME: Replace with the correct values once deep images are fully supported!
//
//-----------------------------------------------------------------------------

- (void) _initSurfaceRGBA
{
    _bitsPerComponent = _bitsPerPixel / CGBitmapGetChannels(_bitsPerPixel);

    _isRGBA = CGBitmapIsRGBA(_bitsPerPixel, _bitsPerComponent);

    if(!_isRGBA)
    {
        _bitsPerPixel = 4 * _bitsPerComponent;
    } // if
} // _initSurfaceRGBA

- (void) _initSurfaceInfo
{
    if(!_isRGBA)
    {
        _bitsPerPixel = 4 * _bitsPerComponent;
        _alphaInfo    = kCGImageAlphaNoneSkipLast;
    } // if
    else
    {
        _alphaInfo = CGBitmapHasAlpha(_bitsPerPixel)
        ? kCGImageAlphaPremultipliedLast
        : kCGImageAlphaNone;
    } // else

    _byteOrder  = CGBitmapGetByteOrder(_bitsPerPixel);
    _bitmapInfo = _alphaInfo | _byteOrder;
} // _initSurfaceInfo

- (void) _initSurfaceSize
{
    _samplesPerPixel = _bitsPerPixel / _bitsPerComponent;
    _bytesPerPixel   = _bitsPerPixel / 8;
    _bytesPerRow     = _width  * _bytesPerPixel;
    _size            = _height * _bytesPerRow;
} // _initSurfaceSize

- (void) _initSurfaceType
{
    switch(_bytesPerPixel)
    {
        case kCVPixelFormatType_24RGB_BPP:
            _format = kCVPixelFormatType_24RGB;
            break;

        case kCVPixelFormatType_48RGB_BPP:
            _format = kCVPixelFormatType_48RGB;
            break;

        case kCVPixelFormatType_64RGBAHalf_BPP:
            _format = kCVPixelFormatType_64RGBAHalf;
            break;

        default:
        case kCVPixelFormatType_32RGBA_BPP:
            _format = kCVPixelFormatType_32RGBA;
            break;
    } // switch
} // _initSurfaceType

- (BOOL) _initSurfaceProperties
{
    BOOL success = CGBitmapCheckBPP(_bitsPerPixel);

    if(success)
    {
        [self _initSurfaceRGBA];
        [self _initSurfaceInfo];
        [self _initSurfaceSize];
        [self _initSurfaceType];
    } // if

    return success;
} // _initSurfaceProperties

- (BOOL) _initSurfaceProperties:(nullable CGImageRef)pImage
{
    size_t nBPP = CGImageGetBitsPerPixel(pImage);

    BOOL success = CGBitmapCheckBPP(nBPP);

    if(success)
    {
        _bitsPerPixel     = nBPP;
        _bitsPerComponent = CGImageGetBitsPerComponent(pImage);

        _isRGBA = CGBitmapIsRGBA(_bitsPerPixel, _bitsPerComponent);

        if(!_isRGBA)
        {
            _bitsPerPixel = 4 * _bitsPerComponent;
            _alphaInfo    = kCGImageAlphaNoneSkipLast;
            _byteOrder    = CGBitmapGetByteOrder(_bitsPerPixel);
            _bitmapInfo   = _alphaInfo | _byteOrder;
        } // if
        else
        {
            _alphaInfo  = CGImageGetAlphaInfo(pImage);
            _bitmapInfo = CGImageGetBitmapInfo(pImage);
            _byteOrder  = _bitmapInfo & kCGBitmapByteOrderMask;
        } // else

        _width  = CGImageGetWidth(pImage);
        _height = CGImageGetHeight(pImage);

        [self _initSurfaceSize];
        [self _initSurfaceType];
    } // if

    return success;
} // _initSurfaceProperties

- (nullable IOSurfaceRef) _newSurface
{
    IOSurfaceRef surface = nullptr;

    const void* values[kIOSurface2DCount];

    values[0] = CFNumberCreate(kCFAllocatorDefault, kCFNumberLongType, &_width);
    values[1] = CFNumberCreate(kCFAllocatorDefault, kCFNumberLongType, &_height);
    values[2] = CFNumberCreate(kCFAllocatorDefault, kCFNumberIntType,  &_format);
    values[3] = CFNumberCreate(kCFAllocatorDefault, kCFNumberLongType, &_bytesPerPixel);
    values[4] = CFNumberCreate(kCFAllocatorDefault, kCFNumberLongType, &_bytesPerRow);
    values[5] = CFNumberCreate(kCFAllocatorDefault, kCFNumberLongType, &_size);

    CFDictionaryRef  properties = CFDictionaryCreate(kCFAllocatorDefault,
                                                     kIOSurface2DKeys,
                                                     values,
                                                     kIOSurface2DCount,
                                                     &kCFTypeDictionaryKeyCallBacks,
                                                     &kCFTypeDictionaryValueCallBacks);

    if(properties != nullptr)
    {
        surface = IOSurfaceCreate(properties);

        CFRelease(properties);
    } // if

    size_t i;

    for(i = 0; i < kIOSurface2DCount; ++i)
    {
        if(values[i] != nullptr)
        {
            CFRelease(values[i]);
        } // if
    } // for

    return surface;
} // _newSurface

- (BOOL) _newSurface:(nullable CGImageRef)pImage
{
    isFinalized = pImage != nullptr;

    if(isFinalized)
    {
        isFinalized = [self _initSurfaceProperties:pImage];

        if(isFinalized)
        {
            _surface = [self _newSurface];

            isFinalized = _surface != nullptr;
        } // if
    } // if

    return isFinalized;
} // _newSurface

- (BOOL) _drawImage:(nullable CGImageRef)pImage
{
    BOOL success = [self _newSurface:pImage];

    if(success)
    {
        CGColorSpaceRef pColorSpace = CGColorSpaceCreateDeviceRGB();

        if(pColorSpace != nullptr)
        {
            IOReturn result = IOSurfaceLock(_surface, 0, &seed);

            success = result == kIOReturnSuccess;

            if(success)
            {
                void* pBaseAddr = IOSurfaceGetBaseAddressOfPlane(_surface, 0);

                if(pBaseAddr != nullptr)
                {
                    CGContextRef pContext = CGBitmapContextCreate(pBaseAddr,
                                                                  _width,
                                                                  _height,
                                                                  _bitsPerComponent,
                                                                  _bytesPerRow,
                                                                  pColorSpace,
                                                                  _bitmapInfo);

                    if(pContext != nullptr)
                    {
                        CGRect bounds = CGRectMake(0, 0, _width, _height);

                        CGContextDrawImage(pContext, bounds, pImage);

                        CFRelease(pContext);
                    } // if
                } // if

                IOSurfaceUnlock(_surface, 0, &seed);
            } // if

            CFRelease(pColorSpace);
        } // if
    } // if

    return success;
} // _drawImage

- (BOOL) _initSurfaceWithImageSource:(nullable CGImageSourceRef)pImageSource
{
    BOOL success = pImageSource != nullptr;

    if(success)
    {
        CGImageRef pImage = CGImageSourceCreateImageAtIndex(pImageSource,
                                                            0,
                                                            NULL);

        success = pImage != nullptr;

        if(success)
        {
            success = [self _drawImage:pImage];

            CFRelease(pImage);
        } // if
    } // if

    return success;
} // _initSurfaceWithImageSource

- (BOOL) _initSurfaceWithImage:(nullable NSImage *)image
{
    BOOL success = NO;

    if(image)
    {
        NSBitmapImageRep* bitmap = [NSBitmap bitmapWithImage:image].bitmap;

        if(bitmap)
        {
            success = !bitmap.isPlanar;

            if(success)
            {
                success = [self _drawImage:bitmap.CGImage];
            } // if
        } // if
    } // if

    return success;
} // _initSurfaceWithImage

- (void) _initSurfaceWithURL:(nullable NSURL *)url
{
    if(url)
    {
        // Create an image source from the URL.
        CGImageSourceRef pImageSource = CGImageSourceCreateWithURL(CFURLRef(url), nullptr);

        if(pImageSource != nullptr)
        {
            [self _initSurfaceWithImageSource:pImageSource];

            CFRelease(pImageSource);
        } // if
    } // if
} // _initSurfaceWithFile


- (void) _initSurfaceWithFile:(nullable NSString *)path
{
    if(path)
    {
        // Load the source image
        NSURL* url = [NSURL fileURLWithPath:path];

        if(url)
        {
            [self _initSurfaceWithURL:url];
        } // if
    } // if
} // _initSurfaceWithFile

- (void) _initIOSurface2DWithResource:(nullable NSString *)name
{
    if(name)
    {
        // Acquire the absolute pathname to the image resource in application's bundle
        NSBundle* bundle   = [NSBundle mainBundle];
        NSString* resource = [bundle resourcePath];
        NSString* path     = [NSString stringWithFormat:@"%@/%@", resource, name];

        [self _initSurfaceWithFile:path];
    } // if
} // initTextureWithResource

// Initialize instance variables
- (void) _initialize
{
    _bytesPerPixel    = 0;
    _samplesPerPixel  = 0;
    _bytesPerRow      = 0;
    _size             = 0;
    _bitmapInfo       = 0;
    _byteOrder        = 0;
    _format           = 0;
    _width            = 1920;
    _height           = 1080;
    _bitsPerPixel     = 32;
    _bitsPerComponent = 8;
    _alphaInfo        = kCGImageAlphaPremultipliedLast;
    _surface          = nullptr;
    _avoidSync        = YES;
    _isRGBA           = YES;

    isFinalized = NO;
    seed        = 0;
    options     = 0;
} // _initialize

// Default initializer to create a 2D I/O surface
- (nullable instancetype) init
{
    self = [super init];

    if(self)
    {
        [self _initialize];
    } // if

    return self;
} // init

+ (nullable instancetype) surface
{
    return [[[IOSurface2D allocWithZone:[self zone]] init] autorelease];
} // surfaceWithImage

// Designated initializer to create a 2D I/O surface from an image.
- (nullable instancetype) initWithImage:(nullable NSImage *)image
{
    self = [super init];

    if(self)
    {
        [self _initialize];
        [self _initSurfaceWithImage:image];
    } // if

    return self;
} // initWithImage

+ (nullable instancetype) surfaceWithImage:(nullable NSImage *)image
{
    return [[[IOSurface2D allocWithZone:[self zone]] initWithImage:image] autorelease];
} // surfaceWithImage

// Designated initializer to create a 2D I/O surface from an image
- (nullable instancetype) initWithImageRef:(nullable CGImageRef)image
{
    self = [super init];

    if(self)
    {
        [self _initialize];
        [self _drawImage:image];
    } // if

    return self;
} // initWithImageRef

+ (nullable instancetype) surfaceWithImageRef:(nullable CGImageRef)image
{
    return [[[IOSurface2D allocWithZone:[self zone]] initWithImageRef:image] autorelease];
} // surfaceWithImageRef

// Designated initializer to create a 2D I/O surface from an image file located at a URL
- (nullable instancetype) initWithURL:(nullable NSURL *)url
{
    self = [super init];

    if(self)
    {
        [self _initialize];
        [self _initSurfaceWithURL:url];
    } // if

    return self;
} // initWithURL

+ (nullable instancetype) surfaceWithURL:(nullable NSURL *)url
{
    return [[[IOSurface2D allocWithZone:[self zone]] initWithURL:url] autorelease];
} // surfaceWithURL

// Designated initializer to create a 2D I/O surface from an image file located at an absolute path
- (nullable instancetype) initWithFile:(nullable NSString *)path
{
    self = [super init];

    if(self)
    {
        [self _initialize];
        [self _initSurfaceWithFile:path];
    } // if

    return self;
} // initWithFile

+ (nullable instancetype) surfaceWithFile:(nullable NSString *)path
{
    return [[[IOSurface2D allocWithZone:[self zone]] initWithFile:path] autorelease];
} // surfaceWithFile

// Designated initializer to create a 2D I/O surface from an image file in application's bundle
- (nullable instancetype) initWithResource:(nullable NSString *)name
{
    self = [super init];

    if(self)
    {
        [self _initialize];
        [self _initIOSurface2DWithResource:name];
    } // if

    return self;
} // initWithResource

+ (nullable instancetype) surfaceWithResource:(nullable NSString *)name
{
    return [[[IOSurface2D allocWithZone:[self zone]] initWithResource:name] autorelease];
} // surfaceWithResource

// Destructor
- (void) dealloc
{
    if(_surface != nullptr)
    {
        CFRelease(_surface);
    } // if

    [super dealloc];
} // dealloc

- (nonnull instancetype) copyWithZone:(NSZone *)zone
{
    IOSurface2D* pSurface = [IOSurface2D new];

    if(pSurface)
    {
        pSurface.avoidSync        = _avoidSync;
        pSurface.bitsPerComponent = _bitsPerComponent;
        pSurface.bitsPerPixel     = _bitsPerPixel;
        pSurface.alphaInfo        = _alphaInfo;
        pSurface.width            = _width;
        pSurface.height           = _height;

        if([pSurface acquire])
        {
            [pSurface copy:_surface];
        } // if
    } // if

    return pSurface;
} // copyWithZone

// I/O surface bits-per-component
- (void) setBitsPerComponent:(size_t)bitsPerComponent
{
    if(!isFinalized)
    {
        _bitsPerComponent = bitsPerComponent;
    } // if
} // setBitsPerSample

// I/O surface bits-per-pixel
- (void) setBitsPerPixel:(size_t)bitsPerPixel
{
    if(!isFinalized)
    {
        _bitsPerPixel = bitsPerPixel;
    } // if
} // setSamplesPerPixel

// I/O surface alpha info
- (void) setAlphaInfo:(CGImageAlphaInfo)alphaInfo
{
    if(!isFinalized)
    {
        _alphaInfo = alphaInfo;
    } // if
} // setAlphaInfo

// I/O surface width
- (void) setWidth:(size_t)width
{
    if(!isFinalized)
    {
        _width = width;
    } // if
} // setWidth

// I/O surface height
- (void) setHeight:(size_t)height
{
    if(!isFinalized)
    {
        _height = height;
    } // if
} // setHeight

// Create a new I/O surface if the properties were set and default
// initializer was used to instantiate the object
- (BOOL) acquire
{
    BOOL success = _surface == nullptr;

    if(success)
    {
        success = [self _initSurfaceProperties];

        if(success)
        {
            _surface = [self _newSurface];

            isFinalized = _surface != nullptr;
        } // if
    } // if

    return success;
} // acquire

// Update the I/O surface data.  Does not require locking or unlocking.
// Also, note that the source data properties used here for write must
// match the created i/o surface.  You can not use this method to copy
// RGB to RGBA image.
- (BOOL) update:(nullable const uint8_t *)pBaseAddrSrc
{
    BOOL success = (pBaseAddrSrc != nullptr) && isFinalized;

    if(success)
    {
        IOReturn result = IOSurfaceLock(_surface, 0, &seed);

        success = result == kIOReturnSuccess;

        if(success)
        {
            uint8_t* pBaseAddrDst = static_cast<uint8_t *>(IOSurfaceGetBaseAddressOfPlane(_surface, 0));

            success = pBaseAddrDst != nullptr;

            if(success)
            {
                CG::memcpy(_size, pBaseAddrSrc, pBaseAddrDst);
            } // if

            IOSurfaceUnlock(_surface, 0, &seed);
        } // if
    } // if

    return success;
} // update

// The copy methods below do not require locking or unlocking.
// Also, note that the source i/o surface properties used here
// for copy must match the created i/o surface.  Furthermore,
// you can not use this method to copy RGB to RGBA i/o surface.

// Make a copy of an I/O surface image in a plane with index 0.
- (BOOL) copy:(nullable const IOSurfaceRef)surface
{
    IOReturn nResult = kIOReturnError;

    CG::s2dcpy(0, surface, 0, _surface, nResult);

    return nResult == kIOReturnSuccess;
} // copy

// Make a copy of an I/O surface image in a plane at an index.
- (BOOL) copy:(nullable const IOSurfaceRef)surface
        index:(const size_t)index
{
    IOReturn nResult = kIOReturnError;

    CG::s2dcpy(index, surface, 0, _surface, nResult);

    return nResult == kIOReturnSuccess;
} // copy

// Map the base address of the I/O surface for reading data
- (nullable uint8_t *) map
{
    uint8_t* pBaseAddr = nullptr;

    if(isFinalized)
    {
        pBaseAddr = static_cast<uint8_t *>(IOSurfaceGetBaseAddress(_surface));
    } // if

    return pBaseAddr;
} // map

// Map the base address of the I/O surface for reading/writing data
- (nullable uint8_t *) map:(const NSPoint)point
{
    uint8_t* ptr = nullptr;

    if(isFinalized)
    {        
        uint8_t* base = static_cast<uint8_t *>(IOSurfaceGetBaseAddressOfPlane(_surface, 0));

        const size_t width  = size_t(point.x) * _bytesPerPixel;
        const size_t height = size_t(point.y) * _bytesPerRow;
        const size_t offset = width + height;

        ptr = base + offset;
    } // if

    return ptr;
} // map

// Lock the I/O surface before mapping to read or write
- (BOOL) lock:(const BOOL)isReadOnly
{
    IOReturn result = kIOReturnError;

    if(isFinalized)
    {
        options = (isReadOnly) ? (kIOSurfaceLockReadOnly | ((_avoidSync) ? kIOSurfaceLockAvoidSync : 0)) : 0;

        result = IOSurfaceLock(_surface, options, &seed);
    } // if

    return result == kIOReturnSuccess;
} // lock

// Unlock the I/O surface after a mapped read or write
- (BOOL) unlock
{
    IOReturn result = kIOReturnError;

    if(isFinalized)
    {
        result = IOSurfaceUnlock(_surface, options, &seed);
    } // if

    return result == kIOReturnSuccess;
} // unlock

@end
```

[Next](Sources-GLShader.h.md)[Previous](Sources-CGImageCopy.mm.md)

