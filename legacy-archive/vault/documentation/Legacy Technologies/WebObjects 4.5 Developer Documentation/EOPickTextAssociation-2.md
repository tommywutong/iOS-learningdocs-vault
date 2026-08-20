---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOPickTextAssociation.html
archived_at: '2026-07-15T08:11:45.567158Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOPickTextAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOPickTextAssociation.h

---

## Class Description

---

An EOPickTextAssociation takes the value of its display object,
an NSControl (Application Kit), and uses it to form a qualifier
with up to three LIKE operators, each compared to a different key
of the EODisplayGroup. This allows the user to perform a similarity
search based on whole or partial values.

EOPickTextAssociations are most often used with a table view
to qualify a list of fetched objects that is too long for convenient
scrolling.

|  |
| --- |
| __Usable With__ |
| Any NSControl |

|  |
| --- |
| __Aspects__ |
| matchKey1 | An attribute to match using a LIKE qualifier. |
| matchKey2 | An attribute to match using a LIKE qualifier. |
| matchKey3 | An attribute to match using a LIKE qualifier. |

|  |
| --- |
| __Object Keys Taken__ |
| target | The EOPickTextAssociation applies its qualifier when sent an action message from the NSControl. |
| delegate | The EOPickTextAssociation applies its qualifier when sent a __controlTextDidChange:__ message, causing dynamic update as the user types. |

## Example

Make an EOPickTextAssociation between an NSTextField and an
EODisplayGroup of People objects. Bind the __matchKey1__ and __matchKey2__ aspects
to the "lastName" and "firstName" keys. If the user types "Bi"
in the field, the EOPickTextAssociation applies the following qualifier
to the EODisplayGroup:

> ```
> (lastName like "*Bi*") OR (firstName like "*Bi*")
> ```

which matches names like "Bill Smith" and "Joe Biggs".
The list of objects displayed in the display group is restricted
to those that match the qualifier.

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
