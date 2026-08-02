---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/EOInterface.html
archived_at: '2026-07-15T08:01:58.195723Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOActionAssociation-2.md)

---

# The EOInterface Framework

__Framework:__
System/Library/Frameworks/EOInterface.framework

__Header File Directories:__
System/Library/Frameworks/EOInterface.framework/Headers

# Introduction

The EOInterface framework defines one of the layers of the Enterprise Objects Framework architecture-the interface layer.

The relationship between user interface objects and enterprise objects is managed by an instance of the EODisplayGroup class. EODisplayGroups are used by EOAssociation objects to mediate between enterprise objects and the user interface. EOAssociations link a single user interface object to one ore more class properties (keys) of the objects managed by an EODisplayGroup. The properties' values are displayed in the association's user interface object.

In the Interface layer, EOAssociation objects "observe" EODisplayGroups to make sure that the data displayed in the user interface remains consistent with enterprise object data. EODisplayGroups interact with a data source, which supplies them with enterprise objects.

The interface layer's associations are listed in the following table:

| __Association__ | __Yellow Box__ | __Java Client__ | __Description__ |
| [EOActionAssociation](EOActionAssociation-2.md) | Yes | Yes | Allows you to set up an interface object, such as a button, to send a message to the objects selected in the association's display group when the interface object is acted on |
| [EOActionCellAssociation](EOActionCellAssociation-2.md) | Yes | No | The default association class for use with NSActionCells |
| [EOActionInsertionAssociation](EOActionInsertionAssociation-2.md) | Yes | Yes | Inserts objects from one display group into another. |
| [EOAssociation](EOAssociation-3.md) | Yes | Yes | Defines the mechanism that transfers values between EODisplayGroups and the user interface of an application. |
| [EOColumnAssociation](EOColumnAssociation-2.md) | Yes | No | Cooperates with an EOTableViewAssociation to display values in a column of an NSTableView |
| [EOComboBoxAssociation](EOComboBoxAssociation-2.md) | Yes | Yes | Displays an attribute or to-one relationship value in a combo box |
| [EOControlAssociation](EOControlAssociation-2.md) | Yes | No | The default EOAssociation subclass for use with NSControl objects |
| [EODetailSelectionAssociation](EODetailSelectionAssociation-2.md) | Yes | No | Binds two EODisplayGroups together through a relationship, so that the destination display group acts as an editor for that relationship. |
| [EOGenericControlAssociation](EOGenericControlAssociation-2.md) | Yes | No | the abstract superclass of EOControlAssociation and EOActionCellAssociation. |
| [EOMasterCopyAssociation](EOMasterCopyAssociation-2.md) | Yes | No | Synchronizes two EODisplayGroups that share the same data source but have different qualifiers. |
| [EOMasterDetailAssociation](EOMasterDetailAssociation-2.md) | Yes | Yes | Binds one EODisplayGroup (the detail) to a relationship in another (the master), so that the detail display group contains the destination objects for the object selected in the master. |
| [EOMasterPeerAssociation](EOMasterPeerAssociation-2.md) | Yes | No | Binds two EODisplayGroups together in a master-detail relationship, where the detail EODisplayGroup shows the destination objects for the relationship of the master EODisplayGroup. |
| [EOMatrixAssociation](EOMatrixAssociation-2.md) | Yes | No | Allows you to populate an NSMatrix's cells. |
| [EOPickTextAssociation](EOPickTextAssociation-2.md) | Yes | No | Allows the user to perform a similarity search based on whole or partial values. |
| [EOPopUpAssociation](EOPopUpAssociation-2.md) | Yes | No | Displays an attribute or to-one relationship value in an NSPopUpButton |
| [EORadioMatrixAssociation](EORadioMatrixAssociation-2.md) | Yes | No | Displays a string or an integer in an NSMatrix. |
| [EORecursiveBrowserAssociation](EORecursiveBrowserAssociation-2.md) | Yes | No | The default association for use with a multi-column NSBrowser. |
| [EOTableViewAssociation](EOTableViewAssociation-2.md) | Yes | No | Manages the individual EOColumnAssociations between an NSTableView (Application Kit) and an EODisplayGroup. |
| [EOTextAssociation](EOTextAssociation-2.md) | Yes | Yes | Displays a plain or rich text attribute in an NSText object (Application Kit) or an EOTextField, EOTextArea, or EOFormCell (Java Client) by binding the text object to a string or NSData attribute. |

```
```

In addition to the above association classes, EOInterface defines the following classes for use exclusively with Java Client applications:

- [EOApplet](EOApplet-2.md)
- [EOApplication](EOApplication-2.md)
- [EOArchive](EOArchive-2.md)
- [EOInterfaceController](EOInterfaceController-2.md)
- [EOViewLayout](EOViewLayout-2.md)

---

[[TOC]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html) [Prev] [[Next]](Classes/EOActionAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
