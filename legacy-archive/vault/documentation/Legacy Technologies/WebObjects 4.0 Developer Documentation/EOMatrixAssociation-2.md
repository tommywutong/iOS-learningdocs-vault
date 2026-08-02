---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOMatrixAssociation.html
archived_at: '2026-07-18T01:28:46.458762Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOMasterPeerAssociation-2.md)
[!](EOPickTextAssociation-2.md)

---

# EOMatrixAssociation

__Inherits From:__
EOAssociation : EODelayedObserver (EOControl) : NSObject

__Conforms To:__
NSCoding (EOAssociation)
EOObserving (EODelayedObserver)
NSObject (NSObject)

__Declared in:__
EOInterface/EOMatrixAssociation.h

---

## Class Description

An EOMatrixAssociation allows you to populate an NSMatrix's cells (Application Kit). EOMatrixAssociation supports connections for both cell titles and icons, depending on the matrix's prototype cell. You define the prototype in Interface Builder (to display an icon only, text only, or both).

| __Usable With__ |
| NSMatrix (Application Kit) |

```
```

| __Aspects__ | __Aspects__ |
| enabled | A boolean attribute of the objects, which determines whether the matrix is enabled. |
| image | An NSImage attribute of the objects to display in the cell. |
| title | An attribute of the objects to display in the cell. |

```
```

| __Object Keys Taken__ | __Object Keys Taken__ |
| target | On receiving an action message from the matrix, an EOMatrixAssociation updates its display group's selection. |

```
```


---

## Examples

Suppose that you want to display actors' names and pictures in an NSMatrix. Start with a TalentPhoto display group (where a TalentPhoto object has a relationship to its Talent object). In interface builder, create a button containing both an image and text. Then, alternate-drag to create a matrix of buttons. Control-drag from the matrix to the photo display group. In the Connections inspector, choose EOMatrixAssociation, and bind the `image` aspect to the `photo` attribute. Repeat, binding the `title` aspect to the `talent.lastName` attribute.

Note that you can group the matrix in a scroll view. An EOMatrixAssociation will automatically manage the size of the matrix for this (for vertical scrolling only).

****

---

[!](EOMasterPeerAssociation-2.md)
[!](EOPickTextAssociation-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
