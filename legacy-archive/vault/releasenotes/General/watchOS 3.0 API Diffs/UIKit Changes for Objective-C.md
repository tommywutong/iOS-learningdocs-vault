---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Objective-C/UIKit.html
archived_at: '2026-07-18T02:58:15.842474Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# UIKit Changes for Objective-C

### UIKit

#### NSParagraphStyle.h

Added [NSParagraphStyle.defaultParagraphStyle](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1532681-default)Modified [NSTextTab](https://developer.apple.com/documentation/uikit/nstexttab)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCoding, NSCopying, NSSecureCoding |

#### UIAccessibilityConstants.h

Added [UIAccessibilityTraitTabBar](https://developer.apple.com/documentation/uikit/uiaccessibilitytraittabbar)

#### UIAccessibilityCustomAction.h (Removed)

Removed [UIAccessibilityCustomAction](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction)Removed [-[UIAccessibilityCustomAction initWithName:target:selector:]](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/1620499-initwithname)Removed [UIAccessibilityCustomAction.name](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/1620502-name)Removed [UIAccessibilityCustomAction.selector](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/1620498-selector)Removed [UIAccessibilityCustomAction.target](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/1620501-target)

#### UIColor.h

Added [UIColor.blackColor](https://developer.apple.com/documentation/uikit/uicolor/1621929-black)Added [UIColor.blueColor](https://developer.apple.com/documentation/uikit/uicolor/1621947-bluecolor)Added [UIColor.brownColor](https://developer.apple.com/documentation/uikit/uicolor/1621950-browncolor)Added [UIColor.clearColor](https://developer.apple.com/documentation/uikit/uicolor/1621945-clearcolor)Added [+[UIColor colorWithDisplayP3Red:green:blue:alpha:]](https://developer.apple.com/documentation/uikit/uicolor/1648569-colorwithdisplayp3red)Added [UIColor.cyanColor](https://developer.apple.com/documentation/uikit/uicolor/1621942-cyancolor)Added [UIColor.darkGrayColor](https://developer.apple.com/documentation/uikit/uicolor/1621952-darkgray)Added [UIColor.grayColor](https://developer.apple.com/documentation/uikit/uicolor/1621941-gray)Added [UIColor.greenColor](https://developer.apple.com/documentation/uikit/uicolor/1621946-greencolor)Added [-[UIColor initWithDisplayP3Red:green:blue:alpha:]](https://developer.apple.com/documentation/uikit/uicolor/1648568-init)Added [UIColor.lightGrayColor](https://developer.apple.com/documentation/uikit/uicolor/1621932-lightgraycolor)Added [UIColor.magentaColor](https://developer.apple.com/documentation/uikit/uicolor/1621934-magentacolor)Added [UIColor.orangeColor](https://developer.apple.com/documentation/uikit/uicolor/1621956-orangecolor)Added [UIColor.purpleColor](https://developer.apple.com/documentation/uikit/uicolor/1621923-purplecolor)Added [UIColor.redColor](https://developer.apple.com/documentation/uikit/uicolor/1621924-redcolor)Added [UIColor.whiteColor](https://developer.apple.com/documentation/uikit/uicolor/1621920-whitecolor)Added [UIColor.yellowColor](https://developer.apple.com/documentation/uikit/uicolor/1621953-yellow)

#### UIFont.h

Added [UIFont.familyNames](https://developer.apple.com/documentation/uikit/uifont/1619040-familynames)Added [+[UIFont preferredFontForTextStyle:compatibleWithTraitCollection:]](https://developer.apple.com/documentation/uikit/uifont/1771762-preferredfontfortextstyle)Modified [UIFont.fontDescriptor](https://developer.apple.com/documentation/uikit/uifont/1619037-fontdescriptor)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIFontDescriptor *)fontDescriptor ``` | -- |
| To | ``` @property(nonatomic, readonly) UIFontDescriptor *fontDescriptor ``` | yes |

Modified [+[UIFont preferredFontForTextStyle:]](https://developer.apple.com/documentation/uikit/uifont/1619030-preferredfont)

|  | Declaration |
| --- | --- |
| From | ``` + (UIFont *)preferredFontForTextStyle:(NSString *)style ``` |
| To | ``` + (UIFont *)preferredFontForTextStyle:(UIFontTextStyle)style ``` |

#### UIFontDescriptor.h

Added [+[UIFontDescriptor preferredFontDescriptorWithTextStyle:compatibleWithTraitCollection:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1771750-preferredfontdescriptor)Added [UIFontTextStyle](https://developer.apple.com/documentation/uikit/uifont/textstyle)Modified [UIFontDescriptor.fontAttributes](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616698-fontattributes)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSDictionary<NSString *,id> *)fontAttributes ``` | -- |
| To | ``` @property(nonatomic, readonly) NSDictionary<NSString *,id> *fontAttributes ``` | yes |

Modified [+[UIFontDescriptor preferredFontDescriptorWithTextStyle:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616705-preferredfontdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` + (UIFontDescriptor *)preferredFontDescriptorWithTextStyle:(NSString *)style ``` |
| To | ``` + (UIFontDescriptor *)preferredFontDescriptorWithTextStyle:(UIFontTextStyle)style ``` |

#### UIGeometry.h

Modified [NSValue.CGAffineTransformValue](https://developer.apple.com/documentation/foundation/nsvalue/1624512-cgaffinetransformvalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGAffineTransform)CGAffineTransformValue ``` | -- |
| To | ``` @property(nonatomic, readonly) CGAffineTransform CGAffineTransformValue ``` | yes |

Modified [NSValue.CGPointValue](https://developer.apple.com/documentation/foundation/nsvalue/1624534-cgpointvalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGPoint)CGPointValue ``` | -- |
| To | ``` @property(nonatomic, readonly) CGPoint CGPointValue ``` | yes |

Modified [NSValue.CGRectValue](https://developer.apple.com/documentation/foundation/nsvalue/1624506-cgrectvalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGRect)CGRectValue ``` | -- |
| To | ``` @property(nonatomic, readonly) CGRect CGRectValue ``` | yes |

Modified [NSValue.CGSizeValue](https://developer.apple.com/documentation/foundation/nsvalue/1624489-cgsizevalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGSize)CGSizeValue ``` | -- |
| To | ``` @property(nonatomic, readonly) CGSize CGSizeValue ``` | yes |

Modified [NSValue.CGVectorValue](https://developer.apple.com/documentation/foundation/nsvalue/1624486-cgvectorvalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGVector)CGVectorValue ``` | -- |
| To | ``` @property(nonatomic, readonly) CGVector CGVectorValue ``` | yes |

Modified [NSValue.UIEdgeInsetsValue](https://developer.apple.com/documentation/foundation/nsvalue/1624517-uiedgeinsetsvalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIEdgeInsets)UIEdgeInsetsValue ``` | -- |
| To | ``` @property(nonatomic, readonly) UIEdgeInsets UIEdgeInsetsValue ``` | yes |

Modified [NSValue.UIOffsetValue](https://developer.apple.com/documentation/foundation/nsvalue/1624526-uioffsetvalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIOffset)UIOffsetValue ``` | -- |
| To | ``` @property(nonatomic, readonly) UIOffset UIOffsetValue ``` | yes |

#### UIImage.h

Added [-[UIImage imageWithHorizontallyFlippedOrientation]](https://developer.apple.com/documentation/uikit/uiimage/2113668-imagewithhorizontallyflippedorie)

#### UIKitDefines.h

Added #def UIKIT_CLASS_AVAILABLE_IOS_ONLYAdded #def UIKIT_CLASS_AVAILABLE_WATCHOS_ONLYAdded [#def UIKIT_DEFINE_AS_PROPERTIES](https://developer.apple.com/documentation/uikit/uikit_define_as_properties)Added [#def UIKIT_REMOVE_ZERO_FROM_SWIFT](https://developer.apple.com/documentation/uikit/uikit_remove_zero_from_swift)Added [#def UIKIT_STRING_ENUMS](https://developer.apple.com/documentation/uikit/uikit_string_enums)

#### UILocalNotification.h

Modified [UILocalNotification](https://developer.apple.com/documentation/uikit/uilocalnotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

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

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.hasAction](https://developer.apple.com/documentation/uikit/uilocalnotification/1616649-hasaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [-[UILocalNotification init]](https://developer.apple.com/documentation/uikit/uilocalnotification/1616645-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [-[UILocalNotification initWithCoder:]](https://developer.apple.com/documentation/uikit/uilocalnotification/1616653-init)

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

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.repeatInterval](https://developer.apple.com/documentation/uikit/uilocalnotification/1616643-repeatinterval)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.soundName](https://developer.apple.com/documentation/uikit/uilocalnotification/1616651-soundname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.timeZone](https://developer.apple.com/documentation/uikit/uilocalnotification/1616659-timezone)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [UILocalNotification.userInfo](https://developer.apple.com/documentation/uikit/uilocalnotification/1616657-userinfo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

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
