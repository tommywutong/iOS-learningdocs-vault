---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WOEvent.html
archived_at: '2026-07-15T08:15:15.612178Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOEvent

> **__Inherits from:__**
> : EOEvent : Object

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

WOEvent is a subclass of EOEvent (defined in the EOControl framework) that serves as the parent class for objects that gather information-such as duration-about various operations in WebObjects. You can see the results of this information gathering in your web browser by accessing a special "event display" page, and you can configure how the results are displayed by accessing a special "event setup" page. Both of these are accessed through special direct actions (WOEventDisplay and WOEventSetup, respectively). For example, if you've been running the ComponentElementsTour, the following URL will access the event display page:

http://localhost/cgi-bin/WebObjects/ComponentElementsTour.woa/wa/WOEventDisplay

WOEvent adds knowledge of pages and components to the EOEvent class. Events that are subclasses of WOEvent can be grouped or aggregated by page or by component. Although you can subclass WOEvent, in most cases the following private subclasses will be adequate for analyzing WebObjects applications:

|  |  |
| --- | --- |
| __Event Group__ | __Logged Events__ |
| WOApplication Event | __pageWithName__ |
| WOAssociation Event | __valueForKeyPath__, __takeValueForKeyPath__ |
| WOComponent Event | __takeValuesFromRequest__, __invokeAction__, __appendToResponse__, __awake__, __sleep__ |
| WOComponentReference Event | __pushComponent__ |

## Constants

---

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| AssociationSignature | Description forthcoming. |
| ComponentSignature | Description forthcoming. |
| PageSignature | Description forthcoming. |

## Constructors

---

### WOEvent

`public WOEvent()`

Description forthcoming.

---

## Instance Methods

---

### comment

`public String comment()`

In the default implementation, this method returns the description of the "info" instance variable which is passed at log time. This method can be overridden by subclasses to provide information for the event display.

---

### setComponentName

`public void setComponentName(String componentName)`

Sets the event's component name to _componentName_. Event data can be grouped or aggregated according to the component name.

---

### setPageName

`public void setPageName(String pageName)`

Sets the event's page name to _pageName_. Event data can be grouped or aggregated according to the page name.

---

### signatureOfType

`public String signatureOfType(int type)`

Returns a "signature" for the receiver of the specified type. These signatures are used to group or aggregate data on the WOEventDisplay page. WOEvent is able to generate signatures for the following types:

|  |  |
| --- | --- |
| __Type__ | __Signature__ |
| EOBasicEventSignature | A combination of the event's type and the component name |
| WOComponentSignature | The component name |
| WOPageSignature | The page name |
| WOAssociationSignature | varies based upon the context |

Override this method if you are creating a custom subclass of WOEvent and need to provide signatures for additional event types.

---

### title

`public String title()`

The default implementation of this method returns the "title" value from the EventTypeDescriptions dictionary. This method is required for proper functioning of the event logging display.

---

### toString

`public String toString()`

Returns a String containing a string representation of the receiver.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
