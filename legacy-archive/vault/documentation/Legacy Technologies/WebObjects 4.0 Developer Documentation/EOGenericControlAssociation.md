---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOGenericControlAssociatn.html
archived_at: '2026-07-18T01:28:43.225580Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EODisplayGroup.md)
[!](EOInterfaceController.md)

---

# EOGenericControlAssociation

__Inherits From:__
EOAssociation : EODelayedObserver (EOControl) : NSObject

EOObserving (EODelayedObserver)

__Inherits From:__
com.apple.yellow.eointerface (Yellow Box)

---

## Class Description

EOGenericControlAssociation is the abstract superclass of EOControlAssociation and EOActionCellAssociation. You never use instances of this class directly; its [`isUsableWithObject`](EOAssociation.md#apple-gu2dq) method always returns `false`. See the subclass specifications for more information.

| __Usable With__ | __Aspects__ | __Object Keys Taken__ |
| Nothing | value | target |
|  | enabled | delegate |

```
```

There is no Java Client equivalent of this class.

---

## Instance Methods

---

### control

public com.apple.yellow.application.NSControl `control`()

Overridden by subclasses to return the receiver's display object-an NSControl (Application Kit).

---

### editingAssociation

public EOGenericControlAssociation `editingAssociation`()

Overridden by subclasses to return the association responsible for handling text delegation messages. For example, if the display object is a NSMatrix or NSTableView (Application Kit), this method returns the association for the cell being edited.

---

[!](EODisplayGroup.md)
[!](EOInterfaceController.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
