---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOControlAssociation.html
archived_at: '2026-07-15T08:11:45.409854Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOControlAssociation

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

EOControlAssociation is the default EOAssociation subclass
for use with NSControl objects (Application Kit).

A control association displays the value of the selected object
in its control, and updates the object when the control's value
changes. A sibling class, EOActionCellAssociation, can be used with
individual cells in an NSMatrix or NSForm (both defined in the Application
Kit). Some other subclasses of EOAssociation, such as EOPopUpAssociation
and EOColumnAssociation, supersede these classes for more specialized
behavior.

EOControlAssociations access values using NSControl's __setObjectValue:__ method,
which allows values with non-string representations to be displayed.
An EOControlAssociation can be bound to an NSImageView, for example,
with an attribute whose class is NSImage (both NSImageView and NSImage
are defined in the Application Kit).

|  |
| --- |
| __Usable With__ |
| Any NSControl (Application Kit) |

|  |
| --- |
| __Aspects__ |
| value | An attribute of the selected object, displayed in the NSControl. |
| enabled | A boolean attribute of the selected object, which determines whether the NSControl is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| target | On receiving an action message from the NSControl, an EOControlAssociation sends the NSControl's value to the EODisplayGroup. |
| delegate | An EOControlAssociation accepts messages related to editing and validation of text, such as __control:textShouldBeginEditing:__ and __control:didFailToFormatString:errorDescription:__. |

## Examples

To display a movie's budget in an NSTextField, in Interface
Builder, control-drag a connection from the text field and a Movie
display group. In the Connections inspector, choose EOControlAssociation,
and bind the __value__ aspect to the "budget"
key. Then, if the NSTextField is editable, when the user types a new
value and presses Enter or Tab, the selected movie's __budget__ attribute
is changed.

Assuming that Movie objects implement an __isBudgetNegotiable__ method,
you can make the NSTextField uneditable depending on the selected
movie. To do so, bind the __enabled__ aspect
to the "isBudgetNegotiable" key.

## Instance Methods

---

### control

`- (NSControl *)control`

Returns the receiver's control object. For
EOControlAssociation, this method is equivalent to EOAssociation's [object](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5xwe2tfmn2a) method.

---

### editingAssociation

`- (EOGenericControlAssociation *)editingAssociation`

Returns `self`.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
