---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/GLKit.html
archived_at: '2026-07-18T02:53:06.539281Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# GLKit Changes for Objective-C

### GLKit

#### GLKBaseEffect.h

Modified [GLKBaseEffect.fog](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488697-fog)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) GLKEffectPropertyFog *fog ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GLKEffectPropertyFog *fog ``` |

Modified [GLKBaseEffect.label](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488835-label)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *label ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *label ``` |

Modified [GLKBaseEffect.light0](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488785-light0)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) GLKEffectPropertyLight *light0 ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GLKEffectPropertyLight *light0 ``` |

Modified [GLKBaseEffect.light1](https://developer.apple.com/documentation/glkit/glkbaseeffect/1489095-light1)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) GLKEffectPropertyLight *light1 ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GLKEffectPropertyLight *light1 ``` |

Modified [GLKBaseEffect.light2](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488671-light2)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) GLKEffectPropertyLight *light2 ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GLKEffectPropertyLight *light2 ``` |

Modified [GLKBaseEffect.material](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488753-material)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) GLKEffectPropertyMaterial *material ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GLKEffectPropertyMaterial *material ``` |

Modified [GLKBaseEffect.texture2d0](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488664-texture2d0)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) GLKEffectPropertyTexture *texture2d0 ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GLKEffectPropertyTexture *texture2d0 ``` |

Modified [GLKBaseEffect.texture2d1](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488699-texture2d1)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) GLKEffectPropertyTexture *texture2d1 ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GLKEffectPropertyTexture *texture2d1 ``` |

Modified [GLKBaseEffect.textureOrder](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488830-textureorder)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *textureOrder ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<GLKEffectPropertyTexture *> *textureOrder ``` |

Modified [GLKBaseEffect.transform](https://developer.apple.com/documentation/glkit/glkbaseeffect/1489030-transform)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) GLKEffectPropertyTransform *transform ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GLKEffectPropertyTransform *transform ``` |

#### GLKEffectPropertyLight.h

