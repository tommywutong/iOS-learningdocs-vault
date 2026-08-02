---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/GLKit.html
archived_at: '2026-07-18T02:57:08.583726Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# GLKit Changes for Swift

### GLKit

Modified [GLKBaseEffect](https://developer.apple.com/documentation/glkit/glkbaseeffect)

|  | Protocols |
| --- | --- |
| From | AnyObject, GLKNamedEffect |
| To | GLKNamedEffect |

Modified [GLKEffectProperty](https://developer.apple.com/documentation/glkit/glkeffectproperty)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GLKEffectPropertyFog](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GLKEffectPropertyLight](https://developer.apple.com/documentation/glkit/glkeffectpropertylight)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GLKEffectPropertyMaterial](https://developer.apple.com/documentation/glkit/glkeffectpropertymaterial)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GLKEffectPropertyTexture](https://developer.apple.com/documentation/glkit/glkeffectpropertytexture)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GLKEffectPropertyTransform](https://developer.apple.com/documentation/glkit/glkeffectpropertytransform)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GLKFogMode [enum]](https://developer.apple.com/documentation/glkit/glkfogmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GLKLightingType [enum]](https://developer.apple.com/documentation/glkit/glklightingtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GLKMesh](https://developer.apple.com/documentation/glkit/glkmesh)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GLKMeshBuffer](https://developer.apple.com/documentation/glkit/glkmeshbuffer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKMeshBuffer : NSObject, MDLMeshBuffer, NSCopying {     var length: Int { get }     var allocator: GLKMeshBufferAllocator { get }     var glBufferName: GLuint { get }     var offset: Int { get }     var type: MDLMeshBufferType { get }     func zone() -> MDLMeshBufferZone? } ``` | AnyObject, MDLMeshBuffer, NSCopying, NSObjectProtocol |
| To | ``` class GLKMeshBuffer : NSObject, MDLMeshBuffer {     var length: Int { get }     var allocator: GLKMeshBufferAllocator { get }     var glBufferName: GLuint { get }     var offset: Int { get }     var type: MDLMeshBufferType { get }     func zone() -> MDLMeshBufferZone? } ``` | MDLMeshBuffer |

Modified [GLKMeshBufferAllocator](https://developer.apple.com/documentation/glkit/glkmeshbufferallocator)

|  | Protocols |
| --- | --- |
| From | AnyObject, MDLMeshBufferAllocator, NSObjectProtocol |
| To | MDLMeshBufferAllocator |

Modified [GLKReflectionMapEffect](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKReflectionMapEffect : GLKBaseEffect {     func prepareToDraw()     var textureCubeMap: GLKEffectPropertyTexture { get }     var matrix: GLKMatrix3 } ``` | AnyObject, GLKNamedEffect |
| To | ``` class GLKReflectionMapEffect : GLKBaseEffect, GLKNamedEffect {     func prepareToDraw()     var textureCubeMap: GLKEffectPropertyTexture { get }     var matrix: GLKMatrix3 } ``` | GLKNamedEffect |

Modified [GLKSkyboxEffect](https://developer.apple.com/documentation/glkit/glkskyboxeffect)

|  | Protocols |
| --- | --- |
| From | AnyObject, GLKNamedEffect |
| To | GLKNamedEffect |

Modified [GLKSubmesh](https://developer.apple.com/documentation/glkit/glksubmesh)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GLKTextureEnvMode [enum]](https://developer.apple.com/documentation/glkit/glktextureenvmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GLKTextureInfo](https://developer.apple.com/documentation/glkit/glktextureinfo)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [GLKTextureInfoAlphaState [enum]](https://developer.apple.com/documentation/glkit/glktextureinfoalphastate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GLKTextureInfoOrigin [enum]](https://developer.apple.com/documentation/glkit/glktextureinfoorigin)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GLKTextureLoader](https://developer.apple.com/documentation/glkit/glktextureloader)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GLKTextureLoaderError [enum]](https://developer.apple.com/documentation/glkit/glktextureloadererror/code)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GLKTextureTarget [enum]](https://developer.apple.com/documentation/glkit/glktexturetarget)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GLKVertexAttrib [enum]](https://developer.apple.com/documentation/glkit/glkvertexattrib)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GLKView](https://developer.apple.com/documentation/glkit/glkview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKView : UIView {     init(frame frame: CGRect, context context: EAGLContext)     @IBOutlet unowned(unsafe) var delegate: GLKViewDelegate?     var context: EAGLContext     var drawableWidth: Int { get }     var drawableHeight: Int { get }     var drawableColorFormat: GLKViewDrawableColorFormat     var drawableDepthFormat: GLKViewDrawableDepthFormat     var drawableStencilFormat: GLKViewDrawableStencilFormat     var drawableMultisample: GLKViewDrawableMultisample     func bindDrawable()     func deleteDrawable()     var snapshot: UIImage { get }     var enableSetNeedsDisplay: Bool     func display() } ``` | AnyObject, NSCoding |
| To | ``` class GLKView : UIView, NSCoding {     init(frame frame: CGRect, context context: EAGLContext)     @IBOutlet unowned(unsafe) var delegate: GLKViewDelegate?     var context: EAGLContext     var drawableWidth: Int { get }     var drawableHeight: Int { get }     var drawableColorFormat: GLKViewDrawableColorFormat     var drawableDepthFormat: GLKViewDrawableDepthFormat     var drawableStencilFormat: GLKViewDrawableStencilFormat     var drawableMultisample: GLKViewDrawableMultisample     func bindDrawable()     func deleteDrawable()     var snapshot: UIImage { get }     var enableSetNeedsDisplay: Bool     func display() } ``` | NSCoding |

Modified [GLKViewController](https://developer.apple.com/documentation/glkit/glkviewcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKViewController : UIViewController, GLKViewDelegate {     @IBOutlet unowned(unsafe) var delegate: GLKViewControllerDelegate?     var preferredFramesPerSecond: Int     var framesPerSecond: Int { get }     var paused: Bool     var framesDisplayed: Int { get }     var timeSinceFirstResume: NSTimeInterval { get }     var timeSinceLastResume: NSTimeInterval { get }     var timeSinceLastUpdate: NSTimeInterval { get }     var timeSinceLastDraw: NSTimeInterval { get }     var pauseOnWillResignActive: Bool     var resumeOnDidBecomeActive: Bool } ``` | AnyObject, GLKViewDelegate, NSCoding, NSObjectProtocol |
| To | ``` class GLKViewController : UIViewController, NSCoding, GLKViewDelegate {     @IBOutlet unowned(unsafe) var delegate: GLKViewControllerDelegate?     var preferredFramesPerSecond: Int     var framesPerSecond: Int { get }     var paused: Bool     var framesDisplayed: Int { get }     var timeSinceFirstResume: NSTimeInterval { get }     var timeSinceLastResume: NSTimeInterval { get }     var timeSinceLastUpdate: NSTimeInterval { get }     var timeSinceLastDraw: NSTimeInterval { get }     var pauseOnWillResignActive: Bool     var resumeOnDidBecomeActive: Bool } ``` | GLKViewDelegate, NSCoding |

Modified [GLKViewDrawableColorFormat [enum]](https://developer.apple.com/documentation/glkit/glkviewdrawablecolorformat)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GLKViewDrawableDepthFormat [enum]](https://developer.apple.com/documentation/glkit/glkviewdrawabledepthformat)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GLKViewDrawableMultisample [enum]](https://developer.apple.com/documentation/glkit/glkviewdrawablemultisample)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GLKViewDrawableStencilFormat [enum]](https://developer.apple.com/documentation/glkit/glkviewdrawablestencilformat)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
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
