---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOControlAssociation.html
archived_at: '2026-07-15T08:11:44.648040Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOControlAssociation

> **__Inherits
> from:__**
> : [EOGenericControlAssociation](EOGenericControlAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuozlomvzgsy2dn5xhi4tpnraxg43pmnuwc5djn5xa) : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) :
> EODelayedObserver (EOControl) :
> NSObject

> **__Implements:__**
> : EOObserving (EODelayedObserver)

> **__Package:__**
> : com.apple.yellow.eointerface

---

## Class Description

---

EOControlAssociation is the default EOAssociation subclass
for use with NSControl objects (Application Kit).

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.client.eointerface package. |

A control association displays the value of the selected object
in its control, and updates the object when the control's value
changes. A sibling class, EOActionCellAssociation, can be used with
individual cells in an NSMatrix or NSForm (both defined in the Application
Kit). Some other subclasses of EOAssociation, such as EOPopUpAssociation
and EOColumnAssociation, supersede these classes for more specialized
behavior.

EOControlAssociations access values using NSControl's `setObjectValue` method,
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
| delegate | An EOControlAssociation accepts messages related to editing and validation of text, such as `controlTextShouldBeginEditing` and `controlDidFailToFormatStringErrorDescription`. |

## Examples

To display a movie's budget in an NSTextField, in Interface
Builder, control-drag a connection from the text field and a Movie
display group. In the Connections inspector, choose EOControlAssociation,
and bind the `value` aspect to the "budget"
key. Then, if the NSTextField is editable, when the user types a new
value and presses Enter or Tab, the selected movie's `budget` attribute
is changed.

Assuming that Movie objects implement an `isBudgetNegotiable` method,
you can make the NSTextField uneditable depending on the selected
movie. To do so, bind the `enabled` aspect
to the "isBudgetNegotiable" key.

## Constructors

---

### EOControlAssociation

`public EOControlAssociation(Object  aDisplayObject)`

Creates a new EOControlAssociation to monitor
and update the row values in  _aDisplayObject,_
an NSControl object (Application Kit).

You normally set up
associations with the Interface Builder application, in which case
you don't need to create them programmatically. However, if you
do create them up programmatically, setting them up is a multi-step
process. After creating an association, you must bind its aspects
and establish its connections.

__See
Also:__  [bindAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe2lomraxg4dfmn2a) (EOAssociation), [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) (EOAssociation)

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
