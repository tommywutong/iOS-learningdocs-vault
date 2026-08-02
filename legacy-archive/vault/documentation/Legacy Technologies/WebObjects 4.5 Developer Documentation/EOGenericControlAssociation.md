---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOGenericControlAssoc.html
archived_at: '2026-07-15T08:11:44.812446Z'
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
> : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl)
> : NSObject

> **__Implements:__**
> : EOObserving (EODelayedObserver)

> **__Package:__**
> : com.apple.yellow.eointerface

---

## Class Description

---

EOGenericControlAssociation is the abstract superclass of
EOControlAssociation and EOActionCellAssociation. You never use
instances of this class directly; its [isUsableWithObject](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpnfzvk43bmjwgkv3jorue6ytkmvrxi) method always
returns false. See the subclass specifications for more information.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.client.eointerface package. |

|  |  |  |
| --- | --- | --- |
| __Usable With__ | __Aspects__ | __Object Keys Taken__ |
| Nothing | value | target |
|  | enabled | delegate |

## Instance Methods

---

### control

`public com.apple.yellow.application.NSControl control()`

Overridden by subclasses to return the receiver's
display object-an NSControl (Application Kit).

---

### editingAssociation

`public EOGenericControlAssociation editingAssociation()`

Overridden by subclasses to return the association
responsible for handling text delegation messages. For example,
if the display object is a NSMatrix or NSTableView (Application
Kit), this method returns the association for the cell being edited.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
