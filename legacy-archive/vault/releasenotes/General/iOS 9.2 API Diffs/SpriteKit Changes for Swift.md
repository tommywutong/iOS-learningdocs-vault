---
title: iOS 9.2 API Diffs
apple_id: TP40016605
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS92APIDiffs/Swift/SpriteKit.html
archived_at: '2026-07-18T02:57:12.853308Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.2 API Diffs](iOS%209.1%20to%20iOS%209.2%20API%20Differences.md)


# SpriteKit Changes for Swift

### SpriteKit

Removed SKTexture.CGImageAdded [SKTexture.CGImage() -> CGImage](https://developer.apple.com/documentation/spritekit/sktexture/1519755-cgimage)Modified [SKTexture](https://developer.apple.com/documentation/spritekit/sktexture)

|  | Declaration |
| --- | --- |
| From | ``` class SKTexture : NSObject, NSCopying, NSCoding {     convenience init(imageNamed name: String)     class func textureWithImageNamed(_ name: String) -> Self     convenience init(rect rect: CGRect, inTexture texture: SKTexture)     class func textureWithRect(_ rect: CGRect, inTexture texture: SKTexture) -> Self     convenience init(vectorNoiseWithSmoothness smoothness: CGFloat, size size: CGSize)     class func textureVectorNoiseWithSmoothness(_ smoothness: CGFloat, size size: CGSize) -> Self     convenience init(noiseWithSmoothness smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool)     class func textureNoiseWithSmoothness(_ smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool) -> Self     convenience init(CGImage image: CGImage)     class func textureWithCGImage(_ image: CGImage) -> Self     convenience init(image image: UIImage)     class func textureWithImage(_ image: UIImage) -> Self     convenience init(data pixelData: NSData, size size: CGSize)     class func textureWithData(_ pixelData: NSData, size size: CGSize) -> Self     convenience init(data pixelData: NSData, size size: CGSize, flipped flipped: Bool)     class func textureWithData(_ pixelData: NSData, size size: CGSize, flipped flipped: Bool) -> Self     convenience init(data pixelData: NSData, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32)     class func textureWithData(_ pixelData: NSData, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) -> Self     func textureByApplyingCIFilter(_ filter: CIFilter) -> Self     func textureByGeneratingNormalMap() -> Self     func textureByGeneratingNormalMapWithSmoothness(_ smoothness: CGFloat, contrast contrast: CGFloat) -> Self     func textureRect() -> CGRect     func size() -> CGSize     var filteringMode: SKTextureFilteringMode     var usesMipmaps: Bool     var CGImage: CGImage { get }     class func preloadTextures(_ textures: [SKTexture], withCompletionHandler completionHandler: () -> Void)     func preloadWithCompletionHandler(_ completionHandler: () -> Void) } extension SKTexture : _Reflectable { } extension SKTexture : _Reflectable { } ``` |
| To | ``` class SKTexture : NSObject, NSCopying, NSCoding {     convenience init(imageNamed name: String)     class func textureWithImageNamed(_ name: String) -> Self     convenience init(rect rect: CGRect, inTexture texture: SKTexture)     class func textureWithRect(_ rect: CGRect, inTexture texture: SKTexture) -> Self     convenience init(vectorNoiseWithSmoothness smoothness: CGFloat, size size: CGSize)     class func textureVectorNoiseWithSmoothness(_ smoothness: CGFloat, size size: CGSize) -> Self     convenience init(noiseWithSmoothness smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool)     class func textureNoiseWithSmoothness(_ smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool) -> Self     convenience init(CGImage image: CGImage)     class func textureWithCGImage(_ image: CGImage) -> Self     convenience init(image image: UIImage)     class func textureWithImage(_ image: UIImage) -> Self     convenience init(data pixelData: NSData, size size: CGSize)     class func textureWithData(_ pixelData: NSData, size size: CGSize) -> Self     convenience init(data pixelData: NSData, size size: CGSize, flipped flipped: Bool)     class func textureWithData(_ pixelData: NSData, size size: CGSize, flipped flipped: Bool) -> Self     convenience init(data pixelData: NSData, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32)     class func textureWithData(_ pixelData: NSData, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) -> Self     func textureByApplyingCIFilter(_ filter: CIFilter) -> Self     func textureByGeneratingNormalMap() -> Self     func textureByGeneratingNormalMapWithSmoothness(_ smoothness: CGFloat, contrast contrast: CGFloat) -> Self     func textureRect() -> CGRect     func size() -> CGSize     var filteringMode: SKTextureFilteringMode     var usesMipmaps: Bool     func CGImage() -> CGImage     class func preloadTextures(_ textures: [SKTexture], withCompletionHandler completionHandler: () -> Void)     func preloadWithCompletionHandler(_ completionHandler: () -> Void) } extension SKTexture : _Reflectable { } extension SKTexture : _Reflectable { } ``` |

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
