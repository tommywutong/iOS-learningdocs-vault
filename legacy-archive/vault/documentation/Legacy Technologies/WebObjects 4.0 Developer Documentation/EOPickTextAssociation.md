---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOPickTextAssociation.html
archived_at: '2026-07-18T01:28:43.738285Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOMatrixAssociation.md)
[!](EOPopUpAssociation.md)

---

# EOPickTextAssociation

__Inherits From:__
EOAssociation : EODelayedObserver (EOControl) : NSObject

EOObserving (EODelayedObserver)

__Inherits From:__
com.apple.yellow.eointerface (Yellow Box)

---

## Class Description

An EOPickTextAssociation takes the value of its display object, an NSControl (Application Kit), and uses it to form a qualifier with up to three LIKE operators, each compared to a different key of the EODisplayGroup. This allows the user to perform a similarity search based on whole or partial values. It is for use in Yellow Box applications only; there isn't an equivalent class for Java Client.

EOPickTextAssociations are most often used with a table view to qualify a list of fetched objects that is too long for convenient scrolling.

| __Usable With__ |
| Any NSControl |

```
```

| __Aspects__ | __Aspects__ |
| matchKey1 | An attribute to match using a LIKE qualifier. |
| matchKey2 | An attribute to match using a LIKE qualifier. |
| matchKey3 | An attribute to match using a LIKE qualifier. |

```
```

| __Object Keys Taken__ | __Object Keys Taken__ |
| target | The EOPickTextAssociation applies its qualifier when sent an action message from the NSControl. |
| delegate | The EOPickTextAssociation applies its qualifier when sent a `controlTextDidChange:` message, causing dynamic update as the user types. |

```
```


---

## Example

Make an EOPickTextAssociation between an NSTextField and an EODisplayGroup of People objects. Bind the `matchKey1` and `matchKey2` aspects to the "lastName" and "firstName" keys. If the user types "Bi" in the field, the EOPickTextAssociation applies the following qualifier to the EODisplayGroup:

> ```
> (lastName like "*Bi*") OR (firstName like "*Bi*")
> ```

which matches names like "Bill Smith" and "Joe Biggs". The list of objects displayed in the display group is restricted to those that match the qualifier.

---

## Constructors

public `EOPickTextAssociation`(java.lang.Object _aDisplayObject_)

Creates a new EOPickTextAssociation to monitor and update the row values in _aDisplayObject_, an NSControl (Application Kit) which has a text as an attribute.

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See also:__
[`bindAspect`](EOAssociation.md#apple-gu2tq) (EOAssociation), [`establishConnection`](EOAssociation.md#apple-gu4dq) (EOAssociation)

---

[!](EOMatrixAssociation.md)
[!](EOPopUpAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
