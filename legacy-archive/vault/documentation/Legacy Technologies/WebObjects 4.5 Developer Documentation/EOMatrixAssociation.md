---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOMatrixAssociation.html
archived_at: '2026-07-15T08:11:45.553985Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOMatrixAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOMatrixAssociation.h

---

## Class Description

---

An EOMatrixAssociation allows you to populate an NSMatrix's
cells (Application Kit). EOMatrixAssociation supports connections
for both cell titles and icons, depending on the matrix's prototype
cell. You define the prototype in Interface Builder (to display
an icon only, text only, or both).

|  |
| --- |
| __Usable With__ |
| NSMatrix (Application Kit) |

|  |
| --- |
| __Aspects__ |
| enabled | A boolean attribute of the objects, which determines whether the matrix is enabled. |
| image | An NSImage attribute of the objects to display in the cell. |
| title | An attribute of the objects to display in the cell. |

|  |
| --- |
| __Object Keys Taken__ |
| target | On receiving an action message from the matrix, an EOMatrixAssociation updates its display group's selection. |

## Examples

Suppose that you want to display actors' names and pictures
in an NSMatrix. Start with a TalentPhoto display group (where a
TalentPhoto object has a relationship to its Talent object). In
interface builder, create a button containing both an image and
text. Then, alternate-drag to create a matrix of buttons. Control-drag
from the matrix to the photo display group. In the Connections inspector,
choose EOMatrixAssociation, and bind the __image__ aspect
to the __photo__ attribute. Repeat, binding
the __title__ aspect to the __talent.lastName__ attribute.

Note that you can group the matrix in a scroll view. An EOMatrixAssociation
will automatically manage the size of the matrix for this (for vertical
scrolling only).

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
