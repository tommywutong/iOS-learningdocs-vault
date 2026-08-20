---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOGenericControlAssoc.html
archived_at: '2026-07-15T08:11:45.492640Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOGenericControlAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOControlAssociation.h

---

## Class Description

---

EOGenericControlAssociation is the abstract superclass of
EOControlAssociation and EOActionCellAssociation. You never use
instances of this class directly; its [isUsableWithObject:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3jonkxgylcnrsvo2lunbhwe2tfmn2du) method
always returns NO. See the subclass specifications for more information.

|  |  |  |
| --- | --- | --- |
| __Usable With__ | __Aspects__ | __Object Keys Taken__ |
| Nothing | value | target |
|  | enabled | delegate |

## Instance Methods

---

### control

`- (NSControl *)control`

Overridden by subclasses to return the receiver's
display object-an NSControl (Application Kit).

---

### editingAssociation

`- (EOGenericControlAssociation *)editingAssociation`

Overridden by subclasses to return the association
responsible for handling text delegation messages. For example,
if the display object is a NSMatrix or NSTableView (Application
Kit), this method returns the association for the cell being edited.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
