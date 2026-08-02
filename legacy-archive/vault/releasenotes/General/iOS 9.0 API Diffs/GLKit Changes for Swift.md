---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/GLKit.html
archived_at: '2026-07-18T02:56:50.451754Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# GLKit Changes for Swift

### GLKit

Added [GLKMesh](https://developer.apple.com/documentation/glkit/glkmesh)Added [GLKMesh.init(mesh: MDLMesh) throws](https://developer.apple.com/documentation/glkit/glkmesh/1488759-initwithmesh)Added [GLKMesh.name](https://developer.apple.com/documentation/glkit/glkmesh/1489104-name)Added [GLKMesh.newMeshesFromAsset(_: MDLAsset, sourceMeshes: AutoreleasingUnsafeMutablePointer<NSArray?>) throws -> [GLKMesh] [class]](https://developer.apple.com/documentation/glkit/glkmesh/1488791-newmeshesfromasset)Added [GLKMesh.submeshes](https://developer.apple.com/documentation/glkit/glkmesh/1489060-submeshes)Added [GLKMesh.vertexBuffers](https://developer.apple.com/documentation/glkit/glkmesh/1488688-vertexbuffers)Added [GLKMesh.vertexCount](https://developer.apple.com/documentation/glkit/glkmesh/1489043-vertexcount)Added [GLKMesh.vertexDescriptor](https://developer.apple.com/documentation/glkit/glkmesh/1488990-vertexdescriptor)Added [GLKMeshBuffer](https://developer.apple.com/documentation/glkit/glkmeshbuffer)Added [GLKMeshBuffer.allocator](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1489083-allocator)Added [GLKMeshBuffer.glBufferName](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1488636-glbuffername)Added [GLKMeshBuffer.length](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1488631-length)Added [GLKMeshBuffer.offset](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1488607-offset)Added [GLKMeshBuffer.type](https://developer.apple.com/documentation/glkit/glkmeshbuffer/1488681-type)Added [GLKMeshBufferAllocator](https://developer.apple.com/documentation/glkit/glkmeshbufferallocator)Added [GLKSubmesh](https://developer.apple.com/documentation/glkit/glksubmesh)Added [GLKSubmesh.elementBuffer](https://developer.apple.com/documentation/glkit/glksubmesh/1488972-elementbuffer)Added [GLKSubmesh.elementCount](https://developer.apple.com/documentation/glkit/glksubmesh/1489103-elementcount)Added [GLKSubmesh.mesh](https://developer.apple.com/documentation/glkit/glksubmesh/1489108-mesh)Added [GLKSubmesh.mode](https://developer.apple.com/documentation/glkit/glksubmesh/1488690-mode)Added [GLKSubmesh.name](https://developer.apple.com/documentation/glkit/glksubmesh/1488724-name)Added [GLKSubmesh.type](https://developer.apple.com/documentation/glkit/glksubmesh/1489072-type)Added [GLKVertexAttributeParameters](https://developer.apple.com/documentation/glkit/glkvertexattributeparameters)Added [GLKVertexAttributeParametersFromModelIO(_: MDLVertexFormat) -> GLKVertexAttributeParameters](https://developer.apple.com/documentation/glkit/1488915-glkvertexattributeparametersfrom)Added [kGLKModelErrorDomain](https://developer.apple.com/documentation/glkit/kglkmodelerrordomain)Added [kGLKModelErrorKey](https://developer.apple.com/documentation/glkit/kglkmodelerrorkey)Modified [GLKBaseEffect](https://developer.apple.com/documentation/glkit/glkbaseeffect)

|  | Declaration |
| --- | --- |
| From | ``` class GLKBaseEffect : NSObject, GLKNamedEffect {     func prepareToDraw()     var colorMaterialEnabled: GLboolean     var lightModelTwoSided: GLboolean     var useConstantColor: GLboolean     var transform: GLKEffectPropertyTransform! { get }     var light0: GLKEffectPropertyLight! { get }     var light1: GLKEffectPropertyLight! { get }     var light2: GLKEffectPropertyLight! { get }     var lightingType: GLKLightingType     var lightModelAmbientColor: GLKVector4     var material: GLKEffectPropertyMaterial! { get }     var texture2d0: GLKEffectPropertyTexture! { get }     var texture2d1: GLKEffectPropertyTexture! { get }     var textureOrder: [AnyObject]!     var constantColor: GLKVector4     var fog: GLKEffectPropertyFog! { get }     var label: String! } ``` |
| To | ``` class GLKBaseEffect : NSObject, GLKNamedEffect {     func prepareToDraw()     var colorMaterialEnabled: GLboolean     var lightModelTwoSided: GLboolean     var useConstantColor: GLboolean     var transform: GLKEffectPropertyTransform { get }     var light0: GLKEffectPropertyLight { get }     var light1: GLKEffectPropertyLight { get }     var light2: GLKEffectPropertyLight { get }     var lightingType: GLKLightingType     var lightModelAmbientColor: GLKVector4     var material: GLKEffectPropertyMaterial { get }     var texture2d0: GLKEffectPropertyTexture { get }     var texture2d1: GLKEffectPropertyTexture { get }     var textureOrder: [GLKEffectPropertyTexture]?     var constantColor: GLKVector4     var fog: GLKEffectPropertyFog { get }     var label: String? } ``` |

Modified [GLKBaseEffect.fog](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488697-fog)

|  | Declaration |
| --- | --- |
| From | ``` var fog: GLKEffectPropertyFog! { get } ``` |
| To | ``` var fog: GLKEffectPropertyFog { get } ``` |

Modified [GLKBaseEffect.label](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488835-label)

|  | Declaration |
| --- | --- |
| From | ``` var label: String! ``` |
| To | ``` var label: String? ``` |

Modified [GLKBaseEffect.light0](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488785-light0)

|  | Declaration |
| --- | --- |
| From | ``` var light0: GLKEffectPropertyLight! { get } ``` |
| To | ``` var light0: GLKEffectPropertyLight { get } ``` |

Modified [GLKBaseEffect.light1](https://developer.apple.com/documentation/glkit/glkbaseeffect/1489095-light1)

|  | Declaration |
| --- | --- |
| From | ``` var light1: GLKEffectPropertyLight! { get } ``` |
| To | ``` var light1: GLKEffectPropertyLight { get } ``` |

Modified [GLKBaseEffect.light2](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488671-light2)

|  | Declaration |
| --- | --- |
| From | ``` var light2: GLKEffectPropertyLight! { get } ``` |
| To | ``` var light2: GLKEffectPropertyLight { get } ``` |

Modified [GLKBaseEffect.material](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488753-material)

|  | Declaration |
| --- | --- |
| From | ``` var material: GLKEffectPropertyMaterial! { get } ``` |
| To | ``` var material: GLKEffectPropertyMaterial { get } ``` |

Modified [GLKBaseEffect.texture2d0](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488664-texture2d0)

|  | Declaration |
| --- | --- |
| From | ``` var texture2d0: GLKEffectPropertyTexture! { get } ``` |
| To | ``` var texture2d0: GLKEffectPropertyTexture { get } ``` |

Modified [GLKBaseEffect.texture2d1](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488699-texture2d1)

|  | Declaration |
| --- | --- |
| From | ``` var texture2d1: GLKEffectPropertyTexture! { get } ``` |
| To | ``` var texture2d1: GLKEffectPropertyTexture { get } ``` |

Modified [GLKBaseEffect.textureOrder](https://developer.apple.com/documentation/glkit/glkbaseeffect/1488830-textureorder)

|  | Declaration |
| --- | --- |
| From | ``` var textureOrder: [AnyObject]! ``` |
| To | ``` var textureOrder: [GLKEffectPropertyTexture]? ``` |

Modified [GLKBaseEffect.transform](https://developer.apple.com/documentation/glkit/glkbaseeffect/1489030-transform)

|  | Declaration |
| --- | --- |
| From | ``` var transform: GLKEffectPropertyTransform! { get } ``` |
| To | ``` var transform: GLKEffectPropertyTransform { get } ``` |

Modified [GLKEffectPropertyLight](https://developer.apple.com/documentation/glkit/glkeffectpropertylight)

|  | Declaration |
| --- | --- |
| From | ``` class GLKEffectPropertyLight : GLKEffectProperty {     var enabled: GLboolean     var position: GLKVector4     var ambientColor: GLKVector4     var diffuseColor: GLKVector4     var specularColor: GLKVector4     var spotDirection: GLKVector3     var spotExponent: GLfloat     var spotCutoff: GLfloat     var constantAttenuation: GLfloat     var linearAttenuation: GLfloat     var quadraticAttenuation: GLfloat     var transform: GLKEffectPropertyTransform! } ``` |
| To | ``` class GLKEffectPropertyLight : GLKEffectProperty {     var enabled: GLboolean     var position: GLKVector4     var ambientColor: GLKVector4     var diffuseColor: GLKVector4     var specularColor: GLKVector4     var spotDirection: GLKVector3     var spotExponent: GLfloat     var spotCutoff: GLfloat     var constantAttenuation: GLfloat     var linearAttenuation: GLfloat     var quadraticAttenuation: GLfloat     var transform: GLKEffectPropertyTransform } ``` |

Modified [GLKEffectPropertyLight.transform](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/1473568-transform)

|  | Declaration |
| --- | --- |
| From | ``` var transform: GLKEffectPropertyTransform! ``` |
| To | ``` var transform: GLKEffectPropertyTransform ``` |

Modified GLKMatrix2.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (i: Int) -> Float { get } ``` |
| To | ``` subscript (_ i: Int) -> Float { get } ``` |

Modified GLKMatrix3.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (i: Int) -> Float { get } ``` |
| To | ``` subscript (_ i: Int) -> Float { get } ``` |

Modified GLKMatrix4.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (i: Int) -> Float { get } ``` |
| To | ``` subscript (_ i: Int) -> Float { get } ``` |

Modified GLKQuaternion.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (i: Int) -> Float { get } ``` |
| To | ``` subscript (_ i: Int) -> Float { get } ``` |

Modified [GLKReflectionMapEffect](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect)

|  | Declaration |
| --- | --- |
| From | ``` class GLKReflectionMapEffect : GLKBaseEffect, GLKNamedEffect {     func prepareToDraw()     var textureCubeMap: GLKEffectPropertyTexture! { get }     var matrix: GLKMatrix3 } ``` |
| To | ``` class GLKReflectionMapEffect : GLKBaseEffect {     func prepareToDraw()     var textureCubeMap: GLKEffectPropertyTexture { get }     var matrix: GLKMatrix3 } ``` |

Modified [GLKReflectionMapEffect.textureCubeMap](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect/1415312-texturecubemap)

|  | Declaration |
| --- | --- |
| From | ``` var textureCubeMap: GLKEffectPropertyTexture! { get } ``` |
| To | ``` var textureCubeMap: GLKEffectPropertyTexture { get } ``` |

Modified [GLKSkyboxEffect](https://developer.apple.com/documentation/glkit/glkskyboxeffect)

|  | Declaration |
| --- | --- |
| From | ``` class GLKSkyboxEffect : NSObject, GLKNamedEffect {     func prepareToDraw()     func draw()     var center: GLKVector3     var xSize: GLfloat     var ySize: GLfloat     var zSize: GLfloat     var textureCubeMap: GLKEffectPropertyTexture! { get }     var transform: GLKEffectPropertyTransform! { get }     var label: String! } ``` |
| To | ``` class GLKSkyboxEffect : NSObject, GLKNamedEffect {     func prepareToDraw()     func draw()     var center: GLKVector3     var xSize: GLfloat     var ySize: GLfloat     var zSize: GLfloat     var textureCubeMap: GLKEffectPropertyTexture { get }     var transform: GLKEffectPropertyTransform { get }     var label: String? } ``` |

Modified [GLKSkyboxEffect.label](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1489038-label)

|  | Declaration |
| --- | --- |
| From | ``` var label: String! ``` |
| To | ``` var label: String? ``` |

Modified [GLKSkyboxEffect.textureCubeMap](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1488873-texturecubemap)

|  | Declaration |
| --- | --- |
| From | ``` var textureCubeMap: GLKEffectPropertyTexture! { get } ``` |
| To | ``` var textureCubeMap: GLKEffectPropertyTexture { get } ``` |

Modified [GLKSkyboxEffect.transform](https://developer.apple.com/documentation/glkit/glkskyboxeffect/1489015-transform)

|  | Declaration |
| --- | --- |
| From | ``` var transform: GLKEffectPropertyTransform! { get } ``` |
| To | ``` var transform: GLKEffectPropertyTransform { get } ``` |

Modified [GLKTextureLoader](https://developer.apple.com/documentation/glkit/glktextureloader)

|  | Declaration |
| --- | --- |
| From | ``` class GLKTextureLoader : NSObject {     class func textureWithContentsOfFile(_ path: String!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo!     class func textureWithContentsOfURL(_ url: NSURL!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo!     class func textureWithContentsOfData(_ data: NSData!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo!     class func textureWithCGImage(_ cgImage: CGImage!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo!     class func cubeMapWithContentsOfFiles(_ paths: [AnyObject]!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo!     class func cubeMapWithContentsOfFile(_ path: String!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo!     class func cubeMapWithContentsOfURL(_ url: NSURL!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo!     init!(sharegroup sharegroup: EAGLSharegroup!)     func textureWithContentsOfFile(_ path: String!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!)     func textureWithContentsOfURL(_ url: NSURL!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!)     func textureWithContentsOfData(_ data: NSData!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!)     func textureWithCGImage(_ cgImage: CGImage!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!)     func cubeMapWithContentsOfFiles(_ paths: [AnyObject]!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!)     func cubeMapWithContentsOfFile(_ path: String!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!)     func cubeMapWithContentsOfURL(_ url: NSURL!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!) } ``` |
| To | ``` class GLKTextureLoader : NSObject {     class func textureWithContentsOfFile(_ path: String, options options: [String : NSNumber]?) throws -> GLKTextureInfo     class func textureWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?) throws -> GLKTextureInfo     class func textureWithContentsOfData(_ data: NSData, options options: [String : NSNumber]?) throws -> GLKTextureInfo     class func textureWithCGImage(_ cgImage: CGImage, options options: [String : NSNumber]?) throws -> GLKTextureInfo     class func cubeMapWithContentsOfFiles(_ paths: [AnyObject], options options: [String : NSNumber]?) throws -> GLKTextureInfo     class func cubeMapWithContentsOfFile(_ path: String, options options: [String : NSNumber]?) throws -> GLKTextureInfo     class func cubeMapWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?) throws -> GLKTextureInfo     init(sharegroup sharegroup: EAGLSharegroup)     func textureWithContentsOfFile(_ path: String, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback)     func textureWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback)     func textureWithContentsOfData(_ data: NSData, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback)     func textureWithCGImage(_ cgImage: CGImage, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback)     func cubeMapWithContentsOfFiles(_ paths: [AnyObject], options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback)     func cubeMapWithContentsOfFile(_ path: String, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback)     func cubeMapWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) } ``` |

Modified [GLKTextureLoader.cubeMapWithContentsOfFile(_: String, options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1488848-cubemapwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` class func cubeMapWithContentsOfFile(_ path: String!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo! ``` |
| To | ``` class func cubeMapWithContentsOfFile(_ path: String, options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.cubeMapWithContentsOfFile(_: String, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1488617-cubemap)

|  | Declaration |
| --- | --- |
| From | ``` func cubeMapWithContentsOfFile(_ path: String!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!) ``` |
| To | ``` func cubeMapWithContentsOfFile(_ path: String, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |

Modified [GLKTextureLoader.cubeMapWithContentsOfFiles(_: [AnyObject], options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1488810-cubemap)

|  | Declaration |
| --- | --- |
| From | ``` class func cubeMapWithContentsOfFiles(_ paths: [AnyObject]!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo! ``` |
| To | ``` class func cubeMapWithContentsOfFiles(_ paths: [AnyObject], options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.cubeMapWithContentsOfFiles(_: [AnyObject], options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1488854-cubemap)

|  | Declaration |
| --- | --- |
| From | ``` func cubeMapWithContentsOfFiles(_ paths: [AnyObject]!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!) ``` |
| To | ``` func cubeMapWithContentsOfFiles(_ paths: [AnyObject], options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |

Modified [GLKTextureLoader.cubeMapWithContentsOfURL(_: NSURL, options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1488743-cubemapwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` class func cubeMapWithContentsOfURL(_ url: NSURL!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo! ``` |
| To | ``` class func cubeMapWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.cubeMapWithContentsOfURL(_: NSURL, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1488926-cubemapwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` func cubeMapWithContentsOfURL(_ url: NSURL!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!) ``` |
| To | ``` func cubeMapWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |

Modified [GLKTextureLoader.init(sharegroup: EAGLSharegroup)](https://developer.apple.com/documentation/glkit/glktextureloader/1620707-initwithsharegroup)

|  | Declaration |
| --- | --- |
| From | ``` init!(sharegroup sharegroup: EAGLSharegroup!) ``` |
| To | ``` init(sharegroup sharegroup: EAGLSharegroup) ``` |

Modified [GLKTextureLoader.textureWithCGImage(_: CGImage, options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1488673-texture)

|  | Declaration |
| --- | --- |
| From | ``` class func textureWithCGImage(_ cgImage: CGImage!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo! ``` |
| To | ``` class func textureWithCGImage(_ cgImage: CGImage, options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.textureWithCGImage(_: CGImage, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1488861-texturewithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` func textureWithCGImage(_ cgImage: CGImage!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!) ``` |
| To | ``` func textureWithCGImage(_ cgImage: CGImage, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |

Modified [GLKTextureLoader.textureWithContentsOfData(_: NSData, options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1489081-texturewithcontentsofdata)

|  | Declaration |
| --- | --- |
| From | ``` class func textureWithContentsOfData(_ data: NSData!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo! ``` |
| To | ``` class func textureWithContentsOfData(_ data: NSData, options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.textureWithContentsOfData(_: NSData, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1488905-texturewithcontentsofdata)

|  | Declaration |
| --- | --- |
| From | ``` func textureWithContentsOfData(_ data: NSData!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!) ``` |
| To | ``` func textureWithContentsOfData(_ data: NSData, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |

Modified [GLKTextureLoader.textureWithContentsOfFile(_: String, options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1488932-texture)

|  | Declaration |
| --- | --- |
| From | ``` class func textureWithContentsOfFile(_ path: String!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo! ``` |
| To | ``` class func textureWithContentsOfFile(_ path: String, options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.textureWithContentsOfFile(_: String, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1489064-texture)

|  | Declaration |
| --- | --- |
| From | ``` func textureWithContentsOfFile(_ path: String!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!) ``` |
| To | ``` func textureWithContentsOfFile(_ path: String, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |

Modified [GLKTextureLoader.textureWithContentsOfURL(_: NSURL, options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1489025-texturewithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` class func textureWithContentsOfURL(_ url: NSURL!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> GLKTextureInfo! ``` |
| To | ``` class func textureWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.textureWithContentsOfURL(_: NSURL, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1488621-texturewithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` func textureWithContentsOfURL(_ url: NSURL!, options options: [NSObject : AnyObject]!, queue queue: dispatch_queue_t!, completionHandler block: GLKTextureLoaderCallback!) ``` |
| To | ``` func textureWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |

Modified GLKVector2.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (i: Int) -> Float { get } ``` |
| To | ``` subscript (_ i: Int) -> Float { get } ``` |

Modified GLKVector3.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (i: Int) -> Float { get } ``` |
| To | ``` subscript (_ i: Int) -> Float { get } ``` |

Modified GLKVector4.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (i: Int) -> Float { get } ``` |
| To | ``` subscript (_ i: Int) -> Float { get } ``` |

Modified [GLKView](https://developer.apple.com/documentation/glkit/glkview)

|  | Declaration |
| --- | --- |
| From | ``` class GLKView : UIView, NSCoding {     init!(frame frame: CGRect, context context: EAGLContext!)     @IBOutlet unowned(unsafe) var delegate: GLKViewDelegate!     var context: EAGLContext!     var drawableWidth: Int { get }     var drawableHeight: Int { get }     var drawableColorFormat: GLKViewDrawableColorFormat     var drawableDepthFormat: GLKViewDrawableDepthFormat     var drawableStencilFormat: GLKViewDrawableStencilFormat     var drawableMultisample: GLKViewDrawableMultisample     func bindDrawable()     func deleteDrawable()     var snapshot: UIImage! { get }     var enableSetNeedsDisplay: Bool     func display() } ``` |
| To | ``` class GLKView : UIView {     init(frame frame: CGRect, context context: EAGLContext)     @IBOutlet unowned(unsafe) var delegate: GLKViewDelegate?     var context: EAGLContext     var drawableWidth: Int { get }     var drawableHeight: Int { get }     var drawableColorFormat: GLKViewDrawableColorFormat     var drawableDepthFormat: GLKViewDrawableDepthFormat     var drawableStencilFormat: GLKViewDrawableStencilFormat     var drawableMultisample: GLKViewDrawableMultisample     func bindDrawable()     func deleteDrawable()     var snapshot: UIImage { get }     var enableSetNeedsDisplay: Bool     func display() } ``` |

Modified [GLKView.context](https://developer.apple.com/documentation/glkit/glkview/1615597-context)

|  | Declaration |
| --- | --- |
| From | ``` var context: EAGLContext! ``` |
| To | ``` var context: EAGLContext ``` |

Modified [GLKView.delegate](https://developer.apple.com/documentation/glkit/glkview/1615557-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @IBOutlet unowned(unsafe) var delegate: GLKViewDelegate! ``` |
| To | ``` @IBOutlet unowned(unsafe) var delegate: GLKViewDelegate? ``` |

Modified [GLKView.init(frame: CGRect, context: EAGLContext)](https://developer.apple.com/documentation/glkit/glkview/1615609-initwithframe)

|  | Declaration |
| --- | --- |
| From | ``` init!(frame frame: CGRect, context context: EAGLContext!) ``` |
| To | ``` init(frame frame: CGRect, context context: EAGLContext) ``` |

Modified [GLKView.snapshot](https://developer.apple.com/documentation/glkit/glkview/1615562-snapshot)

|  | Declaration |
| --- | --- |
| From | ``` var snapshot: UIImage! { get } ``` |
| To | ``` var snapshot: UIImage { get } ``` |

Modified [GLKViewController](https://developer.apple.com/documentation/glkit/glkviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class GLKViewController : UIViewController, NSCoding, GLKViewDelegate, NSObjectProtocol {     @IBOutlet unowned(unsafe) var delegate: GLKViewControllerDelegate!     var preferredFramesPerSecond: Int     var framesPerSecond: Int { get }     var paused: Bool     var framesDisplayed: Int { get }     var timeSinceFirstResume: NSTimeInterval { get }     var timeSinceLastResume: NSTimeInterval { get }     var timeSinceLastUpdate: NSTimeInterval { get }     var timeSinceLastDraw: NSTimeInterval { get }     var pauseOnWillResignActive: Bool     var resumeOnDidBecomeActive: Bool } ``` |
| To | ``` class GLKViewController : UIViewController, GLKViewDelegate {     @IBOutlet unowned(unsafe) var delegate: GLKViewControllerDelegate?     var preferredFramesPerSecond: Int     var framesPerSecond: Int { get }     var paused: Bool     var framesDisplayed: Int { get }     var timeSinceFirstResume: NSTimeInterval { get }     var timeSinceLastResume: NSTimeInterval { get }     var timeSinceLastUpdate: NSTimeInterval { get }     var timeSinceLastDraw: NSTimeInterval { get }     var pauseOnWillResignActive: Bool     var resumeOnDidBecomeActive: Bool } ``` |

Modified [GLKViewController.delegate](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620711-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @IBOutlet unowned(unsafe) var delegate: GLKViewControllerDelegate! ``` |
| To | ``` @IBOutlet unowned(unsafe) var delegate: GLKViewControllerDelegate? ``` |

Modified [GLKViewControllerDelegate](https://developer.apple.com/documentation/glkit/glkviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GLKViewControllerDelegate : NSObjectProtocol {     func glkViewControllerUpdate(_ controller: GLKViewController!)     optional func glkViewController(_ controller: GLKViewController!, willPause pause: Bool) } ``` |
| To | ``` protocol GLKViewControllerDelegate : NSObjectProtocol {     func glkViewControllerUpdate(_ controller: GLKViewController)     optional func glkViewController(_ controller: GLKViewController, willPause pause: Bool) } ``` |

Modified [GLKViewControllerDelegate.glkViewController(_: GLKViewController, willPause: Bool)](https://developer.apple.com/documentation/glkit/glkviewcontrollerdelegate/1620776-glkviewcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func glkViewController(_ controller: GLKViewController!, willPause pause: Bool) ``` | iOS 8.0 |
| To | ``` optional func glkViewController(_ controller: GLKViewController, willPause pause: Bool) ``` | iOS 5.0 |

Modified [GLKViewControllerDelegate.glkViewControllerUpdate(_: GLKViewController)](https://developer.apple.com/documentation/glkit/glkviewcontrollerdelegate/1620710-glkviewcontrollerupdate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func glkViewControllerUpdate(_ controller: GLKViewController!) ``` | iOS 8.0 |
| To | ``` func glkViewControllerUpdate(_ controller: GLKViewController) ``` | iOS 5.0 |

Modified [GLKViewDelegate](https://developer.apple.com/documentation/glkit/glkviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GLKViewDelegate : NSObjectProtocol {     func glkView(_ view: GLKView!, drawInRect rect: CGRect) } ``` |
| To | ``` protocol GLKViewDelegate : NSObjectProtocol {     func glkView(_ view: GLKView, drawInRect rect: CGRect) } ``` |

Modified [GLKViewDelegate.glkView(_: GLKView, drawInRect: CGRect)](https://developer.apple.com/documentation/glkit/glkviewdelegate/1615595-glkview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func glkView(_ view: GLKView!, drawInRect rect: CGRect) ``` | iOS 8.0 |
| To | ``` func glkView(_ view: GLKView, drawInRect rect: CGRect) ``` | iOS 5.0 |

Modified [GLKMatrixStackCreate(_: CFAllocator?) -> Unmanaged<GLKMatrixStack>?](https://developer.apple.com/documentation/glkit/1483169-glkmatrixstackcreate)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackCreate(_ alloc: CFAllocator!) -> Unmanaged<GLKMatrixStack>! ``` |
| To | ``` func GLKMatrixStackCreate(_ alloc: CFAllocator?) -> Unmanaged<GLKMatrixStack>? ``` |

Modified [GLKMatrixStackGetMatrix2(_: GLKMatrixStack) -> GLKMatrix2](https://developer.apple.com/documentation/glkit/1483181-glkmatrixstackgetmatrix2)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackGetMatrix2(_ stack: GLKMatrixStack!) -> GLKMatrix2 ``` |
| To | ``` func GLKMatrixStackGetMatrix2(_ stack: GLKMatrixStack) -> GLKMatrix2 ``` |

Modified [GLKMatrixStackGetMatrix3(_: GLKMatrixStack) -> GLKMatrix3](https://developer.apple.com/documentation/glkit/1483158-glkmatrixstackgetmatrix3)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackGetMatrix3(_ stack: GLKMatrixStack!) -> GLKMatrix3 ``` |
| To | ``` func GLKMatrixStackGetMatrix3(_ stack: GLKMatrixStack) -> GLKMatrix3 ``` |

Modified [GLKMatrixStackGetMatrix3Inverse(_: GLKMatrixStack) -> GLKMatrix3](https://developer.apple.com/documentation/glkit/1483159-glkmatrixstackgetmatrix3inverse)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackGetMatrix3Inverse(_ stack: GLKMatrixStack!) -> GLKMatrix3 ``` |
| To | ``` func GLKMatrixStackGetMatrix3Inverse(_ stack: GLKMatrixStack) -> GLKMatrix3 ``` |

Modified [GLKMatrixStackGetMatrix3InverseTranspose(_: GLKMatrixStack) -> GLKMatrix3](https://developer.apple.com/documentation/glkit/1483160-glkmatrixstackgetmatrix3inverset)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackGetMatrix3InverseTranspose(_ stack: GLKMatrixStack!) -> GLKMatrix3 ``` |
| To | ``` func GLKMatrixStackGetMatrix3InverseTranspose(_ stack: GLKMatrixStack) -> GLKMatrix3 ``` |

Modified [GLKMatrixStackGetMatrix4(_: GLKMatrixStack) -> GLKMatrix4](https://developer.apple.com/documentation/glkit/1483163-glkmatrixstackgetmatrix4)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackGetMatrix4(_ stack: GLKMatrixStack!) -> GLKMatrix4 ``` |
| To | ``` func GLKMatrixStackGetMatrix4(_ stack: GLKMatrixStack) -> GLKMatrix4 ``` |

Modified [GLKMatrixStackGetMatrix4Inverse(_: GLKMatrixStack) -> GLKMatrix4](https://developer.apple.com/documentation/glkit/1483168-glkmatrixstackgetmatrix4inverse)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackGetMatrix4Inverse(_ stack: GLKMatrixStack!) -> GLKMatrix4 ``` |
| To | ``` func GLKMatrixStackGetMatrix4Inverse(_ stack: GLKMatrixStack) -> GLKMatrix4 ``` |

Modified [GLKMatrixStackGetMatrix4InverseTranspose(_: GLKMatrixStack) -> GLKMatrix4](https://developer.apple.com/documentation/glkit/1483184-glkmatrixstackgetmatrix4inverset)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackGetMatrix4InverseTranspose(_ stack: GLKMatrixStack!) -> GLKMatrix4 ``` |
| To | ``` func GLKMatrixStackGetMatrix4InverseTranspose(_ stack: GLKMatrixStack) -> GLKMatrix4 ``` |

Modified [GLKMatrixStackLoadMatrix4(_: GLKMatrixStack, _: GLKMatrix4)](https://developer.apple.com/documentation/glkit/1483161-glkmatrixstackloadmatrix4)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackLoadMatrix4(_ stack: GLKMatrixStack!, _ matrix: GLKMatrix4) ``` |
| To | ``` func GLKMatrixStackLoadMatrix4(_ stack: GLKMatrixStack, _ matrix: GLKMatrix4) ``` |

Modified [GLKMatrixStackMultiplyMatrix4(_: GLKMatrixStack, _: GLKMatrix4)](https://developer.apple.com/documentation/glkit/1483162-glkmatrixstackmultiplymatrix4)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackMultiplyMatrix4(_ stack: GLKMatrixStack!, _ matrix: GLKMatrix4) ``` |
| To | ``` func GLKMatrixStackMultiplyMatrix4(_ stack: GLKMatrixStack, _ matrix: GLKMatrix4) ``` |

Modified [GLKMatrixStackMultiplyMatrixStack(_: GLKMatrixStack, _: GLKMatrixStack)](https://developer.apple.com/documentation/glkit/1483197-glkmatrixstackmultiplymatrixstac)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackMultiplyMatrixStack(_ stackLeft: GLKMatrixStack!, _ stackRight: GLKMatrixStack!) ``` |
| To | ``` func GLKMatrixStackMultiplyMatrixStack(_ stackLeft: GLKMatrixStack, _ stackRight: GLKMatrixStack) ``` |

Modified [GLKMatrixStackPop(_: GLKMatrixStack)](https://developer.apple.com/documentation/glkit/1483174-glkmatrixstackpop)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackPop(_ stack: GLKMatrixStack!) ``` |
| To | ``` func GLKMatrixStackPop(_ stack: GLKMatrixStack) ``` |

Modified [GLKMatrixStackPush(_: GLKMatrixStack)](https://developer.apple.com/documentation/glkit/1483190-glkmatrixstackpush)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackPush(_ stack: GLKMatrixStack!) ``` |
| To | ``` func GLKMatrixStackPush(_ stack: GLKMatrixStack) ``` |

Modified [GLKMatrixStackRotate(_: GLKMatrixStack, _: Float, _: Float, _: Float, _: Float)](https://developer.apple.com/documentation/glkit/1483179-glkmatrixstackrotate)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackRotate(_ stack: GLKMatrixStack!, _ radians: Float, _ x: Float, _ y: Float, _ z: Float) ``` |
| To | ``` func GLKMatrixStackRotate(_ stack: GLKMatrixStack, _ radians: Float, _ x: Float, _ y: Float, _ z: Float) ``` |

Modified [GLKMatrixStackRotateWithVector3(_: GLKMatrixStack, _: Float, _: GLKVector3)](https://developer.apple.com/documentation/glkit/1483192-glkmatrixstackrotatewithvector3)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackRotateWithVector3(_ stack: GLKMatrixStack!, _ radians: Float, _ axisVector: GLKVector3) ``` |
| To | ``` func GLKMatrixStackRotateWithVector3(_ stack: GLKMatrixStack, _ radians: Float, _ axisVector: GLKVector3) ``` |

Modified [GLKMatrixStackRotateWithVector4(_: GLKMatrixStack, _: Float, _: GLKVector4)](https://developer.apple.com/documentation/glkit/1483188-glkmatrixstackrotatewithvector4)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackRotateWithVector4(_ stack: GLKMatrixStack!, _ radians: Float, _ axisVector: GLKVector4) ``` |
| To | ``` func GLKMatrixStackRotateWithVector4(_ stack: GLKMatrixStack, _ radians: Float, _ axisVector: GLKVector4) ``` |

Modified [GLKMatrixStackRotateX(_: GLKMatrixStack, _: Float)](https://developer.apple.com/documentation/glkit/1483195-glkmatrixstackrotatex)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackRotateX(_ stack: GLKMatrixStack!, _ radians: Float) ``` |
| To | ``` func GLKMatrixStackRotateX(_ stack: GLKMatrixStack, _ radians: Float) ``` |

Modified [GLKMatrixStackRotateY(_: GLKMatrixStack, _: Float)](https://developer.apple.com/documentation/glkit/1483157-glkmatrixstackrotatey)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackRotateY(_ stack: GLKMatrixStack!, _ radians: Float) ``` |
| To | ``` func GLKMatrixStackRotateY(_ stack: GLKMatrixStack, _ radians: Float) ``` |

Modified [GLKMatrixStackRotateZ(_: GLKMatrixStack, _: Float)](https://developer.apple.com/documentation/glkit/1483171-glkmatrixstackrotatez)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackRotateZ(_ stack: GLKMatrixStack!, _ radians: Float) ``` |
| To | ``` func GLKMatrixStackRotateZ(_ stack: GLKMatrixStack, _ radians: Float) ``` |

Modified [GLKMatrixStackScale(_: GLKMatrixStack, _: Float, _: Float, _: Float)](https://developer.apple.com/documentation/glkit/1483164-glkmatrixstackscale)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackScale(_ stack: GLKMatrixStack!, _ sx: Float, _ sy: Float, _ sz: Float) ``` |
| To | ``` func GLKMatrixStackScale(_ stack: GLKMatrixStack, _ sx: Float, _ sy: Float, _ sz: Float) ``` |

Modified [GLKMatrixStackScaleWithVector3(_: GLKMatrixStack, _: GLKVector3)](https://developer.apple.com/documentation/glkit/1483176-glkmatrixstackscalewithvector3)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackScaleWithVector3(_ stack: GLKMatrixStack!, _ scaleVector: GLKVector3) ``` |
| To | ``` func GLKMatrixStackScaleWithVector3(_ stack: GLKMatrixStack, _ scaleVector: GLKVector3) ``` |

Modified [GLKMatrixStackScaleWithVector4(_: GLKMatrixStack, _: GLKVector4)](https://developer.apple.com/documentation/glkit/1483183-glkmatrixstackscalewithvector4)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackScaleWithVector4(_ stack: GLKMatrixStack!, _ scaleVector: GLKVector4) ``` |
| To | ``` func GLKMatrixStackScaleWithVector4(_ stack: GLKMatrixStack, _ scaleVector: GLKVector4) ``` |

Modified [GLKMatrixStackSize(_: GLKMatrixStack) -> Int32](https://developer.apple.com/documentation/glkit/1483156-glkmatrixstacksize)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackSize(_ stack: GLKMatrixStack!) -> Int32 ``` |
| To | ``` func GLKMatrixStackSize(_ stack: GLKMatrixStack) -> Int32 ``` |

Modified [GLKMatrixStackTranslate(_: GLKMatrixStack, _: Float, _: Float, _: Float)](https://developer.apple.com/documentation/glkit/1483177-glkmatrixstacktranslate)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackTranslate(_ stack: GLKMatrixStack!, _ tx: Float, _ ty: Float, _ tz: Float) ``` |
| To | ``` func GLKMatrixStackTranslate(_ stack: GLKMatrixStack, _ tx: Float, _ ty: Float, _ tz: Float) ``` |

Modified [GLKMatrixStackTranslateWithVector3(_: GLKMatrixStack, _: GLKVector3)](https://developer.apple.com/documentation/glkit/1483186-glkmatrixstacktranslatewithvecto)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackTranslateWithVector3(_ stack: GLKMatrixStack!, _ translationVector: GLKVector3) ``` |
| To | ``` func GLKMatrixStackTranslateWithVector3(_ stack: GLKMatrixStack, _ translationVector: GLKVector3) ``` |

Modified [GLKMatrixStackTranslateWithVector4(_: GLKMatrixStack, _: GLKVector4)](https://developer.apple.com/documentation/glkit/1483172-glkmatrixstacktranslatewithvecto)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrixStackTranslateWithVector4(_ stack: GLKMatrixStack!, _ translationVector: GLKVector4) ``` |
| To | ``` func GLKMatrixStackTranslateWithVector4(_ stack: GLKMatrixStack, _ translationVector: GLKVector4) ``` |

Modified [GLKTextureLoaderCallback](https://developer.apple.com/documentation/glkit/glktextureloadercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias GLKTextureLoaderCallback = (GLKTextureInfo!, NSError!) -> Void ``` |
| To | ``` typealias GLKTextureLoaderCallback = (GLKTextureInfo?, NSError?) -> Void ``` |

Modified [NSStringFromGLKMatrix2(_: GLKMatrix2) -> String](https://developer.apple.com/documentation/glkit/1489099-nsstringfromglkmatrix2)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromGLKMatrix2(_ matrix: GLKMatrix2) -> String! ``` |
| To | ``` func NSStringFromGLKMatrix2(_ matrix: GLKMatrix2) -> String ``` |

Modified [NSStringFromGLKMatrix3(_: GLKMatrix3) -> String](https://developer.apple.com/documentation/glkit/1489048-nsstringfromglkmatrix3)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromGLKMatrix3(_ matrix: GLKMatrix3) -> String! ``` |
| To | ``` func NSStringFromGLKMatrix3(_ matrix: GLKMatrix3) -> String ``` |

Modified [NSStringFromGLKMatrix4(_: GLKMatrix4) -> String](https://developer.apple.com/documentation/glkit/1488877-nsstringfromglkmatrix4)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromGLKMatrix4(_ matrix: GLKMatrix4) -> String! ``` |
| To | ``` func NSStringFromGLKMatrix4(_ matrix: GLKMatrix4) -> String ``` |

Modified [NSStringFromGLKQuaternion(_: GLKQuaternion) -> String](https://developer.apple.com/documentation/glkit/1488908-nsstringfromglkquaternion)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromGLKQuaternion(_ quaternion: GLKQuaternion) -> String! ``` |
| To | ``` func NSStringFromGLKQuaternion(_ quaternion: GLKQuaternion) -> String ``` |

Modified [NSStringFromGLKVector2(_: GLKVector2) -> String](https://developer.apple.com/documentation/glkit/1488857-nsstringfromglkvector2)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromGLKVector2(_ vector: GLKVector2) -> String! ``` |
| To | ``` func NSStringFromGLKVector2(_ vector: GLKVector2) -> String ``` |

Modified [NSStringFromGLKVector3(_: GLKVector3) -> String](https://developer.apple.com/documentation/glkit/1489089-nsstringfromglkvector3)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromGLKVector3(_ vector: GLKVector3) -> String! ``` |
| To | ``` func NSStringFromGLKVector3(_ vector: GLKVector3) -> String ``` |

Modified [NSStringFromGLKVector4(_: GLKVector4) -> String](https://developer.apple.com/documentation/glkit/1489056-nsstringfromglkvector4)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromGLKVector4(_ vector: GLKVector4) -> String! ``` |
| To | ``` func NSStringFromGLKVector4(_ vector: GLKVector4) -> String ``` |

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
