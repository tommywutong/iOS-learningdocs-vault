---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EORadioMatrixAssociation.html
archived_at: '2026-07-15T08:11:45.593393Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EORadioMatrixAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EORadioMatrixAssociation.h

---

## Class Description

---

EORadioMatrixAssociation displays a string or an integer in
an NSMatrix. EORadioMatrixAssociation includes three aspects: `selectedTitle`,
which is useful for values representable as strings; `selectedTag`, for
integer values; and `enabled` for
enabling and disabling the NSMatrix.

|  |
| --- |
| __Usable With__ |
| NSMatrix |

|  |
| --- |
| __Aspects__ |
| selectedTitle | An attribute of the selected object whose values can be represented as strings. |
| selectedTag | An integer attribute of the selected object. |
| enabled | A boolean attribute of the selected object, which determines whether the matrix is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| target | When the user chooses an item in the matrix, the EORadioMatrixAssociation updates the selected object's property with the item's title or tag. |

## Instance Methods

---

### setTagValueForOther:

`- (void)setTagValueForOther:(int)tag`

Records _tag_ as
the "unknown" tag. When a property value doesn't match any
other tag in the matrix, the EORadioMatrixAssociation automatically
selects the item for this tag. If there's no item for this tag, the
radio button selection isn't changed. This tag value is by default
-1.

---

### tagValueForOther

`- (int)tagValueForOther`

Returns the "unknown" tag.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
