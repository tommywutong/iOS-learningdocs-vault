---
title: watchOS 2.2 API Diffs
apple_id: TP40016663
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS22APIDiffs/Swift/UIKit.html
archived_at: '2026-07-18T02:58:12.420426Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.2 API Diffs](watchOS%202.1%20to%20watchOS%202.2%20API%20Differences.md)


# UIKit Changes for Swift

### UIKit

Added [NSTextAlignmentFromCTTextAlignment(_: CTTextAlignment) -> NSTextAlignment](https://developer.apple.com/documentation/uikit/1624537-nstextalignmentfromcttextalignme)Added [NSTextAlignmentToCTTextAlignment(_: NSTextAlignment) -> CTTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/1624536-init)Modified [UIColor](https://developer.apple.com/documentation/uikit/uicolor)

|  | Declaration |
| --- | --- |
| From | ``` class UIColor : NSObject, NSSecureCoding, NSCopying {      init(white white: CGFloat, alpha alpha: CGFloat)     class func colorWithWhite(_ white: CGFloat, alpha alpha: CGFloat) -> UIColor      init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     class func colorWithHue(_ hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat) -> UIColor      init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     class func colorWithRed(_ red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) -> UIColor      init(CGColor cgColor: CGColor)     class func colorWithCGColor(_ cgColor: CGColor) -> UIColor      init(patternImage image: UIImage)     class func colorWithPatternImage(_ image: UIImage) -> UIColor     init(white white: CGFloat, alpha alpha: CGFloat)     init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     init(CGColor cgColor: CGColor)     init(patternImage image: UIImage)     class func blackColor() -> UIColor     class func darkGrayColor() -> UIColor     class func lightGrayColor() -> UIColor     class func whiteColor() -> UIColor     class func grayColor() -> UIColor     class func redColor() -> UIColor     class func greenColor() -> UIColor     class func blueColor() -> UIColor     class func cyanColor() -> UIColor     class func yellowColor() -> UIColor     class func magentaColor() -> UIColor     class func orangeColor() -> UIColor     class func purpleColor() -> UIColor     class func brownColor() -> UIColor     class func clearColor() -> UIColor     func set()     func setFill()     func setStroke()     func getWhite(_ white: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getHue(_ hue: UnsafeMutablePointer<CGFloat>, saturation saturation: UnsafeMutablePointer<CGFloat>, brightness brightness: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getRed(_ red: UnsafeMutablePointer<CGFloat>, green green: UnsafeMutablePointer<CGFloat>, blue blue: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func colorWithAlphaComponent(_ alpha: CGFloat) -> UIColor     var CGColor: CGColor { get } } extension UIColor : _ColorLiteralConvertible {     required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float) } extension UIColor : _ColorLiteralConvertible {     required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float) } ``` |
| To | ``` class UIColor : NSObject, NSSecureCoding, NSCopying {      init(white white: CGFloat, alpha alpha: CGFloat)     class func colorWithWhite(_ white: CGFloat, alpha alpha: CGFloat) -> UIColor      init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     class func colorWithHue(_ hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat) -> UIColor      init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     class func colorWithRed(_ red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) -> UIColor      init(CGColor cgColor: CGColor)     class func colorWithCGColor(_ cgColor: CGColor) -> UIColor      init(patternImage image: UIImage)     class func colorWithPatternImage(_ image: UIImage) -> UIColor     init(white white: CGFloat, alpha alpha: CGFloat)     init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     init(CGColor cgColor: CGColor)     init(patternImage image: UIImage)     class func blackColor() -> UIColor     class func darkGrayColor() -> UIColor     class func lightGrayColor() -> UIColor     class func whiteColor() -> UIColor     class func grayColor() -> UIColor     class func redColor() -> UIColor     class func greenColor() -> UIColor     class func blueColor() -> UIColor     class func cyanColor() -> UIColor     class func yellowColor() -> UIColor     class func magentaColor() -> UIColor     class func orangeColor() -> UIColor     class func purpleColor() -> UIColor     class func brownColor() -> UIColor     class func clearColor() -> UIColor     func set()     func setFill()     func setStroke()     func getWhite(_ white: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getHue(_ hue: UnsafeMutablePointer<CGFloat>, saturation saturation: UnsafeMutablePointer<CGFloat>, brightness brightness: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getRed(_ red: UnsafeMutablePointer<CGFloat>, green green: UnsafeMutablePointer<CGFloat>, blue blue: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func colorWithAlphaComponent(_ alpha: CGFloat) -> UIColor     var CGColor: CGColor { get } } extension UIColor {     required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float) } extension UIColor {     required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float) } ``` |

Modified [UIImage](https://developer.apple.com/documentation/uikit/uiimage)

|  | Declaration |
| --- | --- |
| From | ``` class UIImage : NSObject, NSSecureCoding {      init?(named name: String)     class func imageNamed(_ name: String) -> UIImage?      init?(contentsOfFile path: String)     class func imageWithContentsOfFile(_ path: String) -> UIImage?      init?(data data: NSData)     class func imageWithData(_ data: NSData) -> UIImage?      init?(data data: NSData, scale scale: CGFloat)     class func imageWithData(_ data: NSData, scale scale: CGFloat) -> UIImage?      init(CGImage cgImage: CGImage)     class func imageWithCGImage(_ cgImage: CGImage) -> UIImage      init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     class func imageWithCGImage(_ cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage     init?(contentsOfFile path: String)     init?(data data: NSData)     init?(data data: NSData, scale scale: CGFloat)     init(CGImage cgImage: CGImage)     init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     var size: CGSize { get }     var CGImage: CGImage? { get }     var imageOrientation: UIImageOrientation { get }     var scale: CGFloat { get }     class func animatedImageNamed(_ name: String, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: NSTimeInterval) -> UIImage?     class func animatedImageWithImages(_ images: [UIImage], duration duration: NSTimeInterval) -> UIImage?     var images: [UIImage]? { get }     var duration: NSTimeInterval { get }     func drawAtPoint(_ point: CGPoint)     func drawAtPoint(_ point: CGPoint, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawInRect(_ rect: CGRect)     func drawInRect(_ rect: CGRect, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawAsPatternInRect(_ rect: CGRect)     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets) -> UIImage     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode) -> UIImage     var capInsets: UIEdgeInsets { get }     var resizingMode: UIImageResizingMode { get }     func imageWithAlignmentRectInsets(_ alignmentInsets: UIEdgeInsets) -> UIImage     var alignmentRectInsets: UIEdgeInsets { get }     func imageWithRenderingMode(_ renderingMode: UIImageRenderingMode) -> UIImage     var renderingMode: UIImageRenderingMode { get }     func imageFlippedForRightToLeftLayoutDirection() -> UIImage     var flipsForRightToLeftLayoutDirection: Bool { get } } extension UIImage : _ImageLiteralConvertible {     required convenience init(imageLiteral name: String) } extension UIImage {     func stretchableImageWithLeftCapWidth(_ leftCapWidth: Int, topCapHeight topCapHeight: Int) -> UIImage     var leftCapWidth: Int { get }     var topCapHeight: Int { get } } extension UIImage : _ImageLiteralConvertible {     required convenience init(imageLiteral name: String) } ``` |
| To | ``` class UIImage : NSObject, NSSecureCoding {      init?(named name: String)     class func imageNamed(_ name: String) -> UIImage?      init?(contentsOfFile path: String)     class func imageWithContentsOfFile(_ path: String) -> UIImage?      init?(data data: NSData)     class func imageWithData(_ data: NSData) -> UIImage?      init?(data data: NSData, scale scale: CGFloat)     class func imageWithData(_ data: NSData, scale scale: CGFloat) -> UIImage?      init(CGImage cgImage: CGImage)     class func imageWithCGImage(_ cgImage: CGImage) -> UIImage      init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     class func imageWithCGImage(_ cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage     init?(contentsOfFile path: String)     init?(data data: NSData)     init?(data data: NSData, scale scale: CGFloat)     init(CGImage cgImage: CGImage)     init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     var size: CGSize { get }     var CGImage: CGImage? { get }     var imageOrientation: UIImageOrientation { get }     var scale: CGFloat { get }     class func animatedImageNamed(_ name: String, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: NSTimeInterval) -> UIImage?     class func animatedImageWithImages(_ images: [UIImage], duration duration: NSTimeInterval) -> UIImage?     var images: [UIImage]? { get }     var duration: NSTimeInterval { get }     func drawAtPoint(_ point: CGPoint)     func drawAtPoint(_ point: CGPoint, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawInRect(_ rect: CGRect)     func drawInRect(_ rect: CGRect, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawAsPatternInRect(_ rect: CGRect)     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets) -> UIImage     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode) -> UIImage     var capInsets: UIEdgeInsets { get }     var resizingMode: UIImageResizingMode { get }     func imageWithAlignmentRectInsets(_ alignmentInsets: UIEdgeInsets) -> UIImage     var alignmentRectInsets: UIEdgeInsets { get }     func imageWithRenderingMode(_ renderingMode: UIImageRenderingMode) -> UIImage     var renderingMode: UIImageRenderingMode { get }     func imageFlippedForRightToLeftLayoutDirection() -> UIImage     var flipsForRightToLeftLayoutDirection: Bool { get } } extension UIImage {     required convenience init(imageLiteral name: String) } extension UIImage {     func stretchableImageWithLeftCapWidth(_ leftCapWidth: Int, topCapHeight topCapHeight: Int) -> UIImage     var leftCapWidth: Int { get }     var topCapHeight: Int { get } } extension UIImage {     required convenience init(imageLiteral name: String) } ``` |

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
