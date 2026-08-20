---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/GLKit.html
archived_at: '2026-07-15T07:34:54.970881Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# GLKit Changes

## GLKit (Added)

Added GLKBaseEffectAdded GLKBaseEffect.colorMaterialEnabledAdded GLKBaseEffect.fogAdded GLKBaseEffect.labelAdded GLKBaseEffect.light0Added GLKBaseEffect.light1Added GLKBaseEffect.light2Added GLKBaseEffect.lightModelTwoSidedAdded GLKBaseEffect.lightingTypeAdded GLKBaseEffect.materialAdded GLKBaseEffect.prepareToDraw()Added GLKBaseEffect.texture2d0Added GLKBaseEffect.texture2d1Added GLKBaseEffect.textureOrderAdded GLKBaseEffect.transformAdded GLKBaseEffect.useConstantColorAdded GLKEffectPropertyAdded GLKEffectPropertyFogAdded GLKEffectPropertyFog.densityAdded GLKEffectPropertyFog.enabledAdded GLKEffectPropertyFog.endAdded GLKEffectPropertyFog.modeAdded GLKEffectPropertyFog.startAdded GLKEffectPropertyLightAdded GLKEffectPropertyLight.constantAttenuationAdded GLKEffectPropertyLight.enabledAdded GLKEffectPropertyLight.linearAttenuationAdded GLKEffectPropertyLight.quadraticAttenuationAdded GLKEffectPropertyLight.spotCutoffAdded GLKEffectPropertyLight.spotExponentAdded GLKEffectPropertyLight.transformAdded GLKEffectPropertyMaterialAdded GLKEffectPropertyMaterial.shininessAdded GLKEffectPropertyTextureAdded GLKEffectPropertyTexture.enabledAdded GLKEffectPropertyTexture.envModeAdded GLKEffectPropertyTexture.nameAdded GLKEffectPropertyTexture.targetAdded GLKEffectPropertyTransformAdded GLKFogMode [enum]Added GLKFogMode.ExpAdded GLKFogMode.Exp2Added GLKFogMode.LinearAdded GLKLightingType [enum]Added GLKLightingType.PerPixelAdded GLKLightingType.PerVertexAdded GLKNamedEffectAdded GLKNamedEffect.prepareToDraw()Added GLKReflectionMapEffectAdded GLKReflectionMapEffect.prepareToDraw()Added GLKReflectionMapEffect.textureCubeMapAdded GLKSkyboxEffectAdded GLKSkyboxEffect.draw()Added GLKSkyboxEffect.labelAdded GLKSkyboxEffect.prepareToDraw()Added GLKSkyboxEffect.textureCubeMapAdded GLKSkyboxEffect.transformAdded GLKSkyboxEffect.xSizeAdded GLKSkyboxEffect.ySizeAdded GLKSkyboxEffect.zSizeAdded GLKTextureEnvMode [enum]Added GLKTextureEnvMode.DecalAdded GLKTextureEnvMode.ModulateAdded GLKTextureEnvMode.ReplaceAdded GLKTextureInfoAdded GLKTextureInfo.alphaStateAdded GLKTextureInfo.containsMipmapsAdded GLKTextureInfo.heightAdded GLKTextureInfo.nameAdded GLKTextureInfo.targetAdded GLKTextureInfo.textureOriginAdded GLKTextureInfo.widthAdded GLKTextureInfoAlphaState [enum]Added GLKTextureInfoAlphaState.NonPremultipliedAdded GLKTextureInfoAlphaState.NoneAdded GLKTextureInfoAlphaState.PremultipliedAdded GLKTextureInfoOrigin [enum]Added GLKTextureInfoOrigin.BottomLeftAdded GLKTextureInfoOrigin.TopLeftAdded GLKTextureInfoOrigin.UnknownAdded GLKTextureLoaderAdded GLKTextureLoader.cubeMapWithContentsOfFile(String!, options:[NSObject: AnyObject]!, error: NSErrorPointer) -> GLKTextureInfo! [class]Added GLKTextureLoader.cubeMapWithContentsOfFile(String!, options:[NSObject: AnyObject]!, queue: dispatch_queue_t!, completionHandler: GLKTextureLoaderCallback!)Added GLKTextureLoader.cubeMapWithContentsOfFiles([AnyObject]!, options:[NSObject: AnyObject]!, error: NSErrorPointer) -> GLKTextureInfo! [class]Added GLKTextureLoader.cubeMapWithContentsOfFiles([AnyObject]!, options:[NSObject: AnyObject]!, queue: dispatch_queue_t!, completionHandler: GLKTextureLoaderCallback!)Added GLKTextureLoader.cubeMapWithContentsOfURL(NSURL!, options:[NSObject: AnyObject]!, error: NSErrorPointer) -> GLKTextureInfo! [class]Added GLKTextureLoader.cubeMapWithContentsOfURL(NSURL!, options:[NSObject: AnyObject]!, queue: dispatch_queue_t!, completionHandler: GLKTextureLoaderCallback!)Added GLKTextureLoader.init(shareContext: NSOpenGLContext!)Added GLKTextureLoader.textureWithCGImage(CGImage!, options:[NSObject: AnyObject]!, error: NSErrorPointer) -> GLKTextureInfo! [class]Added GLKTextureLoader.textureWithCGImage(CGImage!, options:[NSObject: AnyObject]!, queue: dispatch_queue_t!, completionHandler: GLKTextureLoaderCallback!)Added GLKTextureLoader.textureWithContentsOfData(NSData!, options:[NSObject: AnyObject]!, error: NSErrorPointer) -> GLKTextureInfo! [class]Added GLKTextureLoader.textureWithContentsOfData(NSData!, options:[NSObject: AnyObject]!, queue: dispatch_queue_t!, completionHandler: GLKTextureLoaderCallback!)Added GLKTextureLoader.textureWithContentsOfFile(String!, options:[NSObject: AnyObject]!, error: NSErrorPointer) -> GLKTextureInfo! [class]Added GLKTextureLoader.textureWithContentsOfFile(String!, options:[NSObject: AnyObject]!, queue: dispatch_queue_t!, completionHandler: GLKTextureLoaderCallback!)Added GLKTextureLoader.textureWithContentsOfURL(NSURL!, options:[NSObject: AnyObject]!, error: NSErrorPointer) -> GLKTextureInfo! [class]Added GLKTextureLoader.textureWithContentsOfURL(NSURL!, options:[NSObject: AnyObject]!, queue: dispatch_queue_t!, completionHandler: GLKTextureLoaderCallback!)Added GLKTextureLoaderError [enum]Added GLKTextureLoaderError.AlphaPremultiplicationFailureAdded GLKTextureLoaderError.CompressedTextureUploadAdded GLKTextureLoaderError.CubeMapInvalidNumFilesAdded GLKTextureLoaderError.DataPreprocessingFailureAdded GLKTextureLoaderError.FileOrURLNotFoundAdded GLKTextureLoaderError.IncompatibleFormatSRGBAdded GLKTextureLoaderError.InvalidCGImageAdded GLKTextureLoaderError.InvalidEAGLContextAdded GLKTextureLoaderError.InvalidNSDataAdded GLKTextureLoaderError.MipmapUnsupportedAdded GLKTextureLoaderError.PVRAtlasUnsupportedAdded GLKTextureLoaderError.ReorientationFailureAdded GLKTextureLoaderError.UncompressedTextureUploadAdded GLKTextureLoaderError.UnknownFileTypeAdded GLKTextureLoaderError.UnknownPathTypeAdded GLKTextureLoaderError.UnsupportedBitDepthAdded GLKTextureLoaderError.UnsupportedCubeMapDimensionsAdded GLKTextureLoaderError.UnsupportedOrientationAdded GLKTextureLoaderError.UnsupportedPVRFormatAdded GLKTextureTarget [enum]Added GLKTextureTarget.Target2DAdded GLKTextureTarget.TargetCtAdded GLKTextureTarget.TargetCubeMapAdded GLKVertexAttrib [enum]Added GLKVertexAttrib.ColorAdded GLKVertexAttrib.NormalAdded GLKVertexAttrib.PositionAdded GLKVertexAttrib.TexCoord0Added GLKVertexAttrib.TexCoord1Added GLKEffectPropertyPrvPtrAdded GLKMathDegreesToRadians(Float) -> FloatAdded GLKMathRadiansToDegrees(Float) -> FloatAdded GLKMatrixStackCreate(CFAllocator!) -> Unmanaged<GLKMatrixStack>!Added GLKMatrixStackGetTypeID() -> CFTypeIDAdded GLKMatrixStackMultiplyMatrixStack(GLKMatrixStack!, GLKMatrixStack!)Added GLKMatrixStackPop(GLKMatrixStack!)Added GLKMatrixStackPush(GLKMatrixStack!)Added GLKMatrixStackRefAdded GLKMatrixStackRotate(GLKMatrixStack!, Float, Float, Float, Float)Added GLKMatrixStackRotateX(GLKMatrixStack!, Float)Added GLKMatrixStackRotateY(GLKMatrixStack!, Float)Added GLKMatrixStackRotateZ(GLKMatrixStack!, Float)Added GLKMatrixStackScale(GLKMatrixStack!, Float, Float, Float)Added GLKMatrixStackSize(GLKMatrixStack!) -> Int32Added GLKMatrixStackTranslate(GLKMatrixStack!, Float, Float, Float)Added GLKTextureLoaderApplyPremultiplicationAdded GLKTextureLoaderCallbackAdded GLKTextureLoaderErrorDomainAdded GLKTextureLoaderErrorKeyAdded GLKTextureLoaderGLErrorKeyAdded GLKTextureLoaderGenerateMipmapsAdded GLKTextureLoaderOriginBottomLeftAdded GLKTextureLoaderSRGB

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
