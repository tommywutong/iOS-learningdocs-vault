---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WOEvent.html
archived_at: '2026-07-15T08:11:47.592402Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOEvent

> __Inherits
> from:__  EOEvent (EOControl framework)

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  WebObjects/WOEvent.h

---

## Class Description

---

WOEvent is a subclass of EOEvent (defined in the EOControl
framework) that serves as the parent class for objects that gather
information-such as duration-about various operations in WebObjects.
You can see the results of this information gathering in your web
browser by accessing a special "event display" page, and you
can configure how the results are displayed by accessing a special
"event setup" page. Both of these are accessed through special
direct actions (WOEventDisplay and WOEventSetup, respectively).
For example, if you've been running the ComponentElementsTour,
the following URL will access the event display page:

http://localhost/cgi-bin/WebObjects/ComponentElementsTour.woa/wa/WOEventDisplay

WOEvent adds knowledge of pages and components to the EOEvent
class. Events that are subclasses of WOEvent can be grouped or aggregated
by page or by component. Although you can subclass WOEvent, in most
cases the following private subclasses will be adequate for analyzing
WebObjects applications:

|  |  |
| --- | --- |
| __Event Group__ | __Logged Events__ |
| WOApplication Event | __pageWithName:inContext:__ |
| WOAssociation Event | __valueForKeyPath__, __takeValueForKeyPath__ |
| WOComponent Event | __takeValuesFromRequest:inContext:__, __invokeActionForRequest:inContext:__, __appendToResponse:inContext:__, __awake__, __sleep__, __init__ |
| WOComponentReference Event | __pushComponentInContext:__ |

## Instance Methods

---

### dealloc

`- (void)dealloc`

Subclassers should override this method
if the subclass needs to do additional cleaning up when the WOEvent
subclass is freed.

---

### setComponentName:

`- (void)setComponentName:(NSString
*)componentName`

Sets the event's component name to _componentName_.
Event data can be grouped or aggregated according to the component
name.

---

### setPageName:

`- (void)setPageName:(NSString
*)pageName`

Sets the event's page name to _pageName_.
Event data can be grouped or aggregated according to the page name.

---

### signatureOfType:

`- (id)signatureOfType:(EOEventSignatureType)type`

Returns a "signature" for the receiver
of the specified type. These signatures are used to group or aggregate
data on the WOEventDisplay page. WOEvent is able to generate signatures
for the following types:

|  |  |
| --- | --- |
| __Type__ | __Signature__ |
| EOBasicEventSignature | A combination of the event's type and the component name |
| WOComponentSignature | The component name |
| WOPageSignature | The page name |
| WOAssociationSignature | varies based upon the context |

Override this method if you are creating a custom
subclass of WOEvent and need to provide signatures for additional
event types.

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
