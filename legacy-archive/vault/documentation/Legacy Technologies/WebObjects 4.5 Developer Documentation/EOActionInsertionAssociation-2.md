---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOActionInsertionAssoc.html
archived_at: '2026-07-15T08:11:45.336879Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOActionInsertionAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOActionInsertionAssociation.h

---

## Class Description

---

An EOActionInsertionAssociation object inserts objects from
one display group into another.

|  |
| --- |
| __Usable With__ |
| Any object that responds to __setAction:__, typically an NSControl. |

|  |
| --- |
| __Aspects__ |
| source | Bound to the EODisplayGroup containing objects to insert. This aspect doesn't use a key. |
| destination | A relationship of the selected object into which objects from the source EODisplayGroup are inserted. Usually bound to a different EODisplayGroup than __source__. |
| enabled | A boolean attribute of the selected object (usually in the destination EODisplayGroup), which determines whether the NSControl is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| target | On receiving an action message from the display object, an EOActionInsertionAssociation inserts objects from the source EODisplayGroup into the destination EODisplayGroup. |

## Example

Suppose an application shows Talent in one display group and
Movies in another. You want a user to be able to select a talent,
select a movie, and then click an Assign Director button that assigns
the selected talent as one of the movie's directors. To do this,
in Interface Builder, control-drag a connection from the button
to the Talent display group. Select EOActionInsertionAssociation
in the Connections inspector, and double-click the association's __source__ aspect,
binding it to the Talent display group. Similarly, control-drag
a connection from the button to the Movie display group. Select EOActionAssociation
in the Connections inspector, and bind the association's __destination__ aspect
to the "directors" key. Now, when the user clicks the button,
the selected Talent is added to the __directors__ relationship
of the selected Movie. If more than one talent is selected, both
are added to the relationship. If more than one Movie is selected,
the selected talent are added to the relationship of the first Movie
in the selection.

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
