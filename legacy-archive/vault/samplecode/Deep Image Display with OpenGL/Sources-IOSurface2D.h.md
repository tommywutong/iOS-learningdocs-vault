---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_IOSurface2D_h.html
archived_at: '2026-07-18T03:06:08.216938Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-GLDIDAppDelegate.h.md)[Previous](Sources-Quad2D.fs.md)

# Sources/IOSurface2D.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating a 2D I/O surface with immutable properties.
 */

#import <IOSurface/IOSurface.h>

//-----------------------------------------------
// NOTE:  If the image is RGB, all constructors
//        will create an i/o surface 2d image
//        that is RGBA.
//-----------------------------------------------

@interface IOSurface2D : NSObject <NSCopying>

// Default (auto-released) initializer.  In addtion you can always
// instantiate a default object using alloc and init.
+ (nullable instancetype) surface;

// Designated initializer to create a 2D I/O surface from an image.
- (nullable instancetype) initWithImage:(nullable NSImage *)image;

+ (nullable instancetype) surfaceWithImage:(nullable NSImage *)image;

// Designated initializer to create a 2D I/O surface from an image
// reference.
- (nullable instancetype) initWithImageRef:(nullable CGImageRef)image;

+ (nullable instancetype) surfaceWithImageRef:(nullable CGImageRef)image;

// Designated initializer to create a 2D I/O surface from an image
// file located at a URL.
- (nullable instancetype) initWithURL:(nullable NSURL *)url;

+ (nullable instancetype) surfaceWithURL:(nullable NSURL *)url;

// Designated initializer to create a 2D I/O surface from an image
// file located at an absolute path.
- (nullable instancetype) initWithFile:(nullable NSString *)path;

+ (nullable instancetype) surfaceWithFile:(nullable NSString *)path;

// Designated initializer to create a 2D I/O surface from an image
// file in application's bundle.
- (nullable instancetype) initWithResource:(nullable NSString *)name;

+ (nullable instancetype) surfaceWithResource:(nullable NSString *)name;

// I/O surface reference
@property (nonatomic, readonly, nullable) IOSurfaceRef surface;

// I/O surface bytes-per-row
@property (nonatomic, readonly) size_t bytesPerRow;

// I/O surface bytes-per-pixel
@property (nonatomic, readonly) size_t bytesPerPixel;

// I/O surface allocation size
@property (nonatomic, readonly) size_t size;

// I/O surface pixel format
@property (nonatomic, readonly) OSType format;

// I/O surface samples-per-pixel
@property (nonatomic, readonly) size_t samplesPerPixel;

// If you want to detect/avoid a potentially expensive paging operation
// (such as readback from a GPU to system memory) when you lock the buffer,
// you may include this flag. If locking the buffer requires a readback,
// the lock will fail with an error return of kIOReturnCannotLock.
@property (nonatomic) BOOL avoidSync;

// I/O surface bits-per-component
@property (nonatomic) size_t bitsPerComponent;

// I/O surface bits-per-pixel
@property (nonatomic) size_t bitsPerPixel;

// I/O surface alpha info
@property (nonatomic) CGImageAlphaInfo alphaInfo;

// I/O surface width
@property (nonatomic) size_t width;

// I/O surface height
@property (nonatomic) size_t height;

// Create a new I/O surface if the properties were set and default
// initializer was used to instantiate the object. The backing-store
// is created for representing RGBA 32-bit or 64-bit images.
- (BOOL) acquire;

// Update the I/O surface data.  Does not require locking or unlocking.
// Also, note that the source data properties used here for write must
// match the created i/o surface.  You can not use this method to copy
// RGB to RGBA image.
- (BOOL) update:(nullable const uint8_t *)baseAddr;

// The copy methods below do not require locking or unlocking.
// Also, note that the source i/o surface properties used here
// for copy must match the created i/o surface.  Furthermore,
// you can not use this method to copy RGB to RGBA i/o surface.

// Make a copy of an I/O surface image in a plane with index 0.
- (BOOL) copy:(nullable const IOSurfaceRef)surface;

// Make a copy of an I/O surface image in a plane at an index.
- (BOOL) copy:(nullable const IOSurfaceRef)surface
        index:(const size_t)index;

// Map the base address of the I/O surface for reading/writing data
- (nullable uint8_t *) map;

// Map the base address of the I/O surface for reading/writing data
- (nullable uint8_t *) map:(const NSPoint)point;

// Lock the I/O surface before mapping to read or write
- (BOOL) lock:(const BOOL)isReadOnly;

// Unlock the I/O surface after a mapped read or write
- (BOOL) unlock;

@end
```

[Next](Sources-GLDIDAppDelegate.h.md)[Previous](Sources-Quad2D.fs.md)

