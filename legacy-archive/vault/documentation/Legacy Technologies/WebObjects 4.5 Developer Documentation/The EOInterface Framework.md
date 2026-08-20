---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Introduction.html
archived_at: '2026-07-15T08:11:45.230386Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](EOInterfaceTOC.md)

# The EOInterface Framework

> **__Package:__**
> : com.apple.client.eocontrol (com.apple.client.eointerface)
> : com.apple.yellow.eointerface (com.apple.yellow.eointerface)

---

## Introduction

The EOInterface framework defines one of the layers of the
Enterprise Objects Framework architecture-the interface layer.

The relationship between user interface objects and enterprise
objects is managed by an instance of the EODisplayGroup class. EODisplayGroups
are used by EOAssociation objects to mediate between enterprise
objects and the user interface. EOAssociations link a single user
interface object to one ore more class properties (keys) of the
objects managed by an EODisplayGroup. The properties' values are displayed
in the association's user interface object.

In the Interface layer, EOAssociation objects "observe"
EODisplayGroups to make sure that the data displayed in the user
interface remains consistent with enterprise object data. EODisplayGroups interact
with a data source, which supplies them with enterprise objects.

The interface layer's associations are listed in the following
table:

|  |  |  |  |
| --- | --- | --- | --- |
| __Association__ | __com.apple.yellow.eointerface__ | __com.apple.client.eointerface__ | __Description__ |
| [EOActionAssociation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOActionAssociation.html#EOActionAssociation) | Yes | Yes | Allows you to set up an interface object, such as a button, to send a message to the objects selected in the association's display group when the interface object is acted on |
| [EOActionCellAssociation](EOActionCellAssociation.md#apple-ivhucy3unfxw4q3fnrwec43tn5rwsylunfxw4) | Yes | No | The default association class for use with NSActionCells |
| [EOActionInsertionAssociation](EOActionInsertionAssociation.md#apple-ivhucy3unfxw4sloonsxe5djn5xec43tn5rwsylunfxw4) | Yes | Yes | Inserts objects from one display group into another. |
| [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4) | Yes | Yes | Defines the mechanism that transfers values between EODisplayGroups and the user interface of an application. |
| [EOColumnAssociation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOColumnAssociation.html#EOColumnAssociation) | Yes | No | Cooperates with an EOTableViewAssociation to display values in a column of an NSTableView |
| [EOComboBoxAssociation](EOComboBoxAssociation.md#apple-ivhug33nmjxue33yifzxg33dnfqxi2lpny) | Yes | Yes | Displays an attribute or to-one relationship value in a combo box |
| [EOControlAssociation](EOControlAssociation.md#apple-ivhug33oorzg63cbonzw6y3jmf2gs33o) | Yes | No | The default EOAssociation subclass for use with NSControl objects |
| [EODetailSelectionAssociation](EODetailSelectionAssociation.md#apple-ivhuizlumfuwyu3fnrswg5djn5xec43tn5rwsylunfxw4) | Yes | No | Binds two EODisplayGroups together through a relationship, so that the destination display group acts as an editor for that relationship. |
| [EOGenericControlAssociation](EOGenericControlAssociation.md#apple-ivhuozlomvzgsy2dn5xhi4tpnraxg43pmnuwc5djn5xa) | Yes | No | the abstract superclass of EOControlAssociation and EOActionCellAssociation. |
| [EOMasterCopyAssociation](EOMasterCopyAssociation.md#apple-ivhu2yltorsxeq3pob4uc43tn5rwsylunfxw4) | Yes | No | Synchronizes two EODisplayGroups that share the same data source but have different qualifiers. |
| [EOMasterDetailAssociation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOMasterDetailAssoc.html#EOMasterDetailAssociation) | Yes | Yes | Binds one EODisplayGroup (the detail) to a relationship in another (the master), so that the detail display group contains the destination objects for the object selected in the master. |
| [EOMasterPeerAssociation](EOMasterPeerAssociation.md#apple-ivhu2yltorsxeudfmvzec43tn5rwsylunfxw4) | Yes | No | Binds two EODisplayGroups together in a master-detail relationship, where the detail EODisplayGroup shows the destination objects for the relationship of the master EODisplayGroup. |
| [EOMatrixAssociation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOMatrixAssociation.html#EOMatrixAssociation) | Yes | No | Allows you to populate an NSMatrix's cells. |
| [EOPickTextAssociation](EOPickTextAssociation.md#apple-ivhva2ldnnkgk6duifzxg33dnfqxi2lpny) | Yes | No | Allows the user to perform a similarity search based on whole or partial values. |
| [EOPopUpAssociation](EOPopUpAssociation.md#apple-ivhva33qkvyec43tn5rwsylunfxw4) | Yes | No | Displays an attribute or to-one relationship value in an NSPopUpButton |
| [EORadioMatrixAssociation](EORadioMatrixAssociation.md#apple-ivhveylenfxu2yluojuxqqltonxwg2lboruw63q) | Yes | No | Displays a string or an integer in an NSMatrix. |
| [EORecursiveBrowserAssociation](EORecursiveBrowserAssociation.md#apple-ivhvezldovzhg2lwmvbhe33xonsxeqltonxwg2lboruw63q) | Yes | No | The default association for use with a multi-column NSBrowser. |
| [EOTableAssociation](EOTableAssociation.md#apple-ivhviylcnrsuc43tn5rwsylunfxw4) | No | Yes | Associates a display group with a Swing JTable. |
| [EOTableColumnAssociation](EOTableColumnAssociation.md#apple-ivhviylcnrsug33movww4qltonxwg2lboruw63q) | No | Yes | Associates a single attribute of all enterprise objects in a display group with a Swing JTable TableColumn. |
| [EOTableViewAssociation](EOTableViewAssociation.md#apple-ivhviylcnrsvm2lfo5axg43pmnuwc5djn5xa) | Yes | No | Manages the individual EOColumnAssociations between an NSTableView (Application Kit) and an EODisplayGroup. |
| [EOTextAssociation](EOTextAssociation.md#apple-ivhvizlyoraxg43pmnuwc5djn5xa) | Yes | Yes | Displays a plain or rich text attribute in an NSText object (Application Kit) or an EOTextField, EOTextArea, or EOFormCell (com.apple.client.eointerface) by binding the text object to a string or NSData attribute. |

[![Table of Contents](attachments/images/up.gif)](EOInterfaceTOC.md)
