---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOActionAssociation.html
archived_at: '2026-07-18T01:28:42.214016Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](The%20EOInterface%20Framework.md)
[!](EOActionCellAssociation.md)

---

# EOActionAssociation

__Inherits From:__
EOAssociation : EODelayedObserver (EOControl) : Object (Java Client)
EOAssociation : EODelayedObserver (EOControl) : NSObject (Yellow Box)

EOObserving (EODelayedObserver)
java.awt.event.ActionListener (Java Client)

__Inherits From:__
com.apple.client.eointerface (Java Client)
com.apple.yellow.eointerface (Yellow Box)

---

## Class Description

An EOActionAssociation object allows you to set up an interface object, such as a button, to send a message to the objects selected in the association's display group when the interface object is acted on.

| __Usable With__ |
| Any control object (in the Yellow Box, any NSControl or NSActionCell) |

```
```

| __Aspects__ | __Aspects__ |
| action | Bound to a key that names the method to invoke on the selected objects. If the `argument` aspect isn't bound, the method must take no arguments. If the `argument` aspect is bound, then the method must take exactly one argument. |
| argument | An object attribute or relationship of the selected object, passed as an argument to the action method. (Usually bound to a different EODisplayGroup than the one bound to `action`.) |
| enabled | A boolean attribute of the selected object, which determines whether the display object is enabled. |

```
```

| __Object Keys Taken__ | __Object Keys Taken__ |
| target | On receiving an action message from the display object, an EOActionAssocation sends its action to the selected objects. |

```
```


---

## Examples

Suppose you have an application that manages member accounts, each of which has a restriction on the outstanding balance allowed. You want a user to be able to increase the restriction limit by selecting one or more members and then clicking a button. To do this, you define a `boostRestrictions` method in the Member class that increases the limit by 20%. In Interface Builder, control-drag a connection from the button to the Member display group. Select EOActionAssociation in the Connections inspector, and bind the association's `action` aspect to the "boostRestrictions" key.

In another scenario, one EODisplayGroup shows Members, while another shows video tapes available for rent. Here, you want a user to be able to select a member, select a video tape, and then click a Rent button that checks the selected tape out to the selected member. To do this, define a `rentVideoTape` method in the Member class that takes a VideoTape as an argument and handles the accounting involved in a video rental. Then, in Interface Builder, control-drag a connection from the button to the Members display group. Select EOActionAssociation in the Connections inspector, and bind the association's `action` aspect to Member's `rentVideoTape` action. Similarly, control-drag a connection from the button to the VideoTape display group. Select EOActionAssociation in the Connections inspector, and bind the association's `argument` aspect to the VideoTape display group. Now, when the user selects a Member, selects a VideoTape, and clicks the button, the selected Member is sent a `rentVideoTape` message with the selected VideoTape.

---

## Constructors

public `EOActionAssociation`(java.lang.Object _aDisplayObject_)

Creates a new EOActionAssociation to monitor and update the value in _aDisplayObject_, which, in the Yellow Box, is typically anNSControl or NSActionCell-most frequently a button.

In Yellow Box applications, you normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See also:__
[`bindAspect`](EOAssociation.md#apple-gu2tq) (EOAssociation), [`establishConnection`](EOAssociation.md#apple-gu4dq) (EOAssociation)

---

## Instance Methods

---

### action

public void `action`()

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Invoked when the receiver's display object is acted upon. Sends the method identified by the receiver's `action` aspect (with an argument, if the `argument` aspect is bound) to the selected objects.

---

### actionPerformed

public void `actionPerformed`(java.awt.event.ActionEvent _anActionEvent_)

This method is available for Java Client applications only; there is no Yellow Box equivalent.

Invoked when the receiver's display object is acted upon. Sends the method identified by the receiver's `action` aspect (with an argument, if the `argument` aspect is bound) to the selected objects.

---

[!](The%20EOInterface%20Framework.md)
[!](EOActionCellAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
