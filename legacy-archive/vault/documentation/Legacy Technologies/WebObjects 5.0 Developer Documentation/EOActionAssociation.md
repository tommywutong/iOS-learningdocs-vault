---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface/Classes/EOActionAssociation.html
archived_at: '2026-07-15T08:13:54.881312Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

# EOActionAssociation

> **__Inherits from:__**
> : [EOActionWidgetAssociation](EOActionWidgetAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhucy3unfxw4v3jmrtwk5cbonzw6y3jmf2gs33o) : [EOWidgetAssociation](EOWidgetAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvo2lem5sxiqltonxwg2lboruw63q) : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl) : Object

> **__Implements:__**
> : NSDisposable: EOObserving (EOControl)

> **__Package:__**
> : com.webobjects.eointerface

---

## Class Description

---

An EOActionAssociation object allows you to set up an interface object, such as a button, to send a message to the objects selected in the association's display group when the interface object is acted on.

|  |
| --- |
| __Usable With__ |
| com.webobjects.eointerface.swing: Any object that implements the method __addActionListener__ (javax.swing.JButton and javax.swing.JMenuItem, for example). com.webobjects.eointerface.cocoa: NSControl, NSActionCell, and their subclasses. |

|  |
| --- |
| __Aspects__ |
| `action` | Bound to a key that names the method to invoke on the selected objects. If the `argument` aspect isn't bound, the method must take no arguments. If the `argument` aspect is bound, then the method must take exactly one argument. |
| `argument` | An object attribute or relationship of the selected object, passed as an argument to the action method. (Usually bound to a different EODisplayGroup than the one bound to `action`.) |
| `enabled` | A boolean attribute of the selected object, which determines whether the display object is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| `target` | On receiving an action message from the display object, an EOActionAssocation sends its action to the selected objects. |

## Examples

Suppose you have an application that manages member accounts, each of which has a restriction on the outstanding balance allowed. You want a user to be able to increase the restriction limit by selecting one or more members and then clicking a button. To do this, you define a __boostRestrictions__ method in the Member class that increases the limit by 20%. In Interface Builder, control-drag a connection from the button to the Member display group. Select EOActionAssociation in the Connections inspector, and bind the association's __action__ aspect to the "boostRestrictions" key.

In another scenario, one EODisplayGroup shows Members, while another shows video tapes available for rent. Here, you want a user to be able to select a member, select a video tape, and then click a Rent button that checks the selected tape out to the selected member. To do this, define a __rentVideoTape__ method in the Member class that takes a VideoTape as an argument and handles the accounting involved in a video rental. Then, in Interface Builder, control-drag a connection from the button to the Members display group. Select EOActionAssociation in the Connections inspector, and bind the association's __action__ aspect to Member's __rentVideoTape__ action. Similarly, control-drag a connection from the button to the VideoTape display group. Select EOActionAssociation in the Connections inspector, and bind the association's __argument__ aspect to the VideoTape display group. Now, when the user selects a Member, selects a VideoTape, and clicks the button, the selected Member is sent a __rentVideoTape__ message with the selected VideoTape.

## Interfaces Implemented

---

> : NSDisposable:
>
> : EOObserving:

## Method Types

---

> **All methods**
>
> : [EOActionAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzaxg43pmnuwc5djn5xc6rkpifrxi2lpnzaxg43pmnuwc5djn5xa): [displayGroupSelectionsAllowEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzaxg43pmnuwc5djn5xc6zdjonygyylzi5zg65lqknswyzldoruw63ttifwgy33xivxgcytmmvsa): [invokeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzaxg43pmnuwc5djn5xc62loozxwwzkbmn2gs33o): [primaryAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzaxg43pmnuwc5djn5xc64dsnfwwc4tzifzxazldoq)

## Constructors

---

### EOActionAssociation

`public EOActionAssociation(Object aDisplayObject)`

Creates a new EOActionAssociation to monitor and update the value in _aDisplayObject_, typically a button or menu item.

You normally set up associations in Interface Builder, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See Also:__ bindAspect (EOAssociation), establishConnection (EOAssociation)

---

## Instance Methods

---

### displayGroupSelectionsAllowEnabled

`protected boolean displayGroupSelectionsAllowEnabled()`

Description forthcoming.

---

### invokeAction

`public void invokeAction()`

Description forthcoming.

---

### primaryAspect

`public String primaryAspect()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
