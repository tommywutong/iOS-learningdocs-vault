---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOPickTextAssociation.html
archived_at: '2026-07-15T08:11:44.908255Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOPickTextAssociation

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

An EOPickTextAssociation takes the value of its display object,
an NSControl (Application Kit), and uses it to form a qualifier
with up to three LIKE operators, each compared to a different key
of the EODisplayGroup. This allows the user to perform a similarity
search based on whole or partial values.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.client.eointerface package. |

EOPickTextAssociations are most often used with a table view
to qualify a list of fetched objects that is too long for convenient
scrolling.

|  |
| --- |
| __Usable With__ |
| Any NSControl |

|  |
| --- |
| __Aspects__ |
| matchKey1 | An attribute to match using a LIKE qualifier. |
| matchKey2 | An attribute to match using a LIKE qualifier. |
| matchKey3 | An attribute to match using a LIKE qualifier. |

|  |
| --- |
| __Object Keys Taken__ |
| target | The EOPickTextAssociation applies its qualifier when sent an action message from the NSControl. |
| delegate | The EOPickTextAssociation applies its qualifier when sent a `controlTextDidChange` message, causing dynamic update as the user types. |

## Example

Make an EOPickTextAssociation between an NSTextField and an
EODisplayGroup of People objects. Bind the `matchKey1` and `matchKey2` aspects
to the "lastName" and "firstName" keys. If the user types "Bi"
in the field, the EOPickTextAssociation applies the following qualifier
to the EODisplayGroup:

> ```
> (lastName like "*Bi*") OR (firstName like "*Bi*")
> ```

which matches names like "Bill Smith" and "Joe Biggs".
The list of objects displayed in the display group is restricted
to those that match the qualifier.

## Constructors

---

### EOPickTextAssociation

`public EOPickTextAssociation(Object  aDisplayObject)`

Creates a new EOPickTextAssociation to monitor
and update the row values in  _aDisplayObject,_
an NSControl (Application Kit) which has a text as an attribute.

You
normally set up associations with the Interface Builder application,
in which case you don't need to create them programmatically.
However, if you do create them up programmatically, setting them up
is a multi-step process. After creating an association, you must
bind its aspects and establish its connections.

__See
Also:__  [bindAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe2lomraxg4dfmn2a) (EOAssociation), [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) (EOAssociation)

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
