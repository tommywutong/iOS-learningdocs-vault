---
title: watchOS 2.1 API Diffs
apple_id: TP40016636
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS21APIDiffs/Swift/UIKit.html
archived_at: '2026-07-18T02:58:09.371800Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.1 API Diffs](watchOS%202.0%20to%20watchOS%202.1%20API%20Differences.md)


# UIKit Changes for Swift

### UIKit

Added UIColor.init(colorLiteralRed: Float, green: Float, blue: Float, alpha: Float)Added UIImage.init(imageLiteral: String)Modified [NSLineBreakMode [enum]](https://developer.apple.com/documentation/uikit/nslinebreakmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSMutableParagraphStyle](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSParagraphStyle](https://developer.apple.com/documentation/uikit/nsparagraphstyle)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSParagraphStyle : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     class func defaultParagraphStyle() -> NSParagraphStyle     class func defaultWritingDirectionForLanguage(_ languageName: String?) -> NSWritingDirection     var lineSpacing: CGFloat { get }     var paragraphSpacing: CGFloat { get }     var alignment: NSTextAlignment { get }     var headIndent: CGFloat { get }     var tailIndent: CGFloat { get }     var firstLineHeadIndent: CGFloat { get }     var minimumLineHeight: CGFloat { get }     var maximumLineHeight: CGFloat { get }     var lineBreakMode: NSLineBreakMode { get }     var baseWritingDirection: NSWritingDirection { get }     var lineHeightMultiple: CGFloat { get }     var paragraphSpacingBefore: CGFloat { get }     var hyphenationFactor: Float { get }     var tabStops: [NSTextTab] { get }     var defaultTabInterval: CGFloat { get }     var allowsDefaultTighteningForTruncation: Bool { get } } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class NSParagraphStyle : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     class func defaultParagraphStyle() -> NSParagraphStyle     class func defaultWritingDirectionForLanguage(_ languageName: String?) -> NSWritingDirection     var lineSpacing: CGFloat { get }     var paragraphSpacing: CGFloat { get }     var alignment: NSTextAlignment { get }     var headIndent: CGFloat { get }     var tailIndent: CGFloat { get }     var firstLineHeadIndent: CGFloat { get }     var minimumLineHeight: CGFloat { get }     var maximumLineHeight: CGFloat { get }     var lineBreakMode: NSLineBreakMode { get }     var baseWritingDirection: NSWritingDirection { get }     var lineHeightMultiple: CGFloat { get }     var paragraphSpacingBefore: CGFloat { get }     var hyphenationFactor: Float { get }     var tabStops: [NSTextTab] { get }     var defaultTabInterval: CGFloat { get }     var allowsDefaultTighteningForTruncation: Bool { get } } ``` | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [NSStringDrawingContext](https://developer.apple.com/documentation/appkit/nsstringdrawingcontext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSTextAlignment [enum]](https://developer.apple.com/documentation/uikit/nstextalignment)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSTextTab](https://developer.apple.com/documentation/uikit/nstexttab)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [NSTextWritingDirection [enum]](https://developer.apple.com/documentation/uikit/nstextwritingdirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSUnderlineStyle [enum]](https://developer.apple.com/documentation/uikit/nsunderlinestyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSWritingDirection [enum]](https://developer.apple.com/documentation/appkit/nswritingdirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSWritingDirectionFormatType [enum]](https://developer.apple.com/documentation/uikit/nswritingdirectionformattype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIAccessibilityNavigationStyle [enum]](https://developer.apple.com/documentation/uikit/uiaccessibilitynavigationstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIBezierPath](https://developer.apple.com/documentation/uikit/uibezierpath)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [UIColor](https://developer.apple.com/documentation/uikit/uicolor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIColor : NSObject, NSSecureCoding, NSCoding, NSCopying {      init(white white: CGFloat, alpha alpha: CGFloat)     class func colorWithWhite(_ white: CGFloat, alpha alpha: CGFloat) -> UIColor      init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     class func colorWithHue(_ hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat) -> UIColor      init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     class func colorWithRed(_ red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) -> UIColor      init(CGColor cgColor: CGColor)     class func colorWithCGColor(_ cgColor: CGColor) -> UIColor      init(patternImage image: UIImage)     class func colorWithPatternImage(_ image: UIImage) -> UIColor     init(white white: CGFloat, alpha alpha: CGFloat)     init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     init(CGColor cgColor: CGColor)     init(patternImage image: UIImage)     class func blackColor() -> UIColor     class func darkGrayColor() -> UIColor     class func lightGrayColor() -> UIColor     class func whiteColor() -> UIColor     class func grayColor() -> UIColor     class func redColor() -> UIColor     class func greenColor() -> UIColor     class func blueColor() -> UIColor     class func cyanColor() -> UIColor     class func yellowColor() -> UIColor     class func magentaColor() -> UIColor     class func orangeColor() -> UIColor     class func purpleColor() -> UIColor     class func brownColor() -> UIColor     class func clearColor() -> UIColor     func set()     func setFill()     func setStroke()     func getWhite(_ white: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getHue(_ hue: UnsafeMutablePointer<CGFloat>, saturation saturation: UnsafeMutablePointer<CGFloat>, brightness brightness: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getRed(_ red: UnsafeMutablePointer<CGFloat>, green green: UnsafeMutablePointer<CGFloat>, blue blue: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func colorWithAlphaComponent(_ alpha: CGFloat) -> UIColor     var CGColor: CGColor { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class UIColor : NSObject, NSSecureCoding, NSCopying {      init(white white: CGFloat, alpha alpha: CGFloat)     class func colorWithWhite(_ white: CGFloat, alpha alpha: CGFloat) -> UIColor      init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     class func colorWithHue(_ hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat) -> UIColor      init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     class func colorWithRed(_ red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) -> UIColor      init(CGColor cgColor: CGColor)     class func colorWithCGColor(_ cgColor: CGColor) -> UIColor      init(patternImage image: UIImage)     class func colorWithPatternImage(_ image: UIImage) -> UIColor     init(white white: CGFloat, alpha alpha: CGFloat)     init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     init(CGColor cgColor: CGColor)     init(patternImage image: UIImage)     class func blackColor() -> UIColor     class func darkGrayColor() -> UIColor     class func lightGrayColor() -> UIColor     class func whiteColor() -> UIColor     class func grayColor() -> UIColor     class func redColor() -> UIColor     class func greenColor() -> UIColor     class func blueColor() -> UIColor     class func cyanColor() -> UIColor     class func yellowColor() -> UIColor     class func magentaColor() -> UIColor     class func orangeColor() -> UIColor     class func purpleColor() -> UIColor     class func brownColor() -> UIColor     class func clearColor() -> UIColor     func set()     func setFill()     func setStroke()     func getWhite(_ white: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getHue(_ hue: UnsafeMutablePointer<CGFloat>, saturation saturation: UnsafeMutablePointer<CGFloat>, brightness brightness: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getRed(_ red: UnsafeMutablePointer<CGFloat>, green green: UnsafeMutablePointer<CGFloat>, blue blue: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func colorWithAlphaComponent(_ alpha: CGFloat) -> UIColor     var CGColor: CGColor { get } } extension UIColor : _ColorLiteralConvertible {     required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float) } extension UIColor : _ColorLiteralConvertible {     required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float) } ``` | NSCopying, NSSecureCoding |

Modified [UIFont](https://developer.apple.com/documentation/uikit/uifont)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIFontDescriptor : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init()     init?(coder aDecoder: NSCoder)     var postscriptName: String { get }     var pointSize: CGFloat { get }     var matrix: CGAffineTransform { get }     var symbolicTraits: UIFontDescriptorSymbolicTraits { get }     func objectForKey(_ anAttribute: String) -> AnyObject?     func fontAttributes() -> [String : AnyObject]     func matchingFontDescriptorsWithMandatoryKeys(_ mandatoryKeys: Set<String>?) -> [UIFontDescriptor]      init(fontAttributes attributes: [String : AnyObject])     class func fontDescriptorWithFontAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor      init(name fontName: String, size size: CGFloat)     class func fontDescriptorWithName(_ fontName: String, size size: CGFloat) -> UIFontDescriptor      init(name fontName: String, matrix matrix: CGAffineTransform)     class func fontDescriptorWithName(_ fontName: String, matrix matrix: CGAffineTransform) -> UIFontDescriptor     class func preferredFontDescriptorWithTextStyle(_ style: String) -> UIFontDescriptor     init(fontAttributes attributes: [String : AnyObject])     func fontDescriptorByAddingAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor     func fontDescriptorWithSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor     func fontDescriptorWithSize(_ newPointSize: CGFloat) -> UIFontDescriptor     func fontDescriptorWithMatrix(_ matrix: CGAffineTransform) -> UIFontDescriptor     func fontDescriptorWithFace(_ newFace: String) -> UIFontDescriptor     func fontDescriptorWithFamily(_ newFamily: String) -> UIFontDescriptor } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class UIFontDescriptor : NSObject, NSCopying, NSSecureCoding {     convenience init()     init?(coder aDecoder: NSCoder)     var postscriptName: String { get }     var pointSize: CGFloat { get }     var matrix: CGAffineTransform { get }     var symbolicTraits: UIFontDescriptorSymbolicTraits { get }     func objectForKey(_ anAttribute: String) -> AnyObject?     func fontAttributes() -> [String : AnyObject]     func matchingFontDescriptorsWithMandatoryKeys(_ mandatoryKeys: Set<String>?) -> [UIFontDescriptor]      init(fontAttributes attributes: [String : AnyObject])     class func fontDescriptorWithFontAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor      init(name fontName: String, size size: CGFloat)     class func fontDescriptorWithName(_ fontName: String, size size: CGFloat) -> UIFontDescriptor      init(name fontName: String, matrix matrix: CGAffineTransform)     class func fontDescriptorWithName(_ fontName: String, matrix matrix: CGAffineTransform) -> UIFontDescriptor     class func preferredFontDescriptorWithTextStyle(_ style: String) -> UIFontDescriptor     init(fontAttributes attributes: [String : AnyObject])     func fontDescriptorByAddingAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor     func fontDescriptorWithSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor     func fontDescriptorWithSize(_ newPointSize: CGFloat) -> UIFontDescriptor     func fontDescriptorWithMatrix(_ matrix: CGAffineTransform) -> UIFontDescriptor     func fontDescriptorWithFace(_ newFace: String) -> UIFontDescriptor     func fontDescriptorWithFamily(_ newFamily: String) -> UIFontDescriptor } ``` | NSCopying, NSSecureCoding |

Modified [UIImage](https://developer.apple.com/documentation/uikit/uiimage)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIImage : NSObject, NSSecureCoding, NSCoding {      init?(named name: String)     class func imageNamed(_ name: String) -> UIImage?      init?(contentsOfFile path: String)     class func imageWithContentsOfFile(_ path: String) -> UIImage?      init?(data data: NSData)     class func imageWithData(_ data: NSData) -> UIImage?      init?(data data: NSData, scale scale: CGFloat)     class func imageWithData(_ data: NSData, scale scale: CGFloat) -> UIImage?      init(CGImage cgImage: CGImage)     class func imageWithCGImage(_ cgImage: CGImage) -> UIImage      init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     class func imageWithCGImage(_ cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage     init?(contentsOfFile path: String)     init?(data data: NSData)     init?(data data: NSData, scale scale: CGFloat)     init(CGImage cgImage: CGImage)     init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     var size: CGSize { get }     var CGImage: CGImage? { get }     var imageOrientation: UIImageOrientation { get }     var scale: CGFloat { get }     class func animatedImageNamed(_ name: String, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: NSTimeInterval) -> UIImage?     class func animatedImageWithImages(_ images: [UIImage], duration duration: NSTimeInterval) -> UIImage?     var images: [UIImage]? { get }     var duration: NSTimeInterval { get }     func drawAtPoint(_ point: CGPoint)     func drawAtPoint(_ point: CGPoint, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawInRect(_ rect: CGRect)     func drawInRect(_ rect: CGRect, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawAsPatternInRect(_ rect: CGRect)     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets) -> UIImage     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode) -> UIImage     var capInsets: UIEdgeInsets { get }     var resizingMode: UIImageResizingMode { get }     func imageWithAlignmentRectInsets(_ alignmentInsets: UIEdgeInsets) -> UIImage     var alignmentRectInsets: UIEdgeInsets { get }     func imageWithRenderingMode(_ renderingMode: UIImageRenderingMode) -> UIImage     var renderingMode: UIImageRenderingMode { get }     func imageFlippedForRightToLeftLayoutDirection() -> UIImage     var flipsForRightToLeftLayoutDirection: Bool { get } } extension UIImage {     func stretchableImageWithLeftCapWidth(_ leftCapWidth: Int, topCapHeight topCapHeight: Int) -> UIImage     var leftCapWidth: Int { get }     var topCapHeight: Int { get } } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class UIImage : NSObject, NSSecureCoding {      init?(named name: String)     class func imageNamed(_ name: String) -> UIImage?      init?(contentsOfFile path: String)     class func imageWithContentsOfFile(_ path: String) -> UIImage?      init?(data data: NSData)     class func imageWithData(_ data: NSData) -> UIImage?      init?(data data: NSData, scale scale: CGFloat)     class func imageWithData(_ data: NSData, scale scale: CGFloat) -> UIImage?      init(CGImage cgImage: CGImage)     class func imageWithCGImage(_ cgImage: CGImage) -> UIImage      init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     class func imageWithCGImage(_ cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage     init?(contentsOfFile path: String)     init?(data data: NSData)     init?(data data: NSData, scale scale: CGFloat)     init(CGImage cgImage: CGImage)     init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     var size: CGSize { get }     var CGImage: CGImage? { get }     var imageOrientation: UIImageOrientation { get }     var scale: CGFloat { get }     class func animatedImageNamed(_ name: String, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: NSTimeInterval) -> UIImage?     class func animatedImageWithImages(_ images: [UIImage], duration duration: NSTimeInterval) -> UIImage?     var images: [UIImage]? { get }     var duration: NSTimeInterval { get }     func drawAtPoint(_ point: CGPoint)     func drawAtPoint(_ point: CGPoint, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawInRect(_ rect: CGRect)     func drawInRect(_ rect: CGRect, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawAsPatternInRect(_ rect: CGRect)     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets) -> UIImage     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode) -> UIImage     var capInsets: UIEdgeInsets { get }     var resizingMode: UIImageResizingMode { get }     func imageWithAlignmentRectInsets(_ alignmentInsets: UIEdgeInsets) -> UIImage     var alignmentRectInsets: UIEdgeInsets { get }     func imageWithRenderingMode(_ renderingMode: UIImageRenderingMode) -> UIImage     var renderingMode: UIImageRenderingMode { get }     func imageFlippedForRightToLeftLayoutDirection() -> UIImage     var flipsForRightToLeftLayoutDirection: Bool { get } } extension UIImage : _ImageLiteralConvertible {     required convenience init(imageLiteral name: String) } extension UIImage {     func stretchableImageWithLeftCapWidth(_ leftCapWidth: Int, topCapHeight topCapHeight: Int) -> UIImage     var leftCapWidth: Int { get }     var topCapHeight: Int { get } } extension UIImage : _ImageLiteralConvertible {     required convenience init(imageLiteral name: String) } ``` | NSSecureCoding |

Modified [UIImageOrientation [enum]](https://developer.apple.com/documentation/uikit/uiimageorientation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIImageRenderingMode [enum]](https://developer.apple.com/documentation/uikit/uiimage/renderingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIImageResizingMode [enum]](https://developer.apple.com/documentation/uikit/uiimageresizingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UILocalNotification](https://developer.apple.com/documentation/uikit/uilocalnotification)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

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
