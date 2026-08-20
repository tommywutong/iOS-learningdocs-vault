---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOActionCellAssociation.html
archived_at: '2026-07-15T08:11:45.312144Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOActionCellAssociation

> **__Inherits
> from:__**
> : [EOGenericControlAssociation](EOGenericControlAssociation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5dwk3tfojuwgq3pnz2he33mifzxg33dnfqxi2lpny) : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOControlAssociation.h

---

## Class Description

---

EOActionCellAssociation is the default association class for
use with NSActionCells (Application Kit).

An EOActionCellAssociation object displays the value of the
selected object in its NSActionCell, and updates the object when
the NSActionCell's value changes. A sibling class, EOControlAssociation,
can be used with independent controls such as NSButtons and NSTextFields.
Other associations, such as EOPopUpAssociation and EOColumnAssociation,
supersede these classes for more specialized behavior.

When multiple EOActionCellAssociations are bound to cells
in the same control (such as in an Application Kit NSMatrix), one
of them becomes the delegate of the control and forwards appropriate messages,
such as __control:isValidObject:__,
to the others. This eliminates the need to add an EOControlAssociation
just to handle delegate messages.

EOActionCellAssociations access values using NSActionCell's __setObjectValue:__ method,
which allows values with non-string representations to be displayed.
An EOActionCellAssociation can be bound to an NSImageCell, for example,
with an attribute whose class is NSImage.

|  |
| --- |
| __Usable With__ |
| Any NSActionCell |

|  |
| --- |
| __Aspects__ |
| value | An attribute of the selected object, displayed in the NSActionCell. |
| enabled | A boolean attribute of the selected object, which determines whether the NSActionCell is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| target | On receiving an action message from the NSActionCell, an EOActionCellAssociation sends the NSActionCell's value to the EODisplayGroup. |
| delegate | See the class description. |

## Examples

To display a movie's budget in an NSTextFieldCell, in Interface
Builder, control-drag a connection from the text field to the Movie
display group. Select EOActionCellAssociation in the Connections
inspector, and bind the __value__ aspect to
the "budget" key. Then, if the NSTextFieldCell is editable,
when the user types a new value and presses Enter or Tab, the selected
movie's __budget__ attribute is changed.

Assuming that Movie objects implement an __isBudgetNegotiable__ method,
you can make the NSTextFieldCell uneditable depending on the selected
movie. To do so, bind the __enabled__ aspect
to the "isBudgetNegotiable" key.

## Instance Methods

---

### control

`- (NSControl *)control`

Returns the NSControl that owns the receiver's
display object.

__See Also:__  [- object](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5xwe2tfmn2a) (EOAssociation), __-
controlView__ (NSActionCell class
of the Application Kit)

---

### editingAssociation

`- (EOGenericControlAssociation *)editingAssociation`

For EOActionCellAssociations in an NSMatrix
(defined in the Application Kit) or other multi-celled control,
returns the selected EOActionCellAssociation (or the one that's
editing text).

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
