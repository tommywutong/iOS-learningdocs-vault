---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/ModelIO.html
archived_at: '2026-07-18T02:57:09.686878Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# ModelIO Changes for Swift

### ModelIO

Modified [MDLAreaLight](https://developer.apple.com/documentation/modelio/mdlarealight)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLAsset](https://developer.apple.com/documentation/modelio/mdlasset)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSFastEnumeration |
| To | NSCopying, NSFastEnumeration |

Modified [MDLCamera](https://developer.apple.com/documentation/modelio/mdlcamera)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLCheckerboardTexture](https://developer.apple.com/documentation/modelio/mdlcheckerboardtexture)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLColorSwatchTexture](https://developer.apple.com/documentation/modelio/mdlcolorswatchtexture)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLGeometryType [enum]](https://developer.apple.com/documentation/modelio/mdlgeometrytype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MDLIndexBitDepth [enum]](https://developer.apple.com/documentation/modelio/mdlindexbitdepth)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MDLLight](https://developer.apple.com/documentation/modelio/mdllight)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLLightProbe](https://developer.apple.com/documentation/modelio/mdllightprobe)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLLightType [enum]](https://developer.apple.com/documentation/modelio/mdllighttype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MDLMaterial](https://developer.apple.com/documentation/modelio/mdlmaterial)

|  | Protocols |
| --- | --- |
| From | AnyObject, MDLNamed, NSFastEnumeration |
| To | MDLNamed, NSFastEnumeration |

Modified [MDLMaterialMipMapFilterMode [enum]](https://developer.apple.com/documentation/modelio/mdlmaterialmipmapfiltermode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MDLMaterialProperty](https://developer.apple.com/documentation/modelio/mdlmaterialproperty)

|  | Protocols |
| --- | --- |
| From | AnyObject, MDLNamed |
| To | MDLNamed |

Modified [MDLMaterialPropertyType [enum]](https://developer.apple.com/documentation/modelio/mdlmaterialpropertytype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MDLMaterialSemantic [enum]](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MDLMaterialTextureFilterMode [enum]](https://developer.apple.com/documentation/modelio/mdlmaterialtexturefiltermode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MDLMaterialTextureWrapMode [enum]](https://developer.apple.com/documentation/modelio/mdlmaterialtexturewrapmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MDLMesh](https://developer.apple.com/documentation/modelio/mdlmesh)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLMeshBufferData](https://developer.apple.com/documentation/modelio/mdlmeshbufferdata)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLMeshBufferData : NSObject, MDLMeshBuffer, NSCopying {     init(type type: MDLMeshBufferType, length length: Int)     init(type type: MDLMeshBufferType, data data: NSData?)     var data: NSData { get } } ``` | AnyObject, MDLMeshBuffer, NSCopying, NSObjectProtocol |
| To | ``` class MDLMeshBufferData : NSObject, MDLMeshBuffer {     init(type type: MDLMeshBufferType, length length: Int)     init(type type: MDLMeshBufferType, data data: NSData?)     var data: NSData { get } } ``` | MDLMeshBuffer |

Modified [MDLMeshBufferDataAllocator](https://developer.apple.com/documentation/modelio/mdlmeshbufferdataallocator)

|  | Protocols |
| --- | --- |
| From | AnyObject, MDLMeshBufferAllocator, NSObjectProtocol |
| To | MDLMeshBufferAllocator |

Modified [MDLMeshBufferMap](https://developer.apple.com/documentation/modelio/mdlmeshbuffermap)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLMeshBufferType [enum]](https://developer.apple.com/documentation/modelio/mdlmeshbuffertype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MDLMeshBufferZoneDefault](https://developer.apple.com/documentation/modelio/mdlmeshbufferzonedefault)

|  | Protocols |
| --- | --- |
| From | AnyObject, MDLMeshBufferZone, NSObjectProtocol |
| To | MDLMeshBufferZone |

Modified [MDLNoiseTexture](https://developer.apple.com/documentation/modelio/mdlnoisetexture)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLNormalMapTexture](https://developer.apple.com/documentation/modelio/mdlnormalmaptexture)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLObject](https://developer.apple.com/documentation/modelio/mdlobject)

|  | Protocols |
| --- | --- |
| From | AnyObject, MDLNamed |
| To | MDLNamed |

Modified [MDLObjectContainer](https://developer.apple.com/documentation/modelio/mdlobjectcontainer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLObjectContainer : NSObject, MDLObjectContainerComponent, MDLComponent, NSFastEnumeration { } ``` | AnyObject, MDLComponent, MDLObjectContainerComponent, NSFastEnumeration, NSObjectProtocol |
| To | ``` class MDLObjectContainer : NSObject, MDLObjectContainerComponent { } ``` | MDLObjectContainerComponent |

Modified [MDLObjectContainerComponent](https://developer.apple.com/documentation/modelio/mdlobjectcontainercomponent)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol MDLObjectContainerComponent : MDLComponent, NSObjectProtocol, NSFastEnumeration {     func addObject(_ object: MDLObject)     func removeObject(_ object: MDLObject)     var objects: [MDLObject] { get } } ``` | MDLComponent, NSFastEnumeration, NSObjectProtocol |
| To | ``` protocol MDLObjectContainerComponent : MDLComponent, NSFastEnumeration {     func addObject(_ object: MDLObject)     func removeObject(_ object: MDLObject)     var objects: [MDLObject] { get } } ``` | MDLComponent, NSFastEnumeration |

Modified [MDLPhotometricLight](https://developer.apple.com/documentation/modelio/mdlphotometriclight)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLPhysicallyPlausibleLight](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblelight)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLPhysicallyPlausibleScatteringFunction](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblescatteringfunction)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLScatteringFunction](https://developer.apple.com/documentation/modelio/mdlscatteringfunction)

|  | Protocols |
| --- | --- |
| From | AnyObject, MDLNamed |
| To | MDLNamed |

Modified [MDLSkyCubeTexture](https://developer.apple.com/documentation/modelio/mdlskycubetexture)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLStereoscopicCamera](https://developer.apple.com/documentation/modelio/mdlstereoscopiccamera)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLSubmesh](https://developer.apple.com/documentation/modelio/mdlsubmesh)

|  | Protocols |
| --- | --- |
| From | AnyObject, MDLNamed |
| To | MDLNamed |

Modified [MDLSubmeshTopology](https://developer.apple.com/documentation/modelio/mdlsubmeshtopology)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLTexture](https://developer.apple.com/documentation/modelio/mdltexture)

|  | Protocols |
| --- | --- |
| From | AnyObject, MDLNamed |
| To | MDLNamed |

Modified [MDLTextureChannelEncoding [enum]](https://developer.apple.com/documentation/modelio/mdltexturechannelencoding)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MDLTextureFilter](https://developer.apple.com/documentation/modelio/mdltexturefilter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLTextureSampler](https://developer.apple.com/documentation/modelio/mdltexturesampler)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLTransform](https://developer.apple.com/documentation/modelio/mdltransform)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLTransform : NSObject, MDLTransformComponent, MDLComponent {     init(identity identity: ())     convenience init(transformComponent component: MDLTransformComponent)     convenience init(matrix matrix: matrix_float4x4)     func setIdentity()     func translationAtTime(_ time: NSTimeInterval) -> vector_float3     func rotationAtTime(_ time: NSTimeInterval) -> vector_float3     func shearAtTime(_ time: NSTimeInterval) -> vector_float3     func scaleAtTime(_ time: NSTimeInterval) -> vector_float3     func setTranslation(_ translation: vector_float3, forTime time: NSTimeInterval)     func setRotation(_ rotation: vector_float3, forTime time: NSTimeInterval)     func setShear(_ shear: vector_float3, forTime time: NSTimeInterval)     func setScale(_ scale: vector_float3, forTime time: NSTimeInterval)     func rotationMatrixAtTime(_ time: NSTimeInterval) -> matrix_float4x4     var translation: vector_float3     var rotation: vector_float3     var shear: vector_float3     var scale: vector_float3 } ``` | AnyObject, MDLComponent, MDLTransformComponent, NSObjectProtocol |
| To | ``` class MDLTransform : NSObject, MDLTransformComponent {     init(identity identity: ())     convenience init(transformComponent component: MDLTransformComponent)     convenience init(matrix matrix: matrix_float4x4)     func setIdentity()     func translationAtTime(_ time: NSTimeInterval) -> vector_float3     func rotationAtTime(_ time: NSTimeInterval) -> vector_float3     func shearAtTime(_ time: NSTimeInterval) -> vector_float3     func scaleAtTime(_ time: NSTimeInterval) -> vector_float3     func setTranslation(_ translation: vector_float3, forTime time: NSTimeInterval)     func setRotation(_ rotation: vector_float3, forTime time: NSTimeInterval)     func setShear(_ shear: vector_float3, forTime time: NSTimeInterval)     func setScale(_ scale: vector_float3, forTime time: NSTimeInterval)     func rotationMatrixAtTime(_ time: NSTimeInterval) -> matrix_float4x4     var translation: vector_float3     var rotation: vector_float3     var shear: vector_float3     var scale: vector_float3 } ``` | MDLTransformComponent |

Modified [MDLTransformComponent](https://developer.apple.com/documentation/modelio/mdltransformcomponent)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol MDLTransformComponent : MDLComponent, NSObjectProtocol {     var matrix: matrix_float4x4 { get set }     var minimumTime: NSTimeInterval { get }     var maximumTime: NSTimeInterval { get }     optional func setLocalTransform(_ transform: matrix_float4x4, forTime time: NSTimeInterval)     optional func setLocalTransform(_ transform: matrix_float4x4)     optional func localTransformAtTime(_ time: NSTimeInterval) -> matrix_float4x4     optional static func globalTransformWithObject(_ object: MDLObject, atTime time: NSTimeInterval) -> matrix_float4x4 } ``` | MDLComponent, NSObjectProtocol |
| To | ``` protocol MDLTransformComponent : MDLComponent {     var matrix: matrix_float4x4 { get set }     var minimumTime: NSTimeInterval { get }     var maximumTime: NSTimeInterval { get }     optional func setLocalTransform(_ transform: matrix_float4x4, forTime time: NSTimeInterval)     optional func setLocalTransform(_ transform: matrix_float4x4)     optional func localTransformAtTime(_ time: NSTimeInterval) -> matrix_float4x4     optional static func globalTransformWithObject(_ object: MDLObject, atTime time: NSTimeInterval) -> matrix_float4x4 } ``` | MDLComponent |

Modified [MDLURLTexture](https://developer.apple.com/documentation/modelio/mdlurltexture)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLVertexAttribute](https://developer.apple.com/documentation/modelio/mdlvertexattribute)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MDLVertexAttributeData](https://developer.apple.com/documentation/modelio/mdlvertexattributedata)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MDLVertexBufferLayout](https://developer.apple.com/documentation/modelio/mdlvertexbufferlayout)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MDLVertexDescriptor](https://developer.apple.com/documentation/modelio/mdlvertexdescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MDLVertexFormat [enum]](https://developer.apple.com/documentation/modelio/mdlvertexformat)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MDLVoxelArray](https://developer.apple.com/documentation/modelio/mdlvoxelarray)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

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
