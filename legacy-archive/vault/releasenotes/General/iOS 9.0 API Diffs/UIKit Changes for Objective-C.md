---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/UIKit.html
archived_at: '2026-07-18T02:56:36.940781Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# UIKit Changes for Objective-C

### UIKit

#### NSAttributedString.h

Removed NSMutableAttributedString(NSMutableAttributedStringKitAdditions)Added [-[NSAttributedString containsAttachmentsInRange:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1525086-containsattachments)Added [-[NSAttributedString initWithURL:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1530490-initwithurl)Added [-[NSMutableAttributedString readFromURL:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1524892-readfromurl)Added NSAttributedString(NSAttributedStringKitAdditions)Added NSAttributedString(NSDeprecatedKitAdditions)Added NSMutableAttributedString(NSAttributedStringAttributeFixing)Added NSMutableAttributedString(NSDeprecatedKitAdditions)Added [NSWritingDirectionEmbedding](https://developer.apple.com/documentation/uikit/nswritingdirectionformattype/nswritingdirectionembedding)Added [NSWritingDirectionFormatType](https://developer.apple.com/documentation/appkit/nswritingdirectionformattype)Added [NSWritingDirectionOverride](https://developer.apple.com/documentation/uikit/nswritingdirectionformattype/nswritingdirectionoverride)Modified [-[NSAttributedString dataFromRange:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1534090-datafromrange)

|  | Declaration |
| --- | --- |
| From | ``` - (NSData *)dataFromRange:(NSRange)range documentAttributes:(NSDictionary *)dict error:(NSError **)error ``` |
| To | ``` - (NSData * _Nullable)dataFromRange:(NSRange)range documentAttributes:(NSDictionary<NSString *,id> * _Nonnull)dict error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSAttributedString fileWrapperFromRange:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1530461-filewrapperfromrange)

|  | Declaration |
| --- | --- |
| From | ``` - (NSFileWrapper *)fileWrapperFromRange:(NSRange)range documentAttributes:(NSDictionary *)dict error:(NSError **)error ``` |
| To | ``` - (NSFileWrapper * _Nullable)fileWrapperFromRange:(NSRange)range documentAttributes:(NSDictionary<NSString *,id> * _Nonnull)dict error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSAttributedString initWithData:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1524613-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithData:(NSData *)data options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict error:(NSError **)error ``` |
| To | ``` - (instancetype _Nullable)initWithData:(NSData * _Nonnull)data options:(NSDictionary<NSString *,id> * _Nonnull)options documentAttributes:(NSDictionary<NSString *,id> * _Nullable * _Nullable)dict error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSAttributedString initWithFileURL:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1620492-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[NSMutableAttributedString readFromData:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1535465-readfromdata)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)readFromData:(NSData *)data options:(NSDictionary *)opts documentAttributes:(NSDictionary **)dict error:(NSError **)error ``` |
| To | ``` - (BOOL)readFromData:(NSData * _Nonnull)data options:(NSDictionary<NSString *,id> * _Nonnull)opts documentAttributes:(NSDictionary<NSString *,id> * _Nullable * _Nullable)dict error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSMutableAttributedString readFromFileURL:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1620496-readfromfileurl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [NSTextWritingDirectionEmbedding](https://developer.apple.com/documentation/appkit/nstextwritingdirectionembedding)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [NSTextWritingDirectionOverride](https://developer.apple.com/documentation/uikit/nstextwritingdirection/override)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### NSDataAsset.h (Added)

Added [NSDataAsset](https://developer.apple.com/documentation/uikit/nsdataasset)Added [NSDataAsset.data](https://developer.apple.com/documentation/appkit/nsdataasset/1403437-data)Added [-[NSDataAsset initWithName:]](https://developer.apple.com/documentation/appkit/nsdataasset/1403439-init)Added [-[NSDataAsset initWithName:bundle:]](https://developer.apple.com/documentation/uikit/nsdataasset/1403436-init)Added [NSDataAsset.name](https://developer.apple.com/documentation/uikit/nsdataasset/1403435-name)Added [NSDataAsset.typeIdentifier](https://developer.apple.com/documentation/appkit/nsdataasset/1403434-typeidentifier)

#### NSLayoutAnchor.h (Added)

Added [NSLayoutAnchor](https://developer.apple.com/documentation/appkit/nslayoutanchor)Added [-[NSLayoutAnchor constraintEqualToAnchor:]](https://developer.apple.com/documentation/appkit/nslayoutanchor/1500946-constraint)Added [-[NSLayoutAnchor constraintEqualToAnchor:constant:]](https://developer.apple.com/documentation/uikit/nslayoutanchor/1500937-constraint)Added [-[NSLayoutAnchor constraintGreaterThanOrEqualToAnchor:]](https://developer.apple.com/documentation/uikit/nslayoutanchor/1500936-constraintgreaterthanorequaltoan)Added [-[NSLayoutAnchor constraintGreaterThanOrEqualToAnchor:constant:]](https://developer.apple.com/documentation/appkit/nslayoutanchor/1500948-constraint)Added [-[NSLayoutAnchor constraintLessThanOrEqualToAnchor:]](https://developer.apple.com/documentation/uikit/nslayoutanchor/1500953-constraint)Added [-[NSLayoutAnchor constraintLessThanOrEqualToAnchor:constant:]](https://developer.apple.com/documentation/appkit/nslayoutanchor/1500959-constraint)Added [NSLayoutDimension](https://developer.apple.com/documentation/appkit/nslayoutdimension)Added [-[NSLayoutDimension constraintEqualToAnchor:multiplier:]](https://developer.apple.com/documentation/uikit/nslayoutdimension/1500951-constraint)Added [-[NSLayoutDimension constraintEqualToAnchor:multiplier:constant:]](https://developer.apple.com/documentation/uikit/nslayoutdimension/1500934-constraintequaltoanchor)Added [-[NSLayoutDimension constraintEqualToConstant:]](https://developer.apple.com/documentation/appkit/nslayoutdimension/1500941-constraint)Added [-[NSLayoutDimension constraintGreaterThanOrEqualToAnchor:multiplier:]](https://developer.apple.com/documentation/uikit/nslayoutdimension/1500961-constraint)Added [-[NSLayoutDimension constraintGreaterThanOrEqualToAnchor:multiplier:constant:]](https://developer.apple.com/documentation/uikit/nslayoutdimension/1500965-constraint)Added [-[NSLayoutDimension constraintGreaterThanOrEqualToConstant:]](https://developer.apple.com/documentation/uikit/nslayoutdimension/1500939-constraintgreaterthanorequaltoco)Added [-[NSLayoutDimension constraintLessThanOrEqualToAnchor:multiplier:]](https://developer.apple.com/documentation/appkit/nslayoutdimension/1500943-constraint)Added [-[NSLayoutDimension constraintLessThanOrEqualToAnchor:multiplier:constant:]](https://developer.apple.com/documentation/appkit/nslayoutdimension/1500957-constraint)Added [-[NSLayoutDimension constraintLessThanOrEqualToConstant:]](https://developer.apple.com/documentation/appkit/nslayoutdimension/1500963-constraint)Added [NSLayoutXAxisAnchor](https://developer.apple.com/documentation/appkit/nslayoutxaxisanchor)Added [NSLayoutYAxisAnchor](https://developer.apple.com/documentation/uikit/nslayoutyaxisanchor)

#### NSLayoutConstraint.h

Added [UILayoutSupport.bottomAnchor](https://developer.apple.com/documentation/uikit/uilayoutsupport/1622239-bottomanchor)Added [UILayoutSupport.heightAnchor](https://developer.apple.com/documentation/uikit/uilayoutsupport/1622236-heightanchor)Added [UILayoutSupport.topAnchor](https://developer.apple.com/documentation/uikit/uilayoutsupport/1622255-topanchor)Modified [+[NSLayoutConstraint activateConstraints:]](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526955-activate)

|  | Declaration |
| --- | --- |
| From | ``` + (void)activateConstraints:(NSArray *)constraints ``` |
| To | ``` + (void)activateConstraints:(NSArray<NSLayoutConstraint *> * _Nonnull)constraints ``` |

Modified [+[NSLayoutConstraint constraintsWithVisualFormat:options:metrics:views:]](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526944-constraints)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)constraintsWithVisualFormat:(NSString *)format options:(NSLayoutFormatOptions)opts metrics:(NSDictionary *)metrics views:(NSDictionary *)views ``` |
| To | ``` + (NSArray<__kindof NSLayoutConstraint *> * _Nonnull)constraintsWithVisualFormat:(NSString * _Nonnull)format options:(NSLayoutFormatOptions)opts metrics:(NSDictionary<NSString *,id> * _Nullable)metrics views:(NSDictionary<NSString *,id> * _Nonnull)views ``` |

Modified [+[NSLayoutConstraint deactivateConstraints:]](https://developer.apple.com/documentation/uikit/nslayoutconstraint/1526066-deactivateconstraints)

|  | Declaration |
| --- | --- |
| From | ``` + (void)deactivateConstraints:(NSArray *)constraints ``` |
| To | ``` + (void)deactivateConstraints:(NSArray<NSLayoutConstraint *> * _Nonnull)constraints ``` |

#### NSLayoutManager.h

Added [-[NSLayoutManager CGGlyphAtIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403039-cgglyphatindex)Added [-[NSLayoutManager CGGlyphAtIndex:isValidIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403132-cgglyphatindex)Added [-[NSLayoutManager init]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402975-init)Added [-[NSLayoutManager initWithCoder:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403043-initwithcoder)Added [-[NSLayoutManager lineFragmentRectForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403116-linefragmentrect)Added [-[NSLayoutManager lineFragmentUsedRectForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403035-linefragmentusedrect)Added [-[NSLayoutManager textContainerForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403055-textcontainerforglyphatindex)Added [-[NSLayoutManagerDelegate layoutManager:shouldSetLineFragmentRect:lineFragmentUsedRect:baselineOffset:inTextContainer:forGlyphRange:]](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/1403122-layoutmanager)Added [NSControlCharacterActionContainerBreak](https://developer.apple.com/documentation/uikit/nslayoutmanager/controlcharacteraction/1403148-containerbreak)Added [NSControlCharacterActionHorizontalTab](https://developer.apple.com/documentation/uikit/nslayoutmanager/controlcharacteraction/1403233-horizontaltab)Added [NSControlCharacterActionLineBreak](https://developer.apple.com/documentation/uikit/nscontrolcharacteraction/nscontrolcharacteractionlinebreak)Added [NSControlCharacterActionParagraphBreak](https://developer.apple.com/documentation/appkit/nslayoutmanager/controlcharacteraction/1403231-paragraphbreak)Added [NSControlCharacterActionWhitespace](https://developer.apple.com/documentation/appkit/nscontrolcharacteraction/nscontrolcharacteractionwhitespace)Added [NSControlCharacterActionZeroAdvancement](https://developer.apple.com/documentation/uikit/nslayoutmanager/controlcharacteraction/1403185-zeroadvancement)Added NSLayoutManager(NSLayoutManagerDeprecated)Modified [-[NSLayoutManager glyphAtIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403083-glyphatindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[NSLayoutManager glyphAtIndex:isValidIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403120-glyph)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[NSLayoutManager showCGGlyphs:positions:count:font:matrix:attributes:inContext:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403247-showcgglyphs)

|  | Declaration |
| --- | --- |
| From | ``` - (void)showCGGlyphs:(const CGGlyph *)glyphs positions:(const CGPoint *)positions count:(NSUInteger)glyphCount font:(UIFont *)font matrix:(CGAffineTransform)textMatrix attributes:(NSDictionary *)attributes inContext:(CGContextRef)graphicsContext ``` |
| To | ``` - (void)showCGGlyphs:(const CGGlyph * _Nonnull)glyphs positions:(const CGPoint * _Nonnull)positions count:(NSUInteger)glyphCount font:(UIFont * _Nonnull)font matrix:(CGAffineTransform)textMatrix attributes:(NSDictionary<NSString *,id> * _Nonnull)attributes inContext:(CGContextRef _Nonnull)graphicsContext ``` |

Modified [NSLayoutManager.textContainers](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403144-textcontainers)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *textContainers ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSArray<NSTextContainer *> *textContainers ``` |

Modified [NSTextLayoutOrientationProvider.layoutOrientation](https://developer.apple.com/documentation/uikit/nstextlayoutorientationprovider/1402990-layoutorientation)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) NSTextLayoutOrientation layoutOrientation ``` |
| To | ``` @property(readonly, nonatomic) NSTextLayoutOrientation layoutOrientation ``` |

Modified [NSControlCharacterContainerBreakAction](https://developer.apple.com/documentation/uikit/1619233-anonymous/nscontrolcharactercontainerbreakaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [NSControlCharacterHorizontalTabAction](https://developer.apple.com/documentation/uikit/nscontrolcharacterhorizontaltabaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [NSControlCharacterLineBreakAction](https://developer.apple.com/documentation/uikit/1619233-anonymous/nscontrolcharacterlinebreakaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [NSControlCharacterParagraphBreakAction](https://developer.apple.com/documentation/uikit/1619233-anonymous/nscontrolcharacterparagraphbreakaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [NSControlCharacterWhitespaceAction](https://developer.apple.com/documentation/uikit/nscontrolcharacterwhitespaceaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [NSControlCharacterZeroAdvancementAction](https://developer.apple.com/documentation/uikit/nscontrolcharacterzeroadvancementaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### NSParagraphStyle.h

Added [-[NSMutableParagraphStyle addTabStop:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1525051-addtabstop)Added [NSMutableParagraphStyle.allowsDefaultTighteningForTruncation](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1534136-allowsdefaulttighteningfortrunca)Added [-[NSMutableParagraphStyle removeTabStop:]](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1535084-removetabstop)Added [-[NSMutableParagraphStyle setParagraphStyle:]](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1533980-setparagraphstyle)Added [NSParagraphStyle.allowsDefaultTighteningForTruncation](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1528994-allowsdefaulttighteningfortrunca)Modified [NSMutableParagraphStyle.alignment](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1534368-alignment)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) NSTextAlignment alignment ``` |
| To | ``` @property(nonatomic) NSTextAlignment alignment ``` |

Modified [NSMutableParagraphStyle.baseWritingDirection](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1534601-basewritingdirection)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) NSWritingDirection baseWritingDirection ``` |
| To | ``` @property(nonatomic) NSWritingDirection baseWritingDirection ``` |

Modified [NSMutableParagraphStyle.defaultTabInterval](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1529861-defaulttabinterval)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, nonatomic) CGFloat defaultTabInterval ``` |
| To | ``` @property(nonatomic) CGFloat defaultTabInterval ``` |

Modified [NSMutableParagraphStyle.firstLineHeadIndent](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1528392-firstlineheadindent)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) CGFloat firstLineHeadIndent ``` |
| To | ``` @property(nonatomic) CGFloat firstLineHeadIndent ``` |

Modified [NSMutableParagraphStyle.headIndent](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1525135-headindent)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) CGFloat headIndent ``` |
| To | ``` @property(nonatomic) CGFloat headIndent ``` |

Modified [NSMutableParagraphStyle.hyphenationFactor](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1535553-hyphenationfactor)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) float hyphenationFactor ``` |
| To | ``` @property(nonatomic) float hyphenationFactor ``` |

Modified [NSMutableParagraphStyle.lineBreakMode](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1535126-linebreakmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) NSLineBreakMode lineBreakMode ``` |
| To | ``` @property(nonatomic) NSLineBreakMode lineBreakMode ``` |

Modified [NSMutableParagraphStyle.lineHeightMultiple](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1524596-lineheightmultiple)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) CGFloat lineHeightMultiple ``` |
| To | ``` @property(nonatomic) CGFloat lineHeightMultiple ``` |

Modified [NSMutableParagraphStyle.lineSpacing](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1528742-linespacing)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) CGFloat lineSpacing ``` |
| To | ``` @property(nonatomic) CGFloat lineSpacing ``` |

Modified [NSMutableParagraphStyle.maximumLineHeight](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1524351-maximumlineheight)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) CGFloat maximumLineHeight ``` |
| To | ``` @property(nonatomic) CGFloat maximumLineHeight ``` |

Modified [NSMutableParagraphStyle.minimumLineHeight](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1531118-minimumlineheight)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) CGFloat minimumLineHeight ``` |
| To | ``` @property(nonatomic) CGFloat minimumLineHeight ``` |

Modified [NSMutableParagraphStyle.paragraphSpacing](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1532528-paragraphspacing)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) CGFloat paragraphSpacing ``` |
| To | ``` @property(nonatomic) CGFloat paragraphSpacing ``` |

Modified [NSMutableParagraphStyle.paragraphSpacingBefore](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1527729-paragraphspacingbefore)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) CGFloat paragraphSpacingBefore ``` |
| To | ``` @property(nonatomic) CGFloat paragraphSpacingBefore ``` |

Modified [NSMutableParagraphStyle.tabStops](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1531988-tabstops)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy, nonatomic) NSArray *tabStops ``` |
| To | ``` @property(copy, nonatomic) NSArray<NSTextTab *> * _Null_unspecified tabStops ``` |

Modified [NSMutableParagraphStyle.tailIndent](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1531666-tailindent)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) CGFloat tailIndent ``` |
| To | ``` @property(nonatomic) CGFloat tailIndent ``` |

Modified [NSParagraphStyle](https://developer.apple.com/documentation/uikit/nsparagraphstyle)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [NSParagraphStyle.alignment](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1532321-alignment)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSTextAlignment alignment ``` |
| To | ``` @property(readonly, nonatomic) NSTextAlignment alignment ``` |

Modified [NSParagraphStyle.baseWritingDirection](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1527354-basewritingdirection)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSWritingDirection baseWritingDirection ``` |
| To | ``` @property(readonly, nonatomic) NSWritingDirection baseWritingDirection ``` |

Modified [NSParagraphStyle.firstLineHeadIndent](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1527764-firstlineheadindent)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGFloat firstLineHeadIndent ``` |
| To | ``` @property(readonly, nonatomic) CGFloat firstLineHeadIndent ``` |

Modified [NSParagraphStyle.headIndent](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1530760-headindent)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGFloat headIndent ``` |
| To | ``` @property(readonly, nonatomic) CGFloat headIndent ``` |

Modified [NSParagraphStyle.hyphenationFactor](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1529275-hyphenationfactor)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) float hyphenationFactor ``` |
| To | ``` @property(readonly, nonatomic) float hyphenationFactor ``` |

Modified [NSParagraphStyle.lineBreakMode](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1529937-linebreakmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSLineBreakMode lineBreakMode ``` |
| To | ``` @property(readonly, nonatomic) NSLineBreakMode lineBreakMode ``` |

Modified [NSParagraphStyle.lineHeightMultiple](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1528614-lineheightmultiple)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGFloat lineHeightMultiple ``` |
| To | ``` @property(readonly, nonatomic) CGFloat lineHeightMultiple ``` |

Modified [NSParagraphStyle.lineSpacing](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1524635-linespacing)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGFloat lineSpacing ``` |
| To | ``` @property(readonly, nonatomic) CGFloat lineSpacing ``` |

Modified [NSParagraphStyle.maximumLineHeight](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1533343-maximumlineheight)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGFloat maximumLineHeight ``` |
| To | ``` @property(readonly, nonatomic) CGFloat maximumLineHeight ``` |

Modified [NSParagraphStyle.minimumLineHeight](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1535639-minimumlineheight)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGFloat minimumLineHeight ``` |
| To | ``` @property(readonly, nonatomic) CGFloat minimumLineHeight ``` |

Modified [NSParagraphStyle.paragraphSpacing](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1530912-paragraphspacing)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGFloat paragraphSpacing ``` |
| To | ``` @property(readonly, nonatomic) CGFloat paragraphSpacing ``` |

Modified [NSParagraphStyle.paragraphSpacingBefore](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1533011-paragraphspacingbefore)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGFloat paragraphSpacingBefore ``` |
| To | ``` @property(readonly, nonatomic) CGFloat paragraphSpacingBefore ``` |

Modified [NSParagraphStyle.tabStops](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1532841-tabstops)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *tabStops ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<NSTextTab *> *tabStops ``` |

Modified [NSParagraphStyle.tailIndent](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1525556-tailindent)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGFloat tailIndent ``` |
| To | ``` @property(readonly, nonatomic) CGFloat tailIndent ``` |

Modified [NSTextTab.alignment](https://developer.apple.com/documentation/appkit/nstexttab/1527212-alignment)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSTextAlignment alignment ``` |
| To | ``` @property(readonly, nonatomic) NSTextAlignment alignment ``` |

Modified [-[NSTextTab initWithTextAlignment:location:options:]](https://developer.apple.com/documentation/uikit/nstexttab/1526080-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithTextAlignment:(NSTextAlignment)alignment location:(CGFloat)loc options:(NSDictionary *)options ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithTextAlignment:(NSTextAlignment)alignment location:(CGFloat)loc options:(NSDictionary<NSString *,id> * _Nonnull)options ``` | yes |

Modified [NSTextTab.location](https://developer.apple.com/documentation/appkit/nstexttab/1527968-location)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGFloat location ``` |
| To | ``` @property(readonly, nonatomic) CGFloat location ``` |

Modified [NSTextTab.options](https://developer.apple.com/documentation/appkit/nstexttab/1534965-options)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDictionary *options ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSDictionary<NSString *,id> *options ``` |

#### NSShadow.h

Added [-[NSShadow init]](https://developer.apple.com/documentation/appkit/nsshadow/1429853-init)Added [-[NSShadow initWithCoder:]](https://developer.apple.com/documentation/uikit/nsshadow/1623903-init)Modified [NSShadow.shadowColor](https://developer.apple.com/documentation/uikit/nsshadow/1429855-shadowcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) id shadowColor ``` |
| To | ``` @property(nonatomic, strong, nullable) id shadowColor ``` |

#### NSStringDrawing.h

Added NSStringDrawingContext(NSStringDrawingContextDeprecated)Modified [-[NSString boundingRectWithSize:options:attributes:context:]](https://developer.apple.com/documentation/foundation/nsstring/1524729-boundingrect)

|  | Declaration |
| --- | --- |
| From | ``` - (CGRect)boundingRectWithSize:(CGSize)size options:(NSStringDrawingOptions)options attributes:(NSDictionary *)attributes context:(NSStringDrawingContext *)context ``` |
| To | ``` - (CGRect)boundingRectWithSize:(CGSize)size options:(NSStringDrawingOptions)options attributes:(NSDictionary<NSString *,id> * _Nullable)attributes context:(NSStringDrawingContext * _Nullable)context ``` |

Modified [-[NSString drawAtPoint:withAttributes:]](https://developer.apple.com/documentation/foundation/nsstring/1533109-drawatpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (void)drawAtPoint:(CGPoint)point withAttributes:(NSDictionary *)attrs ``` |
| To | ``` - (void)drawAtPoint:(CGPoint)point withAttributes:(NSDictionary<NSString *,id> * _Nullable)attrs ``` |

Modified [-[NSString drawInRect:withAttributes:]](https://developer.apple.com/documentation/foundation/nsstring/1529855-drawinrect)

|  | Declaration |
| --- | --- |
| From | ``` - (void)drawInRect:(CGRect)rect withAttributes:(NSDictionary *)attrs ``` |
| To | ``` - (void)drawInRect:(CGRect)rect withAttributes:(NSDictionary<NSString *,id> * _Nullable)attrs ``` |

Modified [-[NSString drawWithRect:options:attributes:context:]](https://developer.apple.com/documentation/foundation/nsstring/1530195-drawwithrect)

|  | Declaration |
| --- | --- |
| From | ``` - (void)drawWithRect:(CGRect)rect options:(NSStringDrawingOptions)options attributes:(NSDictionary *)attributes context:(NSStringDrawingContext *)context ``` |
| To | ``` - (void)drawWithRect:(CGRect)rect options:(NSStringDrawingOptions)options attributes:(NSDictionary<NSString *,id> * _Nullable)attributes context:(NSStringDrawingContext * _Nullable)context ``` |

Modified [-[NSString sizeWithAttributes:]](https://developer.apple.com/documentation/foundation/nsstring/1531844-size)

|  | Declaration |
| --- | --- |
| From | ``` - (CGSize)sizeWithAttributes:(NSDictionary *)attrs ``` |
| To | ``` - (CGSize)sizeWithAttributes:(NSDictionary<NSString *,id> * _Nullable)attrs ``` |

Modified [NSStringDrawingContext.actualScaleFactor](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/1531498-actualscalefactor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) CGFloat actualScaleFactor ``` |
| To | ``` @property(readonly, nonatomic) CGFloat actualScaleFactor ``` |

Modified [NSStringDrawingContext.totalBounds](https://developer.apple.com/documentation/appkit/nsstringdrawingcontext/1530525-totalbounds)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) CGRect totalBounds ``` |
| To | ``` @property(readonly, nonatomic) CGRect totalBounds ``` |

#### NSTextAttachment.h

Modified [NSTextAttachment.contents](https://developer.apple.com/documentation/appkit/nstextattachment/1508401-contents)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) NSData *contents ``` |
| To | ``` @property(copy, nonatomic, nullable) NSData *contents ``` |

Modified [NSTextAttachment.fileType](https://developer.apple.com/documentation/uikit/nstextattachment/1508416-filetype)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) NSString *fileType ``` |
| To | ``` @property(copy, nonatomic, nullable) NSString *fileType ``` |

Modified [NSTextAttachment.fileWrapper](https://developer.apple.com/documentation/uikit/nstextattachment/1508398-filewrapper)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) NSFileWrapper *fileWrapper ``` |
| To | ``` @property(strong, nonatomic, nullable) NSFileWrapper *fileWrapper ``` |

Modified [NSTextAttachment.image](https://developer.apple.com/documentation/uikit/nstextattachment/1508378-image)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) UIImage *image ``` |
| To | ``` @property(strong, nonatomic, nullable) UIImage *image ``` |

Modified [-[NSTextAttachment initWithData:ofType:]](https://developer.apple.com/documentation/appkit/nstextattachment/1508374-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSTextContainer.h

Added [-[NSTextContainer initWithCoder:]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444573-initwithcoder)Added [-[NSTextContainer replaceLayoutManager:]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444545-replacelayoutmanager)Added [NSTextContainer.simpleRectangularTextContainer](https://developer.apple.com/documentation/appkit/nstextcontainer/1444525-simplerectangulartextcontainer)Modified [NSTextContainer.exclusionPaths](https://developer.apple.com/documentation/uikit/nstextcontainer/1444569-exclusionpaths)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, nonatomic) NSArray *exclusionPaths ``` |
| To | ``` @property(copy, nonatomic, nonnull) NSArray<UIBezierPath *> *exclusionPaths ``` |

Modified [-[NSTextContainer initWithSize:]](https://developer.apple.com/documentation/uikit/nstextcontainer/1444529-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSTextStorage.h

Modified [NSTextStorage.changeInLength](https://developer.apple.com/documentation/uikit/nstextstorage/1528400-changeinlength)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) NSInteger changeInLength ``` |
| To | ``` @property(readonly, nonatomic) NSInteger changeInLength ``` |

Modified [NSTextStorage.editedMask](https://developer.apple.com/documentation/appkit/nstextstorage/1525323-editedmask)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) NSTextStorageEditActions editedMask ``` |
| To | ``` @property(readonly, nonatomic) NSTextStorageEditActions editedMask ``` |

Modified [NSTextStorage.editedRange](https://developer.apple.com/documentation/appkit/nstextstorage/1524379-editedrange)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) NSRange editedRange ``` |
| To | ``` @property(readonly, nonatomic) NSRange editedRange ``` |

Modified [NSTextStorage.layoutManagers](https://developer.apple.com/documentation/uikit/nstextstorage/1527938-layoutmanagers)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *layoutManagers ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<NSLayoutManager *> *layoutManagers ``` |

#### UIAccelerometer.h

Modified [UIAccelerometer.delegate](https://developer.apple.com/documentation/uikit/uiaccelerometer/1620646-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIAccelerometerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIAccelerometerDelegate> delegate ``` |

#### UIAccessibility.h

Added [-[NSObject accessibilityAssistiveTechnologyFocusedIdentifiers]](https://developer.apple.com/documentation/objectivec/nsobject/1615206-accessibilityassistivetechnology)Added [UIAccessibilityFocusedElement()](https://developer.apple.com/documentation/uikit/1615119-uiaccessibilityfocusedelement)Added [UIAccessibilityIsShakeToUndoEnabled()](https://developer.apple.com/documentation/uikit/1615103-uiaccessibilityisshaketoundoenab)Added [UIAccessibilityShakeToUndoDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/1615095-shaketoundodidchangenotification)Modified [NSObject.accessibilityCustomActions](https://developer.apple.com/documentation/objectivec/nsobject/1615150-accessibilitycustomactions)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSArray *accessibilityCustomActions ``` |
| To | ``` @property(nonatomic, strong, nullable) NSArray<UIAccessibilityCustomAction *> *accessibilityCustomActions ``` |

Modified [NSObject.accessibilityLanguage](https://developer.apple.com/documentation/objectivec/nsobject/1615192-accessibilitylanguage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSString *accessibilityLanguage ``` |
| To | ``` @property(nonatomic, strong, nullable) NSString *accessibilityLanguage ``` |

#### UIAccessibilityConstants.h

Added [UIAccessibilityAssistiveTechnologyKey](https://developer.apple.com/documentation/uikit/uiaccessibilityassistivetechnologykey)Added [UIAccessibilityElementFocusedNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/1620210-elementfocusednotification)Added [UIAccessibilityFocusedElementKey](https://developer.apple.com/documentation/uikit/uiaccessibilityfocusedelementkey)Added [UIAccessibilityNotificationVoiceOverIdentifier](https://developer.apple.com/documentation/uikit/uiaccessibilitynotificationvoiceoveridentifier)Added [UIAccessibilityUnfocusedElementKey](https://developer.apple.com/documentation/uikit/uiaccessibility/1620196-unfocusedelementuserinfokey)

#### UIAccessibilityElement.h

Modified [UIAccessibilityElement.accessibilityHint](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/1619585-accessibilityhint)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSString *accessibilityHint ``` |
| To | ``` @property(nonatomic, strong, nullable) NSString *accessibilityHint ``` |

Modified [UIAccessibilityElement.accessibilityLabel](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/1619577-accessibilitylabel)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSString *accessibilityLabel ``` |
| To | ``` @property(nonatomic, strong, nullable) NSString *accessibilityLabel ``` |

Modified [UIAccessibilityElement.accessibilityValue](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/1619583-accessibilityvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSString *accessibilityValue ``` |
| To | ``` @property(nonatomic, strong, nullable) NSString *accessibilityValue ``` |

#### UIActionSheet.h

Modified [UIActionSheet](https://developer.apple.com/documentation/uikit/uiactionsheet)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.actionSheetStyle](https://developer.apple.com/documentation/uikit/uiactionsheet/1622881-actionsheetstyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheet addButtonWithTitle:]](https://developer.apple.com/documentation/uikit/uiactionsheet/1622864-addbutton)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheet buttonTitleAtIndex:]](https://developer.apple.com/documentation/uikit/uiactionsheet/1622871-buttontitle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.cancelButtonIndex](https://developer.apple.com/documentation/uikit/uiactionsheet/1622866-cancelbuttonindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.delegate](https://developer.apple.com/documentation/uikit/uiactionsheet/1622878-delegate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, assign) id<UIActionSheetDelegate> delegate ``` | -- |
| To | ``` @property(nonatomic, weak, nullable) id<UIActionSheetDelegate> delegate ``` | iOS 8.3 |

Modified [UIActionSheet.destructiveButtonIndex](https://developer.apple.com/documentation/uikit/uiactionsheet/1622863-destructivebuttonindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheet dismissWithClickedButtonIndex:animated:]](https://developer.apple.com/documentation/uikit/uiactionsheet/1622888-dismisswithclickedbuttonindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.firstOtherButtonIndex](https://developer.apple.com/documentation/uikit/uiactionsheet/1622870-firstotherbuttonindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheet initWithTitle:delegate:cancelButtonTitle:destructiveButtonTitle:otherButtonTitles:]](https://developer.apple.com/documentation/uikit/uiactionsheet/1622875-initwithtitle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.numberOfButtons](https://developer.apple.com/documentation/uikit/uiactionsheet/1622891-numberofbuttons)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheet showFromBarButtonItem:animated:]](https://developer.apple.com/documentation/uikit/uiactionsheet/1622869-showfrombarbuttonitem)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheet showFromRect:inView:animated:]](https://developer.apple.com/documentation/uikit/uiactionsheet/1622892-showfromrect)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheet showFromTabBar:]](https://developer.apple.com/documentation/uikit/uiactionsheet/1622872-show)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheet showFromToolbar:]](https://developer.apple.com/documentation/uikit/uiactionsheet/1622874-showfromtoolbar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheet showInView:]](https://developer.apple.com/documentation/uikit/uiactionsheet/1622886-show)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.title](https://developer.apple.com/documentation/uikit/uiactionsheet/1622882-title)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.visible](https://developer.apple.com/documentation/uikit/uiactionsheet/1622885-visible)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheetDelegate actionSheet:clickedButtonAtIndex:]](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622876-actionsheet)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheetDelegate actionSheet:didDismissWithButtonIndex:]](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622879-actionsheet)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheetDelegate actionSheet:willDismissWithButtonIndex:]](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622884-actionsheet)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheetDelegate actionSheetCancel:]](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622867-actionsheetcancel)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheetDelegate didPresentActionSheet:]](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622877-didpresent)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [-[UIActionSheetDelegate willPresentActionSheet:]](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622865-willpresentactionsheet)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

#### UIActivity.h

Added [UIActivityTypeOpenInIBooks](https://developer.apple.com/documentation/uikit/uiactivitytypeopeninibooks)

#### UIActivityIndicatorView.h

Added [-[UIActivityIndicatorView initWithCoder:]](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/1622844-init)Added [-[UIActivityIndicatorView initWithFrame:]](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/1622841-init)Modified [UIActivityIndicatorView.color](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/1622836-color)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, nonatomic, retain) UIColor *color ``` |
| To | ``` @property(readwrite, nonatomic, strong, nullable) UIColor *color ``` |

Modified [-[UIActivityIndicatorView initWithActivityIndicatorStyle:]](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/1622840-initwithactivityindicatorstyle)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### UIActivityItemProvider.h

Modified [UIActivityItemProvider.activityType](https://developer.apple.com/documentation/uikit/uiactivityitemprovider/1620459-activitytype)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *activityType ``` |
| To | ``` @property(nonatomic, copy, readonly, nullable) NSString *activityType ``` |

Modified [-[UIActivityItemProvider initWithPlaceholderItem:]](https://developer.apple.com/documentation/uikit/uiactivityitemprovider/1620463-initwithplaceholderitem)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIActivityItemProvider.placeholderItem](https://developer.apple.com/documentation/uikit/uiactivityitemprovider/1620454-placeholderitem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain, readonly) id placeholderItem ``` |
| To | ``` @property(nonatomic, strong, readonly, nullable) id placeholderItem ``` |

#### UIActivityViewController.h

Modified [UIActivityViewController.excludedActivityTypes](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/1622009-excludedactivitytypes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *excludedActivityTypes ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *excludedActivityTypes ``` |

Modified [-[UIActivityViewController initWithActivityItems:applicationActivities:]](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/1622019-initwithactivityitems)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithActivityItems:(NSArray *)activityItems applicationActivities:(NSArray *)applicationActivities ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithActivityItems:(NSArray * _Nonnull)activityItems applicationActivities:(NSArray<__kindof UIActivity *> * _Nullable)applicationActivities ``` | yes |

#### UIAlertController.h

Added [UIAlertController.preferredAction](https://developer.apple.com/documentation/uikit/uialertcontroller/1620102-preferredaction)Modified [UIAlertController.actions](https://developer.apple.com/documentation/uikit/uialertcontroller/1620099-actions)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *actions ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<UIAlertAction *> *actions ``` |

Modified [UIAlertController.textFields](https://developer.apple.com/documentation/uikit/uialertcontroller/1620104-textfields)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *textFields ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<UITextField *> *textFields ``` |

#### UIAlertView.h

Added [-[UIAlertView initWithCoder:]](https://developer.apple.com/documentation/uikit/uialertview/1620779-initwithcoder)Added [-[UIAlertView initWithFrame:]](https://developer.apple.com/documentation/uikit/uialertview/1620759-initwithframe)Modified [UIAlertView](https://developer.apple.com/documentation/uikit/uialertview)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIAlertView addButtonWithTitle:]](https://developer.apple.com/documentation/uikit/uialertview/1620761-addbuttonwithtitle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.alertViewStyle](https://developer.apple.com/documentation/uikit/uialertview/1620780-alertviewstyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIAlertView buttonTitleAtIndex:]](https://developer.apple.com/documentation/uikit/uialertview/1620756-buttontitleatindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.cancelButtonIndex](https://developer.apple.com/documentation/uikit/uialertview/1620766-cancelbuttonindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.delegate](https://developer.apple.com/documentation/uikit/uialertview/1620769-delegate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, assign) id delegate ``` | -- |
| To | ``` @property(nonatomic, weak, nullable) id delegate ``` | iOS 9.0 |

Modified [-[UIAlertView dismissWithClickedButtonIndex:animated:]](https://developer.apple.com/documentation/uikit/uialertview/1620754-dismisswithclickedbuttonindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.firstOtherButtonIndex](https://developer.apple.com/documentation/uikit/uialertview/1620771-firstotherbuttonindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIAlertView initWithTitle:message:delegate:cancelButtonTitle:otherButtonTitles:]](https://developer.apple.com/documentation/uikit/uialertview/1620765-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.message](https://developer.apple.com/documentation/uikit/uialertview/1620758-message)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.numberOfButtons](https://developer.apple.com/documentation/uikit/uialertview/1620753-numberofbuttons)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIAlertView show]](https://developer.apple.com/documentation/uikit/uialertview/1620751-show)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIAlertView textFieldAtIndex:]](https://developer.apple.com/documentation/uikit/uialertview/1620757-textfieldatindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.title](https://developer.apple.com/documentation/uikit/uialertview/1620768-title)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.visible](https://developer.apple.com/documentation/uikit/uialertview/1620764-isvisible)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIAlertViewDelegate alertView:clickedButtonAtIndex:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620752-alertview)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIAlertViewDelegate alertView:didDismissWithButtonIndex:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620772-alertview)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIAlertViewDelegate alertView:willDismissWithButtonIndex:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620763-alertview)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIAlertViewDelegate alertViewCancel:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620778-alertviewcancel)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIAlertViewDelegate alertViewShouldEnableFirstOtherButton:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620774-alertviewshouldenablefirstotherb)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [-[UIAlertViewDelegate didPresentAlertView:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620750-didpresent)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIAlertViewDelegate willPresentAlertView:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620767-willpresent)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### UIAppearance.h

Added [+[UIAppearance appearanceForTraitCollection:whenContainedInInstancesOfClasses:]](https://developer.apple.com/documentation/uikit/uiappearance/1615008-appearancefortraitcollection)Added [+[UIAppearance appearanceWhenContainedInInstancesOfClasses:]](https://developer.apple.com/documentation/uikit/uiappearance/1615013-appearancewhencontainedininstanc)Modified [+[UIAppearance appearanceForTraitCollection:whenContainedIn:]](https://developer.apple.com/documentation/uikit/uiappearance/1615012-appearancefortraitcollection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [+[UIAppearance appearanceWhenContainedIn:]](https://developer.apple.com/documentation/uikit/uiappearance/1615006-appearancewhencontainedin)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### UIApplication.h

Added [UIApplication.shortcutItems](https://developer.apple.com/documentation/uikit/uiapplication/1623033-shortcutitems)Added [-[UIApplicationDelegate application:handleActionWithIdentifier:forLocalNotification:withResponseInfo:completionHandler:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623105-application)Added [-[UIApplicationDelegate application:handleActionWithIdentifier:forRemoteNotification:withResponseInfo:completionHandler:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623021-application)Added [-[UIApplicationDelegate application:openURL:options:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623112-application)Added [-[UIApplicationDelegate application:performActionForShortcutItem:completionHandler:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622935-application)Added [-[UIApplicationDelegate applicationShouldRequestHealthAuthorization:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622998-applicationshouldrequesthealthau)Added UIApplication(UIShortcutItems)Added [UIApplicationLaunchOptionsShortcutItemKey](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/1622972-shortcutitem)Added [UIApplicationOpenURLOptionsAnnotationKey](https://developer.apple.com/documentation/uikit/uiapplicationopenurloptionsannotationkey)Added [UIApplicationOpenURLOptionsOpenInPlaceKey](https://developer.apple.com/documentation/uikit/uiapplicationopenurloptionsopeninplacekey)Added [UIApplicationOpenURLOptionsSourceApplicationKey](https://developer.apple.com/documentation/uikit/uiapplication/openurloptionskey/1623128-sourceapplication)Modified [UIApplication](https://developer.apple.com/documentation/uikit/uiapplication)

|  | Protocols |
| --- | --- |
| From | UIActionSheetDelegate |
| To | -- |

Modified [-[UIApplication beginBackgroundTaskWithExpirationHandler:]](https://developer.apple.com/documentation/uikit/uiapplication/1623031-beginbackgroundtaskwithexpiratio)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplication beginBackgroundTaskWithName:expirationHandler:]](https://developer.apple.com/documentation/uikit/uiapplication/1623051-beginbackgroundtask)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplication clearKeepAliveTimeout]](https://developer.apple.com/documentation/uikit/uiapplication/1622986-clearkeepalivetimeout)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIApplication endBackgroundTask:]](https://developer.apple.com/documentation/uikit/uiapplication/1622970-endbackgroundtask)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIApplication.scheduledLocalNotifications](https://developer.apple.com/documentation/uikit/uiapplication/1622993-scheduledlocalnotifications)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *scheduledLocalNotifications ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<UILocalNotification *> *scheduledLocalNotifications ``` |

Modified [-[UIApplication setKeepAliveTimeout:handler:]](https://developer.apple.com/documentation/uikit/uiapplication/1622989-setkeepalivetimeout)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIApplication setNewsstandIconImage:]](https://developer.apple.com/documentation/uikit/uiapplication/1623016-setnewsstandiconimage)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 9.0 | iOS 9.0 |

Modified [-[UIApplication setStatusBarHidden:withAnimation:]](https://developer.apple.com/documentation/uikit/uiapplication/1622949-setstatusbarhidden)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIApplication setStatusBarOrientation:animated:]](https://developer.apple.com/documentation/uikit/uiapplication/1622939-setstatusbarorientation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIApplication setStatusBarStyle:animated:]](https://developer.apple.com/documentation/uikit/uiapplication/1622923-setstatusbarstyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIApplication.statusBarHidden](https://developer.apple.com/documentation/uikit/uiapplication/1622982-statusbarhidden)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, getter=isStatusBarHidden) BOOL statusBarHidden ``` | -- |
| To | ``` @property(readonly, nonatomic, getter=isStatusBarHidden) BOOL statusBarHidden ``` | iOS 9.0 |

Modified [UIApplication.statusBarOrientation](https://developer.apple.com/documentation/uikit/uiapplication/1623026-statusbarorientation)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic) UIInterfaceOrientation statusBarOrientation ``` | -- |
| To | ``` @property(readonly, nonatomic) UIInterfaceOrientation statusBarOrientation ``` | iOS 9.0 |

Modified [UIApplication.statusBarStyle](https://developer.apple.com/documentation/uikit/uiapplication/1622988-statusbarstyle)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic) UIStatusBarStyle statusBarStyle ``` | -- |
| To | ``` @property(readonly, nonatomic) UIStatusBarStyle statusBarStyle ``` | iOS 9.0 |

Modified [-[UIApplication supportedInterfaceOrientationsForWindow:]](https://developer.apple.com/documentation/uikit/uiapplication/1623091-supportedinterfaceorientations)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)supportedInterfaceOrientationsForWindow:(UIWindow *)window ``` |
| To | ``` - (UIInterfaceOrientationMask)supportedInterfaceOrientationsForWindow:(UIWindow * _Nullable)window ``` |

Modified [UIApplication.windows](https://developer.apple.com/documentation/uikit/uiapplication/1623104-windows)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *windows ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<__kindof UIWindow *> *windows ``` |

Modified [-[UIApplicationDelegate application:handleOpenURL:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622964-application)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIApplicationDelegate application:openURL:sourceApplication:annotation:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623073-application)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIApplicationDelegate application:supportedInterfaceOrientationsForWindow:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623107-application)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)application:(UIApplication *)application supportedInterfaceOrientationsForWindow:(UIWindow *)window ``` |
| To | ``` - (UIInterfaceOrientationMask)application:(UIApplication * _Nonnull)application supportedInterfaceOrientationsForWindow:(UIWindow * _Nullable)window ``` |

Modified [UIApplicationDelegate.window](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623056-window)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIWindow *window ``` |
| To | ``` @property(nonatomic, strong, nullable) UIWindow *window ``` |

Modified [UIUserInterfaceLayoutDirection](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIView.h |

Modified [UIUserInterfaceLayoutDirectionLeftToRight](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection/lefttoright)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIView.h |

Modified [UIUserInterfaceLayoutDirectionRightToLeft](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection/righttoleft)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIView.h |

#### UIApplicationShortcutItem.h (Added)

Added [UIApplicationShortcutIcon](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon)Added [+[UIApplicationShortcutIcon iconWithTemplateImageName:]](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/1623367-init)Added [+[UIApplicationShortcutIcon iconWithType:]](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/1623389-init)Added [UIApplicationShortcutItem](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem)Added [UIApplicationShortcutItem.icon](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623352-icon)Added [-[UIApplicationShortcutItem initWithType:localizedTitle:]](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623355-init)Added [-[UIApplicationShortcutItem initWithType:localizedTitle:localizedSubtitle:icon:userInfo:]](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623372-init)Added [UIApplicationShortcutItem.localizedSubtitle](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623376-localizedsubtitle)Added [UIApplicationShortcutItem.localizedTitle](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623354-localizedtitle)Added [UIApplicationShortcutItem.type](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623382-type)Added [UIApplicationShortcutItem.userInfo](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623370-userinfo)Added [UIMutableApplicationShortcutItem](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem)Added [UIMutableApplicationShortcutItem.icon](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/1623351-icon)Added [UIMutableApplicationShortcutItem.localizedSubtitle](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/1623384-localizedsubtitle)Added [UIMutableApplicationShortcutItem.localizedTitle](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/1623371-localizedtitle)Added [UIMutableApplicationShortcutItem.type](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/1623362-type)Added [UIMutableApplicationShortcutItem.userInfo](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/1623375-userinfo)Added [UIApplicationShortcutIconType](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype)Added [UIApplicationShortcutIconTypeAdd](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypeadd)Added [UIApplicationShortcutIconTypeCompose](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypecompose)Added [UIApplicationShortcutIconTypeLocation](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypelocation)Added [UIApplicationShortcutIconTypePause](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypepause)Added [UIApplicationShortcutIconTypePlay](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypeplay)Added [UIApplicationShortcutIconTypeSearch](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/search)Added [UIApplicationShortcutIconTypeShare](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypeshare)

#### UIAttachmentBehavior.h

Added [UIAttachmentBehavior.attachmentRange](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621294-attachmentrange)Added [+[UIAttachmentBehavior fixedAttachmentWithItem:attachedToItem:attachmentAnchor:]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621308-fixedattachmentwithitem)Added [UIAttachmentBehavior.frictionTorque](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621307-frictiontorque)Added [+[UIAttachmentBehavior limitAttachmentWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621320-limitattachmentwithitem)Added [+[UIAttachmentBehavior pinAttachmentWithItem:attachedToItem:attachmentAnchor:]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621322-pinattachmentwithitem)Added [+[UIAttachmentBehavior slidingAttachmentWithItem:attachedToItem:attachmentAnchor:axisOfTranslation:]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621318-slidingattachment)Added [+[UIAttachmentBehavior slidingAttachmentWithItem:attachmentAnchor:axisOfTranslation:]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621314-slidingattachment)Added [UIFloatRange](https://developer.apple.com/documentation/uikit/uifloatrange)Added [UIFloatRangeInfinite](https://developer.apple.com/documentation/uikit/uifloatrangeinfinite)Added [UIFloatRangeIsEqualToRange()](https://developer.apple.com/documentation/uikit/1621316-uifloatrangeisequaltorange)Added [UIFloatRangeIsInfinite()](https://developer.apple.com/documentation/uikit/uifloatrange/1621299-isinfinite)Added [UIFloatRangeMake()](https://developer.apple.com/documentation/uikit/1621310-uifloatrangemake)Added [UIFloatRangeZero](https://developer.apple.com/documentation/uikit/uifloatrange/1621313-zero)Modified [-[UIAttachmentBehavior initWithItem:offsetFromCenter:attachedToAnchor:]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621301-initwithitem)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIAttachmentBehavior initWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621298-initwithitem)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIAttachmentBehavior.items](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621311-items)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *items ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<id<UIDynamicItem>> *items ``` |

#### UIBarButtonItem.h

Added [-[UIBarButtonItem init]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617166-init)Added [-[UIBarButtonItem initWithCoder:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617111-init)Modified [UIBarButtonItem.customView](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617129-customview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *customView ``` |
| To | ``` @property(nonatomic, strong, nullable) __kindof UIView *customView ``` |

Modified [UIBarButtonItem.possibleTitles](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617132-possibletitles)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSSet *possibleTitles ``` |
| To | ``` @property(nonatomic, copy, nullable) NSSet<NSString *> *possibleTitles ``` |

Modified [UIBarButtonItem.target](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617154-target)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id target ``` |
| To | ``` @property(nonatomic, weak, nullable) id target ``` |

Modified [UIBarButtonItem.tintColor](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617135-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *tintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *tintColor ``` |

#### UIBarButtonItemGroup.h (Added)

Added [UIBarButtonItem.buttonGroup](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1623564-buttongroup)Added [UIBarButtonItemGroup](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup)Added [UIBarButtonItemGroup.barButtonItems](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/1623565-barbuttonitems)Added [UIBarButtonItemGroup.displayingRepresentativeItem](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/1623560-isdisplayingrepresentativeitem)Added [-[UIBarButtonItemGroup initWithBarButtonItems:representativeItem:]](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/1623559-init)Added [-[UIBarButtonItemGroup initWithCoder:]](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/1623562-initwithcoder)Added [UIBarButtonItemGroup.representativeItem](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/1623563-representativeitem)Added UIBarButtonItem(UIBarButtonItemGroup)

#### UIBarItem.h

Added [-[UIBarItem init]](https://developer.apple.com/documentation/uikit/uibaritem/1616411-init)Added [-[UIBarItem initWithCoder:]](https://developer.apple.com/documentation/uikit/uibaritem/1616416-init)Modified [UIBarItem](https://developer.apple.com/documentation/uikit/uibaritem)

|  | Protocols |
| --- | --- |
| From | UIAppearance |
| To | NSCoding, UIAppearance |

Modified [UIBarItem.image](https://developer.apple.com/documentation/uikit/uibaritem/1616415-image)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *image ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *image ``` |

Modified [UIBarItem.landscapeImagePhone](https://developer.apple.com/documentation/uikit/uibaritem/1616421-landscapeimagephone)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *landscapeImagePhone ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *landscapeImagePhone ``` |

Modified [-[UIBarItem setTitleTextAttributes:forState:]](https://developer.apple.com/documentation/uikit/uibaritem/1616414-settitletextattributes)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setTitleTextAttributes:(NSDictionary *)attributes forState:(UIControlState)state ``` |
| To | ``` - (void)setTitleTextAttributes:(NSDictionary<NSString *,id> * _Nullable)attributes forState:(UIControlState)state ``` |

Modified [-[UIBarItem titleTextAttributesForState:]](https://developer.apple.com/documentation/uikit/uibaritem/1616422-titletextattributesforstate)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)titleTextAttributesForState:(UIControlState)state ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nullable)titleTextAttributesForState:(UIControlState)state ``` |

#### UIBezierPath.h

Added [-[UIBezierPath init]](https://developer.apple.com/documentation/uikit/uibezierpath/1624381-init)Added [-[UIBezierPath initWithCoder:]](https://developer.apple.com/documentation/uikit/uibezierpath/1624346-init)Modified [+[UIBezierPath bezierPath]](https://developer.apple.com/documentation/uikit/uibezierpath/1624355-bezierpath)

|  | Declaration |
| --- | --- |
| From | ``` + (UIBezierPath *)bezierPath ``` |
| To | ``` + (instancetype _Nonnull)bezierPath ``` |

Modified [+[UIBezierPath bezierPathWithArcCenter:radius:startAngle:endAngle:clockwise:]](https://developer.apple.com/documentation/uikit/uibezierpath/1624358-bezierpathwitharccenter)

|  | Declaration |
| --- | --- |
| From | ``` + (UIBezierPath *)bezierPathWithArcCenter:(CGPoint)center radius:(CGFloat)radius startAngle:(CGFloat)startAngle endAngle:(CGFloat)endAngle clockwise:(BOOL)clockwise ``` |
| To | ``` + (instancetype _Nonnull)bezierPathWithArcCenter:(CGPoint)center radius:(CGFloat)radius startAngle:(CGFloat)startAngle endAngle:(CGFloat)endAngle clockwise:(BOOL)clockwise ``` |

Modified [+[UIBezierPath bezierPathWithCGPath:]](https://developer.apple.com/documentation/uikit/uibezierpath/1624362-bezierpathwithcgpath)

|  | Declaration |
| --- | --- |
| From | ``` + (UIBezierPath *)bezierPathWithCGPath:(CGPathRef)CGPath ``` |
| To | ``` + (instancetype _Nonnull)bezierPathWithCGPath:(CGPathRef _Nonnull)CGPath ``` |

Modified [+[UIBezierPath bezierPathWithOvalInRect:]](https://developer.apple.com/documentation/uikit/uibezierpath/1624379-init)

|  | Declaration |
| --- | --- |
| From | ``` + (UIBezierPath *)bezierPathWithOvalInRect:(CGRect)rect ``` |
| To | ``` + (instancetype _Nonnull)bezierPathWithOvalInRect:(CGRect)rect ``` |

Modified [+[UIBezierPath bezierPathWithRect:]](https://developer.apple.com/documentation/uikit/uibezierpath/1624359-bezierpathwithrect)

|  | Declaration |
| --- | --- |
| From | ``` + (UIBezierPath *)bezierPathWithRect:(CGRect)rect ``` |
| To | ``` + (instancetype _Nonnull)bezierPathWithRect:(CGRect)rect ``` |

Modified [+[UIBezierPath bezierPathWithRoundedRect:byRoundingCorners:cornerRadii:]](https://developer.apple.com/documentation/uikit/uibezierpath/1624368-bezierpathwithroundedrect)

|  | Declaration |
| --- | --- |
| From | ``` + (UIBezierPath *)bezierPathWithRoundedRect:(CGRect)rect byRoundingCorners:(UIRectCorner)corners cornerRadii:(CGSize)cornerRadii ``` |
| To | ``` + (instancetype _Nonnull)bezierPathWithRoundedRect:(CGRect)rect byRoundingCorners:(UIRectCorner)corners cornerRadii:(CGSize)cornerRadii ``` |

Modified [+[UIBezierPath bezierPathWithRoundedRect:cornerRadius:]](https://developer.apple.com/documentation/uikit/uibezierpath/1624356-bezierpathwithroundedrect)

|  | Declaration |
| --- | --- |
| From | ``` + (UIBezierPath *)bezierPathWithRoundedRect:(CGRect)rect cornerRadius:(CGFloat)cornerRadius ``` |
| To | ``` + (instancetype _Nonnull)bezierPathWithRoundedRect:(CGRect)rect cornerRadius:(CGFloat)cornerRadius ``` |

#### UIButton.h

Modified [+[UIButton buttonWithType:]](https://developer.apple.com/documentation/uikit/uibutton/1624028-buttonwithtype)

|  | Declaration |
| --- | --- |
| From | ``` + (id)buttonWithType:(UIButtonType)buttonType ``` |
| To | ``` + (instancetype _Nonnull)buttonWithType:(UIButtonType)buttonType ``` |

Modified [UIButton.currentAttributedTitle](https://developer.apple.com/documentation/uikit/uibutton/1624002-currentattributedtitle)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSAttributedString *currentAttributedTitle ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) NSAttributedString *currentAttributedTitle ``` |

Modified [UIButton.currentBackgroundImage](https://developer.apple.com/documentation/uikit/uibutton/1624035-currentbackgroundimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIImage *currentBackgroundImage ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIImage *currentBackgroundImage ``` |

Modified [UIButton.currentImage](https://developer.apple.com/documentation/uikit/uibutton/1623998-currentimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIImage *currentImage ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIImage *currentImage ``` |

Modified [UIButton.currentTitle](https://developer.apple.com/documentation/uikit/uibutton/1624032-currenttitle)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSString *currentTitle ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) NSString *currentTitle ``` |

Modified [UIButton.currentTitleColor](https://developer.apple.com/documentation/uikit/uibutton/1624006-currenttitlecolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIColor *currentTitleColor ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) UIColor *currentTitleColor ``` |

Modified [UIButton.currentTitleShadowColor](https://developer.apple.com/documentation/uikit/uibutton/1624019-currenttitleshadowcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIColor *currentTitleShadowColor ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIColor *currentTitleShadowColor ``` |

Modified [UIButton.font](https://developer.apple.com/documentation/uikit/uibutton/1624005-font)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIFont *font ``` |
| To | ``` @property(nonatomic, strong, nonnull) UIFont *font ``` |

Modified [UIButton.imageView](https://developer.apple.com/documentation/uikit/uibutton/1624033-imageview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIImageView *imageView ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIImageView *imageView ``` |

Modified [UIButton.tintColor](https://developer.apple.com/documentation/uikit/uibutton/1624025-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *tintColor ``` |
| To | ``` @property(nonatomic, strong) UIColor * _Null_unspecified tintColor ``` |

Modified [UIButton.titleLabel](https://developer.apple.com/documentation/uikit/uibutton/1623992-titlelabel)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UILabel *titleLabel ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UILabel *titleLabel ``` |

#### UICollectionView.h

Added [-[UICollectionView beginInteractiveMovementForItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618019-begininteractivemovementforitema)Added [-[UICollectionView cancelInteractiveMovement]](https://developer.apple.com/documentation/uikit/uicollectionview/1618076-cancelinteractivemovement)Added [-[UICollectionView endInteractiveMovement]](https://developer.apple.com/documentation/uikit/uicollectionview/1618082-endinteractivemovement)Added [-[UICollectionView indexPathsForVisibleSupplementaryElementsOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618034-indexpathsforvisiblesupplementar)Added [-[UICollectionView initWithCoder:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618065-initwithcoder)Added [-[UICollectionView supplementaryViewForElementKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618041-supplementaryviewforelementkind)Added [-[UICollectionView updateInteractiveMovementTargetPosition:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618079-updateinteractivemovementtargetp)Added [-[UICollectionView visibleSupplementaryViewsOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618026-visiblesupplementaryviewsofkind)Added [-[UICollectionViewDataSource collectionView:canMoveItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618015-collectionview)Added [-[UICollectionViewDataSource collectionView:moveItemAtIndexPath:toIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618064-collectionview)Added [-[UICollectionViewDelegate collectionView:targetContentOffsetForProposedContentOffset:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618007-collectionview)Added [-[UICollectionViewDelegate collectionView:targetIndexPathForMoveFromItemAtIndexPath:toProposedIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618052-collectionview)Modified [+[NSIndexPath indexPathForItem:inSection:]](https://developer.apple.com/documentation/foundation/nsindexpath/1526053-indexpathforitem)

|  | Declaration |
| --- | --- |
| From | ``` + (NSIndexPath *)indexPathForItem:(NSInteger)item inSection:(NSInteger)section ``` |
| To | ``` + (instancetype _Nonnull)indexPathForItem:(NSInteger)item inSection:(NSInteger)section ``` |

Modified [UICollectionView.backgroundView](https://developer.apple.com/documentation/uikit/uicollectionview/1618074-backgroundview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *backgroundView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *backgroundView ``` |

Modified [UICollectionView.collectionViewLayout](https://developer.apple.com/documentation/uikit/uicollectionview/1618047-collectionviewlayout)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UICollectionViewLayout *collectionViewLayout ``` |
| To | ``` @property(nonatomic, strong, nonnull) UICollectionViewLayout *collectionViewLayout ``` |

Modified [UICollectionView.dataSource](https://developer.apple.com/documentation/uikit/uicollectionview/1618091-datasource)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UICollectionViewDataSource> dataSource ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UICollectionViewDataSource> dataSource ``` |

Modified [UICollectionView.delegate](https://developer.apple.com/documentation/uikit/uicollectionview/1618033-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UICollectionViewDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UICollectionViewDelegate> delegate ``` |

Modified [-[UICollectionView deleteItemsAtIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618060-deleteitemsatindexpaths)

|  | Declaration |
| --- | --- |
| From | ``` - (void)deleteItemsAtIndexPaths:(NSArray *)indexPaths ``` |
| To | ``` - (void)deleteItemsAtIndexPaths:(NSArray<NSIndexPath *> * _Nonnull)indexPaths ``` |

Modified [-[UICollectionView dequeueReusableCellWithReuseIdentifier:forIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618063-dequeuereusablecell)

|  | Declaration |
| --- | --- |
| From | ``` - (id)dequeueReusableCellWithReuseIdentifier:(NSString *)identifier forIndexPath:(NSIndexPath *)indexPath ``` |
| To | ``` - (__kindof UICollectionViewCell * _Nonnull)dequeueReusableCellWithReuseIdentifier:(NSString * _Nonnull)identifier forIndexPath:(NSIndexPath * _Nonnull)indexPath ``` |

Modified [-[UICollectionView dequeueReusableSupplementaryViewOfKind:withReuseIdentifier:forIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618068-dequeuereusablesupplementaryview)

|  | Declaration |
| --- | --- |
| From | ``` - (id)dequeueReusableSupplementaryViewOfKind:(NSString *)elementKind withReuseIdentifier:(NSString *)identifier forIndexPath:(NSIndexPath *)indexPath ``` |
| To | ``` - (__kindof UICollectionReusableView * _Nonnull)dequeueReusableSupplementaryViewOfKind:(NSString * _Nonnull)elementKind withReuseIdentifier:(NSString * _Nonnull)identifier forIndexPath:(NSIndexPath * _Nonnull)indexPath ``` |

Modified [-[UICollectionView indexPathsForSelectedItems]](https://developer.apple.com/documentation/uikit/uicollectionview/1618099-indexpathsforselecteditems)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)indexPathsForSelectedItems ``` |
| To | ``` - (NSArray<NSIndexPath *> * _Nullable)indexPathsForSelectedItems ``` |

Modified [-[UICollectionView indexPathsForVisibleItems]](https://developer.apple.com/documentation/uikit/uicollectionview/1618020-indexpathsforvisibleitems)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)indexPathsForVisibleItems ``` |
| To | ``` - (NSArray<NSIndexPath *> * _Nonnull)indexPathsForVisibleItems ``` |

Modified [-[UICollectionView initWithFrame:collectionViewLayout:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618053-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionView insertItemsAtIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618097-insertitems)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertItemsAtIndexPaths:(NSArray *)indexPaths ``` |
| To | ``` - (void)insertItemsAtIndexPaths:(NSArray<NSIndexPath *> * _Nonnull)indexPaths ``` |

Modified [-[UICollectionView reloadItemsAtIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618055-reloaditemsatindexpaths)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reloadItemsAtIndexPaths:(NSArray *)indexPaths ``` |
| To | ``` - (void)reloadItemsAtIndexPaths:(NSArray<NSIndexPath *> * _Nonnull)indexPaths ``` |

Modified [-[UICollectionView visibleCells]](https://developer.apple.com/documentation/uikit/uicollectionview/1618056-visiblecells)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)visibleCells ``` |
| To | ``` - (NSArray<__kindof UICollectionViewCell *> * _Nonnull)visibleCells ``` |

#### UICollectionViewCell.h

Modified [UICollectionViewCell.backgroundView](https://developer.apple.com/documentation/uikit/uicollectionviewcell/1620131-backgroundview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *backgroundView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *backgroundView ``` |

Modified [UICollectionViewCell.selectedBackgroundView](https://developer.apple.com/documentation/uikit/uicollectionviewcell/1620138-selectedbackgroundview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *selectedBackgroundView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *selectedBackgroundView ``` |

#### UICollectionViewController.h

Added [-[UICollectionViewController initWithCoder:]](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623981-init)Added [-[UICollectionViewController initWithNibName:bundle:]](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623975-init)Added [UICollectionViewController.installsStandardGestureForInteractiveMovement](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623979-installsstandardgestureforintera)Modified [UICollectionViewController.collectionView](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623983-collectionview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UICollectionView *collectionView ``` |
| To | ``` @property(nonatomic, strong, nullable) __kindof UICollectionView *collectionView ``` |

Modified [-[UICollectionViewController initWithCollectionViewLayout:]](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623976-initwithcollectionviewlayout)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### UICollectionViewFlowLayout.h

Added [UICollectionViewFlowLayout.sectionFootersPinToVisibleBounds](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617701-sectionfooterspintovisiblebounds)Added [UICollectionViewFlowLayout.sectionHeadersPinToVisibleBounds](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617699-sectionheaderspintovisiblebounds)

#### UICollectionViewLayout.h

Added [-[UICollectionViewLayout init]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617734-init)Added [-[UICollectionViewLayout initWithCoder:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617766-initwithcoder)Added [-[UICollectionViewLayout invalidationContextForEndingInteractiveMovementOfItemsToFinalIndexPaths:previousIndexPaths:movementCancelled:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617755-invalidationcontextforendinginte)Added [-[UICollectionViewLayout invalidationContextForInteractivelyMovingItems:withTargetPosition:previousIndexPaths:previousPosition:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617757-invalidationcontext)Added [-[UICollectionViewLayout layoutAttributesForInteractivelyMovingItemAtIndexPath:withTargetPosition:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617788-layoutattributesforinteractively)Added [-[UICollectionViewLayout targetIndexPathForInteractivelyMovingItem:withPosition:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617778-targetindexpathforinteractivelym)Added [UICollectionViewLayoutInvalidationContext.interactiveMovementTarget](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617808-interactivemovementtarget)Added [UICollectionViewLayoutInvalidationContext.previousIndexPathsForInteractivelyMovingItems](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617800-previousindexpathsforinteractive)Added [UICollectionViewLayoutInvalidationContext.targetIndexPathsForInteractivelyMovingItems](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617780-targetindexpathsforinteractively)Added UICollectionViewLayout(UIReorderingSupportHooks)Modified [-[UICollectionViewLayout indexPathsToDeleteForDecorationViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617730-indexpathstodeletefordecorationv)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)indexPathsToDeleteForDecorationViewOfKind:(NSString *)elementKind ``` |
| To | ``` - (NSArray<NSIndexPath *> * _Nonnull)indexPathsToDeleteForDecorationViewOfKind:(NSString * _Nonnull)elementKind ``` |

Modified [-[UICollectionViewLayout indexPathsToDeleteForSupplementaryViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617807-indexpathstodeleteforsupplementa)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)indexPathsToDeleteForSupplementaryViewOfKind:(NSString *)elementKind ``` |
| To | ``` - (NSArray<NSIndexPath *> * _Nonnull)indexPathsToDeleteForSupplementaryViewOfKind:(NSString * _Nonnull)elementKind ``` |

Modified [-[UICollectionViewLayout indexPathsToInsertForDecorationViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617750-indexpathstoinsertfordecorationv)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)indexPathsToInsertForDecorationViewOfKind:(NSString *)elementKind ``` |
| To | ``` - (NSArray<NSIndexPath *> * _Nonnull)indexPathsToInsertForDecorationViewOfKind:(NSString * _Nonnull)elementKind ``` |

Modified [-[UICollectionViewLayout indexPathsToInsertForSupplementaryViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617770-indexpathstoinsertforsupplementa)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)indexPathsToInsertForSupplementaryViewOfKind:(NSString *)elementKind ``` |
| To | ``` - (NSArray<NSIndexPath *> * _Nonnull)indexPathsToInsertForSupplementaryViewOfKind:(NSString * _Nonnull)elementKind ``` |

Modified [-[UICollectionViewLayout layoutAttributesForElementsInRect:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617769-layoutattributesforelementsinrec)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)layoutAttributesForElementsInRect:(CGRect)rect ``` |
| To | ``` - (NSArray<__kindof UICollectionViewLayoutAttributes *> * _Nullable)layoutAttributesForElementsInRect:(CGRect)rect ``` |

Modified [-[UICollectionViewLayout prepareForCollectionViewUpdates:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617784-prepareforcollectionviewupdates)

|  | Declaration |
| --- | --- |
| From | ``` - (void)prepareForCollectionViewUpdates:(NSArray *)updateItems ``` |
| To | ``` - (void)prepareForCollectionViewUpdates:(NSArray<UICollectionViewUpdateItem *> * _Nonnull)updateItems ``` |

Modified [UICollectionViewLayoutAttributes.indexPath](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617776-indexpath)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSIndexPath *indexPath ``` |
| To | ``` @property(nonatomic, strong, nonnull) NSIndexPath *indexPath ``` |

Modified [UICollectionViewLayoutInvalidationContext.invalidatedDecorationIndexPaths](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617805-invalidateddecorationindexpaths)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *invalidatedDecorationIndexPaths ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,NSArray<NSIndexPath *> *> *invalidatedDecorationIndexPaths ``` |

Modified [-[UICollectionViewLayoutInvalidationContext invalidateDecorationElementsOfKind:atIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617736-invalidatedecorationelements)

|  | Declaration |
| --- | --- |
| From | ``` - (void)invalidateDecorationElementsOfKind:(NSString *)elementKind atIndexPaths:(NSArray *)indexPaths ``` |
| To | ``` - (void)invalidateDecorationElementsOfKind:(NSString * _Nonnull)elementKind atIndexPaths:(NSArray<NSIndexPath *> * _Nonnull)indexPaths ``` |

Modified [UICollectionViewLayoutInvalidationContext.invalidatedItemIndexPaths](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617723-invalidateditemindexpaths)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *invalidatedItemIndexPaths ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<NSIndexPath *> *invalidatedItemIndexPaths ``` |

Modified [UICollectionViewLayoutInvalidationContext.invalidatedSupplementaryIndexPaths](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617777-invalidatedsupplementaryindexpat)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *invalidatedSupplementaryIndexPaths ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,NSArray<NSIndexPath *> *> *invalidatedSupplementaryIndexPaths ``` |

Modified [-[UICollectionViewLayoutInvalidationContext invalidateItemsAtIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617795-invalidateitemsatindexpaths)

|  | Declaration |
| --- | --- |
| From | ``` - (void)invalidateItemsAtIndexPaths:(NSArray *)indexPaths ``` |
| To | ``` - (void)invalidateItemsAtIndexPaths:(NSArray<NSIndexPath *> * _Nonnull)indexPaths ``` |

Modified [-[UICollectionViewLayoutInvalidationContext invalidateSupplementaryElementsOfKind:atIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617747-invalidatesupplementaryelements)

|  | Declaration |
| --- | --- |
| From | ``` - (void)invalidateSupplementaryElementsOfKind:(NSString *)elementKind atIndexPaths:(NSArray *)indexPaths ``` |
| To | ``` - (void)invalidateSupplementaryElementsOfKind:(NSString * _Nonnull)elementKind atIndexPaths:(NSArray<NSIndexPath *> * _Nonnull)indexPaths ``` |

#### UICollectionViewTransitionLayout.h

Added [-[UICollectionViewTransitionLayout initWithCoder:]](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/1622192-init)Modified [-[UICollectionViewTransitionLayout initWithCurrentLayout:nextLayout:]](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/1622189-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### UICollisionBehavior.h

Modified [UICollisionBehavior.boundaryIdentifiers](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624812-boundaryidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *boundaryIdentifiers ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSArray<id<NSCopying>> *boundaryIdentifiers ``` |

Modified [UICollisionBehavior.collisionDelegate](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624828-collisiondelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign, readwrite) id<UICollisionBehaviorDelegate> collisionDelegate ``` |
| To | ``` @property(nonatomic, weak, readwrite, nullable) id<UICollisionBehaviorDelegate> collisionDelegate ``` |

Modified [-[UICollisionBehavior initWithItems:]](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624820-initwithitems)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithItems:(NSArray *)items ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithItems:(NSArray<id<UIDynamicItem>> * _Nonnull)items ``` | yes |

Modified [UICollisionBehavior.items](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624819-items)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *items ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<id<UIDynamicItem>> *items ``` |

#### UIControl.h

Added [UIControlEventPrimaryActionTriggered](https://developer.apple.com/documentation/uikit/uicontrolevents/uicontroleventprimaryactiontriggered)Modified [-[UIControl actionsForTarget:forControlEvent:]](https://developer.apple.com/documentation/uikit/uicontrol/1618251-actions)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)actionsForTarget:(id)target forControlEvent:(UIControlEvents)controlEvent ``` |
| To | ``` - (NSArray<NSString *> * _Nullable)actionsForTarget:(id _Nullable)target forControlEvent:(UIControlEvents)controlEvent ``` |

#### UIDatePicker.h

Modified [UIDatePicker.date](https://developer.apple.com/documentation/uikit/uidatepicker/1615975-date)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSDate *date ``` |
| To | ``` @property(nonatomic, strong, nonnull) NSDate *date ``` |

Modified [UIDatePicker.locale](https://developer.apple.com/documentation/uikit/uidatepicker/1615995-locale)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSLocale *locale ``` |
| To | ``` @property(nonatomic, strong, nullable) NSLocale *locale ``` |

Modified [UIDatePicker.maximumDate](https://developer.apple.com/documentation/uikit/uidatepicker/1615999-maximumdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSDate *maximumDate ``` |
| To | ``` @property(nonatomic, strong, nullable) NSDate *maximumDate ``` |

Modified [UIDatePicker.minimumDate](https://developer.apple.com/documentation/uikit/uidatepicker/1615980-minimumdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSDate *minimumDate ``` |
| To | ``` @property(nonatomic, strong, nullable) NSDate *minimumDate ``` |

Modified [UIDatePicker.timeZone](https://developer.apple.com/documentation/uikit/uidatepicker/1615976-timezone)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSTimeZone *timeZone ``` |
| To | ``` @property(nonatomic, strong, nullable) NSTimeZone *timeZone ``` |

#### UIDevice.h

Modified [UIDevice.identifierForVendor](https://developer.apple.com/documentation/uikit/uidevice/1620059-identifierforvendor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSUUID *identifierForVendor ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) NSUUID *identifierForVendor ``` |

Modified [UIDevice.localizedModel](https://developer.apple.com/documentation/uikit/uidevice/1620029-localizedmodel)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSString *localizedModel ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSString *localizedModel ``` |

Modified [UIDevice.model](https://developer.apple.com/documentation/uikit/uidevice/1620044-model)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSString *model ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSString *model ``` |

Modified [UIDevice.name](https://developer.apple.com/documentation/uikit/uidevice/1620015-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSString *name ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSString *name ``` |

Modified [UIDevice.systemName](https://developer.apple.com/documentation/uikit/uidevice/1620054-systemname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSString *systemName ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSString *systemName ``` |

Modified [UIDevice.systemVersion](https://developer.apple.com/documentation/uikit/uidevice/1620043-systemversion)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSString *systemVersion ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSString *systemVersion ``` |

#### UIDocument.h

Added [UIDocumentStateProgressAvailable](https://developer.apple.com/documentation/uikit/uidocument/state/1619983-progressavailable)Modified [UIDocument](https://developer.apple.com/documentation/uikit/uidocument)

|  | Protocols |
| --- | --- |
| From | NSFilePresenter |
| To | NSFilePresenter, NSProgressReporting |

Modified [-[UIDocument initWithFileURL:]](https://developer.apple.com/documentation/uikit/uidocument/1619979-initwithfileurl)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIDocument.undoManager](https://developer.apple.com/documentation/uikit/uidocument/1619953-undomanager)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSUndoManager *undoManager ``` |
| To | ``` @property(strong) NSUndoManager * _Null_unspecified undoManager ``` |

Modified [UIDocument.userActivity](https://developer.apple.com/documentation/uikit/uidocument/1619963-useractivity)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSUserActivity *userActivity ``` |
| To | ``` @property(nonatomic, strong, nullable) NSUserActivity *userActivity ``` |

#### UIDocumentInteractionController.h

Modified [UIDocumentInteractionController.annotation](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616820-annotation)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) id annotation ``` |
| To | ``` @property(nonatomic, strong, nullable) id annotation ``` |

Modified [UIDocumentInteractionController.delegate](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616812-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIDocumentInteractionControllerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIDocumentInteractionControllerDelegate> delegate ``` |

Modified [UIDocumentInteractionController.gestureRecognizers](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616817-gesturerecognizers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *gestureRecognizers ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<__kindof UIGestureRecognizer *> *gestureRecognizers ``` |

Modified [UIDocumentInteractionController.icons](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616801-icons)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *icons ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<UIImage *> *icons ``` |

Modified [UIDocumentInteractionController.URL](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616804-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSURL *URL ``` |
| To | ``` @property(strong, nullable) NSURL *URL ``` |

#### UIDocumentMenuViewController.h

Added [-[UIDocumentMenuViewController initWithCoder:]](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614182-initwithcoder)Modified [-[UIDocumentMenuViewController initWithDocumentTypes:inMode:]](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614187-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithDocumentTypes:(NSArray *)allowedUTIs inMode:(UIDocumentPickerMode)mode ``` |
| To | ``` - (instancetype _Nonnull)initWithDocumentTypes:(NSArray<NSString *> * _Nonnull)allowedUTIs inMode:(UIDocumentPickerMode)mode ``` |

#### UIDocumentPickerExtensionViewController.h

Modified [UIDocumentPickerExtensionViewController.validTypes](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/1614394-validtypes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *validTypes ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSArray<NSString *> *validTypes ``` |

#### UIDocumentPickerViewController.h

Added [-[UIDocumentPickerViewController initWithCoder:]](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618686-init)Modified [-[UIDocumentPickerViewController initWithDocumentTypes:inMode:]](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618678-initwithdocumenttypes)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithDocumentTypes:(NSArray *)allowedUTIs inMode:(UIDocumentPickerMode)mode ``` |
| To | ``` - (instancetype _Nonnull)initWithDocumentTypes:(NSArray<NSString *> * _Nonnull)allowedUTIs inMode:(UIDocumentPickerMode)mode ``` |

#### UIDynamicAnimator.h

Modified [UIDynamicAnimator.behaviors](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621198-behaviors)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *behaviors ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<__kindof UIDynamicBehavior *> *behaviors ``` |

Modified [UIDynamicAnimator.delegate](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621199-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIDynamicAnimatorDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIDynamicAnimatorDelegate> delegate ``` |

Modified [-[UIDynamicAnimator initWithReferenceView:]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621203-initwithreferenceview)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDynamicAnimator itemsInRect:]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621191-itemsinrect)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)itemsInRect:(CGRect)rect ``` |
| To | ``` - (NSArray<id<UIDynamicItem>> * _Nonnull)itemsInRect:(CGRect)rect ``` |

#### UIDynamicBehavior.h

Added [UIDynamicItem.collisionBoundingPath](https://developer.apple.com/documentation/uikit/uidynamicitem/1618494-collisionboundingpath)Added [UIDynamicItem.collisionBoundsType](https://developer.apple.com/documentation/uikit/uidynamicitem/1618493-collisionboundstype)Added [UIDynamicItemGroup](https://developer.apple.com/documentation/uikit/uidynamicitemgroup)Added [-[UIDynamicItemGroup initWithItems:]](https://developer.apple.com/documentation/uikit/uidynamicitemgroup/1618485-initwithitems)Added [UIDynamicItemGroup.items](https://developer.apple.com/documentation/uikit/uidynamicitemgroup/1618489-items)Added [UIDynamicItemCollisionBoundsType](https://developer.apple.com/documentation/uikit/uidynamicitemcollisionboundstype)Added [UIDynamicItemCollisionBoundsTypeEllipse](https://developer.apple.com/documentation/uikit/uidynamicitemcollisionboundstype/uidynamicitemcollisionboundstypeellipse)Added [UIDynamicItemCollisionBoundsTypePath](https://developer.apple.com/documentation/uikit/uidynamicitemcollisionboundstype/path)Added [UIDynamicItemCollisionBoundsTypeRectangle](https://developer.apple.com/documentation/uikit/uidynamicitemcollisionboundstype/uidynamicitemcollisionboundstyperectangle)Modified [UIDynamicBehavior.childBehaviors](https://developer.apple.com/documentation/uikit/uidynamicbehavior/1618482-childbehaviors)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *childBehaviors ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<__kindof UIDynamicBehavior *> *childBehaviors ``` |

#### UIDynamicItemBehavior.h

Added [UIDynamicItemBehavior.anchored](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624394-anchored)Added [UIDynamicItemBehavior.charge](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624390-charge)Modified [-[UIDynamicItemBehavior initWithItems:]](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624397-initwithitems)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithItems:(NSArray *)items ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithItems:(NSArray<id<UIDynamicItem>> * _Nonnull)items ``` | yes |

Modified [UIDynamicItemBehavior.items](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624400-items)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *items ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<id<UIDynamicItem>> *items ``` |

#### UIEvent.h

Added [-[UIEvent coalescedTouchesForTouch:]](https://developer.apple.com/documentation/uikit/uievent/1613808-coalescedtouches)Added [-[UIEvent predictedTouchesForTouch:]](https://developer.apple.com/documentation/uikit/uievent/1613814-predictedtouchesfortouch)Modified [-[UIEvent allTouches]](https://developer.apple.com/documentation/uikit/uievent/1613836-alltouches)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)allTouches ``` |
| To | ``` - (NSSet<UITouch *> * _Nullable)allTouches ``` |

Modified [-[UIEvent touchesForGestureRecognizer:]](https://developer.apple.com/documentation/uikit/uievent/1613832-touchesforgesturerecognizer)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)touchesForGestureRecognizer:(UIGestureRecognizer *)gesture ``` |
| To | ``` - (NSSet<UITouch *> * _Nullable)touchesForGestureRecognizer:(UIGestureRecognizer * _Nonnull)gesture ``` |

Modified [-[UIEvent touchesForView:]](https://developer.apple.com/documentation/uikit/uievent/1613812-touches)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)touchesForView:(UIView *)view ``` |
| To | ``` - (NSSet<UITouch *> * _Nullable)touchesForView:(UIView * _Nonnull)view ``` |

Modified [-[UIEvent touchesForWindow:]](https://developer.apple.com/documentation/uikit/uievent/1613794-touchesforwindow)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)touchesForWindow:(UIWindow *)window ``` |
| To | ``` - (NSSet<UITouch *> * _Nullable)touchesForWindow:(UIWindow * _Nonnull)window ``` |

#### UIFieldBehavior.h (Added)

Added [UIFieldBehavior](https://developer.apple.com/documentation/uikit/uifieldbehavior)Added [-[UIFieldBehavior addItem:]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624996-additem)Added [UIFieldBehavior.animationSpeed](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624986-animationspeed)Added [UIFieldBehavior.direction](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624987-direction)Added [+[UIFieldBehavior dragField]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624990-dragfield)Added [+[UIFieldBehavior electricField]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625004-electricfield)Added [UIFieldBehavior.falloff](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624988-falloff)Added [+[UIFieldBehavior fieldWithEvaluationBlock:]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625001-field)Added [UIFieldBehavior.items](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625002-items)Added [+[UIFieldBehavior linearGravityFieldWithVector:]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624991-lineargravityfieldwithvector)Added [+[UIFieldBehavior magneticField]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625007-magneticfield)Added [UIFieldBehavior.minimumRadius](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624994-minimumradius)Added [+[UIFieldBehavior noiseFieldWithSmoothness:animationSpeed:]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625006-noisefieldwithsmoothness)Added [UIFieldBehavior.position](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625003-position)Added [+[UIFieldBehavior radialGravityFieldWithPosition:]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624985-radialgravityfieldwithposition)Added [UIFieldBehavior.region](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625005-region)Added [-[UIFieldBehavior removeItem:]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624993-removeitem)Added [UIFieldBehavior.smoothness](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624998-smoothness)Added [+[UIFieldBehavior springField]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624995-springfield)Added [UIFieldBehavior.strength](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624997-strength)Added [+[UIFieldBehavior turbulenceFieldWithSmoothness:animationSpeed:]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624992-turbulencefield)Added [+[UIFieldBehavior velocityFieldWithVector:]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624989-velocityfieldwithvector)Added [+[UIFieldBehavior vortexField]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625000-vortexfield)

#### UIFont.h

Added [+[UIFont monospacedDigitSystemFontOfSize:weight:]](https://developer.apple.com/documentation/uikit/uifont/1619022-monospaceddigitsystemfontofsize)Modified [UIFont.familyName](https://developer.apple.com/documentation/uikit/uifont/1619033-familyname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSString *familyName ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSString *familyName ``` |

Modified [+[UIFont familyNames]](https://developer.apple.com/documentation/uikit/uifont/1619040-familynames)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)familyNames ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)familyNames ``` |

Modified [UIFont.fontName](https://developer.apple.com/documentation/uikit/uifont/1619024-fontname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSString *fontName ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSString *fontName ``` |

Modified [+[UIFont fontNamesForFamilyName:]](https://developer.apple.com/documentation/uikit/uifont/1619023-fontnames)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)fontNamesForFamilyName:(NSString *)familyName ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)fontNamesForFamilyName:(NSString * _Nonnull)familyName ``` |

#### UIFontDescriptor.h

Added [-[UIFontDescriptor init]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616667-init)Added [-[UIFontDescriptor initWithCoder:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616662-initwithcoder)Added [UIFontTextStyleCallout](https://developer.apple.com/documentation/uikit/uifont/textstyle/1616710-callout)Added [UIFontTextStyleTitle1](https://developer.apple.com/documentation/uikit/uifonttextstyletitle1)Added [UIFontTextStyleTitle2](https://developer.apple.com/documentation/uikit/uifont/textstyle/1616703-title2)Added [UIFontTextStyleTitle3](https://developer.apple.com/documentation/uikit/uifont/textstyle/1616673-title3)Modified [UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [-[UIFontDescriptor fontAttributes]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616698-fontattributes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)fontAttributes ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nonnull)fontAttributes ``` |

Modified [-[UIFontDescriptor fontDescriptorByAddingAttributes:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616666-addingattributes)

|  | Declaration |
| --- | --- |
| From | ``` - (UIFontDescriptor *)fontDescriptorByAddingAttributes:(NSDictionary *)attributes ``` |
| To | ``` - (UIFontDescriptor * _Nonnull)fontDescriptorByAddingAttributes:(NSDictionary<NSString *,id> * _Nonnull)attributes ``` |

Modified [+[UIFontDescriptor fontDescriptorWithFontAttributes:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616717-fontdescriptorwithfontattributes)

|  | Declaration |
| --- | --- |
| From | ``` + (UIFontDescriptor *)fontDescriptorWithFontAttributes:(NSDictionary *)attributes ``` |
| To | ``` + (UIFontDescriptor * _Nonnull)fontDescriptorWithFontAttributes:(NSDictionary<NSString *,id> * _Nonnull)attributes ``` |

Modified [-[UIFontDescriptor initWithFontAttributes:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616679-initwithfontattributes)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithFontAttributes:(NSDictionary *)attributes ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithFontAttributes:(NSDictionary<NSString *,id> * _Nonnull)attributes ``` | yes |

Modified [-[UIFontDescriptor matchingFontDescriptorsWithMandatoryKeys:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616699-matchingfontdescriptorswithmanda)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)matchingFontDescriptorsWithMandatoryKeys:(NSSet *)mandatoryKeys ``` |
| To | ``` - (NSArray<UIFontDescriptor *> * _Nonnull)matchingFontDescriptorsWithMandatoryKeys:(NSSet<NSString *> * _Nullable)mandatoryKeys ``` |

#### UIGestureRecognizer.h

Modified [UIGestureRecognizer.delegate](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1624207-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIGestureRecognizerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIGestureRecognizerDelegate> delegate ``` |

Modified [-[UIGestureRecognizer initWithTarget:action:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1624211-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### UIGestureRecognizerSubclass.h

Modified [-[UIGestureRecognizer touchesBegan:withEvent:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1620009-touchesbegan)

|  | Declaration |
| --- | --- |
| From | ``` - (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event ``` |
| To | ``` - (void)touchesBegan:(NSSet<UITouch *> * _Nonnull)touches withEvent:(UIEvent * _Nonnull)event ``` |

Modified [-[UIGestureRecognizer touchesCancelled:withEvent:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1620002-touchescancelled)

|  | Declaration |
| --- | --- |
| From | ``` - (void)touchesCancelled:(NSSet *)touches withEvent:(UIEvent *)event ``` |
| To | ``` - (void)touchesCancelled:(NSSet<UITouch *> * _Nonnull)touches withEvent:(UIEvent * _Nonnull)event ``` |

Modified [-[UIGestureRecognizer touchesEnded:withEvent:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1620005-touchesended)

|  | Declaration |
| --- | --- |
| From | ``` - (void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event ``` |
| To | ``` - (void)touchesEnded:(NSSet<UITouch *> * _Nonnull)touches withEvent:(UIEvent * _Nonnull)event ``` |

Modified [-[UIGestureRecognizer touchesMoved:withEvent:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1619996-touchesmoved)

|  | Declaration |
| --- | --- |
| From | ``` - (void)touchesMoved:(NSSet *)touches withEvent:(UIEvent *)event ``` |
| To | ``` - (void)touchesMoved:(NSSet<UITouch *> * _Nonnull)touches withEvent:(UIEvent * _Nonnull)event ``` |

#### UIGravityBehavior.h

Modified [-[UIGravityBehavior initWithItems:]](https://developer.apple.com/documentation/uikit/uigravitybehavior/1620416-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithItems:(NSArray *)items ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithItems:(NSArray<id<UIDynamicItem>> * _Nonnull)items ``` | yes |

Modified [UIGravityBehavior.items](https://developer.apple.com/documentation/uikit/uigravitybehavior/1620420-items)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *items ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<id<UIDynamicItem>> *items ``` |

#### UIGuidedAccessRestrictions.h

Modified [-[UIGuidedAccessRestrictionDelegate guidedAccessRestrictionIdentifiers]](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/1621160-guidedaccessrestrictionidentifie)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)guidedAccessRestrictionIdentifiers ``` |
| To | ``` - (NSArray<NSString *> * _Nullable)guidedAccessRestrictionIdentifiers ``` |

#### UIImage.h

Added [UIImage.flipsForRightToLeftLayoutDirection](https://developer.apple.com/documentation/uikit/uiimage/1624128-flipsforrighttoleftlayoutdirecti)Added [-[UIImage imageFlippedForRightToLeftLayoutDirection]](https://developer.apple.com/documentation/uikit/uiimage/1624140-imageflippedforrighttoleftlayout)Modified [+[UIImage animatedImageWithImages:duration:]](https://developer.apple.com/documentation/uikit/uiimage/1624149-animatedimagewithimages)

|  | Declaration |
| --- | --- |
| From | ``` + (UIImage *)animatedImageWithImages:(NSArray *)images duration:(NSTimeInterval)duration ``` |
| To | ``` + (UIImage * _Nullable)animatedImageWithImages:(NSArray<UIImage *> * _Nonnull)images duration:(NSTimeInterval)duration ``` |

Modified [UIImage.images](https://developer.apple.com/documentation/uikit/uiimage/1624117-images)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *images ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<UIImage *> *images ``` |

Modified [UIImage.traitCollection](https://developer.apple.com/documentation/uikit/uiimage/1624158-traitcollection)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) UITraitCollection *traitCollection ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) UITraitCollection *traitCollection ``` |

#### UIImageAsset.h

Added [-[UIImageAsset init]](https://developer.apple.com/documentation/uikit/uiimageasset/1624977-init)Added [-[UIImageAsset initWithCoder:]](https://developer.apple.com/documentation/uikit/uiimageasset/1624978-init)

#### UIImagePickerController.h

Modified [+[UIImagePickerController availableCaptureModesForCameraDevice:]](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619127-availablecapturemodesforcamerade)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)availableCaptureModesForCameraDevice:(UIImagePickerControllerCameraDevice)cameraDevice ``` |
| To | ``` + (NSArray<NSNumber *> * _Nullable)availableCaptureModesForCameraDevice:(UIImagePickerControllerCameraDevice)cameraDevice ``` |

Modified [+[UIImagePickerController availableMediaTypesForSourceType:]](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619169-availablemediatypesforsourcetype)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)availableMediaTypesForSourceType:(UIImagePickerControllerSourceType)sourceType ``` |
| To | ``` + (NSArray<NSString *> * _Nullable)availableMediaTypesForSourceType:(UIImagePickerControllerSourceType)sourceType ``` |

Modified [UIImagePickerController.cameraOverlayView](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619113-cameraoverlayview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *cameraOverlayView ``` |
| To | ``` @property(nonatomic, strong, nullable) __kindof UIView *cameraOverlayView ``` |

Modified [UIImagePickerController.delegate](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619145-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UINavigationControllerDelegate, UIImagePickerControllerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UINavigationControllerDelegate, UIImagePickerControllerDelegate> delegate ``` |

Modified [UIImagePickerController.mediaTypes](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619173-mediatypes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *mediaTypes ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<NSString *> *mediaTypes ``` |

Modified [-[UIImagePickerControllerDelegate imagePickerController:didFinishPickingImage:editingInfo:]](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/1619152-imagepickercontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)imagePickerController:(UIImagePickerController *)picker didFinishPickingImage:(UIImage *)image editingInfo:(NSDictionary *)editingInfo ``` |
| To | ``` - (void)imagePickerController:(UIImagePickerController * _Nonnull)picker didFinishPickingImage:(UIImage * _Nonnull)image editingInfo:(NSDictionary<NSString *,id> * _Nullable)editingInfo ``` |

Modified [-[UIImagePickerControllerDelegate imagePickerController:didFinishPickingMediaWithInfo:]](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/1619126-imagepickercontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)imagePickerController:(UIImagePickerController *)picker didFinishPickingMediaWithInfo:(NSDictionary *)info ``` |
| To | ``` - (void)imagePickerController:(UIImagePickerController * _Nonnull)picker didFinishPickingMediaWithInfo:(NSDictionary<NSString *,id> * _Nonnull)info ``` |

#### UIImageView.h

Modified [UIImageView.animationImages](https://developer.apple.com/documentation/uikit/uiimageview/1621068-animationimages)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *animationImages ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<UIImage *> *animationImages ``` |

Modified [UIImageView.highlightedAnimationImages](https://developer.apple.com/documentation/uikit/uiimageview/1621065-highlightedanimationimages)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *highlightedAnimationImages ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<UIImage *> *highlightedAnimationImages ``` |

Modified [UIImageView.highlightedImage](https://developer.apple.com/documentation/uikit/uiimageview/1621066-highlightedimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *highlightedImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *highlightedImage ``` |

Modified [UIImageView.image](https://developer.apple.com/documentation/uikit/uiimageview/1621069-image)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *image ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *image ``` |

Modified [UIImageView.tintColor](https://developer.apple.com/documentation/uikit/uiimageview/1621059-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *tintColor ``` |
| To | ``` @property(nonatomic, strong) UIColor * _Null_unspecified tintColor ``` |

#### UIInputView.h

Added [UIInputView.allowsSelfSizing](https://developer.apple.com/documentation/uikit/uiinputview/1619473-allowsselfsizing)Added [-[UIInputView initWithCoder:]](https://developer.apple.com/documentation/uikit/uiinputview/1619475-init)Modified [-[UIInputView initWithFrame:inputViewStyle:]](https://developer.apple.com/documentation/uikit/uiinputview/1619477-initwithframe)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### UIInputViewController.h

Modified [UIInputViewController.inputView](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/1618192-inputview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIInputView *inputView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIInputView *inputView ``` |

Modified [UIInputViewController.textDocumentProxy](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/1618193-textdocumentproxy)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSObject<UITextDocumentProxy> *textDocumentProxy ``` |
| To | ``` @property(nonatomic, readonly, nonnull) id<UITextDocumentProxy> textDocumentProxy ``` |

#### UIKitDefines.h

Added #def UIKIT_AVAILABLE_IOS_ONLYAdded #def UIKIT_AVAILABLE_WATCHOS_ONLY

#### UILabel.h

Added [UILabel.allowsDefaultTighteningForTruncation](https://developer.apple.com/documentation/uikit/uilabel/1620533-allowsdefaulttighteningfortrunca)Modified [UILabel.font](https://developer.apple.com/documentation/uikit/uilabel/1620532-font)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIFont *font ``` |
| To | ``` @property(nonatomic, strong) UIFont * _Null_unspecified font ``` |

Modified [UILabel.highlightedTextColor](https://developer.apple.com/documentation/uikit/uilabel/1620540-highlightedtextcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *highlightedTextColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *highlightedTextColor ``` |

Modified [UILabel.shadowColor](https://developer.apple.com/documentation/uikit/uilabel/1620536-shadowcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *shadowColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *shadowColor ``` |

Modified [UILabel.textColor](https://developer.apple.com/documentation/uikit/uilabel/1620531-textcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *textColor ``` |
| To | ``` @property(nonatomic, strong) UIColor * _Null_unspecified textColor ``` |

#### UILayoutGuide.h (Added)

Added [UILayoutGuide](https://developer.apple.com/documentation/uikit/uilayoutguide)Added [UILayoutGuide.bottomAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619661-bottomanchor)Added [UILayoutGuide.centerXAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619654-centerxanchor)Added [UILayoutGuide.centerYAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619659-centeryanchor)Added [UILayoutGuide.heightAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619652-heightanchor)Added [UILayoutGuide.identifier](https://developer.apple.com/documentation/uikit/uilayoutguide/1619655-identifier)Added [UILayoutGuide.layoutFrame](https://developer.apple.com/documentation/uikit/uilayoutguide/1619657-layoutframe)Added [UILayoutGuide.leadingAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619658-leadinganchor)Added [UILayoutGuide.leftAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619656-leftanchor)Added [UILayoutGuide.owningView](https://developer.apple.com/documentation/uikit/uilayoutguide/1619648-owningview)Added [UILayoutGuide.rightAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619649-rightanchor)Added [UILayoutGuide.topAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619650-topanchor)Added [UILayoutGuide.trailingAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619660-trailinganchor)Added [UILayoutGuide.widthAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619653-widthanchor)

#### UILexicon.h

Modified [UILexicon.entries](https://developer.apple.com/documentation/uikit/uilexicon/1614133-entries)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *entries ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<UILexiconEntry *> *entries ``` |

#### UILocalizedIndexedCollation.h

Modified [+[UILocalizedIndexedCollation currentCollation]](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/1620384-currentcollation)

|  | Declaration |
| --- | --- |
| From | ``` + (id)currentCollation ``` |
| To | ``` + (instancetype _Nonnull)currentCollation ``` |

Modified [UILocalizedIndexedCollation.sectionIndexTitles](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/1620383-sectionindextitles)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *sectionIndexTitles ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *sectionIndexTitles ``` |

Modified [UILocalizedIndexedCollation.sectionTitles](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/1620379-sectiontitles)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *sectionTitles ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *sectionTitles ``` |

#### UILocalNotification.h

Added [-[UILocalNotification init]](https://developer.apple.com/documentation/uikit/uilocalnotification/1616645-init)Added [-[UILocalNotification initWithCoder:]](https://developer.apple.com/documentation/uikit/uilocalnotification/1616653-init)

#### UIManagedDocument.h

Modified [UIManagedDocument.managedObjectContext](https://developer.apple.com/documentation/uikit/uimanageddocument/1622667-managedobjectcontext)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain, readonly) NSManagedObjectContext *managedObjectContext ``` |
| To | ``` @property(nonatomic, strong, readonly, nonnull) NSManagedObjectContext *managedObjectContext ``` |

Modified [UIManagedDocument.managedObjectModel](https://developer.apple.com/documentation/uikit/uimanageddocument/1622669-managedobjectmodel)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain, readonly) NSManagedObjectModel *managedObjectModel ``` |
| To | ``` @property(nonatomic, strong, readonly, nonnull) NSManagedObjectModel *managedObjectModel ``` |

#### UIMenuController.h

Modified [UIMenuController.menuItems](https://developer.apple.com/documentation/uikit/uimenucontroller/1622811-menuitems)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *menuItems ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<UIMenuItem *> *menuItems ``` |

Modified [-[UIMenuItem initWithTitle:action:]](https://developer.apple.com/documentation/uikit/uimenuitem/1622824-initwithtitle)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### UIMotionEffect.h

Added [-[UIInterpolatingMotionEffect initWithCoder:]](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/1622368-init)Added [-[UIMotionEffect init]](https://developer.apple.com/documentation/uikit/uimotioneffect/1622375-init)Added [-[UIMotionEffect initWithCoder:]](https://developer.apple.com/documentation/uikit/uimotioneffect/1622371-init)Modified [-[UIInterpolatingMotionEffect initWithKeyPath:type:]](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/1622372-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIInterpolatingMotionEffect.maximumRelativeValue](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/1622376-maximumrelativevalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) id maximumRelativeValue ``` |
| To | ``` @property(strong, nonatomic, nullable) id maximumRelativeValue ``` |

Modified [UIInterpolatingMotionEffect.minimumRelativeValue](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/1622365-minimumrelativevalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) id minimumRelativeValue ``` |
| To | ``` @property(strong, nonatomic, nullable) id minimumRelativeValue ``` |

Modified [-[UIMotionEffect keyPathsAndRelativeValuesForViewerOffset:]](https://developer.apple.com/documentation/uikit/uimotioneffect/1622380-keypathsandrelativevaluesforview)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)keyPathsAndRelativeValuesForViewerOffset:(UIOffset)viewerOffset ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nullable)keyPathsAndRelativeValuesForViewerOffset:(UIOffset)viewerOffset ``` |

Modified [UIMotionEffectGroup.motionEffects](https://developer.apple.com/documentation/uikit/uimotioneffectgroup/1622374-motioneffects)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, nonatomic) NSArray *motionEffects ``` |
| To | ``` @property(copy, nonatomic, nullable) NSArray<__kindof UIMotionEffect *> *motionEffects ``` |

#### UINavigationBar.h

Added [-[UINavigationItem initWithCoder:]](https://developer.apple.com/documentation/uikit/uinavigationitem/1624950-initwithcoder)Modified [UINavigationBar.backIndicatorImage](https://developer.apple.com/documentation/uikit/uinavigationbar/1624942-backindicatorimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *backIndicatorImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *backIndicatorImage ``` |

Modified [UINavigationBar.backIndicatorTransitionMaskImage](https://developer.apple.com/documentation/uikit/uinavigationbar/1624938-backindicatortransitionmaskimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *backIndicatorTransitionMaskImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *backIndicatorTransitionMaskImage ``` |

Modified [UINavigationBar.backItem](https://developer.apple.com/documentation/uikit/uinavigationbar/1624925-backitem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UINavigationItem *backItem ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UINavigationItem *backItem ``` |

Modified [UINavigationBar.barTintColor](https://developer.apple.com/documentation/uikit/uinavigationbar/1624931-bartintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *barTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *barTintColor ``` |

Modified [UINavigationBar.delegate](https://developer.apple.com/documentation/uikit/uinavigationbar/1624951-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UINavigationBarDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UINavigationBarDelegate> delegate ``` |

Modified [UINavigationBar.items](https://developer.apple.com/documentation/uikit/uinavigationbar/1624961-items)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *items ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<UINavigationItem *> *items ``` |

Modified [-[UINavigationBar setItems:animated:]](https://developer.apple.com/documentation/uikit/uinavigationbar/1624945-setitems)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setItems:(NSArray *)items animated:(BOOL)animated ``` |
| To | ``` - (void)setItems:(NSArray<UINavigationItem *> * _Nullable)items animated:(BOOL)animated ``` |

Modified [UINavigationBar.shadowImage](https://developer.apple.com/documentation/uikit/uinavigationbar/1624963-shadowimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *shadowImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *shadowImage ``` |

Modified [UINavigationBar.tintColor](https://developer.apple.com/documentation/uikit/uinavigationbar/1624937-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *tintColor ``` |
| To | ``` @property(nonatomic, strong) UIColor * _Null_unspecified tintColor ``` |

Modified [UINavigationBar.titleTextAttributes](https://developer.apple.com/documentation/uikit/uinavigationbar/1624953-titletextattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDictionary *titleTextAttributes ``` |
| To | ``` @property(nonatomic, copy, nullable) NSDictionary<NSString *,id> *titleTextAttributes ``` |

Modified [UINavigationBar.topItem](https://developer.apple.com/documentation/uikit/uinavigationbar/1624967-topitem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UINavigationItem *topItem ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UINavigationItem *topItem ``` |

Modified [UINavigationBar.translucent](https://developer.apple.com/documentation/uikit/uinavigationbar/1624928-istranslucent)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UINavigationItem.backBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624958-backbarbuttonitem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIBarButtonItem *backBarButtonItem ``` |
| To | ``` @property(nonatomic, strong, nullable) UIBarButtonItem *backBarButtonItem ``` |

Modified [-[UINavigationItem initWithTitle:]](https://developer.apple.com/documentation/uikit/uinavigationitem/1624943-initwithtitle)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [UINavigationItem.leftBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624936-leftbarbuttonitem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIBarButtonItem *leftBarButtonItem ``` |
| To | ``` @property(nonatomic, strong, nullable) UIBarButtonItem *leftBarButtonItem ``` |

Modified [UINavigationItem.leftBarButtonItems](https://developer.apple.com/documentation/uikit/uinavigationitem/1624946-leftbarbuttonitems)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *leftBarButtonItems ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<UIBarButtonItem *> *leftBarButtonItems ``` |

Modified [UINavigationItem.rightBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624957-rightbarbuttonitem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIBarButtonItem *rightBarButtonItem ``` |
| To | ``` @property(nonatomic, strong, nullable) UIBarButtonItem *rightBarButtonItem ``` |

Modified [UINavigationItem.rightBarButtonItems](https://developer.apple.com/documentation/uikit/uinavigationitem/1624956-rightbarbuttonitems)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *rightBarButtonItems ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<UIBarButtonItem *> *rightBarButtonItems ``` |

Modified [-[UINavigationItem setLeftBarButtonItems:animated:]](https://developer.apple.com/documentation/uikit/uinavigationitem/1624949-setleftbarbuttonitems)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setLeftBarButtonItems:(NSArray *)items animated:(BOOL)animated ``` |
| To | ``` - (void)setLeftBarButtonItems:(NSArray<UIBarButtonItem *> * _Nullable)items animated:(BOOL)animated ``` |

Modified [-[UINavigationItem setRightBarButtonItems:animated:]](https://developer.apple.com/documentation/uikit/uinavigationitem/1624939-setrightbarbuttonitems)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setRightBarButtonItems:(NSArray *)items animated:(BOOL)animated ``` |
| To | ``` - (void)setRightBarButtonItems:(NSArray<UIBarButtonItem *> * _Nullable)items animated:(BOOL)animated ``` |

Modified [UINavigationItem.titleView](https://developer.apple.com/documentation/uikit/uinavigationitem/1624935-titleview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *titleView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *titleView ``` |

#### UINavigationController.h

Modified [UINavigationController.barHideOnSwipeGestureRecognizer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621854-barhideonswipegesturerecognizer)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIPanGestureRecognizer *barHideOnSwipeGestureRecognizer ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) UIPanGestureRecognizer *barHideOnSwipeGestureRecognizer ``` |

Modified [UINavigationController.delegate](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621876-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UINavigationControllerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UINavigationControllerDelegate> delegate ``` |

Modified [-[UINavigationController popToRootViewControllerAnimated:]](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621855-poptorootviewcontrolleranimated)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)popToRootViewControllerAnimated:(BOOL)animated ``` |
| To | ``` - (NSArray<__kindof UIViewController *> * _Nullable)popToRootViewControllerAnimated:(BOOL)animated ``` |

Modified [-[UINavigationController popToViewController:animated:]](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621871-poptoviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)popToViewController:(UIViewController *)viewController animated:(BOOL)animated ``` |
| To | ``` - (NSArray<__kindof UIViewController *> * _Nullable)popToViewController:(UIViewController * _Nonnull)viewController animated:(BOOL)animated ``` |

Modified [-[UINavigationController setViewControllers:animated:]](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621861-setviewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setViewControllers:(NSArray *)viewControllers animated:(BOOL)animated ``` |
| To | ``` - (void)setViewControllers:(NSArray<UIViewController *> * _Nonnull)viewControllers animated:(BOOL)animated ``` |

Modified [UINavigationController.topViewController](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621849-topviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIViewController *topViewController ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIViewController *topViewController ``` |

Modified [UINavigationController.viewControllers](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621873-viewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *viewControllers ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<__kindof UIViewController *> *viewControllers ``` |

Modified [UINavigationController.visibleViewController](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621862-visibleviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIViewController *visibleViewController ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIViewController *visibleViewController ``` |

Modified [-[UINavigationControllerDelegate navigationControllerSupportedInterfaceOrientations:]](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621884-navigationcontrollersupportedint)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)navigationControllerSupportedInterfaceOrientations:(UINavigationController *)navigationController ``` |
| To | ``` - (UIInterfaceOrientationMask)navigationControllerSupportedInterfaceOrientations:(UINavigationController * _Nonnull)navigationController ``` |

Modified [UIViewController.navigationController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621860-navigationcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UINavigationController *navigationController ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UINavigationController *navigationController ``` |

Modified [UIViewController.navigationItem](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621851-navigationitem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UINavigationItem *navigationItem ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) UINavigationItem *navigationItem ``` |

Modified [-[UIViewController setToolbarItems:animated:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621874-settoolbaritems)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setToolbarItems:(NSArray *)toolbarItems animated:(BOOL)animated ``` |
| To | ``` - (void)setToolbarItems:(NSArray<UIBarButtonItem *> * _Nullable)toolbarItems animated:(BOOL)animated ``` |

Modified [UIViewController.toolbarItems](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621867-toolbaritems)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSArray *toolbarItems ``` |
| To | ``` @property(nonatomic, strong, nullable) NSArray<__kindof UIBarButtonItem *> *toolbarItems ``` |

#### UIPageControl.h

Modified [UIPageControl.currentPageIndicatorTintColor](https://developer.apple.com/documentation/uikit/uipagecontrol/1621233-currentpageindicatortintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *currentPageIndicatorTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *currentPageIndicatorTintColor ``` |

Modified [UIPageControl.pageIndicatorTintColor](https://developer.apple.com/documentation/uikit/uipagecontrol/1621239-pageindicatortintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *pageIndicatorTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *pageIndicatorTintColor ``` |

#### UIPageViewController.h

Added [-[UIPageViewController initWithCoder:]](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614108-initwithcoder)Modified [UIPageViewController.dataSource](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614117-datasource)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIPageViewControllerDataSource> dataSource ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIPageViewControllerDataSource> dataSource ``` |

Modified [UIPageViewController.delegate](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614089-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIPageViewControllerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIPageViewControllerDelegate> delegate ``` |

Modified [UIPageViewController.gestureRecognizers](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614107-gesturerecognizers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *gestureRecognizers ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<__kindof UIGestureRecognizer *> *gestureRecognizers ``` |

Modified [-[UIPageViewController initWithTransitionStyle:navigationOrientation:options:]](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614105-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithTransitionStyle:(UIPageViewControllerTransitionStyle)style navigationOrientation:(UIPageViewControllerNavigationOrientation)navigationOrientation options:(NSDictionary *)options ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithTransitionStyle:(UIPageViewControllerTransitionStyle)style navigationOrientation:(UIPageViewControllerNavigationOrientation)navigationOrientation options:(NSDictionary<NSString *,id> * _Nullable)options ``` | yes |

Modified [-[UIPageViewController setViewControllers:direction:animated:completion:]](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614087-setviewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setViewControllers:(NSArray *)viewControllers direction:(UIPageViewControllerNavigationDirection)direction animated:(BOOL)animated completion:(void (^)(BOOL finished))completion ``` |
| To | ``` - (void)setViewControllers:(NSArray<UIViewController *> * _Nullable)viewControllers direction:(UIPageViewControllerNavigationDirection)direction animated:(BOOL)animated completion:(void (^ _Nullable)(BOOL finished))completion ``` |

Modified [UIPageViewController.viewControllers](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614106-viewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *viewControllers ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<__kindof UIViewController *> *viewControllers ``` |

Modified [-[UIPageViewControllerDelegate pageViewController:didFinishAnimating:previousViewControllers:transitionCompleted:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614090-pageviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)pageViewController:(UIPageViewController *)pageViewController didFinishAnimating:(BOOL)finished previousViewControllers:(NSArray *)previousViewControllers transitionCompleted:(BOOL)completed ``` |
| To | ``` - (void)pageViewController:(UIPageViewController * _Nonnull)pageViewController didFinishAnimating:(BOOL)finished previousViewControllers:(NSArray<UIViewController *> * _Nonnull)previousViewControllers transitionCompleted:(BOOL)completed ``` |

Modified [-[UIPageViewControllerDelegate pageViewController:willTransitionToViewControllers:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614091-pageviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)pageViewController:(UIPageViewController *)pageViewController willTransitionToViewControllers:(NSArray *)pendingViewControllers ``` |
| To | ``` - (void)pageViewController:(UIPageViewController * _Nonnull)pageViewController willTransitionToViewControllers:(NSArray<UIViewController *> * _Nonnull)pendingViewControllers ``` |

Modified [-[UIPageViewControllerDelegate pageViewControllerSupportedInterfaceOrientations:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614100-pageviewcontrollersupportedinter)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)pageViewControllerSupportedInterfaceOrientations:(UIPageViewController *)pageViewController ``` |
| To | ``` - (UIInterfaceOrientationMask)pageViewControllerSupportedInterfaceOrientations:(UIPageViewController * _Nonnull)pageViewController ``` |

#### UIPasteboard.h

Modified [-[UIPasteboard addItems:]](https://developer.apple.com/documentation/uikit/uipasteboard/1622101-additems)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addItems:(NSArray *)items ``` |
| To | ``` - (void)addItems:(NSArray<NSDictionary<NSString *,id> *> * _Nonnull)items ``` |

Modified [UIPasteboard.colors](https://developer.apple.com/documentation/uikit/uipasteboard/1622078-colors)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *colors ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<UIColor *> *colors ``` |

Modified [-[UIPasteboard containsPasteboardTypes:]](https://developer.apple.com/documentation/uikit/uipasteboard/1622070-containspasteboardtypes)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)containsPasteboardTypes:(NSArray *)pasteboardTypes ``` |
| To | ``` - (BOOL)containsPasteboardTypes:(NSArray<NSString *> * _Nonnull)pasteboardTypes ``` |

Modified [-[UIPasteboard containsPasteboardTypes:inItemSet:]](https://developer.apple.com/documentation/uikit/uipasteboard/1622100-containspasteboardtypes)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)containsPasteboardTypes:(NSArray *)pasteboardTypes inItemSet:(NSIndexSet *)itemSet ``` |
| To | ``` - (BOOL)containsPasteboardTypes:(NSArray<NSString *> * _Nonnull)pasteboardTypes inItemSet:(NSIndexSet * _Nullable)itemSet ``` |

Modified [UIPasteboard.images](https://developer.apple.com/documentation/uikit/uipasteboard/1622086-images)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *images ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<UIImage *> *images ``` |

Modified [-[UIPasteboard pasteboardTypes]](https://developer.apple.com/documentation/uikit/uipasteboard/1622077-types)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)pasteboardTypes ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)pasteboardTypes ``` |

Modified [UIPasteboard.strings](https://developer.apple.com/documentation/uikit/uipasteboard/1622091-strings)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *strings ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *strings ``` |

Modified [UIPasteboard.URLs](https://developer.apple.com/documentation/uikit/uipasteboard/1622097-urls)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *URLs ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSURL *> *URLs ``` |

#### UIPickerView.h

Modified [UIPickerView.dataSource](https://developer.apple.com/documentation/uikit/uipickerview/1614370-datasource)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIPickerViewDataSource> dataSource ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIPickerViewDataSource> dataSource ``` |

Modified [UIPickerView.delegate](https://developer.apple.com/documentation/uikit/uipickerview/1614379-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIPickerViewDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIPickerViewDelegate> delegate ``` |

#### UIPopoverController.h

Modified [UIPopoverController](https://developer.apple.com/documentation/uikit/uipopovercontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.backgroundColor](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624673-backgroundcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.contentViewController](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624672-contentviewcontroller)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, retain) UIViewController *contentViewController ``` | -- |
| To | ``` @property(nonatomic, strong, nonnull) UIViewController *contentViewController ``` | iOS 9.0 |

Modified [UIPopoverController.delegate](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624666-delegate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, assign) id<UIPopoverControllerDelegate> delegate ``` | -- |
| To | ``` @property(nonatomic, weak, nullable) id<UIPopoverControllerDelegate> delegate ``` | iOS 9.0 |

Modified [-[UIPopoverController dismissPopoverAnimated:]](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624662-dismisspopoveranimated)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIPopoverController initWithContentViewController:]](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624669-initwithcontentviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.passthroughViews](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624654-passthroughviews)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *passthroughViews ``` | -- |
| To | ``` @property(nonatomic, copy, nullable) NSArray<__kindof UIView *> *passthroughViews ``` | iOS 9.0 |

Modified [UIPopoverController.popoverArrowDirection](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624665-arrowdirection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.popoverBackgroundViewClass](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624659-popoverbackgroundviewclass)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, readwrite, retain) Class popoverBackgroundViewClass ``` | -- |
| To | ``` @property(nonatomic, readwrite, strong, nullable) Class popoverBackgroundViewClass ``` | iOS 9.0 |

Modified [UIPopoverController.popoverContentSize](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624667-contentsize)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.popoverLayoutMargins](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624657-layoutmargins)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.popoverVisible](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624656-popovervisible)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIPopoverController presentPopoverFromBarButtonItem:permittedArrowDirections:animated:]](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624668-presentpopoverfrombarbuttonitem)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIPopoverController presentPopoverFromRect:inView:permittedArrowDirections:animated:]](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624660-present)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIPopoverController setContentViewController:animated:]](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624655-setcontentview)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIPopoverController setPopoverContentSize:animated:]](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624670-setpopovercontentsize)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIPopoverControllerDelegate popoverController:willRepositionPopoverToRect:inView:]](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624664-popovercontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIPopoverControllerDelegate popoverControllerDidDismissPopover:]](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624671-popovercontrollerdiddismisspopov)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIPopoverControllerDelegate popoverControllerShouldDismissPopover:]](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624661-popovercontrollershoulddismisspo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### UIPopoverPresentationController.h

Added [UIPopoverPresentationController.canOverlapSourceViewRect](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622325-canoverlapsourceviewrect)Modified [UIPopoverPresentationController.barButtonItem](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622314-barbuttonitem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIBarButtonItem *barButtonItem ``` |
| To | ``` @property(nonatomic, strong, nullable) UIBarButtonItem *barButtonItem ``` |

Modified [UIPopoverPresentationController.delegate](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622320-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIPopoverPresentationControllerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIPopoverPresentationControllerDelegate> delegate ``` |

Modified [UIPopoverPresentationController.passthroughViews](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622312-passthroughviews)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *passthroughViews ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<UIView *> *passthroughViews ``` |

Modified [UIPopoverPresentationController.popoverBackgroundViewClass](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622318-popoverbackgroundviewclass)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readwrite, retain) Class<UIPopoverBackgroundViewMethods> popoverBackgroundViewClass ``` |
| To | ``` @property(nonatomic, readwrite, strong, nullable) Class<UIPopoverBackgroundViewMethods> popoverBackgroundViewClass ``` |

Modified [UIPopoverPresentationController.sourceView](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622313-sourceview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *sourceView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *sourceView ``` |

#### UIPresentationController.h

Modified [UIPresentationController.containerView](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618332-containerview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) UIView *containerView ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIView *containerView ``` |

Modified [UIPresentationController.delegate](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618329-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIAdaptivePresentationControllerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIAdaptivePresentationControllerDelegate> delegate ``` |

Modified [UIPresentationController.presentedViewController](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618322-presentedviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain, readonly) UIViewController *presentedViewController ``` |
| To | ``` @property(nonatomic, strong, readonly, nonnull) UIViewController *presentedViewController ``` |

Modified [UIPresentationController.presentingViewController](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618338-presentingviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain, readonly) UIViewController *presentingViewController ``` |
| To | ``` @property(nonatomic, strong, readonly, nonnull) UIViewController *presentingViewController ``` |

#### UIPrinterPickerController.h

Modified [UIPrinterPickerController.delegate](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/1620511-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIPrinterPickerControllerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIPrinterPickerControllerDelegate> delegate ``` |

#### UIPrintFormatter.h

Modified [UIPrintFormatter.printPageRenderer](https://developer.apple.com/documentation/uikit/uiprintformatter/1621821-printpagerenderer)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, assign) UIPrintPageRenderer *printPageRenderer ``` |
| To | ``` @property(nonatomic, readonly, weak, nullable) UIPrintPageRenderer *printPageRenderer ``` |

Modified [UISimpleTextPrintFormatter.color](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621830-color)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *color ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *color ``` |

Modified [UISimpleTextPrintFormatter.font](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621837-font)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIFont *font ``` |
| To | ``` @property(nonatomic, strong, nullable) UIFont *font ``` |

#### UIPrintInfo.h

Added [-[UIPrintInfo initWithCoder:]](https://developer.apple.com/documentation/uikit/uiprintinfo/1623546-initwithcoder)

#### UIPrintInteractionController.h

Added [-[UIPrintInteractionControllerDelegate printInteractionController:chooseCutterBehavior:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618178-printinteractioncontroller)Added [UIPrinterCutterBehavior](https://developer.apple.com/documentation/uikit/uiprinter/cutterbehavior)Added [UIPrinterCutterBehaviorCutAfterEachCopy](https://developer.apple.com/documentation/uikit/uiprintercutterbehavior/uiprintercutterbehaviorcutaftereachcopy)Added [UIPrinterCutterBehaviorCutAfterEachJob](https://developer.apple.com/documentation/uikit/uiprintercutterbehavior/uiprintercutterbehaviorcutaftereachjob)Added [UIPrinterCutterBehaviorCutAfterEachPage](https://developer.apple.com/documentation/uikit/uiprinter/cutterbehavior/cutaftereachpage)Added [UIPrinterCutterBehaviorNoCut](https://developer.apple.com/documentation/uikit/uiprintercutterbehavior/uiprintercutterbehaviornocut)Added [UIPrinterCutterBehaviorPrinterDefault](https://developer.apple.com/documentation/uikit/uiprinter/cutterbehavior/printerdefault)Modified [UIPrintInteractionController.delegate](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618153-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIPrintInteractionControllerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIPrintInteractionControllerDelegate> delegate ``` |

Modified [+[UIPrintInteractionController printableUTIs]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618150-printableutis)

|  | Declaration |
| --- | --- |
| From | ``` + (NSSet *)printableUTIs ``` |
| To | ``` + (NSSet<NSString *> * _Nonnull)printableUTIs ``` |

Modified [UIPrintInteractionController.printFormatter](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618152-printformatter)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIPrintFormatter *printFormatter ``` |
| To | ``` @property(nonatomic, strong, nullable) UIPrintFormatter *printFormatter ``` |

Modified [UIPrintInteractionController.printInfo](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618171-printinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIPrintInfo *printInfo ``` |
| To | ``` @property(nonatomic, strong, nullable) UIPrintInfo *printInfo ``` |

Modified [UIPrintInteractionController.printPageRenderer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618148-printpagerenderer)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIPrintPageRenderer *printPageRenderer ``` |
| To | ``` @property(nonatomic, strong, nullable) UIPrintPageRenderer *printPageRenderer ``` |

Modified [-[UIPrintInteractionControllerDelegate printInteractionController:choosePaper:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618160-printinteractioncontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (UIPrintPaper *)printInteractionController:(UIPrintInteractionController *)printInteractionController choosePaper:(NSArray *)paperList ``` |
| To | ``` - (UIPrintPaper * _Nonnull)printInteractionController:(UIPrintInteractionController * _Nonnull)printInteractionController choosePaper:(NSArray<UIPrintPaper *> * _Nonnull)paperList ``` |

#### UIPrintPageRenderer.h

Modified [UIPrintPageRenderer.printFormatters](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621640-printformatters)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *printFormatters ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<UIPrintFormatter *> *printFormatters ``` |

Modified [-[UIPrintPageRenderer printFormattersForPageAtIndex:]](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621635-printformattersforpage)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)printFormattersForPageAtIndex:(NSInteger)pageIndex ``` |
| To | ``` - (NSArray<UIPrintFormatter *> * _Nullable)printFormattersForPageAtIndex:(NSInteger)pageIndex ``` |

#### UIPrintPaper.h

Modified [+[UIPrintPaper bestPaperForPageSize:withPapersFromArray:]](https://developer.apple.com/documentation/uikit/uiprintpaper/1623527-bestpaperforpagesize)

|  | Declaration |
| --- | --- |
| From | ``` + (UIPrintPaper *)bestPaperForPageSize:(CGSize)contentSize withPapersFromArray:(NSArray *)paperList ``` |
| To | ``` + (UIPrintPaper * _Nonnull)bestPaperForPageSize:(CGSize)contentSize withPapersFromArray:(NSArray<UIPrintPaper *> * _Nonnull)paperList ``` |

#### UIProgressView.h

Added [-[UIProgressView initWithCoder:]](https://developer.apple.com/documentation/uikit/uiprogressview/1619839-initwithcoder)Added [-[UIProgressView initWithFrame:]](https://developer.apple.com/documentation/uikit/uiprogressview/1619842-initwithframe)Added [UIProgressView.observedProgress](https://developer.apple.com/documentation/uikit/uiprogressview/1619840-observedprogress)Modified [UIProgressView.progressImage](https://developer.apple.com/documentation/uikit/uiprogressview/1619837-progressimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *progressImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *progressImage ``` |

Modified [UIProgressView.progressTintColor](https://developer.apple.com/documentation/uikit/uiprogressview/1619836-progresstintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *progressTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *progressTintColor ``` |

Modified [UIProgressView.trackImage](https://developer.apple.com/documentation/uikit/uiprogressview/1619843-trackimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *trackImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *trackImage ``` |

Modified [UIProgressView.trackTintColor](https://developer.apple.com/documentation/uikit/uiprogressview/1619841-tracktintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *trackTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *trackTintColor ``` |

#### UIPushBehavior.h

Modified [-[UIPushBehavior initWithItems:mode:]](https://developer.apple.com/documentation/uikit/uipushbehavior/1623329-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithItems:(NSArray *)items mode:(UIPushBehaviorMode)mode ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithItems:(NSArray<id<UIDynamicItem>> * _Nonnull)items mode:(UIPushBehaviorMode)mode ``` | yes |

Modified [UIPushBehavior.items](https://developer.apple.com/documentation/uikit/uipushbehavior/1623339-items)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *items ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<id<UIDynamicItem>> *items ``` |

#### UIReferenceLibraryViewController.h

Added [-[UIReferenceLibraryViewController initWithCoder:]](https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller/1624809-initwithcoder)Modified [-[UIReferenceLibraryViewController initWithTerm:]](https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller/1624808-initwithterm)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### UIRefreshControl.h

Modified [UIRefreshControl.attributedTitle](https://developer.apple.com/documentation/uikit/uirefreshcontrol/1624845-attributedtitle)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSAttributedString *attributedTitle ``` |
| To | ``` @property(nonatomic, strong, nullable) NSAttributedString *attributedTitle ``` |

Modified [UIRefreshControl.tintColor](https://developer.apple.com/documentation/uikit/uirefreshcontrol/1624847-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *tintColor ``` |
| To | ``` @property(nonatomic, strong) UIColor * _Null_unspecified tintColor ``` |

#### UIRegion.h (Added)

Added [UIRegion](https://developer.apple.com/documentation/uikit/uiregion)Added [-[UIRegion containsPoint:]](https://developer.apple.com/documentation/uikit/uiregion/1621893-containspoint)Added [+[UIRegion infiniteRegion]](https://developer.apple.com/documentation/uikit/uiregion/1621896-infinite)Added [-[UIRegion initWithRadius:]](https://developer.apple.com/documentation/uikit/uiregion/1621889-initwithradius)Added [-[UIRegion initWithSize:]](https://developer.apple.com/documentation/uikit/uiregion/1621891-initwithsize)Added [-[UIRegion inverseRegion]](https://developer.apple.com/documentation/uikit/uiregion/1621894-inverse)Added [-[UIRegion regionByDifferenceFromRegion:]](https://developer.apple.com/documentation/uikit/uiregion/1621892-regionbydifferencefromregion)Added [-[UIRegion regionByIntersectionWithRegion:]](https://developer.apple.com/documentation/uikit/uiregion/1621895-regionbyintersectionwithregion)Added [-[UIRegion regionByUnionWithRegion:]](https://developer.apple.com/documentation/uikit/uiregion/1621890-byunion)

#### UIResponder.h

Added [UIKeyCommand.discoverabilityTitle](https://developer.apple.com/documentation/uikit/uikeycommand/1621094-discoverabilitytitle)Added [-[UIKeyCommand init]](https://developer.apple.com/documentation/uikit/uikeycommand/1621100-init)Added [-[UIKeyCommand initWithCoder:]](https://developer.apple.com/documentation/uikit/uikeycommand/1621115-init)Added [+[UIKeyCommand keyCommandWithInput:modifierFlags:action:discoverabilityTitle:]](https://developer.apple.com/documentation/uikit/uikeycommand/1621139-init)Added [UIResponder.inputAssistantItem](https://developer.apple.com/documentation/uikit/uiresponder/1621135-inputassistantitem)Modified [UIResponder.inputAccessoryView](https://developer.apple.com/documentation/uikit/uiresponder/1621119-inputaccessoryview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIView *inputAccessoryView ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) __kindof UIView *inputAccessoryView ``` |

Modified [UIResponder.inputAccessoryViewController](https://developer.apple.com/documentation/uikit/uiresponder/1621124-inputaccessoryviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIInputViewController *inputAccessoryViewController ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIInputViewController *inputAccessoryViewController ``` |

Modified [UIResponder.inputView](https://developer.apple.com/documentation/uikit/uiresponder/1621092-inputview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIView *inputView ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) __kindof UIView *inputView ``` |

Modified [UIResponder.inputViewController](https://developer.apple.com/documentation/uikit/uiresponder/1621117-inputviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIInputViewController *inputViewController ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIInputViewController *inputViewController ``` |

Modified [UIResponder.keyCommands](https://developer.apple.com/documentation/uikit/uiresponder/1621141-keycommands)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *keyCommands ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<UIKeyCommand *> *keyCommands ``` |

Modified [UIResponder.textInputContextIdentifier](https://developer.apple.com/documentation/uikit/uiresponder/1621091-textinputcontextidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSString *textInputContextIdentifier ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) NSString *textInputContextIdentifier ``` |

Modified [UIResponder.textInputMode](https://developer.apple.com/documentation/uikit/uiresponder/1621133-textinputmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UITextInputMode *textInputMode ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UITextInputMode *textInputMode ``` |

Modified [-[UIResponder touchesBegan:withEvent:]](https://developer.apple.com/documentation/uikit/uiresponder/1621142-touchesbegan)

|  | Declaration |
| --- | --- |
| From | ``` - (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event ``` |
| To | ``` - (void)touchesBegan:(NSSet<UITouch *> * _Nonnull)touches withEvent:(UIEvent * _Nullable)event ``` |

Modified [-[UIResponder touchesCancelled:withEvent:]](https://developer.apple.com/documentation/uikit/uiresponder/1621116-touchescancelled)

|  | Declaration |
| --- | --- |
| From | ``` - (void)touchesCancelled:(NSSet *)touches withEvent:(UIEvent *)event ``` |
| To | ``` - (void)touchesCancelled:(NSSet<UITouch *> * _Nullable)touches withEvent:(UIEvent * _Nullable)event ``` |

Modified [-[UIResponder touchesEnded:withEvent:]](https://developer.apple.com/documentation/uikit/uiresponder/1621084-touchesended)

|  | Declaration |
| --- | --- |
| From | ``` - (void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event ``` |
| To | ``` - (void)touchesEnded:(NSSet<UITouch *> * _Nonnull)touches withEvent:(UIEvent * _Nullable)event ``` |

Modified [-[UIResponder touchesMoved:withEvent:]](https://developer.apple.com/documentation/uikit/uiresponder/1621107-touchesmoved)

|  | Declaration |
| --- | --- |
| From | ``` - (void)touchesMoved:(NSSet *)touches withEvent:(UIEvent *)event ``` |
| To | ``` - (void)touchesMoved:(NSSet<UITouch *> * _Nonnull)touches withEvent:(UIEvent * _Nullable)event ``` |

Modified [UIResponder.userActivity](https://developer.apple.com/documentation/uikit/uiresponder/1621089-useractivity)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSUserActivity *userActivity ``` |
| To | ``` @property(nonatomic, strong, nullable) NSUserActivity *userActivity ``` |

#### UIScreen.h

Added [UIScreen.overscanCompensationInsets](https://developer.apple.com/documentation/uikit/uiscreen/1617824-overscancompensationinsets)Added [UIScreenOverscanCompensationNone](https://developer.apple.com/documentation/uikit/uiscreenoverscancompensation/uiscreenoverscancompensationnone)Modified [UIScreen.applicationFrame](https://developer.apple.com/documentation/uikit/uiscreen/1617835-applicationframe)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIScreen.availableModes](https://developer.apple.com/documentation/uikit/uiscreen/1617839-availablemodes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *availableModes ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<UIScreenMode *> *availableModes ``` |

Modified [UIScreen.currentMode](https://developer.apple.com/documentation/uikit/uiscreen/1617817-currentmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIScreenMode *currentMode ``` |
| To | ``` @property(nonatomic, strong, nullable) UIScreenMode *currentMode ``` |

Modified [UIScreen.mirroredScreen](https://developer.apple.com/documentation/uikit/uiscreen/1617829-mirrored)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIScreen *mirroredScreen ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIScreen *mirroredScreen ``` |

Modified [UIScreen.preferredMode](https://developer.apple.com/documentation/uikit/uiscreen/1617823-preferredmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIScreenMode *preferredMode ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIScreenMode *preferredMode ``` |

Modified [+[UIScreen screens]](https://developer.apple.com/documentation/uikit/uiscreen/1617812-screens)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)screens ``` |
| To | ``` + (NSArray<UIScreen *> * _Nonnull)screens ``` |

Modified [UIScreenOverscanCompensationInsetApplicationFrame](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation/1617828-insetapplicationframe)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### UIScrollView.h

Modified [UIScrollView.delegate](https://developer.apple.com/documentation/uikit/uiscrollview/1619430-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIScrollViewDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIScrollViewDelegate> delegate ``` |

Modified [-[UIScrollView touchesShouldBegin:withEvent:inContentView:]](https://developer.apple.com/documentation/uikit/uiscrollview/1619418-touchesshouldbegin)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)touchesShouldBegin:(NSSet *)touches withEvent:(UIEvent *)event inContentView:(UIView *)view ``` |
| To | ``` - (BOOL)touchesShouldBegin:(NSSet<UITouch *> * _Nonnull)touches withEvent:(UIEvent * _Nullable)event inContentView:(UIView * _Nonnull)view ``` |

#### UISearchBar.h

Added [-[UISearchBar init]](https://developer.apple.com/documentation/uikit/uisearchbar/1624304-init)Added [-[UISearchBar initWithCoder:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624324-initwithcoder)Added [-[UISearchBar initWithFrame:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624269-initwithframe)Added [UISearchBar.inputAssistantItem](https://developer.apple.com/documentation/uikit/uisearchbar/1624275-inputassistantitem)Modified [UISearchBar.backgroundImage](https://developer.apple.com/documentation/uikit/uisearchbar/1624276-backgroundimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *backgroundImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *backgroundImage ``` |

Modified [UISearchBar.barTintColor](https://developer.apple.com/documentation/uikit/uisearchbar/1624295-bartintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *barTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *barTintColor ``` |

Modified [UISearchBar.delegate](https://developer.apple.com/documentation/uikit/uisearchbar/1624291-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UISearchBarDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UISearchBarDelegate> delegate ``` |

Modified [UISearchBar.inputAccessoryView](https://developer.apple.com/documentation/uikit/uisearchbar/1624279-inputaccessoryview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readwrite, retain) UIView *inputAccessoryView ``` |
| To | ``` @property(nonatomic, readwrite, strong, nullable) UIView *inputAccessoryView ``` |

Modified [UISearchBar.scopeBarBackgroundImage](https://developer.apple.com/documentation/uikit/uisearchbar/1624317-scopebarbackgroundimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *scopeBarBackgroundImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *scopeBarBackgroundImage ``` |

Modified [-[UISearchBar scopeBarButtonTitleTextAttributesForState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624309-scopebarbuttontitletextattribute)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)scopeBarButtonTitleTextAttributesForState:(UIControlState)state ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nullable)scopeBarButtonTitleTextAttributesForState:(UIControlState)state ``` |

Modified [UISearchBar.scopeButtonTitles](https://developer.apple.com/documentation/uikit/uisearchbar/1624292-scopebuttontitles)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *scopeButtonTitles ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *scopeButtonTitles ``` |

Modified [-[UISearchBar setScopeBarButtonTitleTextAttributes:forState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624277-setscopebarbuttontitletextattrib)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setScopeBarButtonTitleTextAttributes:(NSDictionary *)attributes forState:(UIControlState)state ``` |
| To | ``` - (void)setScopeBarButtonTitleTextAttributes:(NSDictionary<NSString *,id> * _Nullable)attributes forState:(UIControlState)state ``` |

Modified [UISearchBar.tintColor](https://developer.apple.com/documentation/uikit/uisearchbar/1624286-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *tintColor ``` |
| To | ``` @property(nonatomic, strong) UIColor * _Null_unspecified tintColor ``` |

#### UISearchController.h

Modified [UISearchController.delegate](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618654-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UISearchControllerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UISearchControllerDelegate> delegate ``` |

Modified [UISearchController.searchBar](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618657-searchbar)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain, readonly) UISearchBar *searchBar ``` |
| To | ``` @property(nonatomic, strong, readonly, nonnull) UISearchBar *searchBar ``` |

Modified [UISearchController.searchResultsController](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618649-searchresultscontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain, readonly) UIViewController *searchResultsController ``` |
| To | ``` @property(nonatomic, strong, readonly, nullable) UIViewController *searchResultsController ``` |

Modified [UISearchController.searchResultsUpdater](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618661-searchresultsupdater)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UISearchResultsUpdating> searchResultsUpdater ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UISearchResultsUpdating> searchResultsUpdater ``` |

#### UISearchDisplayController.h

Modified [UISearchDisplayController.searchResultsDataSource](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/1620390-searchresultsdatasource)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UITableViewDataSource> searchResultsDataSource ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UITableViewDataSource> searchResultsDataSource ``` |

Modified [UISearchDisplayController.searchResultsDelegate](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/1620404-searchresultsdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UITableViewDelegate> searchResultsDelegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UITableViewDelegate> searchResultsDelegate ``` |

#### UISegmentedControl.h

Modified [UISegmentedControl.tintColor](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618552-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *tintColor ``` |
| To | ``` @property(nonatomic, strong) UIColor * _Null_unspecified tintColor ``` |

#### UISlider.h

Modified [UISlider.maximumTrackTintColor](https://developer.apple.com/documentation/uikit/uislider/1621334-maximumtracktintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *maximumTrackTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *maximumTrackTintColor ``` |

Modified [UISlider.maximumValueImage](https://developer.apple.com/documentation/uikit/uislider/1621329-maximumvalueimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *maximumValueImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *maximumValueImage ``` |

Modified [UISlider.minimumTrackTintColor](https://developer.apple.com/documentation/uikit/uislider/1621348-minimumtracktintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *minimumTrackTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *minimumTrackTintColor ``` |

Modified [UISlider.minimumValueImage](https://developer.apple.com/documentation/uikit/uislider/1621337-minimumvalueimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *minimumValueImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *minimumValueImage ``` |

Modified [UISlider.thumbTintColor](https://developer.apple.com/documentation/uikit/uislider/1621332-thumbtintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *thumbTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *thumbTintColor ``` |

#### UISnapBehavior.h

Added [UISnapBehavior.snapPoint](https://developer.apple.com/documentation/uikit/uisnapbehavior/1621013-snappoint)Modified [-[UISnapBehavior initWithItem:snapToPoint:]](https://developer.apple.com/documentation/uikit/uisnapbehavior/1621011-initwithitem)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### UISplitViewController.h

Modified [UISplitViewController.delegate](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623167-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UISplitViewControllerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UISplitViewControllerDelegate> delegate ``` |

Modified [UISplitViewController.viewControllers](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623181-viewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *viewControllers ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<__kindof UIViewController *> *viewControllers ``` |

Modified [-[UISplitViewControllerDelegate splitViewControllerSupportedInterfaceOrientations:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623178-splitviewcontrollersupportedinte)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)splitViewControllerSupportedInterfaceOrientations:(UISplitViewController *)splitViewController ``` |
| To | ``` - (UIInterfaceOrientationMask)splitViewControllerSupportedInterfaceOrientations:(UISplitViewController * _Nonnull)splitViewController ``` |

Modified [UIViewController.splitViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1623187-splitviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UISplitViewController *splitViewController ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UISplitViewController *splitViewController ``` |

#### UIStackView.h (Added)

Added [UIStackView](https://developer.apple.com/documentation/uikit/uistackview)Added [-[UIStackView addArrangedSubview:]](https://developer.apple.com/documentation/uikit/uistackview/1616227-addarrangedsubview)Added [UIStackView.alignment](https://developer.apple.com/documentation/uikit/uistackview/1616243-alignment)Added [UIStackView.arrangedSubviews](https://developer.apple.com/documentation/uikit/uistackview/1616232-arrangedsubviews)Added [UIStackView.axis](https://developer.apple.com/documentation/uikit/uistackview/1616223-axis)Added [UIStackView.baselineRelativeArrangement](https://developer.apple.com/documentation/uikit/uistackview/1616224-baselinerelativearrangement)Added [UIStackView.distribution](https://developer.apple.com/documentation/uikit/uistackview/1616233-distribution)Added [-[UIStackView initWithArrangedSubviews:]](https://developer.apple.com/documentation/uikit/uistackview/1616240-initwitharrangedsubviews)Added [-[UIStackView insertArrangedSubview:atIndex:]](https://developer.apple.com/documentation/uikit/uistackview/1616237-insertarrangedsubview)Added [UIStackView.layoutMarginsRelativeArrangement](https://developer.apple.com/documentation/uikit/uistackview/1616220-layoutmarginsrelativearrangement)Added [-[UIStackView removeArrangedSubview:]](https://developer.apple.com/documentation/uikit/uistackview/1616235-removearrangedsubview)Added [UIStackView.spacing](https://developer.apple.com/documentation/uikit/uistackview/1616225-spacing)Added [UIStackViewAlignment](https://developer.apple.com/documentation/uikit/uistackview/alignment)Added [UIStackViewAlignmentBottom](https://developer.apple.com/documentation/uikit/uistackviewalignment/uistackviewalignmentbottom)Added [UIStackViewAlignmentCenter](https://developer.apple.com/documentation/uikit/uistackview/alignment/center)Added [UIStackViewAlignmentFill](https://developer.apple.com/documentation/uikit/uistackview/alignment/fill)Added [UIStackViewAlignmentFirstBaseline](https://developer.apple.com/documentation/uikit/uistackview/alignment/firstbaseline)Added [UIStackViewAlignmentLastBaseline](https://developer.apple.com/documentation/uikit/uistackviewalignment/uistackviewalignmentlastbaseline)Added [UIStackViewAlignmentLeading](https://developer.apple.com/documentation/uikit/uistackview/alignment/leading)Added [UIStackViewAlignmentTop](https://developer.apple.com/documentation/uikit/uistackview/alignment/1616238-top)Added [UIStackViewAlignmentTrailing](https://developer.apple.com/documentation/uikit/uistackview/alignment/trailing)Added [UIStackViewDistribution](https://developer.apple.com/documentation/uikit/uistackviewdistribution)Added [UIStackViewDistributionEqualCentering](https://developer.apple.com/documentation/uikit/uistackviewdistribution/uistackviewdistributionequalcentering)Added [UIStackViewDistributionEqualSpacing](https://developer.apple.com/documentation/uikit/uistackview/distribution/equalspacing)Added [UIStackViewDistributionFill](https://developer.apple.com/documentation/uikit/uistackview/distribution/fill)Added [UIStackViewDistributionFillEqually](https://developer.apple.com/documentation/uikit/uistackviewdistribution/uistackviewdistributionfillequally)Added [UIStackViewDistributionFillProportionally](https://developer.apple.com/documentation/uikit/uistackview/distribution/fillproportionally)

#### UIStateRestoration.h

Modified [+[UIObjectRestoration objectWithRestorationIdentifierPath:coder:]](https://developer.apple.com/documentation/uikit/uiobjectrestoration/1616855-object)

|  | Declaration |
| --- | --- |
| From | ``` + (id<UIStateRestoring>)objectWithRestorationIdentifierPath:(NSArray *)identifierComponents coder:(NSCoder *)coder ``` |
| To | ``` + (id<UIStateRestoring> _Nullable)objectWithRestorationIdentifierPath:(NSArray<NSString *> * _Nonnull)identifierComponents coder:(NSCoder * _Nonnull)coder ``` |

#### UIStepper.h

Modified [UIStepper.tintColor](https://developer.apple.com/documentation/uikit/uistepper/1624073-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *tintColor ``` |
| To | ``` @property(nonatomic, strong) UIColor * _Null_unspecified tintColor ``` |

#### UIStoryboard.h

Modified [-[UIStoryboard instantiateInitialViewController]](https://developer.apple.com/documentation/uikit/uistoryboard/1616213-instantiateinitialviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (id)instantiateInitialViewController ``` |
| To | ``` - (__kindof UIViewController * _Nullable)instantiateInitialViewController ``` |

Modified [-[UIStoryboard instantiateViewControllerWithIdentifier:]](https://developer.apple.com/documentation/uikit/uistoryboard/1616214-instantiateviewcontrollerwithide)

|  | Declaration |
| --- | --- |
| From | ``` - (id)instantiateViewControllerWithIdentifier:(NSString *)identifier ``` |
| To | ``` - (__kindof UIViewController * _Nonnull)instantiateViewControllerWithIdentifier:(NSString * _Nonnull)identifier ``` |

#### UIStoryboardPopoverSegue.h

Modified [UIStoryboardPopoverSegue](https://developer.apple.com/documentation/uikit/uistoryboardpopoversegue)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIStoryboardPopoverSegue.popoverController](https://developer.apple.com/documentation/uikit/uistoryboardpopoversegue/1624759-popovercontroller)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, retain, readonly) UIPopoverController *popoverController ``` | -- |
| To | ``` @property(nonatomic, strong, readonly, nonnull) UIPopoverController *popoverController ``` | iOS 9.0 |

#### UIStoryboardSegue.h

Added [UIStoryboardUnwindSegueSource](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource)Added [UIStoryboardUnwindSegueSource.sender](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource/1621914-sender)Added [UIStoryboardUnwindSegueSource.sourceViewController](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource/1621917-sourceviewcontroller)Added [UIStoryboardUnwindSegueSource.unwindAction](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource/1621915-unwindaction)Modified [UIStoryboardSegue.destinationViewController](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621916-destinationviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id destinationViewController ``` |
| To | ``` @property(nonatomic, readonly, nonnull) __kindof UIViewController *destinationViewController ``` |

Modified [UIStoryboardSegue.identifier](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621909-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *identifier ``` |
| To | ``` @property(nonatomic, copy, readonly, nullable) NSString *identifier ``` |

Modified [-[UIStoryboardSegue initWithIdentifier:source:destination:]](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621908-initwithidentifier)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIStoryboardSegue.sourceViewController](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621918-source)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id sourceViewController ``` |
| To | ``` @property(nonatomic, readonly, nonnull) __kindof UIViewController *sourceViewController ``` |

#### UISwitch.h

Added [-[UISwitch initWithCoder:]](https://developer.apple.com/documentation/uikit/uiswitch/1623685-initwithcoder)Modified [-[UISwitch initWithFrame:]](https://developer.apple.com/documentation/uikit/uiswitch/1623682-initwithframe)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [UISwitch.offImage](https://developer.apple.com/documentation/uikit/uiswitch/1623683-offimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *offImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *offImage ``` |

Modified [UISwitch.onImage](https://developer.apple.com/documentation/uikit/uiswitch/1623689-onimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *onImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *onImage ``` |

Modified [UISwitch.onTintColor](https://developer.apple.com/documentation/uikit/uiswitch/1623687-ontintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *onTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *onTintColor ``` |

Modified [UISwitch.thumbTintColor](https://developer.apple.com/documentation/uikit/uiswitch/1623684-thumbtintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *thumbTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *thumbTintColor ``` |

Modified [UISwitch.tintColor](https://developer.apple.com/documentation/uikit/uiswitch/1623688-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *tintColor ``` |
| To | ``` @property(nonatomic, strong) UIColor * _Null_unspecified tintColor ``` |

#### UITabBar.h

Modified [UITabBar.backgroundImage](https://developer.apple.com/documentation/uikit/uitabbar/1623469-backgroundimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *backgroundImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *backgroundImage ``` |

Modified [UITabBar.barTintColor](https://developer.apple.com/documentation/uikit/uitabbar/1623445-bartintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *barTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *barTintColor ``` |

Modified [-[UITabBar beginCustomizingItems:]](https://developer.apple.com/documentation/uikit/uitabbar/1623462-begincustomizingitems)

|  | Declaration |
| --- | --- |
| From | ``` - (void)beginCustomizingItems:(NSArray *)items ``` |
| To | ``` - (void)beginCustomizingItems:(NSArray<UITabBarItem *> * _Nonnull)items ``` |

Modified [UITabBar.items](https://developer.apple.com/documentation/uikit/uitabbar/1623466-items)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *items ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<UITabBarItem *> *items ``` |

Modified [UITabBar.selectedImageTintColor](https://developer.apple.com/documentation/uikit/uitabbar/1623470-selectedimagetintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *selectedImageTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *selectedImageTintColor ``` |

Modified [UITabBar.selectionIndicatorImage](https://developer.apple.com/documentation/uikit/uitabbar/1623456-selectionindicatorimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *selectionIndicatorImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *selectionIndicatorImage ``` |

Modified [-[UITabBar setItems:animated:]](https://developer.apple.com/documentation/uikit/uitabbar/1623455-setitems)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setItems:(NSArray *)items animated:(BOOL)animated ``` |
| To | ``` - (void)setItems:(NSArray<UITabBarItem *> * _Nullable)items animated:(BOOL)animated ``` |

Modified [UITabBar.shadowImage](https://developer.apple.com/documentation/uikit/uitabbar/1623452-shadowimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *shadowImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *shadowImage ``` |

Modified [UITabBar.tintColor](https://developer.apple.com/documentation/uikit/uitabbar/1623460-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *tintColor ``` |
| To | ``` @property(nonatomic, strong) UIColor * _Null_unspecified tintColor ``` |

Modified [-[UITabBarDelegate tabBar:didBeginCustomizingItems:]](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623471-tabbar)

|  | Declaration |
| --- | --- |
| From | ``` - (void)tabBar:(UITabBar *)tabBar didBeginCustomizingItems:(NSArray *)items ``` |
| To | ``` - (void)tabBar:(UITabBar * _Nonnull)tabBar didBeginCustomizingItems:(NSArray<UITabBarItem *> * _Nonnull)items ``` |

Modified [-[UITabBarDelegate tabBar:didEndCustomizingItems:changed:]](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623447-tabbar)

|  | Declaration |
| --- | --- |
| From | ``` - (void)tabBar:(UITabBar *)tabBar didEndCustomizingItems:(NSArray *)items changed:(BOOL)changed ``` |
| To | ``` - (void)tabBar:(UITabBar * _Nonnull)tabBar didEndCustomizingItems:(NSArray<UITabBarItem *> * _Nonnull)items changed:(BOOL)changed ``` |

Modified [-[UITabBarDelegate tabBar:willBeginCustomizingItems:]](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623451-tabbar)

|  | Declaration |
| --- | --- |
| From | ``` - (void)tabBar:(UITabBar *)tabBar willBeginCustomizingItems:(NSArray *)items ``` |
| To | ``` - (void)tabBar:(UITabBar * _Nonnull)tabBar willBeginCustomizingItems:(NSArray<UITabBarItem *> * _Nonnull)items ``` |

Modified [-[UITabBarDelegate tabBar:willEndCustomizingItems:changed:]](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623464-tabbar)

|  | Declaration |
| --- | --- |
| From | ``` - (void)tabBar:(UITabBar *)tabBar willEndCustomizingItems:(NSArray *)items changed:(BOOL)changed ``` |
| To | ``` - (void)tabBar:(UITabBar * _Nonnull)tabBar willEndCustomizingItems:(NSArray<UITabBarItem *> * _Nonnull)items changed:(BOOL)changed ``` |

#### UITabBarController.h

Modified [UITabBarController.customizableViewControllers](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621184-customizableviewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *customizableViewControllers ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<__kindof UIViewController *> *customizableViewControllers ``` |

Modified [UITabBarController.delegate](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621164-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UITabBarControllerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UITabBarControllerDelegate> delegate ``` |

Modified [UITabBarController.selectedViewController](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621172-selectedviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) UIViewController *selectedViewController ``` |
| To | ``` @property(nonatomic, assign, nullable) __kindof UIViewController *selectedViewController ``` |

Modified [-[UITabBarController setViewControllers:animated:]](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621177-setviewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setViewControllers:(NSArray *)viewControllers animated:(BOOL)animated ``` |
| To | ``` - (void)setViewControllers:(NSArray<__kindof UIViewController *> * _Nullable)viewControllers animated:(BOOL)animated ``` |

Modified [UITabBarController.viewControllers](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621185-viewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *viewControllers ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<__kindof UIViewController *> *viewControllers ``` |

Modified [-[UITabBarControllerDelegate tabBarController:didEndCustomizingViewControllers:changed:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621168-tabbarcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)tabBarController:(UITabBarController *)tabBarController didEndCustomizingViewControllers:(NSArray *)viewControllers changed:(BOOL)changed ``` |
| To | ``` - (void)tabBarController:(UITabBarController * _Nonnull)tabBarController didEndCustomizingViewControllers:(NSArray<__kindof UIViewController *> * _Nonnull)viewControllers changed:(BOOL)changed ``` |

Modified [-[UITabBarControllerDelegate tabBarController:willBeginCustomizingViewControllers:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621179-tabbarcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)tabBarController:(UITabBarController *)tabBarController willBeginCustomizingViewControllers:(NSArray *)viewControllers ``` |
| To | ``` - (void)tabBarController:(UITabBarController * _Nonnull)tabBarController willBeginCustomizingViewControllers:(NSArray<__kindof UIViewController *> * _Nonnull)viewControllers ``` |

Modified [-[UITabBarControllerDelegate tabBarController:willEndCustomizingViewControllers:changed:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621178-tabbarcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)tabBarController:(UITabBarController *)tabBarController willEndCustomizingViewControllers:(NSArray *)viewControllers changed:(BOOL)changed ``` |
| To | ``` - (void)tabBarController:(UITabBarController * _Nonnull)tabBarController willEndCustomizingViewControllers:(NSArray<__kindof UIViewController *> * _Nonnull)viewControllers changed:(BOOL)changed ``` |

Modified [-[UITabBarControllerDelegate tabBarControllerSupportedInterfaceOrientations:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621180-tabbarcontrollersupportedinterfa)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)tabBarControllerSupportedInterfaceOrientations:(UITabBarController *)tabBarController ``` |
| To | ``` - (UIInterfaceOrientationMask)tabBarControllerSupportedInterfaceOrientations:(UITabBarController * _Nonnull)tabBarController ``` |

Modified [UIViewController.tabBarController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621169-tabbarcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UITabBarController *tabBarController ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UITabBarController *tabBarController ``` |

Modified [UIViewController.tabBarItem](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621175-tabbaritem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UITabBarItem *tabBarItem ``` |
| To | ``` @property(nonatomic, strong) UITabBarItem * _Null_unspecified tabBarItem ``` |

#### UITabBarItem.h

Removed [-[UITabBarItem setTitlePositionAdjustment:]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617070-titlepositionadjustment)Added [-[UITabBarItem init]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617055-init)Added [-[UITabBarItem initWithCoder:]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617071-initwithcoder)Modified [UITabBarItem.selectedImage](https://developer.apple.com/documentation/uikit/uitabbaritem/1617072-selectedimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *selectedImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *selectedImage ``` |

Modified [UITabBarItem.titlePositionAdjustment](https://developer.apple.com/documentation/uikit/uitabbaritem/1617070-titlepositionadjustment)

|  | Declaration |
| --- | --- |
| From | ``` - (UIOffset)titlePositionAdjustment ``` |
| To | ``` @property(nonatomic, readwrite, assign) UIOffset titlePositionAdjustment ``` |

#### UITableView.h

Added [UITableView.cellLayoutMarginsFollowReadableWidth](https://developer.apple.com/documentation/uikit/uitableview/1614849-celllayoutmarginsfollowreadablew)Added [-[UITableView initWithCoder:]](https://developer.apple.com/documentation/uikit/uitableview/1614859-init)Modified [+[NSIndexPath indexPathForRow:inSection:]](https://developer.apple.com/documentation/foundation/nsindexpath/1614934-init)

|  | Declaration |
| --- | --- |
| From | ``` + (NSIndexPath *)indexPathForRow:(NSInteger)row inSection:(NSInteger)section ``` |
| To | ``` + (instancetype _Nonnull)indexPathForRow:(NSInteger)row inSection:(NSInteger)section ``` |

Modified [UITableView.backgroundView](https://developer.apple.com/documentation/uikit/uitableview/1614986-backgroundview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readwrite, retain) UIView *backgroundView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *backgroundView ``` |

Modified [-[UITableView cellForRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableview/1614983-cellforrowatindexpath)

|  | Declaration |
| --- | --- |
| From | ``` - (UITableViewCell *)cellForRowAtIndexPath:(NSIndexPath *)indexPath ``` |
| To | ``` - (__kindof UITableViewCell * _Nullable)cellForRowAtIndexPath:(NSIndexPath * _Nonnull)indexPath ``` |

Modified [UITableView.dataSource](https://developer.apple.com/documentation/uikit/uitableview/1614955-datasource)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UITableViewDataSource> dataSource ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UITableViewDataSource> dataSource ``` |

Modified [UITableView.delegate](https://developer.apple.com/documentation/uikit/uitableview/1614894-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UITableViewDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UITableViewDelegate> delegate ``` |

Modified [-[UITableView deleteRowsAtIndexPaths:withRowAnimation:]](https://developer.apple.com/documentation/uikit/uitableview/1614960-deleterowsatindexpaths)

|  | Declaration |
| --- | --- |
| From | ``` - (void)deleteRowsAtIndexPaths:(NSArray *)indexPaths withRowAnimation:(UITableViewRowAnimation)animation ``` |
| To | ``` - (void)deleteRowsAtIndexPaths:(NSArray<NSIndexPath *> * _Nonnull)indexPaths withRowAnimation:(UITableViewRowAnimation)animation ``` |

Modified [-[UITableView dequeueReusableCellWithIdentifier:]](https://developer.apple.com/documentation/uikit/uitableview/1614891-dequeuereusablecell)

|  | Declaration |
| --- | --- |
| From | ``` - (id)dequeueReusableCellWithIdentifier:(NSString *)identifier ``` |
| To | ``` - (__kindof UITableViewCell * _Nullable)dequeueReusableCellWithIdentifier:(NSString * _Nonnull)identifier ``` |

Modified [-[UITableView dequeueReusableCellWithIdentifier:forIndexPath:]](https://developer.apple.com/documentation/uikit/uitableview/1614878-dequeuereusablecellwithidentifie)

|  | Declaration |
| --- | --- |
| From | ``` - (id)dequeueReusableCellWithIdentifier:(NSString *)identifier forIndexPath:(NSIndexPath *)indexPath ``` |
| To | ``` - (__kindof UITableViewCell * _Nonnull)dequeueReusableCellWithIdentifier:(NSString * _Nonnull)identifier forIndexPath:(NSIndexPath * _Nonnull)indexPath ``` |

Modified [-[UITableView dequeueReusableHeaderFooterViewWithIdentifier:]](https://developer.apple.com/documentation/uikit/uitableview/1614975-dequeuereusableheaderfootervieww)

|  | Declaration |
| --- | --- |
| From | ``` - (id)dequeueReusableHeaderFooterViewWithIdentifier:(NSString *)identifier ``` |
| To | ``` - (__kindof UITableViewHeaderFooterView * _Nullable)dequeueReusableHeaderFooterViewWithIdentifier:(NSString * _Nonnull)identifier ``` |

Modified [UITableView.indexPathForSelectedRow](https://developer.apple.com/documentation/uikit/uitableview/1615000-indexpathforselectedrow)

|  | Declaration |
| --- | --- |
| From | ``` - (NSIndexPath *)indexPathForSelectedRow ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSIndexPath *indexPathForSelectedRow ``` |

Modified [-[UITableView indexPathsForRowsInRect:]](https://developer.apple.com/documentation/uikit/uitableview/1614991-indexpathsforrowsinrect)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)indexPathsForRowsInRect:(CGRect)rect ``` |
| To | ``` - (NSArray<NSIndexPath *> * _Nullable)indexPathsForRowsInRect:(CGRect)rect ``` |

Modified [UITableView.indexPathsForSelectedRows](https://developer.apple.com/documentation/uikit/uitableview/1614864-indexpathsforselectedrows)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)indexPathsForSelectedRows ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<NSIndexPath *> *indexPathsForSelectedRows ``` |

Modified [UITableView.indexPathsForVisibleRows](https://developer.apple.com/documentation/uikit/uitableview/1614885-indexpathsforvisiblerows)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)indexPathsForVisibleRows ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<NSIndexPath *> *indexPathsForVisibleRows ``` |

Modified [-[UITableView initWithFrame:style:]](https://developer.apple.com/documentation/uikit/uitableview/1614886-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableView insertRowsAtIndexPaths:withRowAnimation:]](https://developer.apple.com/documentation/uikit/uitableview/1614879-insertrowsatindexpaths)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertRowsAtIndexPaths:(NSArray *)indexPaths withRowAnimation:(UITableViewRowAnimation)animation ``` |
| To | ``` - (void)insertRowsAtIndexPaths:(NSArray<NSIndexPath *> * _Nonnull)indexPaths withRowAnimation:(UITableViewRowAnimation)animation ``` |

Modified [UITableView.numberOfSections](https://developer.apple.com/documentation/uikit/uitableview/1614924-numberofsections)

|  | Declaration |
| --- | --- |
| From | ``` - (NSInteger)numberOfSections ``` |
| To | ``` @property(nonatomic, readonly) NSInteger numberOfSections ``` |

Modified [-[UITableView reloadRowsAtIndexPaths:withRowAnimation:]](https://developer.apple.com/documentation/uikit/uitableview/1614935-reloadrowsatindexpaths)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reloadRowsAtIndexPaths:(NSArray *)indexPaths withRowAnimation:(UITableViewRowAnimation)animation ``` |
| To | ``` - (void)reloadRowsAtIndexPaths:(NSArray<NSIndexPath *> * _Nonnull)indexPaths withRowAnimation:(UITableViewRowAnimation)animation ``` |

Modified [UITableView.sectionIndexBackgroundColor](https://developer.apple.com/documentation/uikit/uitableview/1614918-sectionindexbackgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *sectionIndexBackgroundColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *sectionIndexBackgroundColor ``` |

Modified [UITableView.sectionIndexColor](https://developer.apple.com/documentation/uikit/uitableview/1614915-sectionindexcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *sectionIndexColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *sectionIndexColor ``` |

Modified [UITableView.sectionIndexTrackingBackgroundColor](https://developer.apple.com/documentation/uikit/uitableview/1614992-sectionindextrackingbackgroundco)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *sectionIndexTrackingBackgroundColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *sectionIndexTrackingBackgroundColor ``` |

Modified [UITableView.separatorColor](https://developer.apple.com/documentation/uikit/uitableview/1614984-separatorcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *separatorColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *separatorColor ``` |

Modified [UITableView.tableFooterView](https://developer.apple.com/documentation/uikit/uitableview/1614976-tablefooterview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *tableFooterView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *tableFooterView ``` |

Modified [UITableView.tableHeaderView](https://developer.apple.com/documentation/uikit/uitableview/1614904-tableheaderview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *tableHeaderView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *tableHeaderView ``` |

Modified [UITableView.visibleCells](https://developer.apple.com/documentation/uikit/uitableview/1614896-visiblecells)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)visibleCells ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<__kindof UITableViewCell *> *visibleCells ``` |

Modified [-[UITableViewDataSource sectionIndexTitlesForTableView:]](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614857-sectionindextitles)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sectionIndexTitlesForTableView:(UITableView *)tableView ``` |
| To | ``` - (NSArray<NSString *> * _Nullable)sectionIndexTitlesForTableView:(UITableView * _Nonnull)tableView ``` |

Modified [-[UITableViewDelegate tableView:editActionsForRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614956-tableview)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)tableView:(UITableView *)tableView editActionsForRowAtIndexPath:(NSIndexPath *)indexPath ``` |
| To | ``` - (NSArray<UITableViewRowAction *> * _Nullable)tableView:(UITableView * _Nonnull)tableView editActionsForRowAtIndexPath:(NSIndexPath * _Nonnull)indexPath ``` |

#### UITableViewCell.h

Added [-[UITableViewCell initWithCoder:]](https://developer.apple.com/documentation/uikit/uitableviewcell/1623220-initwithcoder)Modified [UITableViewCell.accessoryView](https://developer.apple.com/documentation/uikit/uitableviewcell/1623219-accessoryview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *accessoryView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *accessoryView ``` |

Modified [UITableViewCell.backgroundView](https://developer.apple.com/documentation/uikit/uitableviewcell/1623260-backgroundview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *backgroundView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *backgroundView ``` |

Modified [UITableViewCell.contentView](https://developer.apple.com/documentation/uikit/uitableviewcell/1623229-contentview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIView *contentView ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) UIView *contentView ``` |

Modified [UITableViewCell.detailTextLabel](https://developer.apple.com/documentation/uikit/uitableviewcell/1623273-detailtextlabel)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UILabel *detailTextLabel ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UILabel *detailTextLabel ``` |

Modified [UITableViewCell.editingAccessoryView](https://developer.apple.com/documentation/uikit/uitableviewcell/1623264-editingaccessoryview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *editingAccessoryView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *editingAccessoryView ``` |

Modified [UITableViewCell.font](https://developer.apple.com/documentation/uikit/uitableviewcell/1623236-font)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIFont *font ``` |
| To | ``` @property(nonatomic, strong, nullable) UIFont *font ``` |

Modified [UITableViewCell.image](https://developer.apple.com/documentation/uikit/uitableviewcell/1623213-image)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *image ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *image ``` |

Modified [UITableViewCell.imageView](https://developer.apple.com/documentation/uikit/uitableviewcell/1623270-imageview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIImageView *imageView ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIImageView *imageView ``` |

Modified [-[UITableViewCell initWithStyle:reuseIdentifier:]](https://developer.apple.com/documentation/uikit/uitableviewcell/1623276-initwithstyle)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITableViewCell.multipleSelectionBackgroundView](https://developer.apple.com/documentation/uikit/uitableviewcell/1623275-multipleselectionbackgroundview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *multipleSelectionBackgroundView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *multipleSelectionBackgroundView ``` |

Modified [UITableViewCell.selectedBackgroundView](https://developer.apple.com/documentation/uikit/uitableviewcell/1623226-selectedbackgroundview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *selectedBackgroundView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *selectedBackgroundView ``` |

Modified [UITableViewCell.selectedImage](https://developer.apple.com/documentation/uikit/uitableviewcell/1623215-selectedimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *selectedImage ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *selectedImage ``` |

Modified [UITableViewCell.selectedTextColor](https://developer.apple.com/documentation/uikit/uitableviewcell/1623251-selectedtextcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *selectedTextColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *selectedTextColor ``` |

Modified [UITableViewCell.textColor](https://developer.apple.com/documentation/uikit/uitableviewcell/1623235-textcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *textColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *textColor ``` |

Modified [UITableViewCell.textLabel](https://developer.apple.com/documentation/uikit/uitableviewcell/1623210-textlabel)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UILabel *textLabel ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UILabel *textLabel ``` |

#### UITableViewController.h

Modified [UITableViewController.refreshControl](https://developer.apple.com/documentation/uikit/uitableviewcontroller/1614752-refreshcontrol)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIRefreshControl *refreshControl ``` |
| To | ``` @property(nonatomic, strong, nullable) UIRefreshControl *refreshControl ``` |

Modified [UITableViewController.tableView](https://developer.apple.com/documentation/uikit/uitableviewcontroller/1614753-tableview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UITableView *tableView ``` |
| To | ``` @property(nonatomic, strong) UITableView * _Null_unspecified tableView ``` |

#### UITableViewHeaderFooterView.h

Added [-[UITableViewHeaderFooterView initWithCoder:]](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624917-init)Modified [UITableViewHeaderFooterView.backgroundView](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624913-backgroundview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *backgroundView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *backgroundView ``` |

Modified [UITableViewHeaderFooterView.contentView](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624914-contentview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIView *contentView ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) UIView *contentView ``` |

Modified [UITableViewHeaderFooterView.detailTextLabel](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624910-detailtextlabel)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UILabel *detailTextLabel ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UILabel *detailTextLabel ``` |

Modified [-[UITableViewHeaderFooterView initWithReuseIdentifier:]](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624918-initwithreuseidentifier)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITableViewHeaderFooterView.textLabel](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624912-textlabel)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UILabel *textLabel ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UILabel *textLabel ``` |

Modified UITableViewHeaderFooterView.tintColor

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *tintColor ``` |
| To | ``` @property(nonatomic, strong) UIColor * _Null_unspecified tintColor ``` |

#### UITextField.h

Modified [UITextField.background](https://developer.apple.com/documentation/uikit/uitextfield/1619623-background)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *background ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *background ``` |

Modified [UITextField.defaultTextAttributes](https://developer.apple.com/documentation/uikit/uitextfield/1619618-defaulttextattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDictionary *defaultTextAttributes ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSDictionary<NSString *,id> *defaultTextAttributes ``` |

Modified [UITextField.delegate](https://developer.apple.com/documentation/uikit/uitextfield/1619595-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UITextFieldDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UITextFieldDelegate> delegate ``` |

Modified [UITextField.disabledBackground](https://developer.apple.com/documentation/uikit/uitextfield/1619611-disabledbackground)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIImage *disabledBackground ``` |
| To | ``` @property(nonatomic, strong, nullable) UIImage *disabledBackground ``` |

Modified [UITextField.font](https://developer.apple.com/documentation/uikit/uitextfield/1619604-font)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIFont *font ``` |
| To | ``` @property(nonatomic, strong, nullable) UIFont *font ``` |

Modified [UITextField.inputAccessoryView](https://developer.apple.com/documentation/uikit/uitextfield/1619627-inputaccessoryview)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, retain) UIView *inputAccessoryView ``` |
| To | ``` @property(readwrite, strong, nullable) UIView *inputAccessoryView ``` |

Modified [UITextField.inputView](https://developer.apple.com/documentation/uikit/uitextfield/1619620-inputview)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, retain) UIView *inputView ``` |
| To | ``` @property(readwrite, strong, nullable) UIView *inputView ``` |

Modified [UITextField.leftView](https://developer.apple.com/documentation/uikit/uitextfield/1619597-leftview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *leftView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *leftView ``` |

Modified [UITextField.rightView](https://developer.apple.com/documentation/uikit/uitextfield/1619596-rightview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *rightView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *rightView ``` |

Modified [UITextField.textColor](https://developer.apple.com/documentation/uikit/uitextfield/1619617-textcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *textColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *textColor ``` |

Modified [UITextField.typingAttributes](https://developer.apple.com/documentation/uikit/uitextfield/1619632-typingattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDictionary *typingAttributes ``` |
| To | ``` @property(nonatomic, copy, nullable) NSDictionary<NSString *,id> *typingAttributes ``` |

#### UITextInput.h

Added [-[UITextInput beginFloatingCursorAtPoint:]](https://developer.apple.com/documentation/uikit/uitextinput/1614557-beginfloatingcursoratpoint)Added [-[UITextInput endFloatingCursor]](https://developer.apple.com/documentation/uikit/uitextinput/1614497-endfloatingcursor)Added [-[UITextInput updateFloatingCursorAtPoint:]](https://developer.apple.com/documentation/uikit/uitextinput/1614550-updatefloatingcursor)Added [UITextInputAssistantItem](https://developer.apple.com/documentation/uikit/uitextinputassistantitem)Added [UITextInputAssistantItem.allowsHidingShortcuts](https://developer.apple.com/documentation/uikit/uitextinputassistantitem/1614529-allowshidingshortcuts)Added [UITextInputAssistantItem.leadingBarButtonGroups](https://developer.apple.com/documentation/uikit/uitextinputassistantitem/1614575-leadingbarbuttongroups)Added [UITextInputAssistantItem.trailingBarButtonGroups](https://developer.apple.com/documentation/uikit/uitextinputassistantitem/1614532-trailingbarbuttongroups)Modified [UIDictationPhrase.alternativeInterpretations](https://developer.apple.com/documentation/uikit/uidictationphrase/1614510-alternativeinterpretations)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *alternativeInterpretations ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<NSString *> *alternativeInterpretations ``` |

Modified [UITextInput.inputDelegate](https://developer.apple.com/documentation/uikit/uitextinput/1614508-inputdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UITextInputDelegate> inputDelegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UITextInputDelegate> inputDelegate ``` |

Modified [-[UITextInput insertDictationResult:]](https://developer.apple.com/documentation/uikit/uitextinput/1614568-insertdictationresult)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertDictationResult:(NSArray *)dictationResult ``` |
| To | ``` - (void)insertDictationResult:(NSArray<UIDictationPhrase *> * _Nonnull)dictationResult ``` |

Modified [UITextInput.textInputView](https://developer.apple.com/documentation/uikit/uitextinput/1614564-textinputview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) UIView *textInputView ``` |
| To | ``` @property(nonatomic, readonly, nonnull) __kindof UIView *textInputView ``` |

Modified [-[UITextInput textStylingAtPosition:inDirection:]](https://developer.apple.com/documentation/uikit/uitextinput/1614566-textstyling)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)textStylingAtPosition:(UITextPosition *)position inDirection:(UITextStorageDirection)direction ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nullable)textStylingAtPosition:(UITextPosition * _Nonnull)position inDirection:(UITextStorageDirection)direction ``` |

Modified [+[UITextInputMode activeInputModes]](https://developer.apple.com/documentation/uikit/uitextinputmode/1614522-activeinputmodes)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)activeInputModes ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)activeInputModes ``` |

Modified [UITextInputMode.primaryLanguage](https://developer.apple.com/documentation/uikit/uitextinputmode/1614535-primarylanguage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSString *primaryLanguage ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) NSString *primaryLanguage ``` |

#### UITextInputTraits.h

Added [UIReturnKeyContinue](https://developer.apple.com/documentation/uikit/uireturnkeytype/uireturnkeycontinue)

#### UITextView.h

Added [-[UITextView initWithCoder:]](https://developer.apple.com/documentation/uikit/uitextview/1618617-initwithcoder)Modified [UITextView.attributedText](https://developer.apple.com/documentation/uikit/uitextview/1618626-attributedtext)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSAttributedString *attributedText ``` |
| To | ``` @property(copy) NSAttributedString * _Null_unspecified attributedText ``` |

Modified [UITextView.delegate](https://developer.apple.com/documentation/uikit/uitextview/1618631-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UITextViewDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UITextViewDelegate> delegate ``` |

Modified [UITextView.font](https://developer.apple.com/documentation/uikit/uitextview/1618600-font)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIFont *font ``` |
| To | ``` @property(nonatomic, strong, nullable) UIFont *font ``` |

Modified [-[UITextView initWithFrame:textContainer:]](https://developer.apple.com/documentation/uikit/uitextview/1618597-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITextView.inputAccessoryView](https://developer.apple.com/documentation/uikit/uitextview/1618596-inputaccessoryview)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, retain) UIView *inputAccessoryView ``` |
| To | ``` @property(readwrite, strong, nullable) UIView *inputAccessoryView ``` |

Modified [UITextView.inputView](https://developer.apple.com/documentation/uikit/uitextview/1618614-inputview)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, retain) UIView *inputView ``` |
| To | ``` @property(readwrite, strong, nullable) UIView *inputView ``` |

Modified [UITextView.linkTextAttributes](https://developer.apple.com/documentation/uikit/uitextview/1618632-linktextattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDictionary *linkTextAttributes ``` |
| To | ``` @property(nonatomic, copy) NSDictionary<NSString *,id> * _Null_unspecified linkTextAttributes ``` |

Modified [UITextView.textColor](https://developer.apple.com/documentation/uikit/uitextview/1618601-textcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *textColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *textColor ``` |

Modified [UITextView.textStorage](https://developer.apple.com/documentation/uikit/uitextview/1618611-textstorage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSTextStorage *textStorage ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSTextStorage *textStorage ``` |

Modified [UITextView.typingAttributes](https://developer.apple.com/documentation/uikit/uitextview/1618629-typingattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDictionary *typingAttributes ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSDictionary<NSString *,id> *typingAttributes ``` |

#### UIToolbar.h

Modified [UIToolbar.barTintColor](https://developer.apple.com/documentation/uikit/uitoolbar/1618002-bartintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *barTintColor ``` |
| To | ``` @property(nonatomic, strong, nullable) UIColor *barTintColor ``` |

Modified [UIToolbar.items](https://developer.apple.com/documentation/uikit/uitoolbar/1617997-items)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *items ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<UIBarButtonItem *> *items ``` |

Modified [-[UIToolbar setItems:animated:]](https://developer.apple.com/documentation/uikit/uitoolbar/1617999-setitems)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setItems:(NSArray *)items animated:(BOOL)animated ``` |
| To | ``` - (void)setItems:(NSArray<UIBarButtonItem *> * _Nullable)items animated:(BOOL)animated ``` |

Modified [UIToolbar.tintColor](https://developer.apple.com/documentation/uikit/uitoolbar/1617995-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *tintColor ``` |
| To | ``` @property(nonatomic, strong) UIColor * _Null_unspecified tintColor ``` |

Modified [UIToolbar.translucent](https://developer.apple.com/documentation/uikit/uitoolbar/1618001-istranslucent)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

#### UITouch.h

Added [UITouch.force](https://developer.apple.com/documentation/uikit/uitouch/1618110-force)Added [UITouch.maximumPossibleForce](https://developer.apple.com/documentation/uikit/uitouch/1618121-maximumpossibleforce)Added [UIForceTouchCapability](https://developer.apple.com/documentation/uikit/uiforcetouchcapability)Added [UIForceTouchCapabilityAvailable](https://developer.apple.com/documentation/uikit/uiforcetouchcapability/available)Added [UIForceTouchCapabilityUnavailable](https://developer.apple.com/documentation/uikit/uiforcetouchcapability/unavailable)Added [UIForceTouchCapabilityUnknown](https://developer.apple.com/documentation/uikit/uiforcetouchcapability/unknown)Modified [UITouch.gestureRecognizers](https://developer.apple.com/documentation/uikit/uitouch/1618114-gesturerecognizers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *gestureRecognizers ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSArray<UIGestureRecognizer *> *gestureRecognizers ``` |

Modified [UITouch.view](https://developer.apple.com/documentation/uikit/uitouch/1618109-view)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIView *view ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIView *view ``` |

Modified [UITouch.window](https://developer.apple.com/documentation/uikit/uitouch/1618126-window)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIWindow *window ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIWindow *window ``` |

#### UITraitCollection.h

Added [UITraitCollection.forceTouchCapability](https://developer.apple.com/documentation/uikit/uitraitcollection/1623515-forcetouchcapability)Added [-[UITraitCollection init]](https://developer.apple.com/documentation/uikit/uitraitcollection/1623517-init)Added [-[UITraitCollection initWithCoder:]](https://developer.apple.com/documentation/uikit/uitraitcollection/1623504-initwithcoder)Added [+[UITraitCollection traitCollectionWithForceTouchCapability:]](https://developer.apple.com/documentation/uikit/uitraitcollection/1623511-init)Modified [+[UITraitCollection traitCollectionWithTraitsFromCollections:]](https://developer.apple.com/documentation/uikit/uitraitcollection/1623512-traitcollectionwithtraitsfromcol)

|  | Declaration |
| --- | --- |
| From | ``` + (UITraitCollection *)traitCollectionWithTraitsFromCollections:(NSArray *)traitCollections ``` |
| To | ``` + (UITraitCollection * _Nonnull)traitCollectionWithTraitsFromCollections:(NSArray<UITraitCollection *> * _Nonnull)traitCollections ``` |

#### UIUserNotificationSettings.h

Added [UIMutableUserNotificationAction.behavior](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/1615395-behavior)Added [UIMutableUserNotificationAction.parameters](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/1615354-parameters)Added [UIUserNotificationAction.behavior](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615399-behavior)Added [-[UIUserNotificationAction init]](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615368-init)Added [-[UIUserNotificationAction initWithCoder:]](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615366-init)Added [UIUserNotificationAction.parameters](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615337-parameters)Added [-[UIUserNotificationCategory init]](https://developer.apple.com/documentation/uikit/uiusernotificationcategory/1615327-init)Added [-[UIUserNotificationCategory initWithCoder:]](https://developer.apple.com/documentation/uikit/uiusernotificationcategory/1615391-init)Added [UIUserNotificationActionBehavior](https://developer.apple.com/documentation/uikit/uiusernotificationactionbehavior)Added [UIUserNotificationActionBehaviorDefault](https://developer.apple.com/documentation/uikit/uiusernotificationactionbehavior/default)Added [UIUserNotificationActionBehaviorTextInput](https://developer.apple.com/documentation/uikit/uiusernotificationactionbehavior/textinput)Added [UIUserNotificationActionResponseTypedTextKey](https://developer.apple.com/documentation/watchkit/uiusernotificationactionresponsetypedtextkey)Added [UIUserNotificationTextInputActionButtonTitleKey](https://developer.apple.com/documentation/uikit/uiusernotificationtextinputactionbuttontitlekey)Modified [-[UIMutableUserNotificationCategory setActions:forContext:]](https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory/1615397-setactions)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setActions:(NSArray *)actions forContext:(UIUserNotificationActionContext)context ``` |
| To | ``` - (void)setActions:(NSArray<UIUserNotificationAction *> * _Nullable)actions forContext:(UIUserNotificationActionContext)context ``` |

Modified [-[UIUserNotificationCategory actionsForContext:]](https://developer.apple.com/documentation/uikit/uiusernotificationcategory/1615374-actionsforcontext)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)actionsForContext:(UIUserNotificationActionContext)context ``` |
| To | ``` - (NSArray<UIUserNotificationAction *> * _Nullable)actionsForContext:(UIUserNotificationActionContext)context ``` |

Modified [UIUserNotificationSettings.categories](https://developer.apple.com/documentation/uikit/uiusernotificationsettings/1615365-categories)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy, readonly) NSSet *categories ``` |
| To | ``` @property(nonatomic, copy, readonly, nullable) NSSet<UIUserNotificationCategory *> *categories ``` |

Modified [+[UIUserNotificationSettings settingsForTypes:categories:]](https://developer.apple.com/documentation/uikit/uiusernotificationsettings/1615401-settingsfortypes)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)settingsForTypes:(UIUserNotificationType)types categories:(NSSet *)categories ``` |
| To | ``` + (instancetype _Nonnull)settingsForTypes:(UIUserNotificationType)types categories:(NSSet<UIUserNotificationCategory *> * _Nullable)categories ``` |

#### UIView.h

Removed [-[UIView setTranslatesAutoresizingMaskIntoConstraints:]](https://developer.apple.com/documentation/uikit/uiview/1622572-translatesautoresizingmaskintoco)Added [-[UIView addLayoutGuide:]](https://developer.apple.com/documentation/uikit/uiview/1622414-addlayoutguide)Added [UIView.bottomAnchor](https://developer.apple.com/documentation/uikit/uiview/1622483-bottomanchor)Added [UIView.centerXAnchor](https://developer.apple.com/documentation/uikit/uiview/1622596-centerxanchor)Added [UIView.centerYAnchor](https://developer.apple.com/documentation/uikit/uiview/1622447-centeryanchor)Added [UIView.firstBaselineAnchor](https://developer.apple.com/documentation/uikit/uiview/1622508-firstbaselineanchor)Added [UIView.heightAnchor](https://developer.apple.com/documentation/uikit/uiview/1622590-heightanchor)Added [+[UIView inheritedAnimationDuration]](https://developer.apple.com/documentation/uikit/uiview/1622479-inheritedanimationduration)Added [-[UIView initWithCoder:]](https://developer.apple.com/documentation/uikit/uiview/1622477-initwithcoder)Added [UIView.lastBaselineAnchor](https://developer.apple.com/documentation/uikit/uiview/1622471-lastbaselineanchor)Added [UIView.layoutGuides](https://developer.apple.com/documentation/uikit/uiview/1622536-layoutguides)Added [UIView.layoutMarginsGuide](https://developer.apple.com/documentation/uikit/uiview/1622651-layoutmarginsguide)Added [UIView.leadingAnchor](https://developer.apple.com/documentation/uikit/uiview/1622520-leadinganchor)Added [UIView.leftAnchor](https://developer.apple.com/documentation/uikit/uiview/1622435-leftanchor)Added [UIView.readableContentGuide](https://developer.apple.com/documentation/uikit/uiview/1622644-readablecontentguide)Added [-[UIView removeLayoutGuide:]](https://developer.apple.com/documentation/uikit/uiview/1622506-removelayoutguide)Added [UIView.rightAnchor](https://developer.apple.com/documentation/uikit/uiview/1622579-rightanchor)Added [UIView.semanticContentAttribute](https://developer.apple.com/documentation/uikit/uiview/1622461-semanticcontentattribute)Added [UIView.topAnchor](https://developer.apple.com/documentation/uikit/uiview/1622613-topanchor)Added [UIView.trailingAnchor](https://developer.apple.com/documentation/uikit/uiview/1622522-trailinganchor)Added [+[UIView userInterfaceLayoutDirectionForSemanticContentAttribute:]](https://developer.apple.com/documentation/uikit/uiview/1622480-userinterfacelayoutdirectionfors)Added [UIView.viewForFirstBaselineLayout](https://developer.apple.com/documentation/uikit/uiview/1622452-forfirstbaselinelayout)Added [UIView.viewForLastBaselineLayout](https://developer.apple.com/documentation/uikit/uiview/1622633-viewforlastbaselinelayout)Added [UIView.widthAnchor](https://developer.apple.com/documentation/uikit/uiview/1622605-widthanchor)Added [UISemanticContentAttribute](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute)Added [UISemanticContentAttributeForceLeftToRight](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute/forcelefttoright)Added [UISemanticContentAttributeForceRightToLeft](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute/forcerighttoleft)Added [UISemanticContentAttributePlayback](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute/uisemanticcontentattributeplayback)Added [UISemanticContentAttributeSpatial](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute/spatial)Added [UISemanticContentAttributeUnspecified](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute/uisemanticcontentattributeunspecified)Added UIView(UILayoutGuideSupport)Added UIView(UIViewLayoutConstraintCreation)Modified [-[UIView addConstraints:]](https://developer.apple.com/documentation/uikit/uiview/1622513-addconstraints)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addConstraints:(NSArray *)constraints ``` |
| To | ``` - (void)addConstraints:(NSArray<__kindof NSLayoutConstraint *> * _Nonnull)constraints ``` |

Modified [UIView.constraints](https://developer.apple.com/documentation/uikit/uiview/1622464-constraints)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)constraints ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<__kindof NSLayoutConstraint *> *constraints ``` |

Modified [-[UIView constraintsAffectingLayoutForAxis:]](https://developer.apple.com/documentation/uikit/uiview/1622432-constraintsaffectinglayoutforaxi)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)constraintsAffectingLayoutForAxis:(UILayoutConstraintAxis)axis ``` |
| To | ``` - (NSArray<__kindof NSLayoutConstraint *> * _Nonnull)constraintsAffectingLayoutForAxis:(UILayoutConstraintAxis)axis ``` |

Modified [UIView.gestureRecognizers](https://developer.apple.com/documentation/uikit/uiview/1622542-gesturerecognizers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *gestureRecognizers ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<__kindof UIGestureRecognizer *> *gestureRecognizers ``` |

Modified [-[UIView initWithFrame:]](https://developer.apple.com/documentation/uikit/uiview/1622488-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIView.layer](https://developer.apple.com/documentation/uikit/uiview/1622436-layer)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) CALayer *layer ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) CALayer *layer ``` |

Modified [UIView.maskView](https://developer.apple.com/documentation/uikit/uiview/1622557-maskview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *maskView ``` |
| To | ``` @property(nonatomic, strong, nullable) UIView *maskView ``` |

Modified [UIView.motionEffects](https://developer.apple.com/documentation/uikit/uiview/1622428-motioneffects)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, nonatomic) NSArray *motionEffects ``` |
| To | ``` @property(copy, nonatomic, nonnull) NSArray<__kindof UIMotionEffect *> *motionEffects ``` |

Modified [+[UIView performSystemAnimation:onViews:options:animations:completion:]](https://developer.apple.com/documentation/uikit/uiview/1622635-perform)

|  | Declaration |
| --- | --- |
| From | ``` + (void)performSystemAnimation:(UISystemAnimation)animation onViews:(NSArray *)views options:(UIViewAnimationOptions)options animations:(void (^)(void))parallelAnimations completion:(void (^)(BOOL finished))completion ``` |
| To | ``` + (void)performSystemAnimation:(UISystemAnimation)animation onViews:(NSArray<__kindof UIView *> * _Nonnull)views options:(UIViewAnimationOptions)options animations:(void (^ _Nullable)(void))parallelAnimations completion:(void (^ _Nullable)(BOOL finished))completion ``` |

Modified [-[UIView removeConstraints:]](https://developer.apple.com/documentation/uikit/uiview/1622593-removeconstraints)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeConstraints:(NSArray *)constraints ``` |
| To | ``` - (void)removeConstraints:(NSArray<__kindof NSLayoutConstraint *> * _Nonnull)constraints ``` |

Modified [UIView.subviews](https://developer.apple.com/documentation/uikit/uiview/1622614-subviews)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *subviews ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<__kindof UIView *> *subviews ``` |

Modified [UIView.tintColor](https://developer.apple.com/documentation/uikit/uiview/1622467-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIColor *tintColor ``` |
| To | ``` @property(nonatomic, strong) UIColor * _Null_unspecified tintColor ``` |

Modified [UIView.translatesAutoresizingMaskIntoConstraints](https://developer.apple.com/documentation/uikit/uiview/1622572-translatesautoresizingmaskintoco)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)translatesAutoresizingMaskIntoConstraints ``` |
| To | ``` @property(nonatomic) BOOL translatesAutoresizingMaskIntoConstraints ``` |

Modified [-[UIView viewForBaselineLayout]](https://developer.apple.com/documentation/uikit/uiview/1622439-forbaselinelayout)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIUserInterfaceLayoutDirection](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIView.h |

Modified [UIUserInterfaceLayoutDirectionLeftToRight](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection/lefttoright)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIView.h |

Modified [UIUserInterfaceLayoutDirectionRightToLeft](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection/righttoleft)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIView.h |

#### UIViewController.h

Added [UIPreviewAction](https://developer.apple.com/documentation/uikit/uipreviewaction)Added [+[UIPreviewAction actionWithTitle:style:handler:]](https://developer.apple.com/documentation/uikit/uipreviewaction/1621445-init)Added [UIPreviewAction.handler](https://developer.apple.com/documentation/uikit/uipreviewaction/1621447-handler)Added [UIPreviewActionGroup](https://developer.apple.com/documentation/uikit/uipreviewactiongroup)Added [+[UIPreviewActionGroup actionGroupWithTitle:style:actions:]](https://developer.apple.com/documentation/uikit/uipreviewactiongroup/1621514-init)Added [UIPreviewActionItem](https://developer.apple.com/documentation/uikit/uipreviewactionitem)Added [UIPreviewActionItem.title](https://developer.apple.com/documentation/uikit/uipreviewactionitem/1621352-title)Added [-[UIViewController addKeyCommand:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621439-addkeycommand)Added [-[UIViewController allowedChildViewControllersForUnwindingFromSource:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621371-allowedchildviewcontrollersforun)Added [-[UIViewController childViewControllerContainingSegueSource:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621384-childviewcontrollercontainingseg)Added [-[UIViewController initWithCoder:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621403-init)Added [-[UIViewController loadViewIfNeeded]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621446-loadviewifneeded)Added [-[UIViewController previewActionItems]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621408-previewactionitems)Added [-[UIViewController registerForPreviewingWithDelegate:sourceView:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621463-registerforpreviewingwithdelegat)Added [-[UIViewController removeKeyCommand:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621410-removekeycommand)Added [-[UIViewController unregisterForPreviewingWithContext:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621395-unregisterforpreviewingwithconte)Added [-[UIViewController unwindForSegue:towardsViewController:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621473-unwind)Added [UIViewController.viewIfLoaded](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621360-viewifloaded)Added [UIViewControllerPreviewing](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing)Added [UIViewControllerPreviewing.delegate](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/1621422-delegate)Added [UIViewControllerPreviewing.previewingGestureRecognizerForFailureRelationship](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/1621467-previewinggesturerecognizerforfa)Added [UIViewControllerPreviewing.sourceRect](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/1621431-sourcerect)Added [UIViewControllerPreviewing.sourceView](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/1621436-sourceview)Added [UIViewControllerPreviewingDelegate](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate)Added [-[UIViewControllerPreviewingDelegate previewingContext:commitViewController:]](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate/1621366-previewingcontext)Added [-[UIViewControllerPreviewingDelegate previewingContext:viewControllerForLocation:]](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate/1621464-previewingcontext)Added [UIPreviewActionStyle](https://developer.apple.com/documentation/uikit/uipreviewaction/style)Added [UIPreviewActionStyleDefault](https://developer.apple.com/documentation/uikit/uipreviewactionstyle/uipreviewactionstyledefault)Added [UIPreviewActionStyleDestructive](https://developer.apple.com/documentation/uikit/uipreviewaction/style/destructive)Added [UIPreviewActionStyleSelected](https://developer.apple.com/documentation/uikit/uipreviewactionstyle/uipreviewactionstyleselected)Added UIViewController()Added UIViewController(UIKeyCommand)Added UIViewController(UIViewControllerPreviewingRegistration)Modified [UIViewController.bottomLayoutGuide](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621504-bottomlayoutguide)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) id<UILayoutSupport> bottomLayoutGuide ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) id<UILayoutSupport> bottomLayoutGuide ``` |

Modified [UIViewController.childViewControllers](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621452-children)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *childViewControllers ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<__kindof UIViewController *> *childViewControllers ``` |

Modified [UIViewController.extensionContext](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621411-extensioncontext)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSExtensionContext *extensionContext ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) NSExtensionContext *extensionContext ``` |

Modified [-[UIViewController initWithNibName:bundle:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621359-initwithnibname)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIViewController.nibBundle](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621489-nibbundle)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSBundle *nibBundle ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) NSBundle *nibBundle ``` |

Modified [UIViewController.parentViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621362-parent)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) UIViewController *parentViewController ``` |
| To | ``` @property(nonatomic, weak, readonly, nullable) UIViewController *parentViewController ``` |

Modified [UIViewController.searchDisplayController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621420-searchdisplaycontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UISearchDisplayController *searchDisplayController ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UISearchDisplayController *searchDisplayController ``` |

Modified [-[UIViewController segueForUnwindingToViewController:fromViewController:identifier:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621500-segueforunwinding)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIViewController.storyboard](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621399-storyboard)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIStoryboard *storyboard ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) UIStoryboard *storyboard ``` |

Modified [-[UIViewController supportedInterfaceOrientations]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621435-supportedinterfaceorientations)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)supportedInterfaceOrientations ``` |
| To | ``` - (UIInterfaceOrientationMask)supportedInterfaceOrientations ``` |

Modified [UIViewController.topLayoutGuide](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621367-toplayoutguide)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) id<UILayoutSupport> topLayoutGuide ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) id<UILayoutSupport> topLayoutGuide ``` |

Modified [UIViewController.transitioningDelegate](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621421-transitioningdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UIViewControllerTransitioningDelegate> transitioningDelegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<UIViewControllerTransitioningDelegate> transitioningDelegate ``` |

Modified [UIViewController.view](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621460-view)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIView *view ``` |
| To | ``` @property(nonatomic, strong) UIView * _Null_unspecified view ``` |

Modified [-[UIViewController viewControllerForUnwindSegueAction:fromViewController:withSender:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621448-forunwindsegueaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### UIViewControllerTransitionCoordinator.h

Modified [-[UIViewControllerTransitionCoordinatorContext viewControllerForKey:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619293-viewcontrollerforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (UIViewController *)viewControllerForKey:(NSString *)key ``` |
| To | ``` - (__kindof UIViewController * _Nullable)viewControllerForKey:(NSString * _Nonnull)key ``` |

Modified [-[UIViewControllerTransitionCoordinatorContext viewForKey:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619302-viewforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (UIView *)viewForKey:(NSString *)key ``` |
| To | ``` - (__kindof UIView * _Nullable)viewForKey:(NSString * _Nonnull)key ``` |

#### UIViewControllerTransitioning.h

Modified [-[UIViewControllerContextTransitioning viewControllerForKey:]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622043-viewcontrollerforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (UIViewController *)viewControllerForKey:(NSString *)key ``` |
| To | ``` - (__kindof UIViewController * _Nullable)viewControllerForKey:(NSString * _Nonnull)key ``` |

Modified [-[UIViewControllerContextTransitioning viewForKey:]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622055-view)

|  | Declaration |
| --- | --- |
| From | ``` - (UIView *)viewForKey:(NSString *)key ``` |
| To | ``` - (__kindof UIView * _Nullable)viewForKey:(NSString * _Nonnull)key ``` |

#### UIVisualEffectView.h

Added [-[UIVisualEffectView initWithCoder:]](https://developer.apple.com/documentation/uikit/uivisualeffectview/1615054-initwithcoder)Modified [UIVisualEffectView.contentView](https://developer.apple.com/documentation/uikit/uivisualeffectview/1615068-contentview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain, readonly) UIView *contentView ``` |
| To | ``` @property(nonatomic, strong, readonly, nonnull) UIView *contentView ``` |

Modified [UIVisualEffectView.effect](https://developer.apple.com/documentation/uikit/uivisualeffectview/1615072-effect)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy, readonly) UIVisualEffect *effect ``` |
| To | ``` @property(nonatomic, copy, nullable) UIVisualEffect *effect ``` |

#### UIWebView.h

Added [UIWebView.allowsLinkPreview](https://developer.apple.com/documentation/uikit/uiwebview/1617976-allowslinkpreview)Added [UIWebView.allowsPictureInPictureMediaPlayback](https://developer.apple.com/documentation/uikit/uiwebview/1617944-allowspictureinpicturemediaplayb)Modified [UIWebView.request](https://developer.apple.com/documentation/uikit/uiwebview/1617972-request)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSURLRequest *request ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) NSURLRequest *request ``` |

Modified [UIWebView.scrollView](https://developer.apple.com/documentation/uikit/uiwebview/1617955-scrollview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) UIScrollView *scrollView ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) UIScrollView *scrollView ``` |

#### UIWindow.h

Added [UIKeyboardIsLocalUserInfoKey](https://developer.apple.com/documentation/uikit/uiresponder/1621603-keyboardislocaluserinfokey)Modified [UIWindow.rootViewController](https://developer.apple.com/documentation/uikit/uiwindow/1621581-rootviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIViewController *rootViewController ``` |
| To | ``` @property(nonatomic, strong, nullable) UIViewController *rootViewController ``` |

Modified [UIWindow.screen](https://developer.apple.com/documentation/uikit/uiwindow/1621597-screen)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) UIScreen *screen ``` |
| To | ``` @property(nonatomic, strong, nonnull) UIScreen *screen ``` |

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
