---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOTextAssociation.html
archived_at: '2026-07-15T08:11:45.640061Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOTextAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOTextAssociation.h

---

## Class Description

---

An EOTextAssociation object displays a plain or rich text
attribute in an NSText object (Application Kit) by binding the text
object to a string or NSData attribute. It determines the kind of
text received from an object by examining the beginning for signature
codes specific to RTF and RTFD. When writing text back to the object,
the association examines the configuration of the NSText object
to determine the type to use according to the following table:

|  |  |  |
| --- | --- | --- |
| __Multiple Fonts__ | __Allows Graphics__ | __Type Written to Object__ |
| NO | NO | NSString text |
| YES | NO | NSData containing RTF |
| YES | YES | NSData containing RTFD |

The following tables describe the display objects an EOTextAssociation
can be used with, the aspects of an EOTextAssociation, and the object
keys it takes.

|  |
| --- |
| __Usable With__ |
| NSText, NSTextView, NSCStringText |

|  |
| --- |
| __Aspects__ |
| value | A text attribute of the selected object. |
| editable | A boolean attribute of the selected object, which determines whether the text object is editable. |

|  |
| --- |
| __Object Keys Taken__ |
| delegate | An EOTextAssociation accepts delegate messages related to the editing and validation of text; see the NSText, NSTextView, and NSCStringText class specifications for more information. |

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
