---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOActionInsertionAssoc.html
archived_at: '2026-07-18T01:28:45.050353Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOActionCellAssociation-2.md)
[!](EOApplet-2.md)

---

# EOActionInsertionAssociation

__Inherits From:__
EOAssociation : EODelayedObserver (EOControl) : NSObject

__Conforms To:__
NSCoding (EOAssociation)
EOObserving (EODelayedObserver)
NSObject (NSObject)

__Declared in:__
EOInterface/EOActionInsertionAssociation.h

---

## Class Description

An EOActionInsertionAssociation object inserts objects from one display group into another. In the Yellow Box, the EOActionInsertion object uses NSControl's
action
method as a signal to perform the insertion.

| __Usable With__ |
| Any object that responds to setAction: , in the Yellow Box typically an NSControl. |

```
```

| __Aspects__ | __Aspects__ |
| source | Bound to the EODisplayGroup containing objects to insert. This aspect doesn't use a key. |
| destination | A relationship of the selected object into which objects from the source EODisplayGroup are inserted. Usually bound to a different EODisplayGroup than `source`. |
| enabled | A boolean attribute of the selected object (usually in the destination EODisplayGroup), which determines whether the NSControl is enabled. |

```
```

| __Object Keys Taken__ | __Object Keys Taken__ |
| target | On receiving an action message from the display object, an EOActionInsertionAssociation inserts objects from the source EODisplayGroup into the destination EODisplayGroup. |

```
```


## Example

Suppose an application shows Talent in one display group and Movies in another. You want a user to be able to select a talent, select a movie, and then click an Assign Director button that assigns the selected talent as one of the movie's directors. To do this, in Interface Builder, control-drag a connection from the button to the Talent display group. Select EOActionInsertionAssociation in the Connections inspector, and double-click the association's `source` aspect, binding it to the Talent display group. Similarly, control-drag a connection from the button to the Movie display group. Select EOActionAssociation in the Connections inspector, and bind the association's `destination` aspect to the "directors" key. Now, when the user clicks the button, the selected Talent is added to the `directors` relationship of the selected Movie. If more than one talent is selected, both are added to the relationship. If more than one Movie is selected, the selected talent are added to the relationship of the first Movie in the selection.

---

[!](EOActionCellAssociation-2.md)
[!](EOApplet-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
