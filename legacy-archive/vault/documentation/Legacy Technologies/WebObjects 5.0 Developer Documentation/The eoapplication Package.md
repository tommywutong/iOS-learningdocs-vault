---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Introduction.html
archived_at: '2026-07-15T08:13:43.329936Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](WebObjectsTOC.md)

# The eoapplication Package

> **__Package:__**
> : com.webobjects.eoapplication

---

## Introduction

Documentation for this package is forthcoming. For information on using this package, see the book _Getting Started with Direct to Java Client_.

The most important classes in this package are:

|  |  |
| --- | --- |
| __Class__ | __Description__ |
| EOController | A representation of controller objects responsible for managing and sometimes generating the user interface of a Java Client application |
| EOComponentController | A controller that manages user interface components |
| EOEntityController | A controller that displays enterprise objects in a user interface |
| EODocumentController | A controller that displays and edits enterprise objects in a user interface |
| EOInterfaceController | A controller that represents an Interface Builder nib file |
| EOApplication | The Java Client application |
| EOAppletController | A representation of an EOApplet as a controller in the controller hierarchy |
| EOApplet | The default Applet class used in Java Client applications |
| EOAction | An abstract representation of operations the user can invoke from the user interface |
| EOXMLUnarchiver | An object containing the parameters from an XML specification used to create the controllers in the controller hierarchy |

## Rule System and XML Description

For Direct to Java Client applications, the controller hierarchy for the client side of the application is created from an XML description. The XML description is created by a rule system on the server side of the application. The details of this process are described in the book _Getting Started With Direct to Java Client_.

There are three pieces of information associated with an EOController class that are used to generate a controller hierarchy with the rule system: the controller's `controllerType`, its corresponding XML tag, and its corresponding XML attributes. Each controller class specification identifies this information in a section titled "Rule System and XML Description".

### controllerType

You use the `controllerType` key to define custom rules that should fire only for certain kinds of controllers. For example, suppose you want to set the minimum width of all an application's windows. To do so, you write a rule whose condition specifies that the `controllerType` is 'windowController'. Then the rule only fires for controllers that control windows. Each controller falls into one of the following controller types:

- windowController
- modalDialogController
- entityController
- widgetController
- tableController
- groupingController
- dividingController
- actionWidgetController

### XML Tag and Attributes

As an XML description is parsed, an EOXMLUnarchiver maps XML tags to particular EOController classes. All concrete controller classes-classes whose instances can actually be used in a controller hierarchy-have an XML tag.

XML attributes tell the EOXMLUnarchiver how to configure the controllers. XML attributes are inherited. For example, there are three XML attributes defined for EOController-className, disabledActionNames, and typeName. These attributes can be used by any controller, however, because all controllers are subclasses of EOController.

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
