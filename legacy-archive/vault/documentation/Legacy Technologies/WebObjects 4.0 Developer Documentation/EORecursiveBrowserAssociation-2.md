---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EORecursiveBrowserAssoctn.html
archived_at: '2026-07-18T01:28:46.798402Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EORadioMatrixAssociation-2.md)
[!](EOTableViewAssociation-2.md)

---

# EORecursiveBrowserAssociation

__Inherits From:__
EOAssociation : EODelayedObserver (EOControl) : NSObject

__Conforms To:__
NSCoding (EOAssociation)
EOObserving (EODelayedObserver)
NSObject (NSObject)

__Declared in:__
EOInterface/EORecursiveBrowserAssociation.h

---

## Class Description

An EORecursiveBrowserAssociation is the default association for use with a multi-column NSBrowser (Application Kit). EORecursiveBrowserAssociation manages hierarchical structures, such as a company's management chain-the first column is filled with top-level managers, the second column is filled with the employees who report directly to the selected top-level manager, and so on.

| __Usable With__ |
| NSBrowser (Application Kit) |

```
```

| __Aspects__ | __Aspects__ |
| rootChildren | An array of objects with which to fill the browser's first column. |
| title | An attribute of objects to display in the browser's cells. |
| isLeaf | A boolean attribute of objects that determines whether the corresponding browser cell is a leaf (YES) or a branch (NO). |
| children | An NSArray attribute of the selected object, with which to fill the next column. This aspect is only used when the selected object is a branch (responds NO to `isLeaf`). |

```
```

| __Object Keys Taken__ | __Object Keys Taken__ |
| target | used to handle user click actions within the browser. The association sends the proper synchronization msg to the DG. |
| delegate | used to fill in the values of the browser |

```
```


---

## Example

Suppose you want to display a company's management structure in a browser. Start with a display group for Employee objects. Programmatically qualify this display group to fetch only the top-level management (the Employees with which to fill the browser's first column).

Drag a browser into a window. Be sure to set it to "Allow branch selection." Control-drag from the browser to your Employee display group. In the Interface Builder's Connections Inspector (EORecursiveBrowserAssociation-labeled EORecBrowser-is chosen by default), bind the `rootChildren` aspect to Employee's `directReports` relationship (a recursive, to-many relationship). Making this binding has the effect of:

- Creating a new display group named "LastEmployeeColumn." More generally, the new display group has a name of the form, "Last_NameOfFirstDisplayGroup_Column."
- Preconnecting the new display group to a data source.
- Binding the EORecursiveBrowserAssociation's `children` aspect to the `directReports` relationship-the same relationship used for the `rootChildren` aspect.

Now bind the `title` and `isLeaf` aspects. (Note that if you try to bind these aspects before you bind the `rootChildren` aspect, you'll bypass work that the association can do for you automatically.) Control-drag from the browser to either of the display groups, and bind the association's `title` aspect to the `fullName` key and the `isLeaf` aspect to the `isIndividualContributor` key (a method that returns NO if the Employee is a manager with direct reports). It doesn't matter what display group you make these bindings to, because the association expects `rootChildren` and `children` to reference the same kind of objects (have the same keys).

Now the association populates the browser's columns based on the selection in the previous column. You might want to create a master-detail association between the _LastColumn_ display group and another display group. For example, the Employees application might display information about the employee selected in the browser's right-most column.

---

## The rootChildren Aspect

When you bind an EORecursiveBrowserAssociation's `rootChildren` aspect, the association assumes that `children` will be bound to the same key. However, it's possible for you to bind these aspects to different keys. If you want to do this, you'll have to disconnect the `children` binding that the association creates automatically, and then rebind it to the key you want to use. Note that you only have this freedom with the first column. Subsequent columns must all use the same key to satisfy the `children` aspect.

****

---

[!](EORadioMatrixAssociation-2.md)
[!](EOTableViewAssociation-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
