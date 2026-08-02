---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Swift/UIKit.html
archived_at: '2026-07-18T02:58:35.537862Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# UIKit Changes for Swift

### UIKit

Removed [NSParagraphStyle.defaultParagraphStyle() -> NSParagraphStyle [class]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1532681-default)Removed [NSValue.CGAffineTransformValue() -> CGAffineTransform](https://developer.apple.com/documentation/foundation/nsvalue/1624512-cgaffinetransformvalue)Removed [NSValue.CGPointValue() -> CGPoint](https://developer.apple.com/documentation/foundation/nsvalue/1624534-cgpointvalue)Removed [NSValue.CGRectValue() -> CGRect](https://developer.apple.com/documentation/foundation/nsvalue/1624506-cgrectvalue)Removed [NSValue.CGSizeValue() -> CGSize](https://developer.apple.com/documentation/foundation/nsvalue/1624489-cgsizevalue)Removed [NSValue.CGVectorValue() -> CGVector](https://developer.apple.com/documentation/foundation/nsvalue/1624486-cgvectorvalue)Removed [NSValue.UIEdgeInsetsValue() -> UIEdgeInsets](https://developer.apple.com/documentation/foundation/nsvalue/1624517-uiedgeinsetsvalue)Removed [NSValue.UIOffsetValue() -> UIOffset](https://developer.apple.com/documentation/foundation/nsvalue/1624526-uioffsetvalue)Removed [UIColor.blackColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621929-blackcolor)Removed [UIColor.blueColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621947-bluecolor)Removed [UIColor.brownColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621950-brown)Removed [UIColor.clearColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621945-clearcolor)Removed [UIColor.cyanColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621942-cyan)Removed [UIColor.darkGrayColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621952-darkgraycolor)Removed [UIColor.grayColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621941-gray)Removed [UIColor.greenColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621946-greencolor)Removed [UIColor.lightGrayColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621932-lightgraycolor)Removed [UIColor.magentaColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621934-magentacolor)Removed [UIColor.orangeColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621956-orangecolor)Removed [UIColor.purpleColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621923-purplecolor)Removed [UIColor.redColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621924-red)Removed [UIColor.whiteColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621920-whitecolor)Removed [UIColor.yellowColor() -> UIColor [class]](https://developer.apple.com/documentation/uikit/uicolor/1621953-yellow)Removed [UIFont.familyNames() -> [String] [class]](https://developer.apple.com/documentation/uikit/uifont/1619040-familynames)Removed [UIFont.fontDescriptor() -> UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifont/1619037-fontdescriptor)Removed [UIFontDescriptor.fontAttributes() -> [String : AnyObject]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616698-fontattributes)Removed [UIFontDescriptorSymbolicTraits.ClassUnknown](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptorclassunknown)Removed UIImage.init(imageLiteral: String)Removed [UIRectEdge.None](https://developer.apple.com/documentation/uikit/uirectedge/uirectedgenone)Removed [UIEdgeInsetsZero](https://developer.apple.com/documentation/uikit/uiedgeinsets/1624518-zero)Removed [UIOffsetZero](https://developer.apple.com/documentation/uikit/uioffset/1624501-zero)Added [IndexPath.init(item: Int, section: Int)](https://developer.apple.com/documentation/foundation/indexpath/1924279-init)Added [IndexPath.init(row: Int, section: Int)](https://developer.apple.com/documentation/foundation/indexpath/1779555-init)Added [IndexPath.item](https://developer.apple.com/documentation/foundation/indexpath/1779557-item)Added [IndexPath.row](https://developer.apple.com/documentation/foundation/indexpath/1779554-row)Added [IndexPath.section](https://developer.apple.com/documentation/foundation/indexpath/1779112-section)Added [NSParagraphStyle.default](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1532681-default)Added [NSValue.cgAffineTransformValue](https://developer.apple.com/documentation/foundation/nsvalue/1624512-cgaffinetransformvalue)Added [NSValue.cgPointValue](https://developer.apple.com/documentation/foundation/nsvalue/1624534-cgpointvalue)Added [NSValue.cgRectValue](https://developer.apple.com/documentation/foundation/nsvalue/1624506-cgrectvalue)Added [NSValue.cgSizeValue](https://developer.apple.com/documentation/foundation/nsvalue/1624489-cgsizevalue)Added [NSValue.cgVectorValue](https://developer.apple.com/documentation/foundation/nsvalue/1624486-cgvectorvalue)Added [NSValue.uiEdgeInsetsValue](https://developer.apple.com/documentation/foundation/nsvalue/1624517-uiedgeinsetsvalue)Added [NSValue.uiOffsetValue](https://developer.apple.com/documentation/foundation/nsvalue/1624526-uioffsetvalue)Added [UIColor.black](https://developer.apple.com/documentation/uikit/uicolor/1621929-black)Added [UIColor.blue](https://developer.apple.com/documentation/uikit/uicolor/1621947-bluecolor)Added [UIColor.brown](https://developer.apple.com/documentation/uikit/uicolor/1621950-browncolor)Added [UIColor.clear](https://developer.apple.com/documentation/uikit/uicolor/1621945-clear)Added [UIColor.cyan](https://developer.apple.com/documentation/uikit/uicolor/1621942-cyan)Added [UIColor.darkGray](https://developer.apple.com/documentation/uikit/uicolor/1621952-darkgraycolor)Added [UIColor.gray](https://developer.apple.com/documentation/uikit/uicolor/1621941-graycolor)Added [UIColor.green](https://developer.apple.com/documentation/uikit/uicolor/1621946-greencolor)Added [UIColor.init(displayP3Red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](https://developer.apple.com/documentation/uikit/uicolor/1648568-init)Added [UIColor.lightGray](https://developer.apple.com/documentation/uikit/uicolor/1621932-lightgray)Added [UIColor.magenta](https://developer.apple.com/documentation/uikit/uicolor/1621934-magentacolor)Added [UIColor.orange](https://developer.apple.com/documentation/uikit/uicolor/1621956-orange)Added [UIColor.purple](https://developer.apple.com/documentation/uikit/uicolor/1621923-purple)Added [UIColor.red](https://developer.apple.com/documentation/uikit/uicolor/1621924-redcolor)Added [UIColor.white](https://developer.apple.com/documentation/uikit/uicolor/1621920-whitecolor)Added [UIColor.yellow](https://developer.apple.com/documentation/uikit/uicolor/1621953-yellowcolor)Added UIEdgeInsets.zeroAdded [UIFont.familyNames](https://developer.apple.com/documentation/uikit/uifont/1619040-familynames)Added [UIFont.fontDescriptor](https://developer.apple.com/documentation/uikit/uifont/1619037-fontdescriptor)Added [UIFont.preferredFont(forTextStyle: UIFontTextStyle, compatibleWith: UITraitCollection?) -> UIFont [class]](https://developer.apple.com/documentation/uikit/uifont/1771762-preferredfontfortextstyle)Added [UIFontDescriptor.fontAttributes](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616698-fontattributes)Added [UIFontDescriptor.preferredFontDescriptor(withTextStyle: UIFontTextStyle, compatibleWith: UITraitCollection?) -> UIFontDescriptor [class]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1771750-preferredfontdescriptorwithtexts)Added [UIFontTextStyle [struct]](https://developer.apple.com/documentation/uikit/uifonttextstyle)Added UIFontTextStyle.init(_: String)Added [UIFontTextStyle.init(rawValue: String)](https://developer.apple.com/documentation/uikit/uifont/textstyle/2427160-init)Added [UIImage.init(imageLiteralResourceName: String)](https://developer.apple.com/documentation/uikit/uiimage/1849766-init)Added [UIImage.withHorizontallyFlippedOrientation() -> UIImage](https://developer.apple.com/documentation/uikit/uiimage/2113668-imagewithhorizontallyflippedorie)Added UIOffset.zeroAdded URLResourceValues.thumbnailDictionaryAdded [UIAccessibilityTraitTabBar](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits/1648592-tabbar)Modified [NSAttributedString.boundingRect(with: CGSize, options: NSStringDrawingOptions, context: NSStringDrawingContext?) -> CGRect](https://developer.apple.com/documentation/foundation/nsattributedstring/1529154-boundingrectwithsize)

|  | Declaration |
| --- | --- |
| From | ``` func boundingRectWithSize(_ size: CGSize, options options: NSStringDrawingOptions, context context: NSStringDrawingContext?) -> CGRect ``` |
| To | ``` func boundingRect(with size: CGSize, options options: NSStringDrawingOptions = [], context context: NSStringDrawingContext?) -> CGRect ``` |

Modified [NSAttributedString.containsAttachments(in: NSRange) -> Bool](https://developer.apple.com/documentation/foundation/nsattributedstring/1525086-containsattachments)

|  | Declaration |
| --- | --- |
| From | ``` func containsAttachmentsInRange(_ range: NSRange) -> Bool ``` |
| To | ``` func containsAttachments(in range: NSRange) -> Bool ``` |

Modified [NSAttributedString.data(from: NSRange, documentAttributes: [String : Any]) throws -> Data](https://developer.apple.com/documentation/foundation/nsattributedstring/1534090-data)

|  | Declaration |
| --- | --- |
| From | ``` func dataFromRange(_ range: NSRange, documentAttributes dict: [String : AnyObject]) throws -> NSData ``` |
| To | ``` func data(from range: NSRange, documentAttributes dict: [String : Any] = [:]) throws -> Data ``` |

Modified [NSAttributedString.draw(at: CGPoint)](https://developer.apple.com/documentation/foundation/nsattributedstring/1529478-drawatpoint)

|  | Declaration |
| --- | --- |
| From | ``` func drawAtPoint(_ point: CGPoint) ``` |
| To | ``` func draw(at point: CGPoint) ``` |

Modified [NSAttributedString.draw(in: CGRect)](https://developer.apple.com/documentation/foundation/nsattributedstring/1531631-drawinrect)

|  | Declaration |
| --- | --- |
| From | ``` func drawInRect(_ rect: CGRect) ``` |
| To | ``` func draw(in rect: CGRect) ``` |

Modified [NSAttributedString.draw(with: CGRect, options: NSStringDrawingOptions, context: NSStringDrawingContext?)](https://developer.apple.com/documentation/foundation/nsattributedstring/1524971-draw)

|  | Declaration |
| --- | --- |
| From | ``` func drawWithRect(_ rect: CGRect, options options: NSStringDrawingOptions, context context: NSStringDrawingContext?) ``` |
| To | ``` func draw(with rect: CGRect, options options: NSStringDrawingOptions = [], context context: NSStringDrawingContext?) ``` |

Modified [NSAttributedString.fileWrapper(from: NSRange, documentAttributes: [String : Any]) throws -> FileWrapper](https://developer.apple.com/documentation/foundation/nsattributedstring/1530461-filewrapperfromrange)

|  | Declaration |
| --- | --- |
| From | ``` func fileWrapperFromRange(_ range: NSRange, documentAttributes dict: [String : AnyObject]) throws -> NSFileWrapper ``` |
| To | ``` func fileWrapper(from range: NSRange, documentAttributes dict: [String : Any] = [:]) throws -> FileWrapper ``` |

Modified [NSAttributedString.init(data: Data, options: [String : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](https://developer.apple.com/documentation/foundation/nsattributedstring/1524613-init)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData, options options: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws ``` |
| To | ``` init(data data: Data, options options: [String : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws ``` |

Modified [NSAttributedString.init(fileURL: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](https://developer.apple.com/documentation/foundation/nsattributedstring/1620492-init)

|  | Declaration |
| --- | --- |
| From | ``` init(fileURL url: NSURL, options options: [NSObject : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws ``` |
| To | ``` init(fileURL url: URL, options options: [AnyHashable : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws ``` |

Modified [NSAttributedString.init(url: URL, options: [String : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](https://developer.apple.com/documentation/foundation/nsattributedstring/1530490-init)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL, options options: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws ``` |
| To | ``` init(url url: URL, options options: [String : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws ``` |

Modified [NSCoder.decodeCGAffineTransform(forKey: String) -> CGAffineTransform](https://developer.apple.com/documentation/foundation/nscoder/1624478-decodecgaffinetransformforkey)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCGAffineTransformForKey(_ key: String) -> CGAffineTransform ``` |
| To | ``` func decodeCGAffineTransform(forKey key: String) -> CGAffineTransform ``` |

Modified [NSCoder.decodeCGPoint(forKey: String) -> CGPoint](https://developer.apple.com/documentation/foundation/nscoder/1624523-decodecgpointforkey)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCGPointForKey(_ key: String) -> CGPoint ``` |
| To | ``` func decodeCGPoint(forKey key: String) -> CGPoint ``` |

Modified [NSCoder.decodeCGRect(forKey: String) -> CGRect](https://developer.apple.com/documentation/foundation/nscoder/1624522-decodecgrect)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCGRectForKey(_ key: String) -> CGRect ``` |
| To | ``` func decodeCGRect(forKey key: String) -> CGRect ``` |

Modified [NSCoder.decodeCGSize(forKey: String) -> CGSize](https://developer.apple.com/documentation/foundation/nscoder/1624519-decodecgsizeforkey)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCGSizeForKey(_ key: String) -> CGSize ``` |
| To | ``` func decodeCGSize(forKey key: String) -> CGSize ``` |

Modified [NSCoder.decodeCGVector(forKey: String) -> CGVector](https://developer.apple.com/documentation/foundation/nscoder/1624488-decodecgvectorforkey)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCGVectorForKey(_ key: String) -> CGVector ``` |
| To | ``` func decodeCGVector(forKey key: String) -> CGVector ``` |

Modified [NSCoder.decodeUIEdgeInsets(forKey: String) -> UIEdgeInsets](https://developer.apple.com/documentation/foundation/nscoder/1624492-decodeuiedgeinsetsforkey)

|  | Declaration |
| --- | --- |
| From | ``` func decodeUIEdgeInsetsForKey(_ key: String) -> UIEdgeInsets ``` |
| To | ``` func decodeUIEdgeInsets(forKey key: String) -> UIEdgeInsets ``` |

Modified [NSCoder.decodeUIOffset(forKey: String) -> UIOffset](https://developer.apple.com/documentation/foundation/nscoder/1624507-decodeuioffset)

|  | Declaration |
| --- | --- |
| From | ``` func decodeUIOffsetForKey(_ key: String) -> UIOffset ``` |
| To | ``` func decodeUIOffset(forKey key: String) -> UIOffset ``` |

Modified [NSCoder.encode(_: UIEdgeInsets, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624481-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeUIEdgeInsets(_ insets: UIEdgeInsets, forKey key: String) ``` |
| To | ``` func encode(_ insets: UIEdgeInsets, forKey key: String) ``` |

Modified [NSCoder.encode(_: CGVector, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624532-encodecgvector)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCGVector(_ vector: CGVector, forKey key: String) ``` |
| To | ``` func encode(_ vector: CGVector, forKey key: String) ``` |

Modified [NSCoder.encode(_: CGAffineTransform, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624502-encodecgaffinetransform)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCGAffineTransform(_ transform: CGAffineTransform, forKey key: String) ``` |
| To | ``` func encode(_ transform: CGAffineTransform, forKey key: String) ``` |

Modified [NSCoder.encode(_: CGPoint, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624520-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCGPoint(_ point: CGPoint, forKey key: String) ``` |
| To | ``` func encode(_ point: CGPoint, forKey key: String) ``` |

Modified [NSCoder.encode(_: CGRect, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624472-encodecgrect)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCGRect(_ rect: CGRect, forKey key: String) ``` |
| To | ``` func encode(_ rect: CGRect, forKey key: String) ``` |

Modified [NSCoder.encode(_: UIOffset, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624494-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeUIOffset(_ offset: UIOffset, forKey key: String) ``` |
| To | ``` func encode(_ offset: UIOffset, forKey key: String) ``` |

Modified [NSCoder.encode(_: CGSize, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624482-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCGSize(_ size: CGSize, forKey key: String) ``` |
| To | ``` func encode(_ size: CGSize, forKey key: String) ``` |

Modified [NSLineBreakMode [enum]](https://developer.apple.com/documentation/uikit/nslinebreakmode)

|  | Declaration |
| --- | --- |
| From | ``` enum NSLineBreakMode : Int {     case ByWordWrapping     case ByCharWrapping     case ByClipping     case ByTruncatingHead     case ByTruncatingTail     case ByTruncatingMiddle } ``` |
| To | ``` enum NSLineBreakMode : Int {     case byWordWrapping     case byCharWrapping     case byClipping     case byTruncatingHead     case byTruncatingTail     case byTruncatingMiddle } ``` |

Modified [NSLineBreakMode.byCharWrapping](https://developer.apple.com/documentation/uikit/nslinebreakmode/nslinebreakbycharwrapping)

|  | Declaration |
| --- | --- |
| From | ``` case ByCharWrapping ``` |
| To | ``` case byCharWrapping ``` |

Modified [NSLineBreakMode.byClipping](https://developer.apple.com/documentation/uikit/nslinebreakmode/byclipping)

|  | Declaration |
| --- | --- |
| From | ``` case ByClipping ``` |
| To | ``` case byClipping ``` |

Modified [NSLineBreakMode.byTruncatingHead](https://developer.apple.com/documentation/appkit/nslinebreakmode/nslinebreakbytruncatinghead)

|  | Declaration |
| --- | --- |
| From | ``` case ByTruncatingHead ``` |
| To | ``` case byTruncatingHead ``` |

Modified [NSLineBreakMode.byTruncatingMiddle](https://developer.apple.com/documentation/uikit/nslinebreakmode/nslinebreakbytruncatingmiddle)

|  | Declaration |
| --- | --- |
| From | ``` case ByTruncatingMiddle ``` |
| To | ``` case byTruncatingMiddle ``` |

Modified [NSLineBreakMode.byTruncatingTail](https://developer.apple.com/documentation/uikit/nslinebreakmode/nslinebreakbytruncatingtail)

|  | Declaration |
| --- | --- |
| From | ``` case ByTruncatingTail ``` |
| To | ``` case byTruncatingTail ``` |

Modified [NSLineBreakMode.byWordWrapping](https://developer.apple.com/documentation/appkit/nsparagraphstyle/nslinebreakmode/bywordwrapping)

|  | Declaration |
| --- | --- |
| From | ``` case ByWordWrapping ``` |
| To | ``` case byWordWrapping ``` |

Modified [NSMutableAttributedString.fixAttributes(in: NSRange)](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1533823-fixattributesinrange)

|  | Declaration |
| --- | --- |
| From | ``` func fixAttributesInRange(_ range: NSRange) ``` |
| To | ``` func fixAttributes(in range: NSRange) ``` |

Modified [NSMutableAttributedString.read(from: Data, options: [String : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1535465-read)

|  | Declaration |
| --- | --- |
| From | ``` func readFromData(_ data: NSData, options opts: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws ``` |
| To | ``` func read(from data: Data, options opts: [String : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws ``` |

Modified [NSMutableAttributedString.read(from: URL, options: [String : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1524892-readfromurl)

|  | Declaration |
| --- | --- |
| From | ``` func readFromURL(_ url: NSURL, options opts: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws ``` |
| To | ``` func read(from url: URL, options opts: [String : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws ``` |

Modified [NSMutableAttributedString.read(fromFileURL: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1620496-readfromfileurl)

|  | Declaration |
| --- | --- |
| From | ``` func readFromFileURL(_ url: NSURL, options opts: [NSObject : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws ``` |
| To | ``` func read(fromFileURL url: URL, options opts: [AnyHashable : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws ``` |

Modified [NSNotification.Name.UIAccessibilityAnnouncementDidFinish](https://developer.apple.com/documentation/uikit/uiaccessibilityannouncementdidfinishnotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | UIAccessibilityAnnouncementDidFinishNotification | ``` let UIAccessibilityAnnouncementDidFinishNotification: String ``` |
| To | UIAccessibilityAnnouncementDidFinish | ``` static let UIAccessibilityAnnouncementDidFinish: NSNotification.Name ``` |

Modified [NSNotification.Name.UIAccessibilityElementFocused](https://developer.apple.com/documentation/uikit/uiaccessibility/1620210-elementfocusednotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | UIAccessibilityElementFocusedNotification | ``` let UIAccessibilityElementFocusedNotification: String ``` |
| To | UIAccessibilityElementFocused | ``` static let UIAccessibilityElementFocused: NSNotification.Name ``` |

Modified [NSParagraphStyle](https://developer.apple.com/documentation/uikit/nsparagraphstyle)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSParagraphStyle : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     class func defaultParagraphStyle() -> NSParagraphStyle     class func defaultWritingDirectionForLanguage(_ languageName: String?) -> NSWritingDirection     var lineSpacing: CGFloat { get }     var paragraphSpacing: CGFloat { get }     var alignment: NSTextAlignment { get }     var headIndent: CGFloat { get }     var tailIndent: CGFloat { get }     var firstLineHeadIndent: CGFloat { get }     var minimumLineHeight: CGFloat { get }     var maximumLineHeight: CGFloat { get }     var lineBreakMode: NSLineBreakMode { get }     var baseWritingDirection: NSWritingDirection { get }     var lineHeightMultiple: CGFloat { get }     var paragraphSpacingBefore: CGFloat { get }     var hyphenationFactor: Float { get }     var tabStops: [NSTextTab] { get }     var defaultTabInterval: CGFloat { get }     var allowsDefaultTighteningForTruncation: Bool { get } } ``` | NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class NSParagraphStyle : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     class var `default`: NSParagraphStyle { get }     class func defaultWritingDirection(forLanguage languageName: String?) -> NSWritingDirection     var lineSpacing: CGFloat { get }     var paragraphSpacing: CGFloat { get }     var alignment: NSTextAlignment { get }     var headIndent: CGFloat { get }     var tailIndent: CGFloat { get }     var firstLineHeadIndent: CGFloat { get }     var minimumLineHeight: CGFloat { get }     var maximumLineHeight: CGFloat { get }     var lineBreakMode: NSLineBreakMode { get }     var baseWritingDirection: NSWritingDirection { get }     var lineHeightMultiple: CGFloat { get }     var paragraphSpacingBefore: CGFloat { get }     var hyphenationFactor: Float { get }     var tabStops: [NSTextTab] { get }     var defaultTabInterval: CGFloat { get }     var allowsDefaultTighteningForTruncation: Bool { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSParagraphStyle : CVarArg { } extension NSParagraphStyle : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying, NSSecureCoding |

Modified [NSParagraphStyle.defaultWritingDirection(forLanguage: String?) -> NSWritingDirection [class]](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1535327-defaultwritingdirection)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultWritingDirectionForLanguage(_ languageName: String?) -> NSWritingDirection ``` |
| To | ``` class func defaultWritingDirection(forLanguage languageName: String?) -> NSWritingDirection ``` |

Modified [NSString.boundingRect(with: CGSize, options: NSStringDrawingOptions, attributes: [String : Any]?, context: NSStringDrawingContext?) -> CGRect](https://developer.apple.com/documentation/foundation/nsstring/1524729-boundingrect)

|  | Declaration |
| --- | --- |
| From | ``` func boundingRectWithSize(_ size: CGSize, options options: NSStringDrawingOptions, attributes attributes: [String : AnyObject]?, context context: NSStringDrawingContext?) -> CGRect ``` |
| To | ``` func boundingRect(with size: CGSize, options options: NSStringDrawingOptions = [], attributes attributes: [String : Any]? = nil, context context: NSStringDrawingContext?) -> CGRect ``` |

Modified [NSString.draw(at: CGPoint, withAttributes: [String : Any]?)](https://developer.apple.com/documentation/foundation/nsstring/1533109-draw)

|  | Declaration |
| --- | --- |
| From | ``` func drawAtPoint(_ point: CGPoint, withAttributes attrs: [String : AnyObject]?) ``` |
| To | ``` func draw(at point: CGPoint, withAttributes attrs: [String : Any]? = nil) ``` |

Modified [NSString.draw(in: CGRect, withAttributes: [String : Any]?)](https://developer.apple.com/documentation/foundation/nsstring/1529855-drawinrect)

|  | Declaration |
| --- | --- |
| From | ``` func drawInRect(_ rect: CGRect, withAttributes attrs: [String : AnyObject]?) ``` |
| To | ``` func draw(in rect: CGRect, withAttributes attrs: [String : Any]? = nil) ``` |

Modified [NSString.draw(with: CGRect, options: NSStringDrawingOptions, attributes: [String : Any]?, context: NSStringDrawingContext?)](https://developer.apple.com/documentation/foundation/nsstring/1530195-drawwithrect)

|  | Declaration |
| --- | --- |
| From | ``` func drawWithRect(_ rect: CGRect, options options: NSStringDrawingOptions, attributes attributes: [String : AnyObject]?, context context: NSStringDrawingContext?) ``` |
| To | ``` func draw(with rect: CGRect, options options: NSStringDrawingOptions = [], attributes attributes: [String : Any]? = nil, context context: NSStringDrawingContext?) ``` |

Modified [NSString.size(attributes: [String : Any]?) -> CGSize](https://developer.apple.com/documentation/foundation/nsstring/1531844-sizewithattributes)

|  | Declaration |
| --- | --- |
| From | ``` func sizeWithAttributes(_ attrs: [String : AnyObject]?) -> CGSize ``` |
| To | ``` func size(attributes attrs: [String : Any]? = nil) -> CGSize ``` |

Modified [NSStringDrawingContext](https://developer.apple.com/documentation/appkit/nsstringdrawingcontext)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSStringDrawingContext : NSObject {     var minimumScaleFactor: CGFloat     var actualScaleFactor: CGFloat { get }     var totalBounds: CGRect { get } } extension NSStringDrawingContext {     var minimumTrackingAdjustment: CGFloat     var actualTrackingAdjustment: CGFloat { get } } ``` | -- |
| To | ``` class NSStringDrawingContext : NSObject {     var minimumScaleFactor: CGFloat     var actualScaleFactor: CGFloat { get }     var totalBounds: CGRect { get }     var minimumTrackingAdjustment: CGFloat     var actualTrackingAdjustment: CGFloat { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSStringDrawingContext : CVarArg { } extension NSStringDrawingContext : Equatable, Hashable {     var hashValue: Int { get } } extension NSStringDrawingContext {     var minimumTrackingAdjustment: CGFloat     var actualTrackingAdjustment: CGFloat { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSStringDrawingOptions [struct]](https://developer.apple.com/documentation/uikit/nsstringdrawingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSStringDrawingOptions : OptionSetType {     init(rawValue rawValue: Int)     static var UsesLineFragmentOrigin: NSStringDrawingOptions { get }     static var UsesFontLeading: NSStringDrawingOptions { get }     static var UsesDeviceMetrics: NSStringDrawingOptions { get }     static var TruncatesLastVisibleLine: NSStringDrawingOptions { get } } ``` | OptionSetType |
| To | ``` struct NSStringDrawingOptions : OptionSet {     init(rawValue rawValue: Int)     static var usesLineFragmentOrigin: NSStringDrawingOptions { get }     static var usesFontLeading: NSStringDrawingOptions { get }     static var usesDeviceMetrics: NSStringDrawingOptions { get }     static var truncatesLastVisibleLine: NSStringDrawingOptions { get }     func intersect(_ other: NSStringDrawingOptions) -> NSStringDrawingOptions     func exclusiveOr(_ other: NSStringDrawingOptions) -> NSStringDrawingOptions     mutating func unionInPlace(_ other: NSStringDrawingOptions)     mutating func intersectInPlace(_ other: NSStringDrawingOptions)     mutating func exclusiveOrInPlace(_ other: NSStringDrawingOptions)     func isSubsetOf(_ other: NSStringDrawingOptions) -> Bool     func isDisjointWith(_ other: NSStringDrawingOptions) -> Bool     func isSupersetOf(_ other: NSStringDrawingOptions) -> Bool     mutating func subtractInPlace(_ other: NSStringDrawingOptions)     func isStrictSupersetOf(_ other: NSStringDrawingOptions) -> Bool     func isStrictSubsetOf(_ other: NSStringDrawingOptions) -> Bool } extension NSStringDrawingOptions {     func union(_ other: NSStringDrawingOptions) -> NSStringDrawingOptions     func intersection(_ other: NSStringDrawingOptions) -> NSStringDrawingOptions     func symmetricDifference(_ other: NSStringDrawingOptions) -> NSStringDrawingOptions } extension NSStringDrawingOptions {     func contains(_ member: NSStringDrawingOptions) -> Bool     mutating func insert(_ newMember: NSStringDrawingOptions) -> (inserted: Bool, memberAfterInsert: NSStringDrawingOptions)     mutating func remove(_ member: NSStringDrawingOptions) -> NSStringDrawingOptions?     mutating func update(with newMember: NSStringDrawingOptions) -> NSStringDrawingOptions? } extension NSStringDrawingOptions {     convenience init()     mutating func formUnion(_ other: NSStringDrawingOptions)     mutating func formIntersection(_ other: NSStringDrawingOptions)     mutating func formSymmetricDifference(_ other: NSStringDrawingOptions) } extension NSStringDrawingOptions {     convenience init<S : Sequence where S.Iterator.Element == NSStringDrawingOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: NSStringDrawingOptions...)     mutating func subtract(_ other: NSStringDrawingOptions)     func isSubset(of other: NSStringDrawingOptions) -> Bool     func isSuperset(of other: NSStringDrawingOptions) -> Bool     func isDisjoint(with other: NSStringDrawingOptions) -> Bool     func subtracting(_ other: NSStringDrawingOptions) -> NSStringDrawingOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: NSStringDrawingOptions) -> Bool     func isStrictSubset(of other: NSStringDrawingOptions) -> Bool } ``` | OptionSet |

Modified [NSStringDrawingOptions.truncatesLastVisibleLine](https://developer.apple.com/documentation/foundation/nsstring/nsstringdrawingoptions/1527952-truncateslastvisibleline)

|  | Declaration |
| --- | --- |
| From | ``` static var TruncatesLastVisibleLine: NSStringDrawingOptions { get } ``` |
| To | ``` static var truncatesLastVisibleLine: NSStringDrawingOptions { get } ``` |

Modified [NSStringDrawingOptions.usesDeviceMetrics](https://developer.apple.com/documentation/foundation/nsstring/nsstringdrawingoptions/1524942-usesdevicemetrics)

|  | Declaration |
| --- | --- |
| From | ``` static var UsesDeviceMetrics: NSStringDrawingOptions { get } ``` |
| To | ``` static var usesDeviceMetrics: NSStringDrawingOptions { get } ``` |

Modified [NSStringDrawingOptions.usesFontLeading](https://developer.apple.com/documentation/uikit/nsstringdrawingoptions/nsstringdrawingusesfontleading)

|  | Declaration |
| --- | --- |
| From | ``` static var UsesFontLeading: NSStringDrawingOptions { get } ``` |
| To | ``` static var usesFontLeading: NSStringDrawingOptions { get } ``` |

Modified [NSStringDrawingOptions.usesLineFragmentOrigin](https://developer.apple.com/documentation/foundation/nsstring/nsstringdrawingoptions/1534956-useslinefragmentorigin)

|  | Declaration |
| --- | --- |
| From | ``` static var UsesLineFragmentOrigin: NSStringDrawingOptions { get } ``` |
| To | ``` static var usesLineFragmentOrigin: NSStringDrawingOptions { get } ``` |

Modified [NSTextAlignment [enum]](https://developer.apple.com/documentation/uikit/nstextalignment)

|  | Declaration |
| --- | --- |
| From | ``` enum NSTextAlignment : Int {     case Left     case Center     case Right     case Justified     case Natural } ``` |
| To | ``` enum NSTextAlignment : Int {     case left     case center     case right     case justified     case natural } ``` |

Modified [NSTextAlignment.center](https://developer.apple.com/documentation/appkit/nstextalignment/center)

|  | Declaration |
| --- | --- |
| From | ``` case Center ``` |
| To | ``` case center ``` |

Modified [NSTextAlignment.justified](https://developer.apple.com/documentation/appkit/nstextalignment/nstextalignmentjustified)

|  | Declaration |
| --- | --- |
| From | ``` case Justified ``` |
| To | ``` case justified ``` |

Modified [NSTextAlignment.left](https://developer.apple.com/documentation/uikit/nstextalignment/nstextalignmentleft)

|  | Declaration |
| --- | --- |
| From | ``` case Left ``` |
| To | ``` case left ``` |

Modified [NSTextAlignment.natural](https://developer.apple.com/documentation/uikit/nstextalignment/natural)

|  | Declaration |
| --- | --- |
| From | ``` case Natural ``` |
| To | ``` case natural ``` |

Modified [NSTextAlignment.right](https://developer.apple.com/documentation/uikit/nstextalignment/nstextalignmentright)

|  | Declaration |
| --- | --- |
| From | ``` case Right ``` |
| To | ``` case right ``` |

Modified [NSTextTab](https://developer.apple.com/documentation/uikit/nstexttab)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSTextTab : NSObject, NSCopying, NSCoding {     class func columnTerminatorsForLocale(_ aLocale: NSLocale?) -> NSCharacterSet     init(textAlignment alignment: NSTextAlignment, location loc: CGFloat, options options: [String : AnyObject])     var alignment: NSTextAlignment { get }     var location: CGFloat { get }     var options: [String : AnyObject] { get } } ``` | NSCoding, NSCopying |
| To | ``` class NSTextTab : NSObject, NSCopying, NSCoding, NSSecureCoding {     class func columnTerminators(for aLocale: Locale?) -> CharacterSet     init(textAlignment alignment: NSTextAlignment, location loc: CGFloat, options options: [String : Any] = [:])     var alignment: NSTextAlignment { get }     var location: CGFloat { get }     var options: [String : Any] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSTextTab : CVarArg { } extension NSTextTab : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying, NSSecureCoding |

Modified [NSTextTab.columnTerminators(for: Locale?) -> CharacterSet [class]](https://developer.apple.com/documentation/uikit/nstexttab/1535107-columnterminatorsforlocale)

|  | Declaration |
| --- | --- |
| From | ``` class func columnTerminatorsForLocale(_ aLocale: NSLocale?) -> NSCharacterSet ``` |
| To | ``` class func columnTerminators(for aLocale: Locale?) -> CharacterSet ``` |

Modified [NSTextTab.init(textAlignment: NSTextAlignment, location: CGFloat, options: [String : Any])](https://developer.apple.com/documentation/appkit/nstexttab/1526080-init)

|  | Declaration |
| --- | --- |
| From | ``` init(textAlignment alignment: NSTextAlignment, location loc: CGFloat, options options: [String : AnyObject]) ``` |
| To | ``` init(textAlignment alignment: NSTextAlignment, location loc: CGFloat, options options: [String : Any] = [:]) ``` |

Modified [NSTextTab.options](https://developer.apple.com/documentation/appkit/nstexttab/1534965-options)

|  | Declaration |
| --- | --- |
| From | ``` var options: [String : AnyObject] { get } ``` |
| To | ``` var options: [String : Any] { get } ``` |

Modified [NSTextWritingDirection [enum]](https://developer.apple.com/documentation/uikit/nstextwritingdirection)

|  | Declaration |
| --- | --- |
| From | ``` enum NSTextWritingDirection : Int {     case Embedding     case Override } ``` |
| To | ``` enum NSTextWritingDirection : Int {     case embedding     case override } ``` |

Modified [NSTextWritingDirection.embedding](https://developer.apple.com/documentation/uikit/nstextwritingdirection/embedding)

|  | Declaration |
| --- | --- |
| From | ``` case Embedding ``` |
| To | ``` case embedding ``` |

Modified [NSTextWritingDirection.override](https://developer.apple.com/documentation/uikit/nstextwritingdirection/nstextwritingdirectionoverride)

|  | Declaration |
| --- | --- |
| From | ``` case Override ``` |
| To | ``` case override ``` |

Modified [NSUnderlineStyle [enum]](https://developer.apple.com/documentation/uikit/nsunderlinestyle)

|  | Declaration |
| --- | --- |
| From | ``` enum NSUnderlineStyle : Int {     case StyleNone     case StyleSingle     case StyleThick     case StyleDouble     static var PatternSolid: NSUnderlineStyle { get }     case PatternDot     case PatternDash     case PatternDashDot     case PatternDashDotDot     case ByWord } ``` |
| To | ``` enum NSUnderlineStyle : Int {     case styleNone     case styleSingle     case styleThick     case styleDouble     static var patternSolid: NSUnderlineStyle { get }     case patternDot     case patternDash     case patternDashDot     case patternDashDotDot     case byWord } ``` |

Modified [NSUnderlineStyle.byWord](https://developer.apple.com/documentation/appkit/nsunderlinestyle/1531227-byword)

|  | Declaration |
| --- | --- |
| From | ``` case ByWord ``` |
| To | ``` case byWord ``` |

Modified [NSUnderlineStyle.patternDash](https://developer.apple.com/documentation/appkit/nsunderlinestyle/nsunderlinestylepatterndash)

|  | Declaration |
| --- | --- |
| From | ``` case PatternDash ``` |
| To | ``` case patternDash ``` |

Modified [NSUnderlineStyle.patternDashDot](https://developer.apple.com/documentation/uikit/nsunderlinestyle/1526174-patterndashdot)

|  | Declaration |
| --- | --- |
| From | ``` case PatternDashDot ``` |
| To | ``` case patternDashDot ``` |

Modified [NSUnderlineStyle.patternDashDotDot](https://developer.apple.com/documentation/appkit/nsunderlinestyle/1524607-patterndashdotdot)

|  | Declaration |
| --- | --- |
| From | ``` case PatternDashDotDot ``` |
| To | ``` case patternDashDotDot ``` |

Modified [NSUnderlineStyle.patternDot](https://developer.apple.com/documentation/uikit/nsunderlinestyle/nsunderlinestylepatterndot)

|  | Declaration |
| --- | --- |
| From | ``` case PatternDot ``` |
| To | ``` case patternDot ``` |

Modified [NSUnderlineStyle.patternSolid](https://developer.apple.com/documentation/uikit/nsunderlinestyle/nsunderlinestylepatternsolid)

|  | Declaration |
| --- | --- |
| From | ``` static var PatternSolid: NSUnderlineStyle { get } ``` |
| To | ``` static var patternSolid: NSUnderlineStyle { get } ``` |

Modified [NSUnderlineStyle.styleDouble](https://developer.apple.com/documentation/appkit/nsunderlinestyle/nsunderlinestyledouble)

|  | Declaration |
| --- | --- |
| From | ``` case StyleDouble ``` |
| To | ``` case styleDouble ``` |

Modified [NSUnderlineStyle.styleNone](https://developer.apple.com/documentation/uikit/nsunderlinestyle/nsunderlinestylenone)

|  | Declaration |
| --- | --- |
| From | ``` case StyleNone ``` |
| To | ``` case styleNone ``` |

Modified [NSUnderlineStyle.styleSingle](https://developer.apple.com/documentation/uikit/nsunderlinestyle/nsunderlinestylesingle)

|  | Declaration |
| --- | --- |
| From | ``` case StyleSingle ``` |
| To | ``` case styleSingle ``` |

Modified [NSUnderlineStyle.styleThick](https://developer.apple.com/documentation/appkit/nsunderlinestyle/nsunderlinestylethick)

|  | Declaration |
| --- | --- |
| From | ``` case StyleThick ``` |
| To | ``` case styleThick ``` |

Modified [NSValue.init(cgAffineTransform: CGAffineTransform)](https://developer.apple.com/documentation/foundation/nsvalue/1624503-valuewithcgaffinetransform)

|  | Declaration |
| --- | --- |
| From | ``` init(CGAffineTransform transform: CGAffineTransform) ``` |
| To | ``` init(cgAffineTransform transform: CGAffineTransform) ``` |

Modified [NSValue.init(cgPoint: CGPoint)](https://developer.apple.com/documentation/foundation/nsvalue/1624531-valuewithcgpoint)

|  | Declaration |
| --- | --- |
| From | ``` init(CGPoint point: CGPoint) ``` |
| To | ``` init(cgPoint point: CGPoint) ``` |

Modified [NSValue.init(cgRect: CGRect)](https://developer.apple.com/documentation/foundation/nsvalue/1624529-valuewithcgrect)

|  | Declaration |
| --- | --- |
| From | ``` init(CGRect rect: CGRect) ``` |
| To | ``` init(cgRect rect: CGRect) ``` |

Modified [NSValue.init(cgSize: CGSize)](https://developer.apple.com/documentation/foundation/nsvalue/1624511-init)

|  | Declaration |
| --- | --- |
| From | ``` init(CGSize size: CGSize) ``` |
| To | ``` init(cgSize size: CGSize) ``` |

Modified [NSValue.init(cgVector: CGVector)](https://developer.apple.com/documentation/foundation/nsvalue/1624493-init)

|  | Declaration |
| --- | --- |
| From | ``` init(CGVector vector: CGVector) ``` |
| To | ``` init(cgVector vector: CGVector) ``` |

Modified [NSValue.init(uiEdgeInsets: UIEdgeInsets)](https://developer.apple.com/documentation/foundation/nsvalue/1624485-init)

|  | Declaration |
| --- | --- |
| From | ``` init(UIEdgeInsets insets: UIEdgeInsets) ``` |
| To | ``` init(uiEdgeInsets insets: UIEdgeInsets) ``` |

Modified [NSValue.init(uiOffset: UIOffset)](https://developer.apple.com/documentation/foundation/nsvalue/1624530-valuewithuioffset)

|  | Declaration |
| --- | --- |
| From | ``` init(UIOffset insets: UIOffset) ``` |
| To | ``` init(uiOffset insets: UIOffset) ``` |

Modified [NSWritingDirection [enum]](https://developer.apple.com/documentation/appkit/nswritingdirection)

|  | Declaration |
| --- | --- |
| From | ``` enum NSWritingDirection : Int {     case Natural     case LeftToRight     case RightToLeft } ``` |
| To | ``` enum NSWritingDirection : Int {     case natural     case leftToRight     case rightToLeft } ``` |

Modified [NSWritingDirection.leftToRight](https://developer.apple.com/documentation/uikit/nswritingdirection/nswritingdirectionlefttoright)

|  | Declaration |
| --- | --- |
| From | ``` case LeftToRight ``` |
| To | ``` case leftToRight ``` |

Modified [NSWritingDirection.natural](https://developer.apple.com/documentation/uikit/nswritingdirection/nswritingdirectionnatural)

|  | Declaration |
| --- | --- |
| From | ``` case Natural ``` |
| To | ``` case natural ``` |

Modified [NSWritingDirection.rightToLeft](https://developer.apple.com/documentation/uikit/nswritingdirection/nswritingdirectionrighttoleft)

|  | Declaration |
| --- | --- |
| From | ``` case RightToLeft ``` |
| To | ``` case rightToLeft ``` |

Modified [NSWritingDirectionFormatType [enum]](https://developer.apple.com/documentation/uikit/nswritingdirectionformattype)

|  | Declaration |
| --- | --- |
| From | ``` enum NSWritingDirectionFormatType : Int {     case Embedding     case Override } ``` |
| To | ``` enum NSWritingDirectionFormatType : Int {     case embedding     case override } ``` |

Modified [NSWritingDirectionFormatType.embedding](https://developer.apple.com/documentation/appkit/nswritingdirectionformattype/nswritingdirectionembedding)

|  | Declaration |
| --- | --- |
| From | ``` case Embedding ``` |
| To | ``` case embedding ``` |

Modified [NSWritingDirectionFormatType.override](https://developer.apple.com/documentation/appkit/nswritingdirectionformattype/nswritingdirectionoverride)

|  | Declaration |
| --- | --- |
| From | ``` case Override ``` |
| To | ``` case override ``` |

Modified [UIAccessibilityNavigationStyle [enum]](https://developer.apple.com/documentation/uikit/uiaccessibilitynavigationstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum UIAccessibilityNavigationStyle : Int {     case Automatic     case Separate     case Combined } ``` |
| To | ``` enum UIAccessibilityNavigationStyle : Int {     case automatic     case separate     case combined } ``` |

Modified [UIAccessibilityNavigationStyle.automatic](https://developer.apple.com/documentation/uikit/uiaccessibilitynavigationstyle/uiaccessibilitynavigationstyleautomatic)

|  | Declaration |
| --- | --- |
| From | ``` case Automatic ``` |
| To | ``` case automatic ``` |

Modified [UIAccessibilityNavigationStyle.combined](https://developer.apple.com/documentation/uikit/uiaccessibilitynavigationstyle/uiaccessibilitynavigationstylecombined)

|  | Declaration |
| --- | --- |
| From | ``` case Combined ``` |
| To | ``` case combined ``` |

Modified [UIAccessibilityNavigationStyle.separate](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitynavigationstyle/separate)

|  | Declaration |
| --- | --- |
| From | ``` case Separate ``` |
| To | ``` case separate ``` |

Modified [UIBezierPath](https://developer.apple.com/documentation/uikit/uibezierpath)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIBezierPath : NSObject, NSCopying, NSCoding {     convenience init()     class func bezierPath() -> Self     convenience init(rect rect: CGRect)     class func bezierPathWithRect(_ rect: CGRect) -> Self     convenience init(ovalInRect rect: CGRect)     class func bezierPathWithOvalInRect(_ rect: CGRect) -> Self     convenience init(roundedRect rect: CGRect, cornerRadius cornerRadius: CGFloat)     class func bezierPathWithRoundedRect(_ rect: CGRect, cornerRadius cornerRadius: CGFloat) -> Self     convenience init(roundedRect rect: CGRect, byRoundingCorners corners: UIRectCorner, cornerRadii cornerRadii: CGSize)     class func bezierPathWithRoundedRect(_ rect: CGRect, byRoundingCorners corners: UIRectCorner, cornerRadii cornerRadii: CGSize) -> Self     convenience init(arcCenter center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool)     class func bezierPathWithArcCenter(_ center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool) -> Self     convenience init(CGPath CGPath: CGPath)     class func bezierPathWithCGPath(_ CGPath: CGPath) -> Self     init()     init?(coder aDecoder: NSCoder)     var CGPath: CGPath     func moveToPoint(_ point: CGPoint)     func addLineToPoint(_ point: CGPoint)     func addCurveToPoint(_ endPoint: CGPoint, controlPoint1 controlPoint1: CGPoint, controlPoint2 controlPoint2: CGPoint)     func addQuadCurveToPoint(_ endPoint: CGPoint, controlPoint controlPoint: CGPoint)     func addArcWithCenter(_ center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool)     func closePath()     func removeAllPoints()     func appendPath(_ bezierPath: UIBezierPath)     func bezierPathByReversingPath() -> UIBezierPath     func applyTransform(_ transform: CGAffineTransform)     var empty: Bool { get }     var bounds: CGRect { get }     var currentPoint: CGPoint { get }     func containsPoint(_ point: CGPoint) -> Bool     var lineWidth: CGFloat     var lineCapStyle: CGLineCap     var lineJoinStyle: CGLineJoin     var miterLimit: CGFloat     var flatness: CGFloat     var usesEvenOddFillRule: Bool     func setLineDash(_ pattern: UnsafePointer<CGFloat>, count count: Int, phase phase: CGFloat)     func getLineDash(_ pattern: UnsafeMutablePointer<CGFloat>, count count: UnsafeMutablePointer<Int>, phase phase: UnsafeMutablePointer<CGFloat>)     func fill()     func stroke()     func fillWithBlendMode(_ blendMode: CGBlendMode, alpha alpha: CGFloat)     func strokeWithBlendMode(_ blendMode: CGBlendMode, alpha alpha: CGFloat)     func addClip() } ``` | NSCoding, NSCopying |
| To | ``` class UIBezierPath : NSObject, NSCopying, NSCoding {     convenience init()     class func bezierPath() -> Self     convenience init(rect rect: CGRect)     class func withRect(_ rect: CGRect) -> Self     convenience init(ovalIn rect: CGRect)     class func withOvalIn(_ rect: CGRect) -> Self     convenience init(roundedRect rect: CGRect, cornerRadius cornerRadius: CGFloat)     class func withRoundedRect(_ rect: CGRect, cornerRadius cornerRadius: CGFloat) -> Self     convenience init(roundedRect rect: CGRect, byRoundingCorners corners: UIRectCorner, cornerRadii cornerRadii: CGSize)     class func withRoundedRect(_ rect: CGRect, byRoundingCorners corners: UIRectCorner, cornerRadii cornerRadii: CGSize) -> Self     convenience init(arcCenter center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool)     class func withArcCenter(_ center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool) -> Self     convenience init(cgPath CGPath: CGPath)     class func withCGPath(_ CGPath: CGPath) -> Self     init()     init?(coder aDecoder: NSCoder)     var cgPath: CGPath     func move(to point: CGPoint)     func addLine(to point: CGPoint)     func addCurve(to endPoint: CGPoint, controlPoint1 controlPoint1: CGPoint, controlPoint2 controlPoint2: CGPoint)     func addQuadCurve(to endPoint: CGPoint, controlPoint controlPoint: CGPoint)     func addArc(withCenter center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool)     func close()     func removeAllPoints()     func append(_ bezierPath: UIBezierPath)     func reversing() -> UIBezierPath     func apply(_ transform: CGAffineTransform)     var isEmpty: Bool { get }     var bounds: CGRect { get }     var currentPoint: CGPoint { get }     func contains(_ point: CGPoint) -> Bool     var lineWidth: CGFloat     var lineCapStyle: CGLineCap     var lineJoinStyle: CGLineJoin     var miterLimit: CGFloat     var flatness: CGFloat     var usesEvenOddFillRule: Bool     func setLineDash(_ pattern: UnsafePointer<CGFloat>?, count count: Int, phase phase: CGFloat)     func getLineDash(_ pattern: UnsafeMutablePointer<CGFloat>?, count count: UnsafeMutablePointer<Int>?, phase phase: UnsafeMutablePointer<CGFloat>?)     func fill()     func stroke()     func fill(with blendMode: CGBlendMode, alpha alpha: CGFloat)     func stroke(with blendMode: CGBlendMode, alpha alpha: CGFloat)     func addClip()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension UIBezierPath : CVarArg { } extension UIBezierPath : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying |

Modified [UIBezierPath.addArc(withCenter: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](https://developer.apple.com/documentation/uikit/uibezierpath/1624367-addarcwithcenter)

|  | Declaration |
| --- | --- |
| From | ``` func addArcWithCenter(_ center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool) ``` |
| To | ``` func addArc(withCenter center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool) ``` |

Modified [UIBezierPath.addCurve(to: CGPoint, controlPoint1: CGPoint, controlPoint2: CGPoint)](https://developer.apple.com/documentation/uikit/uibezierpath/1624357-addcurvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` func addCurveToPoint(_ endPoint: CGPoint, controlPoint1 controlPoint1: CGPoint, controlPoint2 controlPoint2: CGPoint) ``` |
| To | ``` func addCurve(to endPoint: CGPoint, controlPoint1 controlPoint1: CGPoint, controlPoint2 controlPoint2: CGPoint) ``` |

Modified [UIBezierPath.addLine(to: CGPoint)](https://developer.apple.com/documentation/uikit/uibezierpath/1624354-addline)

|  | Declaration |
| --- | --- |
| From | ``` func addLineToPoint(_ point: CGPoint) ``` |
| To | ``` func addLine(to point: CGPoint) ``` |

Modified [UIBezierPath.addQuadCurve(to: CGPoint, controlPoint: CGPoint)](https://developer.apple.com/documentation/uikit/uibezierpath/1624351-addquadcurvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` func addQuadCurveToPoint(_ endPoint: CGPoint, controlPoint controlPoint: CGPoint) ``` |
| To | ``` func addQuadCurve(to endPoint: CGPoint, controlPoint controlPoint: CGPoint) ``` |

Modified [UIBezierPath.append(_: UIBezierPath)](https://developer.apple.com/documentation/uikit/uibezierpath/1624377-appendpath)

|  | Declaration |
| --- | --- |
| From | ``` func appendPath(_ bezierPath: UIBezierPath) ``` |
| To | ``` func append(_ bezierPath: UIBezierPath) ``` |

Modified [UIBezierPath.apply(_: CGAffineTransform)](https://developer.apple.com/documentation/uikit/uibezierpath/1624340-applytransform)

|  | Declaration |
| --- | --- |
| From | ``` func applyTransform(_ transform: CGAffineTransform) ``` |
| To | ``` func apply(_ transform: CGAffineTransform) ``` |

Modified [UIBezierPath.cgPath](https://developer.apple.com/documentation/uikit/uibezierpath/1624342-cgpath)

|  | Declaration |
| --- | --- |
| From | ``` var CGPath: CGPath ``` |
| To | ``` var cgPath: CGPath ``` |

Modified [UIBezierPath.close()](https://developer.apple.com/documentation/uikit/uibezierpath/1624338-close)

|  | Declaration |
| --- | --- |
| From | ``` func closePath() ``` |
| To | ``` func close() ``` |

Modified [UIBezierPath.contains(_: CGPoint) -> Bool](https://developer.apple.com/documentation/uikit/uibezierpath/1624345-containspoint)

|  | Declaration |
| --- | --- |
| From | ``` func containsPoint(_ point: CGPoint) -> Bool ``` |
| To | ``` func contains(_ point: CGPoint) -> Bool ``` |

Modified [UIBezierPath.fill(with: CGBlendMode, alpha: CGFloat)](https://developer.apple.com/documentation/uikit/uibezierpath/1624366-fill)

|  | Declaration |
| --- | --- |
| From | ``` func fillWithBlendMode(_ blendMode: CGBlendMode, alpha alpha: CGFloat) ``` |
| To | ``` func fill(with blendMode: CGBlendMode, alpha alpha: CGFloat) ``` |

Modified [UIBezierPath.getLineDash(_: UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)](https://developer.apple.com/documentation/uikit/uibezierpath/1624374-getlinedash)

|  | Declaration |
| --- | --- |
| From | ``` func getLineDash(_ pattern: UnsafeMutablePointer<CGFloat>, count count: UnsafeMutablePointer<Int>, phase phase: UnsafeMutablePointer<CGFloat>) ``` |
| To | ``` func getLineDash(_ pattern: UnsafeMutablePointer<CGFloat>?, count count: UnsafeMutablePointer<Int>?, phase phase: UnsafeMutablePointer<CGFloat>?) ``` |

Modified [UIBezierPath.init(cgPath: CGPath)](https://developer.apple.com/documentation/uikit/uibezierpath/1624362-bezierpathwithcgpath)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(CGPath CGPath: CGPath) ``` |
| To | ``` convenience init(cgPath CGPath: CGPath) ``` |

Modified [UIBezierPath.init(ovalIn: CGRect)](https://developer.apple.com/documentation/uikit/uibezierpath/1624379-bezierpathwithovalinrect)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(ovalInRect rect: CGRect) ``` |
| To | ``` convenience init(ovalIn rect: CGRect) ``` |

Modified [UIBezierPath.isEmpty](https://developer.apple.com/documentation/uikit/uibezierpath/1624382-isempty)

|  | Declaration |
| --- | --- |
| From | ``` var empty: Bool { get } ``` |
| To | ``` var isEmpty: Bool { get } ``` |

Modified [UIBezierPath.move(to: CGPoint)](https://developer.apple.com/documentation/uikit/uibezierpath/1624343-movetopoint)

|  | Declaration |
| --- | --- |
| From | ``` func moveToPoint(_ point: CGPoint) ``` |
| To | ``` func move(to point: CGPoint) ``` |

Modified [UIBezierPath.reversing() -> UIBezierPath](https://developer.apple.com/documentation/uikit/uibezierpath/1624348-reversing)

|  | Declaration |
| --- | --- |
| From | ``` func bezierPathByReversingPath() -> UIBezierPath ``` |
| To | ``` func reversing() -> UIBezierPath ``` |

Modified [UIBezierPath.setLineDash(_: UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)](https://developer.apple.com/documentation/uikit/uibezierpath/1624373-setlinedash)

|  | Declaration |
| --- | --- |
| From | ``` func setLineDash(_ pattern: UnsafePointer<CGFloat>, count count: Int, phase phase: CGFloat) ``` |
| To | ``` func setLineDash(_ pattern: UnsafePointer<CGFloat>?, count count: Int, phase phase: CGFloat) ``` |

Modified [UIBezierPath.stroke(with: CGBlendMode, alpha: CGFloat)](https://developer.apple.com/documentation/uikit/uibezierpath/1624380-stroke)

|  | Declaration |
| --- | --- |
| From | ``` func strokeWithBlendMode(_ blendMode: CGBlendMode, alpha alpha: CGFloat) ``` |
| To | ``` func stroke(with blendMode: CGBlendMode, alpha alpha: CGFloat) ``` |

Modified [UIColor](https://developer.apple.com/documentation/uikit/uicolor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIColor : NSObject, NSSecureCoding, NSCopying {      init(white white: CGFloat, alpha alpha: CGFloat)     class func colorWithWhite(_ white: CGFloat, alpha alpha: CGFloat) -> UIColor      init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     class func colorWithHue(_ hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat) -> UIColor      init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     class func colorWithRed(_ red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) -> UIColor      init(CGColor cgColor: CGColor)     class func colorWithCGColor(_ cgColor: CGColor) -> UIColor      init(patternImage image: UIImage)     class func colorWithPatternImage(_ image: UIImage) -> UIColor     init(white white: CGFloat, alpha alpha: CGFloat)     init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     init(CGColor cgColor: CGColor)     init(patternImage image: UIImage)     class func blackColor() -> UIColor     class func darkGrayColor() -> UIColor     class func lightGrayColor() -> UIColor     class func whiteColor() -> UIColor     class func grayColor() -> UIColor     class func redColor() -> UIColor     class func greenColor() -> UIColor     class func blueColor() -> UIColor     class func cyanColor() -> UIColor     class func yellowColor() -> UIColor     class func magentaColor() -> UIColor     class func orangeColor() -> UIColor     class func purpleColor() -> UIColor     class func brownColor() -> UIColor     class func clearColor() -> UIColor     func set()     func setFill()     func setStroke()     func getWhite(_ white: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getHue(_ hue: UnsafeMutablePointer<CGFloat>, saturation saturation: UnsafeMutablePointer<CGFloat>, brightness brightness: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getRed(_ red: UnsafeMutablePointer<CGFloat>, green green: UnsafeMutablePointer<CGFloat>, blue blue: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func colorWithAlphaComponent(_ alpha: CGFloat) -> UIColor     var CGColor: CGColor { get } } extension UIColor {     required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float) } extension UIColor {     required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float) } ``` | NSCopying, NSSecureCoding |
| To | ``` class UIColor : NSObject, NSSecureCoding, NSCopying {      init(white white: CGFloat, alpha alpha: CGFloat)     class func withWhite(_ white: CGFloat, alpha alpha: CGFloat) -> UIColor      init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     class func withHue(_ hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat) -> UIColor      init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     class func withRed(_ red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) -> UIColor      init(displayP3Red displayP3Red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     class func withDisplayP3Red(_ displayP3Red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) -> UIColor      init(cgColor cgColor: CGColor)     class func withCGColor(_ cgColor: CGColor) -> UIColor      init(patternImage image: UIImage)     class func withPatternImage(_ image: UIImage) -> UIColor     init(white white: CGFloat, alpha alpha: CGFloat)     init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     init(displayP3Red displayP3Red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     init(cgColor cgColor: CGColor)     init(patternImage image: UIImage)     class var black: UIColor { get }     class var darkGray: UIColor { get }     class var lightGray: UIColor { get }     class var white: UIColor { get }     class var gray: UIColor { get }     class var red: UIColor { get }     class var green: UIColor { get }     class var blue: UIColor { get }     class var cyan: UIColor { get }     class var yellow: UIColor { get }     class var magenta: UIColor { get }     class var orange: UIColor { get }     class var purple: UIColor { get }     class var brown: UIColor { get }     class var clear: UIColor { get }     func set()     func setFill()     func setStroke()     func getWhite(_ white: UnsafeMutablePointer<CGFloat>?, alpha alpha: UnsafeMutablePointer<CGFloat>?) -> Bool     func getHue(_ hue: UnsafeMutablePointer<CGFloat>?, saturation saturation: UnsafeMutablePointer<CGFloat>?, brightness brightness: UnsafeMutablePointer<CGFloat>?, alpha alpha: UnsafeMutablePointer<CGFloat>?) -> Bool     func getRed(_ red: UnsafeMutablePointer<CGFloat>?, green green: UnsafeMutablePointer<CGFloat>?, blue blue: UnsafeMutablePointer<CGFloat>?, alpha alpha: UnsafeMutablePointer<CGFloat>?) -> Bool     func withAlphaComponent(_ alpha: CGFloat) -> UIColor     var cgColor: CGColor { get }     @nonobjc required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension UIColor : CVarArg { } extension UIColor : Equatable, Hashable {     var hashValue: Int { get } } extension UIColor {     @nonobjc required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float) } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [UIColor.cgColor](https://developer.apple.com/documentation/uikit/uicolor/1621954-cgcolor)

|  | Declaration |
| --- | --- |
| From | ``` var CGColor: CGColor { get } ``` |
| To | ``` var cgColor: CGColor { get } ``` |

Modified [UIColor.getHue(_: UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](https://developer.apple.com/documentation/uikit/uicolor/1621949-gethue)

|  | Declaration |
| --- | --- |
| From | ``` func getHue(_ hue: UnsafeMutablePointer<CGFloat>, saturation saturation: UnsafeMutablePointer<CGFloat>, brightness brightness: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool ``` |
| To | ``` func getHue(_ hue: UnsafeMutablePointer<CGFloat>?, saturation saturation: UnsafeMutablePointer<CGFloat>?, brightness brightness: UnsafeMutablePointer<CGFloat>?, alpha alpha: UnsafeMutablePointer<CGFloat>?) -> Bool ``` |

Modified [UIColor.getRed(_: UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](https://developer.apple.com/documentation/uikit/uicolor/1621919-getred)

|  | Declaration |
| --- | --- |
| From | ``` func getRed(_ red: UnsafeMutablePointer<CGFloat>, green green: UnsafeMutablePointer<CGFloat>, blue blue: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool ``` |
| To | ``` func getRed(_ red: UnsafeMutablePointer<CGFloat>?, green green: UnsafeMutablePointer<CGFloat>?, blue blue: UnsafeMutablePointer<CGFloat>?, alpha alpha: UnsafeMutablePointer<CGFloat>?) -> Bool ``` |

Modified [UIColor.getWhite(_: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](https://developer.apple.com/documentation/uikit/uicolor/1621927-getwhite)

|  | Declaration |
| --- | --- |
| From | ``` func getWhite(_ white: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool ``` |
| To | ``` func getWhite(_ white: UnsafeMutablePointer<CGFloat>?, alpha alpha: UnsafeMutablePointer<CGFloat>?) -> Bool ``` |

Modified [UIColor.init(cgColor: CGColor)](https://developer.apple.com/documentation/uikit/uicolor/1621921-initwithcgcolor)

|  | Declaration |
| --- | --- |
| From | ``` init(CGColor cgColor: CGColor) ``` |
| To | ``` init(cgColor cgColor: CGColor) ``` |

Modified UIColor.init(colorLiteralRed: Float, green: Float, blue: Float, alpha: Float)

|  | Declaration |
| --- | --- |
| From | ``` required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float) ``` |
| To | ``` @nonobjc required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float) ``` |

Modified [UIColor.withAlphaComponent(_: CGFloat) -> UIColor](https://developer.apple.com/documentation/uikit/uicolor/1621922-withalphacomponent)

|  | Declaration |
| --- | --- |
| From | ``` func colorWithAlphaComponent(_ alpha: CGFloat) -> UIColor ``` |
| To | ``` func withAlphaComponent(_ alpha: CGFloat) -> UIColor ``` |

Modified [UIEdgeInsets [struct]](https://developer.apple.com/documentation/uikit/uiedgeinsets)

|  | Declaration |
| --- | --- |
| From | ``` struct UIEdgeInsets {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat     init()     init(top top: CGFloat, left left: CGFloat, bottom bottom: CGFloat, right right: CGFloat) } extension UIEdgeInsets : Equatable { } extension UIEdgeInsets : Equatable { } ``` |
| To | ``` struct UIEdgeInsets {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat     init()     init(top top: CGFloat, left left: CGFloat, bottom bottom: CGFloat, right right: CGFloat)     static var zero: UIEdgeInsets { get } } extension UIEdgeInsets {     static var zero: UIEdgeInsets { get } } extension UIEdgeInsets : Equatable { } ``` |

Modified [UIFont](https://developer.apple.com/documentation/uikit/uifont)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIFont : NSObject, NSCopying {     class func preferredFontForTextStyle(_ style: String) -> UIFont      init?(name fontName: String, size fontSize: CGFloat)     class func fontWithName(_ fontName: String, size fontSize: CGFloat) -> UIFont?     class func familyNames() -> [String]     class func fontNamesForFamilyName(_ familyName: String) -> [String]     class func systemFontOfSize(_ fontSize: CGFloat) -> UIFont     class func boldSystemFontOfSize(_ fontSize: CGFloat) -> UIFont     class func italicSystemFontOfSize(_ fontSize: CGFloat) -> UIFont     class func systemFontOfSize(_ fontSize: CGFloat, weight weight: CGFloat) -> UIFont     class func monospacedDigitSystemFontOfSize(_ fontSize: CGFloat, weight weight: CGFloat) -> UIFont     var familyName: String { get }     var fontName: String { get }     var pointSize: CGFloat { get }     var ascender: CGFloat { get }     var descender: CGFloat { get }     var capHeight: CGFloat { get }     var xHeight: CGFloat { get }     var lineHeight: CGFloat { get }     var leading: CGFloat { get }     func fontWithSize(_ fontSize: CGFloat) -> UIFont      init(descriptor descriptor: UIFontDescriptor, size pointSize: CGFloat)     class func fontWithDescriptor(_ descriptor: UIFontDescriptor, size pointSize: CGFloat) -> UIFont     func fontDescriptor() -> UIFontDescriptor } ``` | NSCopying |
| To | ``` class UIFont : NSObject, NSCopying {     class func preferredFont(forTextStyle style: UIFontTextStyle) -> UIFont     class func preferredFont(forTextStyle style: UIFontTextStyle, compatibleWith traitCollection: UITraitCollection?) -> UIFont      init?(name fontName: String, size fontSize: CGFloat)     class func withName(_ fontName: String, size fontSize: CGFloat) -> UIFont?     class var familyNames: [String] { get }     class func fontNames(forFamilyName familyName: String) -> [String]     class func systemFont(ofSize fontSize: CGFloat) -> UIFont     class func boldSystemFont(ofSize fontSize: CGFloat) -> UIFont     class func italicSystemFont(ofSize fontSize: CGFloat) -> UIFont     class func systemFont(ofSize fontSize: CGFloat, weight weight: CGFloat) -> UIFont     class func monospacedDigitSystemFont(ofSize fontSize: CGFloat, weight weight: CGFloat) -> UIFont     var familyName: String { get }     var fontName: String { get }     var pointSize: CGFloat { get }     var ascender: CGFloat { get }     var descender: CGFloat { get }     var capHeight: CGFloat { get }     var xHeight: CGFloat { get }     var lineHeight: CGFloat { get }     var leading: CGFloat { get }     func withSize(_ fontSize: CGFloat) -> UIFont      init(descriptor descriptor: UIFontDescriptor, size pointSize: CGFloat)     class func withDescriptor(_ descriptor: UIFontDescriptor, size pointSize: CGFloat) -> UIFont     var fontDescriptor: UIFontDescriptor { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension UIFont : CVarArg { } extension UIFont : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [UIFont.boldSystemFont(ofSize: CGFloat) -> UIFont [class]](https://developer.apple.com/documentation/uikit/uifont/1619039-boldsystemfontofsize)

|  | Declaration |
| --- | --- |
| From | ``` class func boldSystemFontOfSize(_ fontSize: CGFloat) -> UIFont ``` |
| To | ``` class func boldSystemFont(ofSize fontSize: CGFloat) -> UIFont ``` |

Modified [UIFont.fontNames(forFamilyName: String) -> [String] [class]](https://developer.apple.com/documentation/uikit/uifont/1619023-fontnamesforfamilyname)

|  | Declaration |
| --- | --- |
| From | ``` class func fontNamesForFamilyName(_ familyName: String) -> [String] ``` |
| To | ``` class func fontNames(forFamilyName familyName: String) -> [String] ``` |

Modified [UIFont.italicSystemFont(ofSize: CGFloat) -> UIFont [class]](https://developer.apple.com/documentation/uikit/uifont/1619043-italicsystemfont)

|  | Declaration |
| --- | --- |
| From | ``` class func italicSystemFontOfSize(_ fontSize: CGFloat) -> UIFont ``` |
| To | ``` class func italicSystemFont(ofSize fontSize: CGFloat) -> UIFont ``` |

Modified [UIFont.monospacedDigitSystemFont(ofSize: CGFloat, weight: CGFloat) -> UIFont [class]](https://developer.apple.com/documentation/uikit/uifont/1619022-monospaceddigitsystemfontofsize)

|  | Declaration |
| --- | --- |
| From | ``` class func monospacedDigitSystemFontOfSize(_ fontSize: CGFloat, weight weight: CGFloat) -> UIFont ``` |
| To | ``` class func monospacedDigitSystemFont(ofSize fontSize: CGFloat, weight weight: CGFloat) -> UIFont ``` |

Modified [UIFont.preferredFont(forTextStyle: UIFontTextStyle) -> UIFont [class]](https://developer.apple.com/documentation/uikit/uifont/1619030-preferredfont)

|  | Declaration |
| --- | --- |
| From | ``` class func preferredFontForTextStyle(_ style: String) -> UIFont ``` |
| To | ``` class func preferredFont(forTextStyle style: UIFontTextStyle) -> UIFont ``` |

Modified [UIFont.systemFont(ofSize: CGFloat) -> UIFont [class]](https://developer.apple.com/documentation/uikit/uifont/1619042-systemfontofsize)

|  | Declaration |
| --- | --- |
| From | ``` class func systemFontOfSize(_ fontSize: CGFloat) -> UIFont ``` |
| To | ``` class func systemFont(ofSize fontSize: CGFloat) -> UIFont ``` |

Modified [UIFont.systemFont(ofSize: CGFloat, weight: CGFloat) -> UIFont [class]](https://developer.apple.com/documentation/uikit/uifont/1619027-systemfontofsize)

|  | Declaration |
| --- | --- |
| From | ``` class func systemFontOfSize(_ fontSize: CGFloat, weight weight: CGFloat) -> UIFont ``` |
| To | ``` class func systemFont(ofSize fontSize: CGFloat, weight weight: CGFloat) -> UIFont ``` |

Modified [UIFont.withSize(_: CGFloat) -> UIFont](https://developer.apple.com/documentation/uikit/uifont/1619032-fontwithsize)

|  | Declaration |
| --- | --- |
| From | ``` func fontWithSize(_ fontSize: CGFloat) -> UIFont ``` |
| To | ``` func withSize(_ fontSize: CGFloat) -> UIFont ``` |

Modified [UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIFontDescriptor : NSObject, NSCopying, NSSecureCoding {     convenience init()     init?(coder aDecoder: NSCoder)     var postscriptName: String { get }     var pointSize: CGFloat { get }     var matrix: CGAffineTransform { get }     var symbolicTraits: UIFontDescriptorSymbolicTraits { get }     func objectForKey(_ anAttribute: String) -> AnyObject?     func fontAttributes() -> [String : AnyObject]     func matchingFontDescriptorsWithMandatoryKeys(_ mandatoryKeys: Set<String>?) -> [UIFontDescriptor]      init(fontAttributes attributes: [String : AnyObject])     class func fontDescriptorWithFontAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor      init(name fontName: String, size size: CGFloat)     class func fontDescriptorWithName(_ fontName: String, size size: CGFloat) -> UIFontDescriptor      init(name fontName: String, matrix matrix: CGAffineTransform)     class func fontDescriptorWithName(_ fontName: String, matrix matrix: CGAffineTransform) -> UIFontDescriptor     class func preferredFontDescriptorWithTextStyle(_ style: String) -> UIFontDescriptor     init(fontAttributes attributes: [String : AnyObject])     func fontDescriptorByAddingAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor     func fontDescriptorWithSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor     func fontDescriptorWithSize(_ newPointSize: CGFloat) -> UIFontDescriptor     func fontDescriptorWithMatrix(_ matrix: CGAffineTransform) -> UIFontDescriptor     func fontDescriptorWithFace(_ newFace: String) -> UIFontDescriptor     func fontDescriptorWithFamily(_ newFamily: String) -> UIFontDescriptor } ``` | NSCopying, NSSecureCoding |
| To | ``` class UIFontDescriptor : NSObject, NSCopying, NSSecureCoding {     convenience init()     init?(coder aDecoder: NSCoder)     var postscriptName: String { get }     var pointSize: CGFloat { get }     var matrix: CGAffineTransform { get }     var symbolicTraits: UIFontDescriptorSymbolicTraits { get }     func object(forKey anAttribute: String) -> Any?     var fontAttributes: [String : Any] { get }     func matchingFontDescriptors(withMandatoryKeys mandatoryKeys: Set<String>?) -> [UIFontDescriptor]      init(fontAttributes attributes: [String : Any] = [:])     class func withFontAttributes(_ attributes: [String : Any] = [:]) -> UIFontDescriptor      init(name fontName: String, size size: CGFloat)     class func withName(_ fontName: String, size size: CGFloat) -> UIFontDescriptor      init(name fontName: String, matrix matrix: CGAffineTransform)     class func withName(_ fontName: String, matrix matrix: CGAffineTransform) -> UIFontDescriptor     class func preferredFontDescriptor(withTextStyle style: UIFontTextStyle) -> UIFontDescriptor     class func preferredFontDescriptor(withTextStyle style: UIFontTextStyle, compatibleWith traitCollection: UITraitCollection?) -> UIFontDescriptor     init(fontAttributes attributes: [String : Any] = [:])     func addingAttributes(_ attributes: [String : Any] = [:]) -> UIFontDescriptor     func withSize(_ newPointSize: CGFloat) -> UIFontDescriptor     func withMatrix(_ matrix: CGAffineTransform) -> UIFontDescriptor     func withFace(_ newFace: String) -> UIFontDescriptor     func withFamily(_ newFamily: String) -> UIFontDescriptor     func withSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension UIFontDescriptor : CVarArg { } extension UIFontDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [UIFontDescriptor.addingAttributes(_: [String : Any]) -> UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616666-fontdescriptorbyaddingattributes)

|  | Declaration |
| --- | --- |
| From | ``` func fontDescriptorByAddingAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor ``` |
| To | ``` func addingAttributes(_ attributes: [String : Any] = [:]) -> UIFontDescriptor ``` |

Modified [UIFontDescriptor.init(fontAttributes: [String : Any])](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616679-init)

|  | Declaration |
| --- | --- |
| From | ``` init(fontAttributes attributes: [String : AnyObject]) ``` |
| To | ``` init(fontAttributes attributes: [String : Any] = [:]) ``` |

Modified [UIFontDescriptor.matchingFontDescriptors(withMandatoryKeys: Set<String>?) -> [UIFontDescriptor]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616699-matchingfontdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` func matchingFontDescriptorsWithMandatoryKeys(_ mandatoryKeys: Set<String>?) -> [UIFontDescriptor] ``` |
| To | ``` func matchingFontDescriptors(withMandatoryKeys mandatoryKeys: Set<String>?) -> [UIFontDescriptor] ``` |

Modified [UIFontDescriptor.object(forKey: String) -> Any?](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616733-object)

|  | Declaration |
| --- | --- |
| From | ``` func objectForKey(_ anAttribute: String) -> AnyObject? ``` |
| To | ``` func object(forKey anAttribute: String) -> Any? ``` |

Modified [UIFontDescriptor.preferredFontDescriptor(withTextStyle: UIFontTextStyle) -> UIFontDescriptor [class]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616705-preferredfontdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` class func preferredFontDescriptorWithTextStyle(_ style: String) -> UIFontDescriptor ``` |
| To | ``` class func preferredFontDescriptor(withTextStyle style: UIFontTextStyle) -> UIFontDescriptor ``` |

Modified [UIFontDescriptor.withFace(_: String) -> UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616681-fontdescriptorwithface)

|  | Declaration |
| --- | --- |
| From | ``` func fontDescriptorWithFace(_ newFace: String) -> UIFontDescriptor ``` |
| To | ``` func withFace(_ newFace: String) -> UIFontDescriptor ``` |

Modified [UIFontDescriptor.withFamily(_: String) -> UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616676-withfamily)

|  | Declaration |
| --- | --- |
| From | ``` func fontDescriptorWithFamily(_ newFamily: String) -> UIFontDescriptor ``` |
| To | ``` func withFamily(_ newFamily: String) -> UIFontDescriptor ``` |

Modified [UIFontDescriptor.withMatrix(_: CGAffineTransform) -> UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616731-fontdescriptorwithmatrix)

|  | Declaration |
| --- | --- |
| From | ``` func fontDescriptorWithMatrix(_ matrix: CGAffineTransform) -> UIFontDescriptor ``` |
| To | ``` func withMatrix(_ matrix: CGAffineTransform) -> UIFontDescriptor ``` |

Modified [UIFontDescriptor.withSize(_: CGFloat) -> UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616675-withsize)

|  | Declaration |
| --- | --- |
| From | ``` func fontDescriptorWithSize(_ newPointSize: CGFloat) -> UIFontDescriptor ``` |
| To | ``` func withSize(_ newPointSize: CGFloat) -> UIFontDescriptor ``` |

Modified [UIFontDescriptor.withSymbolicTraits(_: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor?](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616665-fontdescriptorwithsymbolictraits)

|  | Declaration |
| --- | --- |
| From | ``` func fontDescriptorWithSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor ``` |
| To | ``` func withSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor? ``` |

Modified [UIFontDescriptorSymbolicTraits [struct]](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIFontDescriptorSymbolicTraits : OptionSetType {     init(rawValue rawValue: UInt32)     static var TraitItalic: UIFontDescriptorSymbolicTraits { get }     static var TraitBold: UIFontDescriptorSymbolicTraits { get }     static var TraitExpanded: UIFontDescriptorSymbolicTraits { get }     static var TraitCondensed: UIFontDescriptorSymbolicTraits { get }     static var TraitMonoSpace: UIFontDescriptorSymbolicTraits { get }     static var TraitVertical: UIFontDescriptorSymbolicTraits { get }     static var TraitUIOptimized: UIFontDescriptorSymbolicTraits { get }     static var TraitTightLeading: UIFontDescriptorSymbolicTraits { get }     static var TraitLooseLeading: UIFontDescriptorSymbolicTraits { get }     static var ClassMask: UIFontDescriptorSymbolicTraits { get }     static var ClassUnknown: UIFontDescriptorSymbolicTraits { get }     static var ClassOldStyleSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassTransitionalSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassModernSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassClarendonSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassSlabSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassFreeformSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassSansSerif: UIFontDescriptorSymbolicTraits { get }     static var ClassOrnamentals: UIFontDescriptorSymbolicTraits { get }     static var ClassScripts: UIFontDescriptorSymbolicTraits { get }     static var ClassSymbolic: UIFontDescriptorSymbolicTraits { get } } ``` | OptionSetType |
| To | ``` struct UIFontDescriptorSymbolicTraits : OptionSet {     init(rawValue rawValue: UInt32)     static var traitItalic: UIFontDescriptorSymbolicTraits { get }     static var traitBold: UIFontDescriptorSymbolicTraits { get }     static var traitExpanded: UIFontDescriptorSymbolicTraits { get }     static var traitCondensed: UIFontDescriptorSymbolicTraits { get }     static var traitMonoSpace: UIFontDescriptorSymbolicTraits { get }     static var traitVertical: UIFontDescriptorSymbolicTraits { get }     static var traitUIOptimized: UIFontDescriptorSymbolicTraits { get }     static var traitTightLeading: UIFontDescriptorSymbolicTraits { get }     static var traitLooseLeading: UIFontDescriptorSymbolicTraits { get }     static var classMask: UIFontDescriptorSymbolicTraits { get }     static var classUnknown: UIFontDescriptorSymbolicTraits { get }     static var classOldStyleSerifs: UIFontDescriptorSymbolicTraits { get }     static var classTransitionalSerifs: UIFontDescriptorSymbolicTraits { get }     static var classModernSerifs: UIFontDescriptorSymbolicTraits { get }     static var classClarendonSerifs: UIFontDescriptorSymbolicTraits { get }     static var classSlabSerifs: UIFontDescriptorSymbolicTraits { get }     static var classFreeformSerifs: UIFontDescriptorSymbolicTraits { get }     static var classSansSerif: UIFontDescriptorSymbolicTraits { get }     static var classOrnamentals: UIFontDescriptorSymbolicTraits { get }     static var classScripts: UIFontDescriptorSymbolicTraits { get }     static var classSymbolic: UIFontDescriptorSymbolicTraits { get }     func intersect(_ other: UIFontDescriptorSymbolicTraits) -> UIFontDescriptorSymbolicTraits     func exclusiveOr(_ other: UIFontDescriptorSymbolicTraits) -> UIFontDescriptorSymbolicTraits     mutating func unionInPlace(_ other: UIFontDescriptorSymbolicTraits)     mutating func intersectInPlace(_ other: UIFontDescriptorSymbolicTraits)     mutating func exclusiveOrInPlace(_ other: UIFontDescriptorSymbolicTraits)     func isSubsetOf(_ other: UIFontDescriptorSymbolicTraits) -> Bool     func isDisjointWith(_ other: UIFontDescriptorSymbolicTraits) -> Bool     func isSupersetOf(_ other: UIFontDescriptorSymbolicTraits) -> Bool     mutating func subtractInPlace(_ other: UIFontDescriptorSymbolicTraits)     func isStrictSupersetOf(_ other: UIFontDescriptorSymbolicTraits) -> Bool     func isStrictSubsetOf(_ other: UIFontDescriptorSymbolicTraits) -> Bool } extension UIFontDescriptorSymbolicTraits {     func union(_ other: UIFontDescriptorSymbolicTraits) -> UIFontDescriptorSymbolicTraits     func intersection(_ other: UIFontDescriptorSymbolicTraits) -> UIFontDescriptorSymbolicTraits     func symmetricDifference(_ other: UIFontDescriptorSymbolicTraits) -> UIFontDescriptorSymbolicTraits } extension UIFontDescriptorSymbolicTraits {     func contains(_ member: UIFontDescriptorSymbolicTraits) -> Bool     mutating func insert(_ newMember: UIFontDescriptorSymbolicTraits) -> (inserted: Bool, memberAfterInsert: UIFontDescriptorSymbolicTraits)     mutating func remove(_ member: UIFontDescriptorSymbolicTraits) -> UIFontDescriptorSymbolicTraits?     mutating func update(with newMember: UIFontDescriptorSymbolicTraits) -> UIFontDescriptorSymbolicTraits? } extension UIFontDescriptorSymbolicTraits {     convenience init()     mutating func formUnion(_ other: UIFontDescriptorSymbolicTraits)     mutating func formIntersection(_ other: UIFontDescriptorSymbolicTraits)     mutating func formSymmetricDifference(_ other: UIFontDescriptorSymbolicTraits) } extension UIFontDescriptorSymbolicTraits {     convenience init<S : Sequence where S.Iterator.Element == UIFontDescriptorSymbolicTraits>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: UIFontDescriptorSymbolicTraits...)     mutating func subtract(_ other: UIFontDescriptorSymbolicTraits)     func isSubset(of other: UIFontDescriptorSymbolicTraits) -> Bool     func isSuperset(of other: UIFontDescriptorSymbolicTraits) -> Bool     func isDisjoint(with other: UIFontDescriptorSymbolicTraits) -> Bool     func subtracting(_ other: UIFontDescriptorSymbolicTraits) -> UIFontDescriptorSymbolicTraits     var isEmpty: Bool { get }     func isStrictSuperset(of other: UIFontDescriptorSymbolicTraits) -> Bool     func isStrictSubset(of other: UIFontDescriptorSymbolicTraits) -> Bool } ``` | OptionSet |

Modified [UIFontDescriptorSymbolicTraits.classClarendonSerifs](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptorclassclarendonserifs)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassClarendonSerifs: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var classClarendonSerifs: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.classFreeformSerifs](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptorclassfreeformserifs)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassFreeformSerifs: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var classFreeformSerifs: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.classMask](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptorclassmask)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassMask: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var classMask: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.classModernSerifs](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616734-classmodernserifs)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassModernSerifs: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var classModernSerifs: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.classOldStyleSerifs](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616680-classoldstyleserifs)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassOldStyleSerifs: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var classOldStyleSerifs: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.classOrnamentals](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616716-classornamentals)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassOrnamentals: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var classOrnamentals: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.classSansSerif](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616704-classsansserif)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassSansSerif: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var classSansSerif: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.classScripts](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptorclassscripts)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassScripts: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var classScripts: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.classSlabSerifs](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616740-classslabserifs)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassSlabSerifs: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var classSlabSerifs: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.classSymbolic](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptorclasssymbolic)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassSymbolic: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var classSymbolic: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.classTransitionalSerifs](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616721-classtransitionalserifs)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassTransitionalSerifs: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var classTransitionalSerifs: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.traitBold](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptortraitbold)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitBold: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var traitBold: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.traitCondensed](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptortraitcondensed)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitCondensed: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var traitCondensed: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.traitExpanded](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptortraitexpanded)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitExpanded: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var traitExpanded: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.traitItalic](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptortraititalic)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitItalic: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var traitItalic: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.traitLooseLeading](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616689-traitlooseleading)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitLooseLeading: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var traitLooseLeading: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.traitMonoSpace](https://developer.apple.com/documentation/uikit/uifontdescriptorsymbolictraits/uifontdescriptortraitmonospace)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitMonoSpace: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var traitMonoSpace: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.traitTightLeading](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616694-traittightleading)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitTightLeading: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var traitTightLeading: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.traitUIOptimized](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616737-traituioptimized)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitUIOptimized: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var traitUIOptimized: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontDescriptorSymbolicTraits.traitVertical](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits/1616709-traitvertical)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitVertical: UIFontDescriptorSymbolicTraits { get } ``` |
| To | ``` static var traitVertical: UIFontDescriptorSymbolicTraits { get } ``` |

Modified [UIFontTextStyle.body](https://developer.apple.com/documentation/uikit/uifont/textstyle/1616682-body)

|  | Name | Declaration |
| --- | --- | --- |
| From | UIFontTextStyleBody | ``` let UIFontTextStyleBody: String ``` |
| To | body | ``` static let body: UIFontTextStyle ``` |

Modified [UIFontTextStyle.callout](https://developer.apple.com/documentation/uikit/uifont/textstyle/1616710-callout)

|  | Name | Declaration |
| --- | --- | --- |
| From | UIFontTextStyleCallout | ``` let UIFontTextStyleCallout: String ``` |
| To | callout | ``` static let callout: UIFontTextStyle ``` |

Modified [UIFontTextStyle.caption1](https://developer.apple.com/documentation/uikit/uifonttextstylecaption1)

|  | Name | Declaration |
| --- | --- | --- |
| From | UIFontTextStyleCaption1 | ``` let UIFontTextStyleCaption1: String ``` |
| To | caption1 | ``` static let caption1: UIFontTextStyle ``` |

Modified [UIFontTextStyle.caption2](https://developer.apple.com/documentation/uikit/uifonttextstylecaption2)

|  | Name | Declaration |
| --- | --- | --- |
| From | UIFontTextStyleCaption2 | ``` let UIFontTextStyleCaption2: String ``` |
| To | caption2 | ``` static let caption2: UIFontTextStyle ``` |

Modified [UIFontTextStyle.footnote](https://developer.apple.com/documentation/uikit/uifonttextstylefootnote)

|  | Name | Declaration |
| --- | --- | --- |
| From | UIFontTextStyleFootnote | ``` let UIFontTextStyleFootnote: String ``` |
| To | footnote | ``` static let footnote: UIFontTextStyle ``` |

Modified [UIFontTextStyle.headline](https://developer.apple.com/documentation/uikit/uifonttextstyleheadline)

|  | Name | Declaration |
| --- | --- | --- |
| From | UIFontTextStyleHeadline | ``` let UIFontTextStyleHeadline: String ``` |
| To | headline | ``` static let headline: UIFontTextStyle ``` |

Modified [UIFontTextStyle.subheadline](https://developer.apple.com/documentation/uikit/uifonttextstylesubheadline)

|  | Name | Declaration |
| --- | --- | --- |
| From | UIFontTextStyleSubheadline | ``` let UIFontTextStyleSubheadline: String ``` |
| To | subheadline | ``` static let subheadline: UIFontTextStyle ``` |

Modified [UIFontTextStyle.title1](https://developer.apple.com/documentation/uikit/uifont/textstyle/1616677-title1)

|  | Name | Declaration |
| --- | --- | --- |
| From | UIFontTextStyleTitle1 | ``` let UIFontTextStyleTitle1: String ``` |
| To | title1 | ``` static let title1: UIFontTextStyle ``` |

Modified [UIFontTextStyle.title2](https://developer.apple.com/documentation/uikit/uifonttextstyletitle2)

|  | Name | Declaration |
| --- | --- | --- |
| From | UIFontTextStyleTitle2 | ``` let UIFontTextStyleTitle2: String ``` |
| To | title2 | ``` static let title2: UIFontTextStyle ``` |

Modified [UIFontTextStyle.title3](https://developer.apple.com/documentation/uikit/uifont/textstyle/1616673-title3)

|  | Name | Declaration |
| --- | --- | --- |
| From | UIFontTextStyleTitle3 | ``` let UIFontTextStyleTitle3: String ``` |
| To | title3 | ``` static let title3: UIFontTextStyle ``` |

Modified [UIImage](https://developer.apple.com/documentation/uikit/uiimage)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIImage : NSObject, NSSecureCoding {      init?(named name: String)     class func imageNamed(_ name: String) -> UIImage?      init?(contentsOfFile path: String)     class func imageWithContentsOfFile(_ path: String) -> UIImage?      init?(data data: NSData)     class func imageWithData(_ data: NSData) -> UIImage?      init?(data data: NSData, scale scale: CGFloat)     class func imageWithData(_ data: NSData, scale scale: CGFloat) -> UIImage?      init(CGImage cgImage: CGImage)     class func imageWithCGImage(_ cgImage: CGImage) -> UIImage      init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     class func imageWithCGImage(_ cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage     init?(contentsOfFile path: String)     init?(data data: NSData)     init?(data data: NSData, scale scale: CGFloat)     init(CGImage cgImage: CGImage)     init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     var size: CGSize { get }     var CGImage: CGImage? { get }     var imageOrientation: UIImageOrientation { get }     var scale: CGFloat { get }     class func animatedImageNamed(_ name: String, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: NSTimeInterval) -> UIImage?     class func animatedImageWithImages(_ images: [UIImage], duration duration: NSTimeInterval) -> UIImage?     var images: [UIImage]? { get }     var duration: NSTimeInterval { get }     func drawAtPoint(_ point: CGPoint)     func drawAtPoint(_ point: CGPoint, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawInRect(_ rect: CGRect)     func drawInRect(_ rect: CGRect, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawAsPatternInRect(_ rect: CGRect)     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets) -> UIImage     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode) -> UIImage     var capInsets: UIEdgeInsets { get }     var resizingMode: UIImageResizingMode { get }     func imageWithAlignmentRectInsets(_ alignmentInsets: UIEdgeInsets) -> UIImage     var alignmentRectInsets: UIEdgeInsets { get }     func imageWithRenderingMode(_ renderingMode: UIImageRenderingMode) -> UIImage     var renderingMode: UIImageRenderingMode { get }     func imageFlippedForRightToLeftLayoutDirection() -> UIImage     var flipsForRightToLeftLayoutDirection: Bool { get } } extension UIImage {     required convenience init(imageLiteral name: String) } extension UIImage {     func stretchableImageWithLeftCapWidth(_ leftCapWidth: Int, topCapHeight topCapHeight: Int) -> UIImage     var leftCapWidth: Int { get }     var topCapHeight: Int { get } } extension UIImage {     required convenience init(imageLiteral name: String) } ``` | NSSecureCoding |
| To | ``` class UIImage : NSObject, NSSecureCoding {      init?(named name: String)     class func imageNamed(_ name: String) -> UIImage?      init?(contentsOfFile path: String)     class func withContentsOfFile(_ path: String) -> UIImage?      init?(data data: Data)     class func withData(_ data: Data) -> UIImage?      init?(data data: Data, scale scale: CGFloat)     class func withData(_ data: Data, scale scale: CGFloat) -> UIImage?      init(cgImage cgImage: CGImage)     class func withCGImage(_ cgImage: CGImage) -> UIImage      init(cgImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     class func withCGImage(_ cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage     init?(contentsOfFile path: String)     init?(data data: Data)     init?(data data: Data, scale scale: CGFloat)     init(cgImage cgImage: CGImage)     init(cgImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     var size: CGSize { get }     var cgImage: CGImage? { get }     var imageOrientation: UIImageOrientation { get }     var scale: CGFloat { get }     class func animatedImageNamed(_ name: String, duration duration: TimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: TimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: TimeInterval) -> UIImage?     class func animatedImage(with images: [UIImage], duration duration: TimeInterval) -> UIImage?     var images: [UIImage]? { get }     var duration: TimeInterval { get }     func draw(at point: CGPoint)     func draw(at point: CGPoint, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func draw(in rect: CGRect)     func draw(in rect: CGRect, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawAsPattern(in rect: CGRect)     func resizableImage(withCapInsets capInsets: UIEdgeInsets) -> UIImage     func resizableImage(withCapInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode) -> UIImage     var capInsets: UIEdgeInsets { get }     var resizingMode: UIImageResizingMode { get }     func withAlignmentRectInsets(_ alignmentInsets: UIEdgeInsets) -> UIImage     var alignmentRectInsets: UIEdgeInsets { get }     func withRenderingMode(_ renderingMode: UIImageRenderingMode) -> UIImage     var renderingMode: UIImageRenderingMode { get }     func imageFlippedForRightToLeftLayoutDirection() -> UIImage     var flipsForRightToLeftLayoutDirection: Bool { get }     func withHorizontallyFlippedOrientation() -> UIImage     required convenience init(imageLiteralResourceName name: String)     func stretchableImage(withLeftCapWidth leftCapWidth: Int, topCapHeight topCapHeight: Int) -> UIImage     var leftCapWidth: Int { get }     var topCapHeight: Int { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension UIImage : CVarArg { } extension UIImage : Equatable, Hashable {     var hashValue: Int { get } } extension UIImage {     func stretchableImage(withLeftCapWidth leftCapWidth: Int, topCapHeight topCapHeight: Int) -> UIImage     var leftCapWidth: Int { get }     var topCapHeight: Int { get } } extension UIImage {     required convenience init(imageLiteralResourceName name: String) } ``` | CVarArg, Equatable, Hashable, NSSecureCoding |

Modified [UIImage.animatedImage(with: [UIImage], duration: TimeInterval) -> UIImage? [class]](https://developer.apple.com/documentation/uikit/uiimage/1624149-animatedimage)

|  | Declaration |
| --- | --- |
| From | ``` class func animatedImageWithImages(_ images: [UIImage], duration duration: NSTimeInterval) -> UIImage? ``` |
| To | ``` class func animatedImage(with images: [UIImage], duration duration: TimeInterval) -> UIImage? ``` |

Modified [UIImage.animatedImageNamed(_: String, duration: TimeInterval) -> UIImage? [class]](https://developer.apple.com/documentation/uikit/uiimage/1624094-animatedimagenamed)

|  | Declaration |
| --- | --- |
| From | ``` class func animatedImageNamed(_ name: String, duration duration: NSTimeInterval) -> UIImage? ``` |
| To | ``` class func animatedImageNamed(_ name: String, duration duration: TimeInterval) -> UIImage? ``` |

Modified [UIImage.animatedResizableImageNamed(_: String, capInsets: UIEdgeInsets, duration: TimeInterval) -> UIImage? [class]](https://developer.apple.com/documentation/uikit/uiimage/1624143-animatedresizableimagenamed)

|  | Declaration |
| --- | --- |
| From | ``` class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: NSTimeInterval) -> UIImage? ``` |
| To | ``` class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: TimeInterval) -> UIImage? ``` |

Modified [UIImage.animatedResizableImageNamed(_: String, capInsets: UIEdgeInsets, resizingMode: UIImageResizingMode, duration: TimeInterval) -> UIImage? [class]](https://developer.apple.com/documentation/uikit/uiimage/1624103-animatedresizableimagenamed)

|  | Declaration |
| --- | --- |
| From | ``` class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: NSTimeInterval) -> UIImage? ``` |
| To | ``` class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: TimeInterval) -> UIImage? ``` |

Modified [UIImage.cgImage](https://developer.apple.com/documentation/uikit/uiimage/1624147-cgimage)

|  | Declaration |
| --- | --- |
| From | ``` var CGImage: CGImage? { get } ``` |
| To | ``` var cgImage: CGImage? { get } ``` |

Modified [UIImage.draw(at: CGPoint)](https://developer.apple.com/documentation/uikit/uiimage/1624132-draw)

|  | Declaration |
| --- | --- |
| From | ``` func drawAtPoint(_ point: CGPoint) ``` |
| To | ``` func draw(at point: CGPoint) ``` |

Modified [UIImage.draw(at: CGPoint, blendMode: CGBlendMode, alpha: CGFloat)](https://developer.apple.com/documentation/uikit/uiimage/1624095-draw)

|  | Declaration |
| --- | --- |
| From | ``` func drawAtPoint(_ point: CGPoint, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat) ``` |
| To | ``` func draw(at point: CGPoint, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat) ``` |

Modified [UIImage.draw(in: CGRect)](https://developer.apple.com/documentation/uikit/uiimage/1624092-drawinrect)

|  | Declaration |
| --- | --- |
| From | ``` func drawInRect(_ rect: CGRect) ``` |
| To | ``` func draw(in rect: CGRect) ``` |

Modified [UIImage.draw(in: CGRect, blendMode: CGBlendMode, alpha: CGFloat)](https://developer.apple.com/documentation/uikit/uiimage/1624101-draw)

|  | Declaration |
| --- | --- |
| From | ``` func drawInRect(_ rect: CGRect, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat) ``` |
| To | ``` func draw(in rect: CGRect, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat) ``` |

Modified [UIImage.drawAsPattern(in: CGRect)](https://developer.apple.com/documentation/uikit/uiimage/1624144-drawaspattern)

|  | Declaration |
| --- | --- |
| From | ``` func drawAsPatternInRect(_ rect: CGRect) ``` |
| To | ``` func drawAsPattern(in rect: CGRect) ``` |

Modified [UIImage.duration](https://developer.apple.com/documentation/uikit/uiimage/1624155-duration)

|  | Declaration |
| --- | --- |
| From | ``` var duration: NSTimeInterval { get } ``` |
| To | ``` var duration: TimeInterval { get } ``` |

Modified [UIImage.init(cgImage: CGImage)](https://developer.apple.com/documentation/uikit/uiimage/1624090-initwithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` init(CGImage cgImage: CGImage) ``` |
| To | ``` init(cgImage cgImage: CGImage) ``` |

Modified [UIImage.init(cgImage: CGImage, scale: CGFloat, orientation: UIImageOrientation)](https://developer.apple.com/documentation/uikit/uiimage/1624091-initwithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) ``` |
| To | ``` init(cgImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) ``` |

Modified [UIImage.init(data: Data)](https://developer.apple.com/documentation/uikit/uiimage/1624106-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` init?(data data: NSData) ``` |
| To | ``` init?(data data: Data) ``` |

Modified [UIImage.init(data: Data, scale: CGFloat)](https://developer.apple.com/documentation/uikit/uiimage/1624109-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(data data: NSData, scale scale: CGFloat) ``` |
| To | ``` init?(data data: Data, scale scale: CGFloat) ``` |

Modified [UIImage.resizableImage(withCapInsets: UIEdgeInsets) -> UIImage](https://developer.apple.com/documentation/uikit/uiimage/1624102-resizableimage)

|  | Declaration |
| --- | --- |
| From | ``` func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets) -> UIImage ``` |
| To | ``` func resizableImage(withCapInsets capInsets: UIEdgeInsets) -> UIImage ``` |

Modified [UIImage.resizableImage(withCapInsets: UIEdgeInsets, resizingMode: UIImageResizingMode) -> UIImage](https://developer.apple.com/documentation/uikit/uiimage/1624127-resizableimage)

|  | Declaration |
| --- | --- |
| From | ``` func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode) -> UIImage ``` |
| To | ``` func resizableImage(withCapInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode) -> UIImage ``` |

Modified [UIImage.stretchableImage(withLeftCapWidth: Int, topCapHeight: Int) -> UIImage](https://developer.apple.com/documentation/uikit/uiimage/1624145-stretchableimagewithleftcapwidth)

|  | Declaration |
| --- | --- |
| From | ``` func stretchableImageWithLeftCapWidth(_ leftCapWidth: Int, topCapHeight topCapHeight: Int) -> UIImage ``` |
| To | ``` func stretchableImage(withLeftCapWidth leftCapWidth: Int, topCapHeight topCapHeight: Int) -> UIImage ``` |

Modified [UIImage.withAlignmentRectInsets(_: UIEdgeInsets) -> UIImage](https://developer.apple.com/documentation/uikit/uiimage/1624100-withalignmentrectinsets)

|  | Declaration |
| --- | --- |
| From | ``` func imageWithAlignmentRectInsets(_ alignmentInsets: UIEdgeInsets) -> UIImage ``` |
| To | ``` func withAlignmentRectInsets(_ alignmentInsets: UIEdgeInsets) -> UIImage ``` |

Modified [UIImage.withRenderingMode(_: UIImageRenderingMode) -> UIImage](https://developer.apple.com/documentation/uikit/uiimage/1624153-imagewithrenderingmode)

|  | Declaration |
| --- | --- |
| From | ``` func imageWithRenderingMode(_ renderingMode: UIImageRenderingMode) -> UIImage ``` |
| To | ``` func withRenderingMode(_ renderingMode: UIImageRenderingMode) -> UIImage ``` |

Modified [UIImageOrientation [enum]](https://developer.apple.com/documentation/uikit/uiimageorientation)

|  | Declaration |
| --- | --- |
| From | ``` enum UIImageOrientation : Int {     case Up     case Down     case Left     case Right     case UpMirrored     case DownMirrored     case LeftMirrored     case RightMirrored } ``` |
| To | ``` enum UIImageOrientation : Int {     case up     case down     case left     case right     case upMirrored     case downMirrored     case leftMirrored     case rightMirrored } ``` |

Modified [UIImageOrientation.down](https://developer.apple.com/documentation/uikit/uiimage/orientation/down)

|  | Declaration |
| --- | --- |
| From | ``` case Down ``` |
| To | ``` case down ``` |

Modified [UIImageOrientation.downMirrored](https://developer.apple.com/documentation/uikit/uiimage/orientation/downmirrored)

|  | Declaration |
| --- | --- |
| From | ``` case DownMirrored ``` |
| To | ``` case downMirrored ``` |

Modified [UIImageOrientation.left](https://developer.apple.com/documentation/uikit/uiimage/orientation/left)

|  | Declaration |
| --- | --- |
| From | ``` case Left ``` |
| To | ``` case left ``` |

Modified [UIImageOrientation.leftMirrored](https://developer.apple.com/documentation/uikit/uiimageorientation/uiimageorientationleftmirrored)

|  | Declaration |
| --- | --- |
| From | ``` case LeftMirrored ``` |
| To | ``` case leftMirrored ``` |

Modified [UIImageOrientation.right](https://developer.apple.com/documentation/uikit/uiimageorientation/uiimageorientationright)

|  | Declaration |
| --- | --- |
| From | ``` case Right ``` |
| To | ``` case right ``` |

Modified [UIImageOrientation.rightMirrored](https://developer.apple.com/documentation/uikit/uiimageorientation/uiimageorientationrightmirrored)

|  | Declaration |
| --- | --- |
| From | ``` case RightMirrored ``` |
| To | ``` case rightMirrored ``` |

Modified [UIImageOrientation.up](https://developer.apple.com/documentation/uikit/uiimageorientation/uiimageorientationup)

|  | Declaration |
| --- | --- |
| From | ``` case Up ``` |
| To | ``` case up ``` |

Modified [UIImageOrientation.upMirrored](https://developer.apple.com/documentation/uikit/uiimageorientation/uiimageorientationupmirrored)

|  | Declaration |
| --- | --- |
| From | ``` case UpMirrored ``` |
| To | ``` case upMirrored ``` |

Modified [UIImageRenderingMode [enum]](https://developer.apple.com/documentation/uikit/uiimage/renderingmode)

|  | Declaration |
| --- | --- |
| From | ``` enum UIImageRenderingMode : Int {     case Automatic     case AlwaysOriginal     case AlwaysTemplate } ``` |
| To | ``` enum UIImageRenderingMode : Int {     case automatic     case alwaysOriginal     case alwaysTemplate } ``` |

Modified [UIImageRenderingMode.alwaysOriginal](https://developer.apple.com/documentation/uikit/uiimage/renderingmode/alwaysoriginal)

|  | Declaration |
| --- | --- |
| From | ``` case AlwaysOriginal ``` |
| To | ``` case alwaysOriginal ``` |

Modified [UIImageRenderingMode.alwaysTemplate](https://developer.apple.com/documentation/uikit/uiimage/renderingmode/alwaystemplate)

|  | Declaration |
| --- | --- |
| From | ``` case AlwaysTemplate ``` |
| To | ``` case alwaysTemplate ``` |

Modified [UIImageRenderingMode.automatic](https://developer.apple.com/documentation/uikit/uiimagerenderingmode/uiimagerenderingmodeautomatic)

|  | Declaration |
| --- | --- |
| From | ``` case Automatic ``` |
| To | ``` case automatic ``` |

Modified [UIImageResizingMode [enum]](https://developer.apple.com/documentation/uikit/uiimageresizingmode)

|  | Declaration |
| --- | --- |
| From | ``` enum UIImageResizingMode : Int {     case Tile     case Stretch } ``` |
| To | ``` enum UIImageResizingMode : Int {     case tile     case stretch } ``` |

Modified [UIImageResizingMode.stretch](https://developer.apple.com/documentation/uikit/uiimage/resizingmode/stretch)

|  | Declaration |
| --- | --- |
| From | ``` case Stretch ``` |
| To | ``` case stretch ``` |

Modified [UIImageResizingMode.tile](https://developer.apple.com/documentation/uikit/uiimage/resizingmode/tile)

|  | Declaration |
| --- | --- |
| From | ``` case Tile ``` |
| To | ``` case tile ``` |

Modified [UILocalNotification](https://developer.apple.com/documentation/uikit/uilocalnotification)

|  | Declaration | Protocols | Deprecation |
| --- | --- | --- | --- |
| From | ``` class UILocalNotification : NSObject, NSCopying, NSCoding {     init()     init?(coder aDecoder: NSCoder)     @NSCopying var fireDate: NSDate?     @NSCopying var timeZone: NSTimeZone?     var repeatInterval: NSCalendarUnit     @NSCopying var repeatCalendar: NSCalendar?     @NSCopying var region: CLRegion?     var regionTriggersOnce: Bool     var alertBody: String?     var hasAction: Bool     var alertAction: String?     var alertLaunchImage: String?     var alertTitle: String?     var soundName: String?     var applicationIconBadgeNumber: Int     var userInfo: [NSObject : AnyObject]?     var category: String? } ``` | NSCoding, NSCopying | -- |
| To | ``` class UILocalNotification : NSObject, NSCopying, NSCoding {     init()     init?(coder aDecoder: NSCoder)     var fireDate: Date?     var timeZone: TimeZone?     var repeatInterval: NSCalendar.Unit     var repeatCalendar: Calendar?     @NSCopying var region: CLRegion?     var regionTriggersOnce: Bool     var alertBody: String?     var hasAction: Bool     var alertAction: String?     var alertLaunchImage: String?     var alertTitle: String?     var soundName: String?     var applicationIconBadgeNumber: Int     var userInfo: [AnyHashable : Any]?     var category: String?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension UILocalNotification : CVarArg { } extension UILocalNotification : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying | watchOS 3.0 |

Modified [UILocalNotification.alertAction](https://developer.apple.com/documentation/uikit/uilocalnotification/1616648-alertaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.alertBody](https://developer.apple.com/documentation/uikit/uilocalnotification/1616646-alertbody)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.alertLaunchImage](https://developer.apple.com/documentation/uikit/uilocalnotification/1616660-alertlaunchimage)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.alertTitle](https://developer.apple.com/documentation/uikit/uilocalnotification/1616647-alerttitle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.applicationIconBadgeNumber](https://developer.apple.com/documentation/uikit/uilocalnotification/1616658-applicationiconbadgenumber)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.category](https://developer.apple.com/documentation/uikit/uilocalnotification/1616655-category)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.fireDate](https://developer.apple.com/documentation/uikit/uilocalnotification/1616650-firedate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @NSCopying var fireDate: NSDate? ``` | -- |
| To | ``` var fireDate: Date? ``` | watchOS 3.0 |

Modified [UILocalNotification.hasAction](https://developer.apple.com/documentation/uikit/uilocalnotification/1616649-hasaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.init()](https://developer.apple.com/documentation/uikit/uilocalnotification/1616645-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uilocalnotification/1616653-initwithcoder)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.region](https://developer.apple.com/documentation/uikit/uilocalnotification/1616644-region)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.regionTriggersOnce](https://developer.apple.com/documentation/uikit/uilocalnotification/1616654-regiontriggersonce)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.repeatCalendar](https://developer.apple.com/documentation/uikit/uilocalnotification/1616656-repeatcalendar)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @NSCopying var repeatCalendar: NSCalendar? ``` | -- |
| To | ``` var repeatCalendar: Calendar? ``` | watchOS 3.0 |

Modified [UILocalNotification.repeatInterval](https://developer.apple.com/documentation/uikit/uilocalnotification/1616643-repeatinterval)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var repeatInterval: NSCalendarUnit ``` | -- |
| To | ``` var repeatInterval: NSCalendar.Unit ``` | watchOS 3.0 |

Modified [UILocalNotification.soundName](https://developer.apple.com/documentation/uikit/uilocalnotification/1616651-soundname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.timeZone](https://developer.apple.com/documentation/uikit/uilocalnotification/1616659-timezone)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @NSCopying var timeZone: NSTimeZone? ``` | -- |
| To | ``` var timeZone: TimeZone? ``` | watchOS 3.0 |

Modified [UILocalNotification.userInfo](https://developer.apple.com/documentation/uikit/uilocalnotification/1616657-userinfo)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]? ``` | -- |
| To | ``` var userInfo: [AnyHashable : Any]? ``` | watchOS 3.0 |

Modified [UIOffset [struct]](https://developer.apple.com/documentation/uikit/uioffset)

|  | Declaration |
| --- | --- |
| From | ``` struct UIOffset {     var horizontal: CGFloat     var vertical: CGFloat     init()     init(horizontal horizontal: CGFloat, vertical vertical: CGFloat) } extension UIOffset : Equatable { } extension UIOffset : Equatable { } ``` |
| To | ``` struct UIOffset {     var horizontal: CGFloat     var vertical: CGFloat     init()     init(horizontal horizontal: CGFloat, vertical vertical: CGFloat)     static var zero: UIOffset { get } } extension UIOffset {     static var zero: UIOffset { get } } extension UIOffset : Equatable { } ``` |

Modified [UIRectCorner [struct]](https://developer.apple.com/documentation/uikit/uirectcorner)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIRectCorner : OptionSetType {     init(rawValue rawValue: UInt)     static var TopLeft: UIRectCorner { get }     static var TopRight: UIRectCorner { get }     static var BottomLeft: UIRectCorner { get }     static var BottomRight: UIRectCorner { get }     static var AllCorners: UIRectCorner { get } } ``` | OptionSetType |
| To | ``` struct UIRectCorner : OptionSet {     init(rawValue rawValue: UInt)     static var topLeft: UIRectCorner { get }     static var topRight: UIRectCorner { get }     static var bottomLeft: UIRectCorner { get }     static var bottomRight: UIRectCorner { get }     static var allCorners: UIRectCorner { get }     func intersect(_ other: UIRectCorner) -> UIRectCorner     func exclusiveOr(_ other: UIRectCorner) -> UIRectCorner     mutating func unionInPlace(_ other: UIRectCorner)     mutating func intersectInPlace(_ other: UIRectCorner)     mutating func exclusiveOrInPlace(_ other: UIRectCorner)     func isSubsetOf(_ other: UIRectCorner) -> Bool     func isDisjointWith(_ other: UIRectCorner) -> Bool     func isSupersetOf(_ other: UIRectCorner) -> Bool     mutating func subtractInPlace(_ other: UIRectCorner)     func isStrictSupersetOf(_ other: UIRectCorner) -> Bool     func isStrictSubsetOf(_ other: UIRectCorner) -> Bool } extension UIRectCorner {     func union(_ other: UIRectCorner) -> UIRectCorner     func intersection(_ other: UIRectCorner) -> UIRectCorner     func symmetricDifference(_ other: UIRectCorner) -> UIRectCorner } extension UIRectCorner {     func contains(_ member: UIRectCorner) -> Bool     mutating func insert(_ newMember: UIRectCorner) -> (inserted: Bool, memberAfterInsert: UIRectCorner)     mutating func remove(_ member: UIRectCorner) -> UIRectCorner?     mutating func update(with newMember: UIRectCorner) -> UIRectCorner? } extension UIRectCorner {     convenience init()     mutating func formUnion(_ other: UIRectCorner)     mutating func formIntersection(_ other: UIRectCorner)     mutating func formSymmetricDifference(_ other: UIRectCorner) } extension UIRectCorner {     convenience init<S : Sequence where S.Iterator.Element == UIRectCorner>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: UIRectCorner...)     mutating func subtract(_ other: UIRectCorner)     func isSubset(of other: UIRectCorner) -> Bool     func isSuperset(of other: UIRectCorner) -> Bool     func isDisjoint(with other: UIRectCorner) -> Bool     func subtracting(_ other: UIRectCorner) -> UIRectCorner     var isEmpty: Bool { get }     func isStrictSuperset(of other: UIRectCorner) -> Bool     func isStrictSubset(of other: UIRectCorner) -> Bool } ``` | OptionSet |

Modified [UIRectCorner.allCorners](https://developer.apple.com/documentation/uikit/uirectcorner/1624361-allcorners)

|  | Declaration |
| --- | --- |
| From | ``` static var AllCorners: UIRectCorner { get } ``` |
| To | ``` static var allCorners: UIRectCorner { get } ``` |

Modified [UIRectCorner.bottomLeft](https://developer.apple.com/documentation/uikit/uirectcorner/1624375-bottomleft)

|  | Declaration |
| --- | --- |
| From | ``` static var BottomLeft: UIRectCorner { get } ``` |
| To | ``` static var bottomLeft: UIRectCorner { get } ``` |

Modified [UIRectCorner.bottomRight](https://developer.apple.com/documentation/uikit/uirectcorner/uirectcornerbottomright)

|  | Declaration |
| --- | --- |
| From | ``` static var BottomRight: UIRectCorner { get } ``` |
| To | ``` static var bottomRight: UIRectCorner { get } ``` |

Modified [UIRectCorner.topLeft](https://developer.apple.com/documentation/uikit/uirectcorner/1624339-topleft)

|  | Declaration |
| --- | --- |
| From | ``` static var TopLeft: UIRectCorner { get } ``` |
| To | ``` static var topLeft: UIRectCorner { get } ``` |

Modified [UIRectCorner.topRight](https://developer.apple.com/documentation/uikit/uirectcorner/uirectcornertopright)

|  | Declaration |
| --- | --- |
| From | ``` static var TopRight: UIRectCorner { get } ``` |
| To | ``` static var topRight: UIRectCorner { get } ``` |

Modified [UIRectEdge [struct]](https://developer.apple.com/documentation/uikit/uirectedge)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIRectEdge : OptionSetType {     init(rawValue rawValue: UInt)     static var None: UIRectEdge { get }     static var Top: UIRectEdge { get }     static var Left: UIRectEdge { get }     static var Bottom: UIRectEdge { get }     static var Right: UIRectEdge { get }     static var All: UIRectEdge { get } } ``` | OptionSetType |
| To | ``` struct UIRectEdge : OptionSet {     init(rawValue rawValue: UInt)     static var none: UIRectEdge { get }     static var top: UIRectEdge { get }     static var left: UIRectEdge { get }     static var bottom: UIRectEdge { get }     static var right: UIRectEdge { get }     static var all: UIRectEdge { get }     func intersect(_ other: UIRectEdge) -> UIRectEdge     func exclusiveOr(_ other: UIRectEdge) -> UIRectEdge     mutating func unionInPlace(_ other: UIRectEdge)     mutating func intersectInPlace(_ other: UIRectEdge)     mutating func exclusiveOrInPlace(_ other: UIRectEdge)     func isSubsetOf(_ other: UIRectEdge) -> Bool     func isDisjointWith(_ other: UIRectEdge) -> Bool     func isSupersetOf(_ other: UIRectEdge) -> Bool     mutating func subtractInPlace(_ other: UIRectEdge)     func isStrictSupersetOf(_ other: UIRectEdge) -> Bool     func isStrictSubsetOf(_ other: UIRectEdge) -> Bool } extension UIRectEdge {     func union(_ other: UIRectEdge) -> UIRectEdge     func intersection(_ other: UIRectEdge) -> UIRectEdge     func symmetricDifference(_ other: UIRectEdge) -> UIRectEdge } extension UIRectEdge {     func contains(_ member: UIRectEdge) -> Bool     mutating func insert(_ newMember: UIRectEdge) -> (inserted: Bool, memberAfterInsert: UIRectEdge)     mutating func remove(_ member: UIRectEdge) -> UIRectEdge?     mutating func update(with newMember: UIRectEdge) -> UIRectEdge? } extension UIRectEdge {     convenience init()     mutating func formUnion(_ other: UIRectEdge)     mutating func formIntersection(_ other: UIRectEdge)     mutating func formSymmetricDifference(_ other: UIRectEdge) } extension UIRectEdge {     convenience init<S : Sequence where S.Iterator.Element == UIRectEdge>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: UIRectEdge...)     mutating func subtract(_ other: UIRectEdge)     func isSubset(of other: UIRectEdge) -> Bool     func isSuperset(of other: UIRectEdge) -> Bool     func isDisjoint(with other: UIRectEdge) -> Bool     func subtracting(_ other: UIRectEdge) -> UIRectEdge     var isEmpty: Bool { get }     func isStrictSuperset(of other: UIRectEdge) -> Bool     func isStrictSubset(of other: UIRectEdge) -> Bool } ``` | OptionSet |

Modified [UIRectEdge.all](https://developer.apple.com/documentation/uikit/uirectedge/1624535-all)

|  | Declaration |
| --- | --- |
| From | ``` static var All: UIRectEdge { get } ``` |
| To | ``` static var all: UIRectEdge { get } ``` |

Modified [UIRectEdge.bottom](https://developer.apple.com/documentation/uikit/uirectedge/1624487-bottom)

|  | Declaration |
| --- | --- |
| From | ``` static var Bottom: UIRectEdge { get } ``` |
| To | ``` static var bottom: UIRectEdge { get } ``` |

Modified [UIRectEdge.left](https://developer.apple.com/documentation/uikit/uirectedge/uirectedgeleft)

|  | Declaration |
| --- | --- |
| From | ``` static var Left: UIRectEdge { get } ``` |
| To | ``` static var left: UIRectEdge { get } ``` |

Modified [UIRectEdge.right](https://developer.apple.com/documentation/uikit/uirectedge/1624496-right)

|  | Declaration |
| --- | --- |
| From | ``` static var Right: UIRectEdge { get } ``` |
| To | ``` static var right: UIRectEdge { get } ``` |

Modified [UIRectEdge.top](https://developer.apple.com/documentation/uikit/uirectedge/1624480-top)

|  | Declaration |
| --- | --- |
| From | ``` static var Top: UIRectEdge { get } ``` |
| To | ``` static var top: UIRectEdge { get } ``` |

Modified ==(_: UIEdgeInsets, _: UIEdgeInsets) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ==(_ lhs: UIEdgeInsets, _ rhs: UIEdgeInsets) -> Bool ``` |
| To | ``` func ==(_ lhs: UIEdgeInsets, _ rhs: UIEdgeInsets) -> Bool ``` |

Modified ==(_: UIOffset, _: UIOffset) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ==(_ lhs: UIOffset, _ rhs: UIOffset) -> Bool ``` |
| To | ``` func ==(_ lhs: UIOffset, _ rhs: UIOffset) -> Bool ``` |

Modified [UIGraphicsBeginPDFContextToData(_: NSMutableData, _: CGRect, _: [AnyHashable : Any]?)](https://developer.apple.com/documentation/uikit/1623931-uigraphicsbeginpdfcontexttodata)

|  | Declaration |
| --- | --- |
| From | ``` func UIGraphicsBeginPDFContextToData(_ data: NSMutableData, _ bounds: CGRect, _ documentInfo: [NSObject : AnyObject]?) ``` |
| To | ``` func UIGraphicsBeginPDFContextToData(_ data: NSMutableData, _ bounds: CGRect, _ documentInfo: [AnyHashable : Any]?) ``` |

Modified [UIGraphicsBeginPDFContextToFile(_: String, _: CGRect, _: [AnyHashable : Any]?) -> Bool](https://developer.apple.com/documentation/uikit/1623927-uigraphicsbeginpdfcontexttofile)

|  | Declaration |
| --- | --- |
| From | ``` func UIGraphicsBeginPDFContextToFile(_ path: String, _ bounds: CGRect, _ documentInfo: [NSObject : AnyObject]?) -> Bool ``` |
| To | ``` func UIGraphicsBeginPDFContextToFile(_ path: String, _ bounds: CGRect, _ documentInfo: [AnyHashable : Any]?) -> Bool ``` |

Modified [UIGraphicsBeginPDFPageWithInfo(_: CGRect, _: [AnyHashable : Any]?)](https://developer.apple.com/documentation/uikit/1623915-uigraphicsbeginpdfpagewithinfo)

|  | Declaration |
| --- | --- |
| From | ``` func UIGraphicsBeginPDFPageWithInfo(_ bounds: CGRect, _ pageInfo: [NSObject : AnyObject]?) ``` |
| To | ``` func UIGraphicsBeginPDFPageWithInfo(_ bounds: CGRect, _ pageInfo: [AnyHashable : Any]?) ``` |

Modified [UIGraphicsGetImageFromCurrentImageContext() -> UIImage?](https://developer.apple.com/documentation/uikit/1623924-uigraphicsgetimagefromcurrentima)

|  | Declaration |
| --- | --- |
| From | ``` func UIGraphicsGetImageFromCurrentImageContext() -> UIImage! ``` |
| To | ``` func UIGraphicsGetImageFromCurrentImageContext() -> UIImage? ``` |

Modified [UIGraphicsSetPDFContextURLForRect(_: URL, _: CGRect)](https://developer.apple.com/documentation/uikit/1623916-uigraphicssetpdfcontexturlforrec)

|  | Declaration |
| --- | --- |
| From | ``` func UIGraphicsSetPDFContextURLForRect(_ url: NSURL, _ rect: CGRect) ``` |
| To | ``` func UIGraphicsSetPDFContextURLForRect(_ url: URL, _ rect: CGRect) ``` |

Modified [UIImageJPEGRepresentation(_: UIImage, _: CGFloat) -> Data?](https://developer.apple.com/documentation/uikit/uiimage/1624115-jpegdata)

|  | Declaration |
| --- | --- |
| From | ``` func UIImageJPEGRepresentation(_ image: UIImage, _ compressionQuality: CGFloat) -> NSData? ``` |
| To | ``` func UIImageJPEGRepresentation(_ image: UIImage, _ compressionQuality: CGFloat) -> Data? ``` |

Modified [UIImagePNGRepresentation(_: UIImage) -> Data?](https://developer.apple.com/documentation/uikit/uiimage/1624096-pngdata)

|  | Declaration |
| --- | --- |
| From | ``` func UIImagePNGRepresentation(_ image: UIImage) -> NSData? ``` |
| To | ``` func UIImagePNGRepresentation(_ image: UIImage) -> Data? ``` |

Modified [UILocalNotificationDefaultSoundName](https://developer.apple.com/documentation/uikit/uilocalnotificationdefaultsoundname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

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
