---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOGenericControlAssociatn.html
archived_at: '2026-07-18T01:28:46.030825Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EODisplayGroupDelegate.md)
[!](EOInterfaceController-2.md)

---

# EOGenericControlAssociation

__Inherits From:__
EOAssociation : EODelayedObserver (EOControl) : NSObject

__Conforms To:__
NSCoding (EOAssociation)
EOObserving (EODelayedObserver)
NSObject (NSObject)

__Declared in:__
EOInterface/EOControlAssociation.h

---

## Class Description

EOGenericControlAssociation is the abstract superclass of EOControlAssociation and EOActionCellAssociation. You never use instances of this class directly; its [`isUsableWithObject:`](EOAssociation.md#apple-gu2dq) method always returns NO. See the subclass specifications for more information.

| __Usable With__ | __Aspects__ | __Object Keys Taken__ |
| Nothing | value | target |
|  | enabled | delegate |

```
```


---

## Instance Methods

---

### control

- (NSControl \*)__control__

Overridden by subclasses to return the receiver's display object-an NSControl (Application Kit).

---

### editingAssociation

- (EOGenericControlAssociation \*)__editingAssociation__

Overridden by subclasses to return the association responsible for handling text delegation messages. For example, if the display object is a NSMatrix or NSTableView (Application Kit), this method returns the association for the cell being edited.

---

[!](EODisplayGroupDelegate.md)
[!](EOInterfaceController-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
