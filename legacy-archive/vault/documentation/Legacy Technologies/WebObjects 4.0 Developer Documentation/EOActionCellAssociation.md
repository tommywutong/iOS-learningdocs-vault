---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOActionCellAssociation.html
archived_at: '2026-07-18T01:28:42.292369Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOActionAssociation.md)
[!](EOActionInsertionAssociation.md)

---

# EOActionCellAssociation

__Inherits From:__
EOGenericControlAssociation :
EOAssociation :
EODelayedObserver (EOControl) :
NSObject

EOObserving (EODelayedObserver)

__Inherits From:__
com.apple.yellow.eointerface (Yellow Box)

---

## Class Description

EOActionCellAssociation is the default association class for use with NSActionCells (Application Kit). It is for use in Yellow Box applications only; there isn't an equivalent class for Java Client.

An EOActionCellAssociation object displays the value of the selected object in its NSActionCell, and updates the object when the NSActionCell's value changes. A sibling class, EOControlAssociation, can be used with independent controls such as NSButtons and NSTextFields. Other associations, such as EOPopUpAssociation and EOColumnAssociation, supersede these classes for more specialized behavior.

When multiple EOActionCellAssociations are bound to cells in the same control (such as in an Application Kit NSMatrix), one of them becomes the delegate of the control and forwards appropriate messages, such as

---

controlIsValidObject
, to the others. This eliminates the need to add an EOControlAssociation just to handle delegate messages.

EOActionCellAssociations access values using NSActionCell's `setObjectValue` method, which allows values with non-string representations to be displayed. An EOActionCellAssociation can be bound to an NSImageCell, for example, with an attribute whose class is NSImage.

| __Usable With__ |
| Any NSActionCell |

```
```

| __Aspects__ | __Aspects__ |
| value | An attribute of the selected object, displayed in the NSActionCell. |
| enabled | A boolean attribute of the selected object, which determines whether the NSActionCell is enabled. |

```
```

| __Object Keys Taken__ | __Object Keys Taken__ |
| target | On receiving an action message from the NSActionCell, an EOActionCellAssociation sends the NSActionCell's value to the EODisplayGroup. |
| delegate | See the class description. |

```
```


---

## Examples

To display a movie's budget in an NSTextFieldCell, in Interface Builder, control-drag a connection from the text field to the Movie display group. Select EOActionCellAssociation in the Connections inspector, and bind the `value` aspect to the "budget" key. Then, if the NSTextFieldCell is editable, when the user types a new value and presses Enter or Tab, the selected movie's `budget` attribute is changed.

Assuming that Movie objects implement an `isBudgetNegotiable` method, you can make the NSTextFieldCell uneditable depending on the selected movie. To do so, bind the `enabled` aspect to the "isBudgetNegotiable" key.

---

## Constructors

public `EOActionCellAssociation`(java.lang.Object _aDisplayObject_)

Creates a new EOActionCellAssociation to monitor and update the value in _aDisplayObject_, which is typically an Application Kit NSActionCell.

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See also:__
[`bindAspect`](EOAssociation.md#apple-gu2tq) (EOAssociation), [`establishConnection`](EOAssociation.md#apple-gu4dq) (EOAssociation)

---

## Instance Methods

---

### control

public com.apple.yellow.application.NSControl `control`()

Returns the NSControl that owns the receiver's display object.

__See also:__
[`object`](EOAssociation.md#apple-gu4tq) (EOAssociation),

---

controlView
(NSActionCell class of the Application Kit)

---

### editingAssociation

public EOGenericControlAssociation `editingAssociation`()

For EOActionCellAssociations in an NSMatrix (defined in the Application Kit) or other multi-celled control, returns the selected EOActionCellAssociation (or the one that's editing text).

---

[!](EOActionAssociation.md)
[!](EOActionInsertionAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
