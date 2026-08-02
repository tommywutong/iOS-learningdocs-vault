---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/GLKit.html
archived_at: '2026-07-18T02:56:33.697045Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# GLKit Changes for Objective-C

### GLKit

#### GLKBaseEffect.h

Modified [GLKBaseEffect.textureOrder](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488830-textureorder)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *textureOrder ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<GLKEffectPropertyTexture *> *textureOrder ``` |

#### GLKModel.h (Added)

Added [GLKMesh](https://developer.apple.com/documentation/glkit/glkmesh)Added [-[GLKMesh initWithMesh:error:]](https://developer.apple.com/documentation/glkit/glkmesh/1488759-init)Added [GLKMesh.name](https://developer.apple.com/documentation/glkit/glkmesh/1489104-name)Added [+[GLKMesh newMeshesFromAsset:sourceMeshes:error:]](https://developer.apple.com/documentation/glkit/glkmesh/1488791-newmeshesfromasset)Added [GLKMesh.submeshes](https://developer.apple.com/documentation/glkit/glkmesh/1489060-submeshes)Added [GLKMesh.vertexBuffers](https://developer.apple.com/documentation/glkit/glkmesh/1488688-vertexbuffers)Added [GLKMesh.vertexCount](https://developer.apple.com/documentation/glkit/glkmesh/1489043-vertexcount)Added [GLKMesh.vertexDescriptor](https://developer.apple.com/documentation/glkit/glkmesh/1488990-vertexdescriptor)Added [GLKMeshBuffer](https://developer.apple.com/documentation/glkit/glkmeshbuffer)Added [GLKMeshBuffer.allocator](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1489083-allocator)Added [GLKMeshBuffer.glBufferName](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1488636-glbuffername)Added [GLKMeshBuffer.length](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1488631-length)Added [GLKMeshBuffer.offset](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1488607-offset)Added [GLKMeshBuffer.type](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1488681-type)Added [GLKMeshBuffer.zone](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1538271-zone)Added [GLKMeshBufferAllocator](https://developer.apple.com/documentation/glkit/glkmeshbufferallocator)Added [GLKSubmesh](https://developer.apple.com/documentation/glkit/glksubmesh)Added [GLKSubmesh.elementBuffer](https://developer.apple.com/documentation/glkit/glksubmesh/1488972-elementbuffer)Added [GLKSubmesh.elementCount](https://developer.apple.com/documentation/glkit/glksubmesh/1489103-elementcount)Added [GLKSubmesh.mesh](https://developer.apple.com/documentation/glkit/glksubmesh/1489108-mesh)Added [GLKSubmesh.mode](https://developer.apple.com/documentation/glkit/glksubmesh/1488690-mode)Added [GLKSubmesh.name](https://developer.apple.com/documentation/glkit/glksubmesh/1488724-name)Added [GLKSubmesh.type](https://developer.apple.com/documentation/glkit/glksubmesh/1489072-type)Added [GLKVertexAttributeParameters](https://developer.apple.com/documentation/glkit/glkvertexattributeparameters)Added [GLKVertexAttributeParametersFromModelIO()](https://developer.apple.com/documentation/glkit/1488915-glkvertexattributeparametersfrom)Added [kGLKModelErrorDomain](https://developer.apple.com/documentation/glkit/kglkmodelerrordomain)Added [kGLKModelErrorKey](https://developer.apple.com/documentation/glkit/kglkmodelerrorkey)

#### GLKTextureLoader.h

Modified [+[GLKTextureLoader cubeMapWithContentsOfFile:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488848-cubemap)

|  | Declaration |
| --- | --- |
| From | ``` + (GLKTextureInfo *)cubeMapWithContentsOfFile:(NSString *)path options:(NSDictionary *)options error:(NSError **)outError ``` |
| To | ``` + (GLKTextureInfo * _Nullable)cubeMapWithContentsOfFile:(NSString * _Nonnull)path options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[GLKTextureLoader cubeMapWithContentsOfFile:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488617-cubemapwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cubeMapWithContentsOfFile:(NSString *)path options:(NSDictionary *)options queue:(dispatch_queue_t)queue completionHandler:(GLKTextureLoaderCallback)block ``` |
| To | ``` - (void)cubeMapWithContentsOfFile:(NSString * _Nonnull)path options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options queue:(dispatch_queue_t _Nullable)queue completionHandler:(GLKTextureLoaderCallback _Nonnull)block ``` |

Modified [+[GLKTextureLoader cubeMapWithContentsOfFiles:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488810-cubemapwithcontentsoffiles)

|  | Declaration |
| --- | --- |
| From | ``` + (GLKTextureInfo *)cubeMapWithContentsOfFiles:(NSArray *)paths options:(NSDictionary *)options error:(NSError **)outError ``` |
| To | ``` + (GLKTextureInfo * _Nullable)cubeMapWithContentsOfFiles:(NSArray<id> * _Nonnull)paths options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[GLKTextureLoader cubeMapWithContentsOfFiles:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488854-cubemapwithcontentsoffiles)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cubeMapWithContentsOfFiles:(NSArray *)paths options:(NSDictionary *)options queue:(dispatch_queue_t)queue completionHandler:(GLKTextureLoaderCallback)block ``` |
| To | ``` - (void)cubeMapWithContentsOfFiles:(NSArray<id> * _Nonnull)paths options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options queue:(dispatch_queue_t _Nullable)queue completionHandler:(GLKTextureLoaderCallback _Nonnull)block ``` |

Modified [+[GLKTextureLoader cubeMapWithContentsOfURL:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488743-cubemap)

|  | Declaration |
| --- | --- |
| From | ``` + (GLKTextureInfo *)cubeMapWithContentsOfURL:(NSURL *)url options:(NSDictionary *)options error:(NSError **)outError ``` |
| To | ``` + (GLKTextureInfo * _Nullable)cubeMapWithContentsOfURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[GLKTextureLoader cubeMapWithContentsOfURL:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488926-cubemap)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cubeMapWithContentsOfURL:(NSURL *)url options:(NSDictionary *)options queue:(dispatch_queue_t)queue completionHandler:(GLKTextureLoaderCallback)block ``` |
| To | ``` - (void)cubeMapWithContentsOfURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options queue:(dispatch_queue_t _Nullable)queue completionHandler:(GLKTextureLoaderCallback _Nonnull)block ``` |

Modified [+[GLKTextureLoader textureWithCGImage:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488673-texture)

|  | Declaration |
| --- | --- |
| From | ``` + (GLKTextureInfo *)textureWithCGImage:(CGImageRef)cgImage options:(NSDictionary *)options error:(NSError **)outError ``` |
| To | ``` + (GLKTextureInfo * _Nullable)textureWithCGImage:(CGImageRef _Nonnull)cgImage options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[GLKTextureLoader textureWithCGImage:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488861-texturewithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)textureWithCGImage:(CGImageRef)cgImage options:(NSDictionary *)options queue:(dispatch_queue_t)queue completionHandler:(GLKTextureLoaderCallback)block ``` |
| To | ``` - (void)textureWithCGImage:(CGImageRef _Nonnull)cgImage options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options queue:(dispatch_queue_t _Nullable)queue completionHandler:(GLKTextureLoaderCallback _Nonnull)block ``` |

Modified [+[GLKTextureLoader textureWithContentsOfData:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1489081-texturewithcontentsofdata)

|  | Declaration |
| --- | --- |
| From | ``` + (GLKTextureInfo *)textureWithContentsOfData:(NSData *)data options:(NSDictionary *)options error:(NSError **)outError ``` |
| To | ``` + (GLKTextureInfo * _Nullable)textureWithContentsOfData:(NSData * _Nonnull)data options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[GLKTextureLoader textureWithContentsOfData:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488905-texturewithcontentsofdata)

|  | Declaration |
| --- | --- |
| From | ``` - (void)textureWithContentsOfData:(NSData *)data options:(NSDictionary *)options queue:(dispatch_queue_t)queue completionHandler:(GLKTextureLoaderCallback)block ``` |
| To | ``` - (void)textureWithContentsOfData:(NSData * _Nonnull)data options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options queue:(dispatch_queue_t _Nullable)queue completionHandler:(GLKTextureLoaderCallback _Nonnull)block ``` |

Modified [+[GLKTextureLoader textureWithContentsOfFile:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488932-texturewithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` + (GLKTextureInfo *)textureWithContentsOfFile:(NSString *)path options:(NSDictionary *)options error:(NSError **)outError ``` |
| To | ``` + (GLKTextureInfo * _Nullable)textureWithContentsOfFile:(NSString * _Nonnull)path options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[GLKTextureLoader textureWithContentsOfFile:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1489064-texture)

|  | Declaration |
| --- | --- |
| From | ``` - (void)textureWithContentsOfFile:(NSString *)path options:(NSDictionary *)options queue:(dispatch_queue_t)queue completionHandler:(GLKTextureLoaderCallback)block ``` |
| To | ``` - (void)textureWithContentsOfFile:(NSString * _Nonnull)path options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options queue:(dispatch_queue_t _Nullable)queue completionHandler:(GLKTextureLoaderCallback _Nonnull)block ``` |

Modified [+[GLKTextureLoader textureWithContentsOfURL:options:error:]](https://developer.apple.com/documentation/glkit/glktextureloader/1489025-texturewithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` + (GLKTextureInfo *)textureWithContentsOfURL:(NSURL *)url options:(NSDictionary *)options error:(NSError **)outError ``` |
| To | ``` + (GLKTextureInfo * _Nullable)textureWithContentsOfURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[GLKTextureLoader textureWithContentsOfURL:options:queue:completionHandler:]](https://developer.apple.com/documentation/glkit/glktextureloader/1488621-texturewithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (void)textureWithContentsOfURL:(NSURL *)url options:(NSDictionary *)options queue:(dispatch_queue_t)queue completionHandler:(GLKTextureLoaderCallback)block ``` |
| To | ``` - (void)textureWithContentsOfURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,NSNumber *> * _Nullable)options queue:(dispatch_queue_t _Nullable)queue completionHandler:(GLKTextureLoaderCallback _Nonnull)block ``` |

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
