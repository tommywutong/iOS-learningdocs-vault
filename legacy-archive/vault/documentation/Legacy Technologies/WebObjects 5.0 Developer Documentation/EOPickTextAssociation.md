---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface/Classes/EOPickTextAssociation.html
archived_at: '2026-07-15T08:13:55.313632Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

# EOPickTextAssociation

> **__Inherits from:__**
> : [EOValueAssociation](EOValueAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvmylmovsuc43tn5rwsylunfxw4) : [EOWidgetAssociation](EOWidgetAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvo2lem5sxiqltonxwg2lboruw63q) : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl) : Object

> **__Implements:__**
> : NSDisposable: EOObserving (EOControl)

> **__Package:__**
> : com.webobjects.eointerface

---

## Class Description

---

An EOPickTextAssociation takes the value of its display object, such as an NSTextField, and uses it to form a qualifier with up to three LIKE operators, each compared to a different key of the EODisplayGroup. This allows the user to perform a similarity search based on whole or partial values.

EOPickTextAssociations are most often used with a table view to qualify a list of fetched objects that is too long for convenient scrolling.

|  |
| --- |
| __Usable With__ |
| Any NSControl |

|  |
| --- |
| __Aspects__ |
| `matchKey1` | An attribute to match using a LIKE qualifier. |
| `matchKey2` | An attribute to match using a LIKE qualifier. |
| `matchKey3` | An attribute to match using a LIKE qualifier. |

|  |
| --- |
| __Object Keys Taken__ |
| `target` | The EOPickTextAssociation applies its qualifier when sent an action message from the NSControl. |
| `delegate` | The EOPickTextAssociation applies its qualifier when sent a __controlTextDidChange__ message, causing dynamic update as the user types. |

## Example

Make an EOPickTextAssociation between an NSTextField and an EODisplayGroup of People objects. Bind the __matchKey1__ and __matchKey2__ aspects to the "lastName" and "firstName" keys. If the user types "Bi" in the field, the EOPickTextAssociation applies the following qualifier to the EODisplayGroup:

> ```
> (lastName like "*Bi*") OR (firstName like "*Bi*")
> ```

which matches names like "Bill Smith" and "Joe Biggs". The list of objects displayed in the display group is restricted to those that match the qualifier.

## Interfaces Implemented

---

> : NSDisposable:
>
> : EOObserving:

## Method Types

---

> **All methods**
>
> : [EOPickTextAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkbuwg22umv4hiqltonxwg2lboruw63rpivhva2ldnnkgk6duifzxg33dnfqxi2lpny): [displayValueAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkbuwg22umv4hiqltonxwg2lboruw63rpmruxg4dmmf4vmylmovsuc43qmvrxi): [primaryAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkbuwg22umv4hiqltonxwg2lboruw63rpobzgs3lboj4uc43qmvrxi)

## Constructors

---

### EOPickTextAssociation

`public EOPickTextAssociation(Object aDisplayObject)`

Creates a new EOPickTextAssociation to monitor and update the row values in _aDisplayObject_, an NSControl (Cocoa) which has a text as an attribute.

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See Also:__ bindAspect (EOAssociation), establishConnection (EOAssociation)

---

## Instance Methods

---

### displayValueAspect

`protected String displayValueAspect()`

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
