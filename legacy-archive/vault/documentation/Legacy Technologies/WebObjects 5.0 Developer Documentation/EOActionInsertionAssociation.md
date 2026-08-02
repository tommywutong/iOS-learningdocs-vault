---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface/Classes/EOActionInsertionAssociat.html
archived_at: '2026-07-15T08:13:55.130965Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

# EOActionInsertionAssociation

> **__Inherits from:__**
> : [EOActionWidgetAssociation](EOActionWidgetAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhucy3unfxw4v3jmrtwk5cbonzw6y3jmf2gs33o) : [EOWidgetAssociation](EOWidgetAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvo2lem5sxiqltonxwg2lboruw63q) : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl) : Object

> **__Implements:__**
> : NSDisposable: EOObserving (EOControl)

> **__Package:__**
> : com.webobjects.eointerface

---

## Class Description

---

An EOActionInsertionAssociation object inserts objects from one display group into another.

|  |
| --- |
| __Usable With__ |
| com.webobjects.eointerface.swing: Any object that implements the method __addActionListener__ (javax.swing.JButton and javax.swing.JMenuItem, for example). com.webobjects.eointerface.cocoa: Any object that responds to __setAction__, typically an NSControl. |

|  |
| --- |
| __Aspects__ |
| `source` | Bound to the EODisplayGroup containing objects to insert. This aspect doesn't use a key. |
| `destination` | A relationship of the selected object into which objects from the source EODisplayGroup are inserted. Usually bound to a different EODisplayGroup than __source__. |
| `enabled` | A boolean attribute of the selected object (usually in the destination EODisplayGroup), which determines whether the NSControl is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| `target` | On receiving an action message from the display object, an EOActionInsertionAssociation inserts objects from the source EODisplayGroup into the destination EODisplayGroup. |

## Example

Suppose an application shows Talent in one display group and Movies in another. You want a user to be able to select a talent, select a movie, and then click an Assign Director button that assigns the selected talent as one of the movie's directors. To do this, in Interface Builder, control-drag a connection from the button to the Talent display group. Select EOActionInsertionAssociation in the Connections inspector, and double-click the association's __source__ aspect, binding it to the Talent display group. Similarly, control-drag a connection from the button to the Movie display group. Select EOActionAssociation in the Connections inspector, and bind the association's __destination__aspect to the "directors" key. Now, when the user clicks the button, the selected Talent is added to the __directors__ relationship of the selected Movie. If more than one talent is selected, both are added to the relationship. If more than one Movie is selected, the selected talent are added to the relationship of the first Movie in the selection.

## Interfaces Implemented

---

> : NSDisposable:
>
> : EOObserving:

## Method Types

---

> **All methods**
>
> : [EOActionInsertionAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzew443foj2gs33oifzxg33dnfqxi2lpnyxukt2bmn2gs33ojfxhgzlsoruw63sbonzw6y3jmf2gs33o): [displayGroupSelectionsAllowEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzew443foj2gs33oifzxg33dnfqxi2lpnyxwi2ltobwgc6khojxxk4ctmvwgky3unfxw442bnrwg652fnzqwe3dfmq): [invokeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzew443foj2gs33oifzxg33dnfqxi2lpnyxws3twn5vwkqldoruw63q): [primaryAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzew443foj2gs33oifzxg33dnfqxi2lpnyxxa4tjnvqxe6kbonygky3u)

## Constructors

---

### EOActionInsertionAssociation

`public EOActionInsertionAssociation(Object anObject)`

Description forthcoming.

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

Returns EOAssociation.SourceAspect.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
