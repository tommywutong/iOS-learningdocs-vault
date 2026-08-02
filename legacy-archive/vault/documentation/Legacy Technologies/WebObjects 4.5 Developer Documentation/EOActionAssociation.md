---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOActionAssociation.html
archived_at: '2026-07-15T08:11:45.295993Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOActionAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOActionAssociation.h

---

## Class Description

---

An EOActionAssociation object allows you to set up an interface
object, such as a button, to send a message to the objects selected
in the association's display group when the interface object is
acted on.

|  |
| --- |
| __Usable With__ |
| Any control object (NSControl, NSActionCell, and their subclasses) |

|  |
| --- |
| __Aspects__ |
| action | Bound to a key that names the method to invoke on the selected objects. If the `argument` aspect isn't bound, the method must take no arguments. If the `argument` aspect is bound, then the method must take exactly one argument. |
| argument | An object attribute or relationship of the selected object, passed as an argument to the action method. (Usually bound to a different EODisplayGroup than the one bound to `action`.) |
| enabled | A boolean attribute of the selected object, which determines whether the display object is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| target | On receiving an action message from the display object, an EOActionAssocation sends its action to the selected objects. |

## Examples

Suppose you have an application that manages member accounts,
each of which has a restriction on the outstanding balance allowed.
You want a user to be able to increase the restriction limit by
selecting one or more members and then clicking a button. To do
this, you define a __boostRestrictions__ method in
the Member class that increases the limit by 20%. In Interface Builder,
control-drag a connection from the button to the Member display
group. Select EOActionAssociation in the Connections inspector,
and bind the association's __action__ aspect
to the "boostRestrictions" key.

In another scenario, one EODisplayGroup shows Members, while
another shows video tapes available for rent. Here, you want a user
to be able to select a member, select a video tape, and then click
a Rent button that checks the selected tape out to the selected
member. To do this, define a __rentVideoTape:__ method
in the Member class that takes a VideoTape as an argument and handles
the accounting involved in a video rental. Then, in Interface Builder,
control-drag a connection from the button to the Members display
group. Select EOActionAssociation in the Connections inspector,
and bind the association's __action__ aspect
to Member's __rentVideoTape:__ action. Similarly,
control-drag a connection from the button to the VideoTape display
group. Select EOActionAssociation in the Connections inspector,
and bind the association's __argument__ aspect
to the VideoTape display group. Now, when the user selects a Member,
selects a VideoTape, and clicks the button, the selected Member
is sent a __rentVideoTape:__ message with the
selected VideoTape.

## Instance Methods

---

### action:

`- (void)action:(id)sender`

Invoked when the receiver's display
object is acted upon. Sends the method identified by the receiver's `action` aspect
(with an argument, if the `argument` aspect
is bound) to the selected objects.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
