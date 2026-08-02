---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/GLKit.html
archived_at: '2026-07-18T02:52:29.701447Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# GLKit Changes

## GLKit

Added GLKBaseEffect.constantColorAdded GLKBaseEffect.lightModelAmbientColorAdded GLKEffectPropertyFog.colorAdded GLKEffectPropertyLight.ambientColorAdded GLKEffectPropertyLight.diffuseColorAdded GLKEffectPropertyLight.positionAdded GLKEffectPropertyLight.specularColorAdded GLKEffectPropertyLight.spotDirectionAdded GLKEffectPropertyMaterial.ambientColorAdded GLKEffectPropertyMaterial.diffuseColorAdded GLKEffectPropertyMaterial.emissiveColorAdded GLKEffectPropertyMaterial.specularColorAdded GLKEffectPropertyTransform.modelviewMatrixAdded GLKEffectPropertyTransform.normalMatrixAdded GLKEffectPropertyTransform.projectionMatrixAdded GLKMatrix2.m00Added GLKMatrix2.m01Added GLKMatrix2.m10Added GLKMatrix2.m11Added GLKMatrix3.m00Added GLKMatrix3.m01Added GLKMatrix3.m02Added GLKMatrix3.m10Added GLKMatrix3.m11Added GLKMatrix3.m12Added GLKMatrix3.m20Added GLKMatrix3.m21Added GLKMatrix3.m22Added GLKMatrix4.m00Added GLKMatrix4.m01Added GLKMatrix4.m02Added GLKMatrix4.m03Added GLKMatrix4.m10Added GLKMatrix4.m11Added GLKMatrix4.m12Added GLKMatrix4.m13Added GLKMatrix4.m20Added GLKMatrix4.m21Added GLKMatrix4.m22Added GLKMatrix4.m23Added GLKMatrix4.m30Added GLKMatrix4.m31Added GLKMatrix4.m32Added GLKMatrix4.m33Added GLKQuaternion.sAdded GLKQuaternion.vAdded GLKQuaternion.wAdded GLKQuaternion.xAdded GLKQuaternion.yAdded GLKQuaternion.zAdded GLKReflectionMapEffect.matrixAdded GLKSkyboxEffect.centerAdded GLKVector2.sAdded GLKVector2.tAdded GLKVector2.xAdded GLKVector2.yAdded GLKVector3.bAdded GLKVector3.gAdded GLKVector3.pAdded GLKVector3.rAdded GLKVector3.sAdded GLKVector3.tAdded GLKVector3.xAdded GLKVector3.yAdded GLKVector3.zAdded GLKVector4.aAdded GLKVector4.bAdded GLKVector4.gAdded GLKVector4.pAdded GLKVector4.qAdded GLKVector4.rAdded GLKVector4.sAdded GLKVector4.tAdded GLKVector4.wAdded GLKVector4.xAdded GLKVector4.yAdded GLKVector4.zAdded GLKMathProject(GLKVector3, GLKMatrix4, GLKMatrix4, UnsafeMutablePointer<Int32>) -> GLKVector3Added GLKMathUnproject(GLKVector3, GLKMatrix4, GLKMatrix4, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Bool>) -> GLKVector3Added GLKMatrix2Added GLKMatrix3Added GLKMatrix3Add(GLKMatrix3, GLKMatrix3) -> GLKMatrix3Added GLKMatrix3GetColumn(GLKMatrix3, Int32) -> GLKVector3Added GLKMatrix3GetMatrix2(GLKMatrix3) -> GLKMatrix2Added GLKMatrix3GetRow(GLKMatrix3, Int32) -> GLKVector3Added GLKMatrix3IdentityAdded GLKMatrix3Invert(GLKMatrix3, UnsafeMutablePointer<Bool>) -> GLKMatrix3Added GLKMatrix3InvertAndTranspose(GLKMatrix3, UnsafeMutablePointer<Bool>) -> GLKMatrix3Added GLKMatrix3Make(Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix3Added GLKMatrix3MakeAndTranspose(Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix3Added GLKMatrix3MakeRotation(Float, Float, Float, Float) -> GLKMatrix3Added GLKMatrix3MakeScale(Float, Float, Float) -> GLKMatrix3Added GLKMatrix3MakeWithArray(UnsafeMutablePointer<Float>) -> GLKMatrix3Added GLKMatrix3MakeWithArrayAndTranspose(UnsafeMutablePointer<Float>) -> GLKMatrix3Added GLKMatrix3MakeWithColumns(GLKVector3, GLKVector3, GLKVector3) -> GLKMatrix3Added GLKMatrix3MakeWithQuaternion(GLKQuaternion) -> GLKMatrix3Added GLKMatrix3MakeWithRows(GLKVector3, GLKVector3, GLKVector3) -> GLKMatrix3Added GLKMatrix3MakeXRotation(Float) -> GLKMatrix3Added GLKMatrix3MakeYRotation(Float) -> GLKMatrix3Added GLKMatrix3MakeZRotation(Float) -> GLKMatrix3Added GLKMatrix3Multiply(GLKMatrix3, GLKMatrix3) -> GLKMatrix3Added GLKMatrix3MultiplyVector3(GLKMatrix3, GLKVector3) -> GLKVector3Added GLKMatrix3MultiplyVector3Array(GLKMatrix3, UnsafeMutablePointer<GLKVector3>, Int)Added GLKMatrix3Rotate(GLKMatrix3, Float, Float, Float, Float) -> GLKMatrix3Added GLKMatrix3RotateWithVector3(GLKMatrix3, Float, GLKVector3) -> GLKMatrix3Added GLKMatrix3RotateWithVector4(GLKMatrix3, Float, GLKVector4) -> GLKMatrix3Added GLKMatrix3RotateX(GLKMatrix3, Float) -> GLKMatrix3Added GLKMatrix3RotateY(GLKMatrix3, Float) -> GLKMatrix3Added GLKMatrix3RotateZ(GLKMatrix3, Float) -> GLKMatrix3Added GLKMatrix3Scale(GLKMatrix3, Float, Float, Float) -> GLKMatrix3Added GLKMatrix3ScaleWithVector3(GLKMatrix3, GLKVector3) -> GLKMatrix3Added GLKMatrix3ScaleWithVector4(GLKMatrix3, GLKVector4) -> GLKMatrix3Added GLKMatrix3SetColumn(GLKMatrix3, Int32, GLKVector3) -> GLKMatrix3Added GLKMatrix3SetRow(GLKMatrix3, Int32, GLKVector3) -> GLKMatrix3Added GLKMatrix3Subtract(GLKMatrix3, GLKMatrix3) -> GLKMatrix3Added GLKMatrix3Transpose(GLKMatrix3) -> GLKMatrix3Added GLKMatrix4Added GLKMatrix4Add(GLKMatrix4, GLKMatrix4) -> GLKMatrix4Added GLKMatrix4GetColumn(GLKMatrix4, Int32) -> GLKVector4Added GLKMatrix4GetMatrix2(GLKMatrix4) -> GLKMatrix2Added GLKMatrix4GetMatrix3(GLKMatrix4) -> GLKMatrix3Added GLKMatrix4GetRow(GLKMatrix4, Int32) -> GLKVector4Added GLKMatrix4IdentityAdded GLKMatrix4Invert(GLKMatrix4, UnsafeMutablePointer<Bool>) -> GLKMatrix4Added GLKMatrix4InvertAndTranspose(GLKMatrix4, UnsafeMutablePointer<Bool>) -> GLKMatrix4Added GLKMatrix4Make(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4Added GLKMatrix4MakeAndTranspose(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4Added GLKMatrix4MakeFrustum(Float, Float, Float, Float, Float, Float) -> GLKMatrix4Added GLKMatrix4MakeLookAt(Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4Added GLKMatrix4MakeOrtho(Float, Float, Float, Float, Float, Float) -> GLKMatrix4Added GLKMatrix4MakePerspective(Float, Float, Float, Float) -> GLKMatrix4Added GLKMatrix4MakeRotation(Float, Float, Float, Float) -> GLKMatrix4Added GLKMatrix4MakeScale(Float, Float, Float) -> GLKMatrix4Added GLKMatrix4MakeTranslation(Float, Float, Float) -> GLKMatrix4Added GLKMatrix4MakeWithArray(UnsafeMutablePointer<Float>) -> GLKMatrix4Added GLKMatrix4MakeWithArrayAndTranspose(UnsafeMutablePointer<Float>) -> GLKMatrix4Added GLKMatrix4MakeWithColumns(GLKVector4, GLKVector4, GLKVector4, GLKVector4) -> GLKMatrix4Added GLKMatrix4MakeWithQuaternion(GLKQuaternion) -> GLKMatrix4Added GLKMatrix4MakeWithRows(GLKVector4, GLKVector4, GLKVector4, GLKVector4) -> GLKMatrix4Added GLKMatrix4MakeXRotation(Float) -> GLKMatrix4Added GLKMatrix4MakeYRotation(Float) -> GLKMatrix4Added GLKMatrix4MakeZRotation(Float) -> GLKMatrix4Added GLKMatrix4Multiply(GLKMatrix4, GLKMatrix4) -> GLKMatrix4Added GLKMatrix4MultiplyAndProjectVector3(GLKMatrix4, GLKVector3) -> GLKVector3Added GLKMatrix4MultiplyAndProjectVector3Array(GLKMatrix4, UnsafeMutablePointer<GLKVector3>, Int)Added GLKMatrix4MultiplyVector3(GLKMatrix4, GLKVector3) -> GLKVector3Added GLKMatrix4MultiplyVector3Array(GLKMatrix4, UnsafeMutablePointer<GLKVector3>, Int)Added GLKMatrix4MultiplyVector3ArrayWithTranslation(GLKMatrix4, UnsafeMutablePointer<GLKVector3>, Int)Added GLKMatrix4MultiplyVector3WithTranslation(GLKMatrix4, GLKVector3) -> GLKVector3Added GLKMatrix4MultiplyVector4(GLKMatrix4, GLKVector4) -> GLKVector4Added GLKMatrix4MultiplyVector4Array(GLKMatrix4, UnsafeMutablePointer<GLKVector4>, Int)Added GLKMatrix4Rotate(GLKMatrix4, Float, Float, Float, Float) -> GLKMatrix4Added GLKMatrix4RotateWithVector3(GLKMatrix4, Float, GLKVector3) -> GLKMatrix4Added GLKMatrix4RotateWithVector4(GLKMatrix4, Float, GLKVector4) -> GLKMatrix4Added GLKMatrix4RotateX(GLKMatrix4, Float) -> GLKMatrix4Added GLKMatrix4RotateY(GLKMatrix4, Float) -> GLKMatrix4Added GLKMatrix4RotateZ(GLKMatrix4, Float) -> GLKMatrix4Added GLKMatrix4Scale(GLKMatrix4, Float, Float, Float) -> GLKMatrix4Added GLKMatrix4ScaleWithVector3(GLKMatrix4, GLKVector3) -> GLKMatrix4Added GLKMatrix4ScaleWithVector4(GLKMatrix4, GLKVector4) -> GLKMatrix4Added GLKMatrix4SetColumn(GLKMatrix4, Int32, GLKVector4) -> GLKMatrix4Added GLKMatrix4SetRow(GLKMatrix4, Int32, GLKVector4) -> GLKMatrix4Added GLKMatrix4Subtract(GLKMatrix4, GLKMatrix4) -> GLKMatrix4Added GLKMatrix4Translate(GLKMatrix4, Float, Float, Float) -> GLKMatrix4Added GLKMatrix4TranslateWithVector3(GLKMatrix4, GLKVector3) -> GLKMatrix4Added GLKMatrix4TranslateWithVector4(GLKMatrix4, GLKVector4) -> GLKMatrix4Added GLKMatrix4Transpose(GLKMatrix4) -> GLKMatrix4Added GLKMatrixStackGetMatrix2(GLKMatrixStack!) -> GLKMatrix2Added GLKMatrixStackGetMatrix3(GLKMatrixStack!) -> GLKMatrix3Added GLKMatrixStackGetMatrix3Inverse(GLKMatrixStack!) -> GLKMatrix3Added GLKMatrixStackGetMatrix3InverseTranspose(GLKMatrixStack!) -> GLKMatrix3Added GLKMatrixStackGetMatrix4(GLKMatrixStack!) -> GLKMatrix4Added GLKMatrixStackGetMatrix4Inverse(GLKMatrixStack!) -> GLKMatrix4Added GLKMatrixStackGetMatrix4InverseTranspose(GLKMatrixStack!) -> GLKMatrix4Added GLKMatrixStackLoadMatrix4(GLKMatrixStack!, GLKMatrix4)Added GLKMatrixStackMultiplyMatrix4(GLKMatrixStack!, GLKMatrix4)Added GLKMatrixStackRotateWithVector3(GLKMatrixStack!, Float, GLKVector3)Added GLKMatrixStackRotateWithVector4(GLKMatrixStack!, Float, GLKVector4)Added GLKMatrixStackScaleWithVector3(GLKMatrixStack!, GLKVector3)Added GLKMatrixStackScaleWithVector4(GLKMatrixStack!, GLKVector4)Added GLKMatrixStackTranslateWithVector3(GLKMatrixStack!, GLKVector3)Added GLKMatrixStackTranslateWithVector4(GLKMatrixStack!, GLKVector4)Added GLKQuaternionAdded GLKQuaternionAdd(GLKQuaternion, GLKQuaternion) -> GLKQuaternionAdded GLKQuaternionAngle(GLKQuaternion) -> FloatAdded GLKQuaternionAxis(GLKQuaternion) -> GLKVector3Added GLKQuaternionConjugate(GLKQuaternion) -> GLKQuaternionAdded GLKQuaternionIdentityAdded GLKQuaternionInvert(GLKQuaternion) -> GLKQuaternionAdded GLKQuaternionLength(GLKQuaternion) -> FloatAdded GLKQuaternionMake(Float, Float, Float, Float) -> GLKQuaternionAdded GLKQuaternionMakeWithAngleAndAxis(Float, Float, Float, Float) -> GLKQuaternionAdded GLKQuaternionMakeWithAngleAndVector3Axis(Float, GLKVector3) -> GLKQuaternionAdded GLKQuaternionMakeWithArray(UnsafeMutablePointer<Float>) -> GLKQuaternionAdded GLKQuaternionMakeWithMatrix3(GLKMatrix3) -> GLKQuaternionAdded GLKQuaternionMakeWithMatrix4(GLKMatrix4) -> GLKQuaternionAdded GLKQuaternionMakeWithVector3(GLKVector3, Float) -> GLKQuaternionAdded GLKQuaternionMultiply(GLKQuaternion, GLKQuaternion) -> GLKQuaternionAdded GLKQuaternionNormalize(GLKQuaternion) -> GLKQuaternionAdded GLKQuaternionRotateVector3(GLKQuaternion, GLKVector3) -> GLKVector3Added GLKQuaternionRotateVector3Array(GLKQuaternion, UnsafeMutablePointer<GLKVector3>, Int)Added GLKQuaternionRotateVector4(GLKQuaternion, GLKVector4) -> GLKVector4Added GLKQuaternionRotateVector4Array(GLKQuaternion, UnsafeMutablePointer<GLKVector4>, Int)Added GLKQuaternionSlerp(GLKQuaternion, GLKQuaternion, Float) -> GLKQuaternionAdded GLKQuaternionSubtract(GLKQuaternion, GLKQuaternion) -> GLKQuaternionAdded GLKVector2Added GLKVector2Add(GLKVector2, GLKVector2) -> GLKVector2Added GLKVector2AddScalar(GLKVector2, Float) -> GLKVector2Added GLKVector2AllEqualToScalar(GLKVector2, Float) -> BoolAdded GLKVector2AllEqualToVector2(GLKVector2, GLKVector2) -> BoolAdded GLKVector2AllGreaterThanOrEqualToScalar(GLKVector2, Float) -> BoolAdded GLKVector2AllGreaterThanOrEqualToVector2(GLKVector2, GLKVector2) -> BoolAdded GLKVector2AllGreaterThanScalar(GLKVector2, Float) -> BoolAdded GLKVector2AllGreaterThanVector2(GLKVector2, GLKVector2) -> BoolAdded GLKVector2Distance(GLKVector2, GLKVector2) -> FloatAdded GLKVector2Divide(GLKVector2, GLKVector2) -> GLKVector2Added GLKVector2DivideScalar(GLKVector2, Float) -> GLKVector2Added GLKVector2DotProduct(GLKVector2, GLKVector2) -> FloatAdded GLKVector2Length(GLKVector2) -> FloatAdded GLKVector2Lerp(GLKVector2, GLKVector2, Float) -> GLKVector2Added GLKVector2Make(Float, Float) -> GLKVector2Added GLKVector2MakeWithArray(UnsafeMutablePointer<Float>) -> GLKVector2Added GLKVector2Maximum(GLKVector2, GLKVector2) -> GLKVector2Added GLKVector2Minimum(GLKVector2, GLKVector2) -> GLKVector2Added GLKVector2Multiply(GLKVector2, GLKVector2) -> GLKVector2Added GLKVector2MultiplyScalar(GLKVector2, Float) -> GLKVector2Added GLKVector2Negate(GLKVector2) -> GLKVector2Added GLKVector2Normalize(GLKVector2) -> GLKVector2Added GLKVector2Project(GLKVector2, GLKVector2) -> GLKVector2Added GLKVector2Subtract(GLKVector2, GLKVector2) -> GLKVector2Added GLKVector2SubtractScalar(GLKVector2, Float) -> GLKVector2Added GLKVector3Added GLKVector3Add(GLKVector3, GLKVector3) -> GLKVector3Added GLKVector3AddScalar(GLKVector3, Float) -> GLKVector3Added GLKVector3AllEqualToScalar(GLKVector3, Float) -> BoolAdded GLKVector3AllEqualToVector3(GLKVector3, GLKVector3) -> BoolAdded GLKVector3AllGreaterThanOrEqualToScalar(GLKVector3, Float) -> BoolAdded GLKVector3AllGreaterThanOrEqualToVector3(GLKVector3, GLKVector3) -> BoolAdded GLKVector3AllGreaterThanScalar(GLKVector3, Float) -> BoolAdded GLKVector3AllGreaterThanVector3(GLKVector3, GLKVector3) -> BoolAdded GLKVector3CrossProduct(GLKVector3, GLKVector3) -> GLKVector3Added GLKVector3Distance(GLKVector3, GLKVector3) -> FloatAdded GLKVector3Divide(GLKVector3, GLKVector3) -> GLKVector3Added GLKVector3DivideScalar(GLKVector3, Float) -> GLKVector3Added GLKVector3DotProduct(GLKVector3, GLKVector3) -> FloatAdded GLKVector3Length(GLKVector3) -> FloatAdded GLKVector3Lerp(GLKVector3, GLKVector3, Float) -> GLKVector3Added GLKVector3Make(Float, Float, Float) -> GLKVector3Added GLKVector3MakeWithArray(UnsafeMutablePointer<Float>) -> GLKVector3Added GLKVector3Maximum(GLKVector3, GLKVector3) -> GLKVector3Added GLKVector3Minimum(GLKVector3, GLKVector3) -> GLKVector3Added GLKVector3Multiply(GLKVector3, GLKVector3) -> GLKVector3Added GLKVector3MultiplyScalar(GLKVector3, Float) -> GLKVector3Added GLKVector3Negate(GLKVector3) -> GLKVector3Added GLKVector3Normalize(GLKVector3) -> GLKVector3Added GLKVector3Project(GLKVector3, GLKVector3) -> GLKVector3Added GLKVector3Subtract(GLKVector3, GLKVector3) -> GLKVector3Added GLKVector3SubtractScalar(GLKVector3, Float) -> GLKVector3Added GLKVector4Added GLKVector4Add(GLKVector4, GLKVector4) -> GLKVector4Added GLKVector4AddScalar(GLKVector4, Float) -> GLKVector4Added GLKVector4AllEqualToScalar(GLKVector4, Float) -> BoolAdded GLKVector4AllEqualToVector4(GLKVector4, GLKVector4) -> BoolAdded GLKVector4AllGreaterThanOrEqualToScalar(GLKVector4, Float) -> BoolAdded GLKVector4AllGreaterThanOrEqualToVector4(GLKVector4, GLKVector4) -> BoolAdded GLKVector4AllGreaterThanScalar(GLKVector4, Float) -> BoolAdded GLKVector4AllGreaterThanVector4(GLKVector4, GLKVector4) -> BoolAdded GLKVector4CrossProduct(GLKVector4, GLKVector4) -> GLKVector4Added GLKVector4Distance(GLKVector4, GLKVector4) -> FloatAdded GLKVector4Divide(GLKVector4, GLKVector4) -> GLKVector4Added GLKVector4DivideScalar(GLKVector4, Float) -> GLKVector4Added GLKVector4DotProduct(GLKVector4, GLKVector4) -> FloatAdded GLKVector4Length(GLKVector4) -> FloatAdded GLKVector4Lerp(GLKVector4, GLKVector4, Float) -> GLKVector4Added GLKVector4Make(Float, Float, Float, Float) -> GLKVector4Added GLKVector4MakeWithArray(UnsafeMutablePointer<Float>) -> GLKVector4Added GLKVector4MakeWithVector3(GLKVector3, Float) -> GLKVector4Added GLKVector4Maximum(GLKVector4, GLKVector4) -> GLKVector4Added GLKVector4Minimum(GLKVector4, GLKVector4) -> GLKVector4Added GLKVector4Multiply(GLKVector4, GLKVector4) -> GLKVector4Added GLKVector4MultiplyScalar(GLKVector4, Float) -> GLKVector4Added GLKVector4Negate(GLKVector4) -> GLKVector4Added GLKVector4Normalize(GLKVector4) -> GLKVector4Added GLKVector4Project(GLKVector4, GLKVector4) -> GLKVector4Added GLKVector4Subtract(GLKVector4, GLKVector4) -> GLKVector4Added GLKVector4SubtractScalar(GLKVector4, Float) -> GLKVector4Added GLK_SSE3_INTRINSICSAdded NSStringFromGLKMatrix2(GLKMatrix2) -> String!Added NSStringFromGLKMatrix3(GLKMatrix3) -> String!Added NSStringFromGLKMatrix4(GLKMatrix4) -> String!Added NSStringFromGLKQuaternion(GLKQuaternion) -> String!Added NSStringFromGLKVector2(GLKVector2) -> String!Added NSStringFromGLKVector3(GLKVector3) -> String!Added NSStringFromGLKVector4(GLKVector4) -> String!Modified GLKBaseEffect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKEffectProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKEffectPropertyFog

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKEffectPropertyLight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKEffectPropertyMaterial

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKEffectPropertyTexture

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKEffectPropertyTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKFogMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKLightingType [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKReflectionMapEffect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKSkyboxEffect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKTextureEnvMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKTextureInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKTextureInfoAlphaState [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKTextureInfoOrigin [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKTextureLoader

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKTextureLoader.init(shareContext: NSOpenGLContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(shareContext context: NSOpenGLContext!) ``` |
| To | ``` init!(shareContext context: NSOpenGLContext!) ``` |

Modified GLKTextureLoaderError [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKTextureTarget [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKVertexAttrib [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GLKTextureLoaderApplyPremultiplication

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let GLKTextureLoaderApplyPremultiplication: NSString! ``` | OS X 10.10 |
| To | ``` let GLKTextureLoaderApplyPremultiplication: String ``` | OS X 10.8 |

Modified GLKTextureLoaderErrorDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let GLKTextureLoaderErrorDomain: NSString! ``` | OS X 10.10 |
| To | ``` let GLKTextureLoaderErrorDomain: String ``` | OS X 10.8 |

Modified GLKTextureLoaderErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let GLKTextureLoaderErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let GLKTextureLoaderErrorKey: String ``` | OS X 10.8 |

Modified GLKTextureLoaderGLErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let GLKTextureLoaderGLErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let GLKTextureLoaderGLErrorKey: String ``` | OS X 10.8 |

Modified GLKTextureLoaderGenerateMipmaps

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let GLKTextureLoaderGenerateMipmaps: NSString! ``` | OS X 10.10 |
| To | ``` let GLKTextureLoaderGenerateMipmaps: String ``` | OS X 10.8 |

Modified GLKTextureLoaderOriginBottomLeft

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let GLKTextureLoaderOriginBottomLeft: NSString! ``` | OS X 10.10 |
| To | ``` let GLKTextureLoaderOriginBottomLeft: String ``` | OS X 10.8 |

Modified GLKTextureLoaderSRGB

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let GLKTextureLoaderSRGB: NSString! ``` | OS X 10.10 |
| To | ``` let GLKTextureLoaderSRGB: String ``` | OS X 10.9 |

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