Modified [GLKEffectPropertyLight.transform](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473568-transform)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) GLKEffectPropertyTransform *transform ``` |
| To | ``` @property(nonatomic, retain, nonnull) GLKEffectPropertyTransform *transform ``` |

#### GLKMathUtils.h

Modified [GLKMathProject()](https://developer.apple.com/documentation/glkit/1488726-glkmathproject)

|  | Declaration |
| --- | --- |
| From | ``` GLKVector3 GLKMathProject (     GLKVector3 object,     GLKMatrix4 model,     GLKMatrix4 projection,     int *viewport ); ``` |
| To | ``` GLKVector3 GLKMathProject (     GLKVector3 object,     GLKMatrix4 model,     GLKMatrix4 projection,     int * _Nonnull viewport ); ``` |

Modified [GLKMathUnproject()](https://developer.apple.com/documentation/glkit/1488720-glkmathunproject)

|  | Declaration |
| --- | --- |
| From | ``` GLKVector3 GLKMathUnproject (     GLKVector3 window,     GLKMatrix4 model,     GLKMatrix4 projection,     int *viewport,     bool *success ); ``` |
| To | ``` GLKVector3 GLKMathUnproject (     GLKVector3 window,     GLKMatrix4 model,     GLKMatrix4 projection,     int * _Nonnull viewport,     bool * _Nonnull success ); ``` |

Modified [NSStringFromGLKMatrix2()](https://developer.apple.com/documentation/glkit/1489099-nsstringfromglkmatrix2)

|  | Declaration |
| --- | --- |
| From | ``` NSString * NSStringFromGLKMatrix2 (     GLKMatrix2 matrix ); ``` |
| To | ``` NSString * _Nonnull NSStringFromGLKMatrix2 (     GLKMatrix2 matrix ); ``` |

Modified [NSStringFromGLKMatrix3()](https://developer.apple.com/documentation/glkit/1489048-nsstringfromglkmatrix3)

|  | Declaration |
| --- | --- |
| From | ``` NSString * NSStringFromGLKMatrix3 (     GLKMatrix3 matrix ); ``` |
| To | ``` NSString * _Nonnull NSStringFromGLKMatrix3 (     GLKMatrix3 matrix ); ``` |

Modified [NSStringFromGLKMatrix4()](https://developer.apple.com/documentation/glkit/1488877-nsstringfromglkmatrix4)

|  | Declaration |
| --- | --- |
| From | ``` NSString * NSStringFromGLKMatrix4 (     GLKMatrix4 matrix ); ``` |
| To | ``` NSString * _Nonnull NSStringFromGLKMatrix4 (     GLKMatrix4 matrix ); ``` |

Modified [NSStringFromGLKQuaternion()](https://developer.apple.com/documentation/glkit/1488908-nsstringfromglkquaternion)

|  | Declaration |
| --- | --- |
| From | ``` NSString * NSStringFromGLKQuaternion (     GLKQuaternion quaternion ); ``` |
| To | ``` NSString * _Nonnull NSStringFromGLKQuaternion (     GLKQuaternion quaternion ); ``` |

Modified [NSStringFromGLKVector2()](https://developer.apple.com/documentation/glkit/1488857-nsstringfromglkvector2)

|  | Declaration |
| --- | --- |
| From | ``` NSString * NSStringFromGLKVector2 (     GLKVector2 vector ); ``` |
| To | ``` NSString * _Nonnull NSStringFromGLKVector2 (     GLKVector2 vector ); ``` |

Modified [NSStringFromGLKVector3()](https://developer.apple.com/documentation/glkit/1489089-nsstringfromglkvector3)

|  | Declaration |
| --- | --- |
| From | ``` NSString * NSStringFromGLKVector3 (     GLKVector3 vector ); ``` |
| To | ``` NSString * _Nonnull NSStringFromGLKVector3 (     GLKVector3 vector ); ``` |

Modified [NSStringFromGLKVector4()](https://developer.apple.com/documentation/glkit/1489056-nsstringfromglkvector4)

|  | Declaration |
| --- | --- |
| From | ``` NSString * NSStringFromGLKVector4 (     GLKVector4 vector ); ``` |
| To | ``` NSString * _Nonnull NSStringFromGLKVector4 (     GLKVector4 vector ); ``` |

#### GLKMatrixStack.h

Modified [GLKMatrixStackCreate()](https://developer.apple.com/documentation/glkit/1483169-glkmatrixstackcreate)

|  | Declaration |
| --- | --- |
| From | ``` GLKMatrixStackRef GLKMatrixStackCreate (     CFAllocatorRef alloc ); ``` |
| To | ``` GLKMatrixStackRef _Nullable GLKMatrixStackCreate (     CFAllocatorRef _Nullable alloc ); ``` |

Modified [GLKMatrixStackGetMatrix2()](https://developer.apple.com/documentation/glkit/1483181-glkmatrixstackgetmatrix2)

|  | Declaration |
| --- | --- |
| From | ``` GLKMatrix2 GLKMatrixStackGetMatrix2 (     GLKMatrixStackRef stack ); ``` |
| To | ``` GLKMatrix2 GLKMatrixStackGetMatrix2 (     GLKMatrixStackRef _Nonnull stack ); ``` |

Modified [GLKMatrixStackGetMatrix3()](https://developer.apple.com/documentation/glkit/1483158-glkmatrixstackgetmatrix3)

|  | Declaration |
| --- | --- |
| From | ``` GLKMatrix3 GLKMatrixStackGetMatrix3 (     GLKMatrixStackRef stack ); ``` |
| To | ``` GLKMatrix3 GLKMatrixStackGetMatrix3 (     GLKMatrixStackRef _Nonnull stack ); ``` |

Modified [GLKMatrixStackGetMatrix3Inverse()](https://developer.apple.com/documentation/glkit/1483159-glkmatrixstackgetmatrix3inverse)

|  | Declaration |
| --- | --- |
| From | ``` GLKMatrix3 GLKMatrixStackGetMatrix3Inverse (     GLKMatrixStackRef stack ); ``` |
| To | ``` GLKMatrix3 GLKMatrixStackGetMatrix3Inverse (     GLKMatrixStackRef _Nonnull stack ); ``` |

Modified [GLKMatrixStackGetMatrix3InverseTranspose()](https://developer.apple.com/documentation/glkit/1483160-glkmatrixstackgetmatrix3inverset)

|  | Declaration |
| --- | --- |
| From | ``` GLKMatrix3 GLKMatrixStackGetMatrix3InverseTranspose (     GLKMatrixStackRef stack ); ``` |
| To | ``` GLKMatrix3 GLKMatrixStackGetMatrix3InverseTranspose (     GLKMatrixStackRef _Nonnull stack ); ``` |

Modified [GLKMatrixStackGetMatrix4()](https://developer.apple.com/documentation/glkit/1483163-glkmatrixstackgetmatrix4)

|  | Declaration |
| --- | --- |
| From | ``` GLKMatrix4 GLKMatrixStackGetMatrix4 (     GLKMatrixStackRef stack ); ``` |
| To | ``` GLKMatrix4 GLKMatrixStackGetMatrix4 (     GLKMatrixStackRef _Nonnull stack ); ``` |

Modified [GLKMatrixStackGetMatrix4Inverse()](https://developer.apple.com/documentation/glkit/1483168-glkmatrixstackgetmatrix4inverse)

|  | Declaration |
| --- | --- |
| From | ``` GLKMatrix4 GLKMatrixStackGetMatrix4Inverse (     GLKMatrixStackRef stack ); ``` |
| To | ``` GLKMatrix4 GLKMatrixStackGetMatrix4Inverse (     GLKMatrixStackRef _Nonnull stack ); ``` |

Modified [GLKMatrixStackGetMatrix4InverseTranspose()](https://developer.apple.com/documentation/glkit/1483184-glkmatrixstackgetmatrix4inverset)

|  | Declaration |
| --- | --- |
| From | ``` GLKMatrix4 GLKMatrixStackGetMatrix4InverseTranspose (     GLKMatrixStackRef stack ); ``` |
| To | ``` GLKMatrix4 GLKMatrixStackGetMatrix4InverseTranspose (     GLKMatrixStackRef _Nonnull stack ); ``` |

Modified [GLKMatrixStackLoadMatrix4()](https://developer.apple.com/documentation/glkit/1483161-glkmatrixstackloadmatrix4)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackLoadMatrix4 (     GLKMatrixStackRef stack,     GLKMatrix4 matrix ); ``` |
| To | ``` void GLKMatrixStackLoadMatrix4 (     GLKMatrixStackRef _Nonnull stack,     GLKMatrix4 matrix ); ``` |

