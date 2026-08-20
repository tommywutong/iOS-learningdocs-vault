---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/MetalKit.html
archived_at: '2026-07-18T02:50:41.326991Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# MetalKit Changes for Objective-C

### MetalKit

#### MTKModel.h

Added [MTKMetalVertexDescriptorFromModelIOWithError()](https://developer.apple.com/documentation/metalkit/1642764-mtkmetalvertexdescriptorfrommode)Added [MTKModelIOVertexDescriptorFromMetalWithError()](https://developer.apple.com/documentation/metalkit/1642762-mtkmodeliovertexdescriptorfromme)Modified [MTKMesh.name](https://developer.apple.com/documentation/metalkit/mtkmesh/1536038-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) NSString *name ``` |
| To | ``` @property(nonatomic, copy) NSString *name ``` |

Modified [MTKMeshBuffer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer)

|  | Protocols |
| --- | --- |
| From | MDLMeshBuffer |
| To | MDLMeshBuffer, MDLNamed |

Modified [MTKSubmesh.name](https://developer.apple.com/documentation/metalkit/mtksubmesh/1535953-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) NSString *name ``` |
| To | ``` @property(nonatomic, copy) NSString *name ``` |

#### MTKTextureLoader.h

Added [-[MTKTextureLoader newTexturesWithContentsOfURLs:options:completionHandler:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1645856-newtextureswithcontentsofurls)Added [-[MTKTextureLoader newTexturesWithContentsOfURLs:options:error:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1645862-newtextures)Added [-[MTKTextureLoader newTexturesWithNames:scaleFactor:bundle:options:completionHandler:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1645853-newtextureswithnames)Added [-[MTKTextureLoader newTexturesWithNames:scaleFactor:displayGamut:bundle:options:completionHandler:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/2118350-newtextures)Added [-[MTKTextureLoader newTextureWithMDLTexture:options:completionHandler:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1645858-newtexturewithmdltexture)Added [-[MTKTextureLoader newTextureWithMDLTexture:options:error:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1645861-newtexturewithmdltexture)Added [-[MTKTextureLoader newTextureWithName:scaleFactor:bundle:options:completionHandler:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1645851-newtexturewithname)Added [-[MTKTextureLoader newTextureWithName:scaleFactor:bundle:options:error:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1645855-newtexturewithname)Added [-[MTKTextureLoader newTextureWithName:scaleFactor:displayGamut:bundle:options:completionHandler:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/2118345-newtexturewithname)Added [-[MTKTextureLoader newTextureWithName:scaleFactor:displayGamut:bundle:options:error:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/2118347-newtexture)Added [MTKTextureLoaderArrayCallback](https://developer.apple.com/documentation/metalkit/mtktextureloaderarraycallback)Added [MTKTextureLoaderCubeLayoutVertical](https://developer.apple.com/documentation/metalkit/mtktextureloadercubelayoutvertical)Added [MTKTextureLoaderOptionCubeLayout](https://developer.apple.com/documentation/metalkit/mtktextureloaderoptioncubelayout)Added [MTKTextureLoaderOptionGenerateMipmaps](https://developer.apple.com/documentation/metalkit/mtktextureloader/option/1645867-generatemipmaps)Added [MTKTextureLoaderOptionOrigin](https://developer.apple.com/documentation/metalkit/mtktextureloader/option/1645864-origin)Added [MTKTextureLoaderOptionTextureStorageMode](https://developer.apple.com/documentation/metalkit/mtktextureloader/option/1645859-texturestoragemode)Added [MTKTextureLoaderOriginBottomLeft](https://developer.apple.com/documentation/metalkit/mtktextureloaderoriginbottomleft)Added [MTKTextureLoaderOriginFlippedVertically](https://developer.apple.com/documentation/metalkit/mtktextureloader/origin/1645863-flippedvertically)Added [MTKTextureLoaderOriginTopLeft](https://developer.apple.com/documentation/metalkit/mtktextureloader/origin/1645865-topleft)Modified [-[MTKTextureLoader newTextureWithCGImage:options:completionHandler:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1536039-newtexture)

|  | Declaration |
| --- | --- |
| From | ``` - (void)newTextureWithCGImage:(CGImageRef)cgImage options:(NSDictionary<NSString *,NSNumber *> *)options completionHandler:(MTKTextureLoaderCallback)completionHandler ``` |
| To | ``` - (void)newTextureWithCGImage:(CGImageRef)cgImage options:(NSDictionary<NSString *,NSObject *> *)options completionHandler:(MTKTextureLoaderCallback)completionHandler ``` |

Modified [-[MTKTextureLoader newTextureWithCGImage:options:error:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1536028-newtexture)

|  | Declaration |
| --- | --- |
| From | ``` - (id<MTLTexture>)newTextureWithCGImage:(CGImageRef)cgImage options:(NSDictionary<NSString *,NSNumber *> *)options error:(NSError * _Nullable *)error ``` |
| To | ``` - (id<MTLTexture>)newTextureWithCGImage:(CGImageRef)cgImage options:(NSDictionary<NSString *,NSObject *> *)options error:(NSError * _Nullable *)error ``` |

Modified [-[MTKTextureLoader newTextureWithContentsOfURL:options:completionHandler:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1535939-newtexturewithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (void)newTextureWithContentsOfURL:(NSURL *)URL options:(NSDictionary<NSString *,NSNumber *> *)options completionHandler:(MTKTextureLoaderCallback)completionHandler ``` |
| To | ``` - (void)newTextureWithContentsOfURL:(NSURL *)URL options:(NSDictionary<NSString *,NSObject *> *)options completionHandler:(MTKTextureLoaderCallback)completionHandler ``` |

Modified [-[MTKTextureLoader newTextureWithContentsOfURL:options:error:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1535963-newtexturewithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id<MTLTexture>)newTextureWithContentsOfURL:(NSURL *)URL options:(NSDictionary<NSString *,NSNumber *> *)options error:(NSError * _Nullable *)error ``` |
| To | ``` - (id<MTLTexture>)newTextureWithContentsOfURL:(NSURL *)URL options:(NSDictionary<NSString *,NSObject *> *)options error:(NSError * _Nullable *)error ``` |

Modified [-[MTKTextureLoader newTextureWithData:options:completionHandler:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1536031-newtexturewithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (void)newTextureWithData:(NSData *)data options:(NSDictionary<NSString *,NSNumber *> *)options completionHandler:(MTKTextureLoaderCallback)completionHandler ``` |
| To | ``` - (void)newTextureWithData:(NSData *)data options:(NSDictionary<NSString *,NSObject *> *)options completionHandler:(MTKTextureLoaderCallback)completionHandler ``` |

Modified [-[MTKTextureLoader newTextureWithData:options:error:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1535951-newtexturewithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id<MTLTexture>)newTextureWithData:(NSData *)data options:(NSDictionary<NSString *,NSNumber *> *)options error:(NSError * _Nullable *)error ``` |
| To | ``` - (id<MTLTexture>)newTextureWithData:(NSData *)data options:(NSDictionary<NSString *,NSObject *> *)options error:(NSError * _Nullable *)error ``` |

#### MTKView.h

Added [MTKView.colorspace](https://developer.apple.com/documentation/metalkit/mtkview/2177056-colorspace)Modified [MTKView](https://developer.apple.com/documentation/metalkit/mtkview)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | CALayerDelegate, NSCoding |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