Modified [GLKMatrixStackMultiplyMatrix4()](https://developer.apple.com/documentation/glkit/1483162-glkmatrixstackmultiplymatrix4)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackMultiplyMatrix4 (     GLKMatrixStackRef stack,     GLKMatrix4 matrix ); ``` |
| To | ``` void GLKMatrixStackMultiplyMatrix4 (     GLKMatrixStackRef _Nonnull stack,     GLKMatrix4 matrix ); ``` |

Modified [GLKMatrixStackMultiplyMatrixStack()](https://developer.apple.com/documentation/glkit/1483197-glkmatrixstackmultiplymatrixstac)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackMultiplyMatrixStack (     GLKMatrixStackRef stackLeft,     GLKMatrixStackRef stackRight ); ``` |
| To | ``` void GLKMatrixStackMultiplyMatrixStack (     GLKMatrixStackRef _Nonnull stackLeft,     GLKMatrixStackRef _Nonnull stackRight ); ``` |

Modified [GLKMatrixStackPop()](https://developer.apple.com/documentation/glkit/1483174-glkmatrixstackpop)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackPop (     GLKMatrixStackRef stack ); ``` |
| To | ``` void GLKMatrixStackPop (     GLKMatrixStackRef _Nonnull stack ); ``` |

Modified [GLKMatrixStackPush()](https://developer.apple.com/documentation/glkit/1483190-glkmatrixstackpush)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackPush (     GLKMatrixStackRef stack ); ``` |
| To | ``` void GLKMatrixStackPush (     GLKMatrixStackRef _Nonnull stack ); ``` |

Modified [GLKMatrixStackRotate()](https://developer.apple.com/documentation/glkit/1483179-glkmatrixstackrotate)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackRotate (     GLKMatrixStackRef stack,     float radians,     float x,     float y,     float z ); ``` |
| To | ``` void GLKMatrixStackRotate (     GLKMatrixStackRef _Nonnull stack,     float radians,     float x,     float y,     float z ); ``` |

Modified [GLKMatrixStackRotateWithVector3()](https://developer.apple.com/documentation/glkit/1483192-glkmatrixstackrotatewithvector3)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackRotateWithVector3 (     GLKMatrixStackRef stack,     float radians,     GLKVector3 axisVector ); ``` |
| To | ``` void GLKMatrixStackRotateWithVector3 (     GLKMatrixStackRef _Nonnull stack,     float radians,     GLKVector3 axisVector ); ``` |

Modified [GLKMatrixStackRotateWithVector4()](https://developer.apple.com/documentation/glkit/1483188-glkmatrixstackrotatewithvector4)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackRotateWithVector4 (     GLKMatrixStackRef stack,     float radians,     GLKVector4 axisVector ); ``` |
| To | ``` void GLKMatrixStackRotateWithVector4 (     GLKMatrixStackRef _Nonnull stack,     float radians,     GLKVector4 axisVector ); ``` |

Modified [GLKMatrixStackRotateX()](https://developer.apple.com/documentation/glkit/1483195-glkmatrixstackrotatex)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackRotateX (     GLKMatrixStackRef stack,     float radians ); ``` |
| To | ``` void GLKMatrixStackRotateX (     GLKMatrixStackRef _Nonnull stack,     float radians ); ``` |

Modified [GLKMatrixStackRotateY()](https://developer.apple.com/documentation/glkit/1483157-glkmatrixstackrotatey)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackRotateY (     GLKMatrixStackRef stack,     float radians ); ``` |
| To | ``` void GLKMatrixStackRotateY (     GLKMatrixStackRef _Nonnull stack,     float radians ); ``` |

Modified [GLKMatrixStackRotateZ()](https://developer.apple.com/documentation/glkit/1483171-glkmatrixstackrotatez)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackRotateZ (     GLKMatrixStackRef stack,     float radians ); ``` |
| To | ``` void GLKMatrixStackRotateZ (     GLKMatrixStackRef _Nonnull stack,     float radians ); ``` |

Modified [GLKMatrixStackScale()](https://developer.apple.com/documentation/glkit/1483164-glkmatrixstackscale)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackScale (     GLKMatrixStackRef stack,     float sx,     float sy,     float sz ); ``` |
| To | ``` void GLKMatrixStackScale (     GLKMatrixStackRef _Nonnull stack,     float sx,     float sy,     float sz ); ``` |

Modified [GLKMatrixStackScaleWithVector3()](https://developer.apple.com/documentation/glkit/1483176-glkmatrixstackscalewithvector3)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackScaleWithVector3 (     GLKMatrixStackRef stack,     GLKVector3 scaleVector ); ``` |
| To | ``` void GLKMatrixStackScaleWithVector3 (     GLKMatrixStackRef _Nonnull stack,     GLKVector3 scaleVector ); ``` |

Modified [GLKMatrixStackScaleWithVector4()](https://developer.apple.com/documentation/glkit/1483183-glkmatrixstackscalewithvector4)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackScaleWithVector4 (     GLKMatrixStackRef stack,     GLKVector4 scaleVector ); ``` |
| To | ``` void GLKMatrixStackScaleWithVector4 (     GLKMatrixStackRef _Nonnull stack,     GLKVector4 scaleVector ); ``` |

Modified [GLKMatrixStackSize()](https://developer.apple.com/documentation/glkit/1483156-glkmatrixstacksize)

|  | Declaration |
| --- | --- |
| From | ``` int GLKMatrixStackSize (     GLKMatrixStackRef stack ); ``` |
| To | ``` int GLKMatrixStackSize (     GLKMatrixStackRef _Nonnull stack ); ``` |

Modified [GLKMatrixStackTranslate()](https://developer.apple.com/documentation/glkit/1483177-glkmatrixstacktranslate)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackTranslate (     GLKMatrixStackRef stack,     float tx,     float ty,     float tz ); ``` |
| To | ``` void GLKMatrixStackTranslate (     GLKMatrixStackRef _Nonnull stack,     float tx,     float ty,     float tz ); ``` |

Modified [GLKMatrixStackTranslateWithVector3()](https://developer.apple.com/documentation/glkit/1483186-glkmatrixstacktranslatewithvecto)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackTranslateWithVector3 (     GLKMatrixStackRef stack,     GLKVector3 translationVector ); ``` |
| To | ``` void GLKMatrixStackTranslateWithVector3 (     GLKMatrixStackRef _Nonnull stack,     GLKVector3 translationVector ); ``` |

Modified [GLKMatrixStackTranslateWithVector4()](https://developer.apple.com/documentation/glkit/1483172-glkmatrixstacktranslatewithvecto)

|  | Declaration |
| --- | --- |
| From | ``` void GLKMatrixStackTranslateWithVector4 (     GLKMatrixStackRef stack,     GLKVector4 translationVector ); ``` |
| To | ``` void GLKMatrixStackTranslateWithVector4 (     GLKMatrixStackRef _Nonnull stack,     GLKVector4 translationVector ); ``` |

#### GLKModel.h (Added)

Added [GLKMesh](https://developer.apple.com/documentation/glkit/glkmesh)Added [-[GLKMesh initWithMesh:error:]](https://developer.apple.com/documentation/glkit/glkmesh/1488759-init)Added [GLKMesh.name](https://developer.apple.com/documentation/glkit/glkmesh/1489104-name)Added [+[GLKMesh newMeshesFromAsset:sourceMeshes:error:]](https://developer.apple.com/documentation/glkit/glkmesh/1488791-newmeshesfromasset)Added [GLKMesh.submeshes](https://developer.apple.com/documentation/glkit/glkmesh/1489060-submeshes)Added [GLKMesh.vertexBuffers](https://developer.apple.com/documentation/glkit/glkmesh/1488688-vertexbuffers)Added [GLKMesh.vertexCount](https://developer.apple.com/documentation/glkit/glkmesh/1489043-vertexcount)Added [GLKMesh.vertexDescriptor](https://developer.apple.com/documentation/glkit/glkmesh/1488990-vertexdescriptor)Added [GLKMeshBuffer](https://developer.apple.com/documentation/glkit/glkmeshbuffer)Added [GLKMeshBuffer.allocator](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1489083-allocator)Added [GLKMeshBuffer.glBufferName](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1488636-glbuffername)Added [GLKMeshBuffer.length](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1488631-length)Added [GLKMeshBuffer.offset](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1488607-offset)Added [GLKMeshBuffer.type](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1488681-type)Added [GLKMeshBuffer.zone](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1538271-zone)Added [GLKMeshBufferAllocator](https://developer.apple.com/documentation/glkit/glkmeshbufferallocator)Added [GLKSubmesh](https://developer.apple.com/documentation/glkit/glksubmesh)Added [GLKSubmesh.elementBuffer](https://developer.apple.com/documentation/glkit/glksubmesh/1488972-elementbuffer)Added [GLKSubmesh.elementCount](https://developer.apple.com/documentation/glkit/glksubmesh/1489103-elementcount)Added [GLKSubmesh.mesh](https://developer.apple.com/documentation/glkit/glksubmesh/1489108-mesh)Added [GLKSubmesh.mode](https://developer.apple.com/documentation/glkit/glksubmesh/1488690-mode)Added [GLKSubmesh.name](https://developer.apple.com/documentation/glkit/glksubmesh/1488724-name)Added [GLKSubmesh.type](https://developer.apple.com/documentation/glkit/glksubmesh/1489072-type)Added [GLKVertexAttributeParameters](https://developer.apple.com/documentation/glkit/glkvertexattributeparameters)Added [GLKVertexAttributeParametersFromModelIO()](https://developer.apple.com/documentation/glkit/1488915-glkvertexattributeparametersfrom)Added [kGLKModelErrorDomain](https://developer.apple.com/documentation/glkit/kglkmodelerrordomain)Added [kGLKModelErrorKey](https://developer.apple.com/documentation/glkit/kglkmodelerrorkey)

#### GLKReflectionMapEffect.h

Modified [GLKReflectionMapEffect.textureCubeMap](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect/1415312-texturecubemap)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) GLKEffectPropertyTexture *textureCubeMap ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GLKEffectPropertyTexture *textureCubeMap ``` |

#### GLKSkyboxEffect.h

Modified [GLKSkyboxEffect.label](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1489038-label)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *label ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *label ``` |

Modified [GLKSkyboxEffect.textureCubeMap](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1488873-texturecubemap)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) GLKEffectPropertyTexture *textureCubeMap ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GLKEffectPropertyTexture *textureCubeMap ``` |

Modified [GLKSkyboxEffect.transform](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1489015-transform)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) GLKEffectPropertyTransform *transform ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GLKEffectPropertyTransform *transform ``` |

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

Modified [-[GLKTextureLoader initWithShareContext:]](https://developer.apple.com/documentation/glkit/glktextureloader/1489085-initwithsharecontext)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithShareContext:(NSOpenGLContext *)context ``` |
| To | ``` - (instancetype _Nonnull)initWithShareContext:(NSOpenGLContext * _Nonnull)context ``` |

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
