---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WODynamicElement.html
archived_at: '2026-07-18T01:28:53.985847Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WODisplayGroup-2.md)
[!](WOElement-2.md)

---

# WODynamicElement

__Inherits From:__
[WOElement](WOElement-2.md) : NSObject

__Declared in:__
WebObjects/WODynamicElement.h

---

## Class Description

WODynamicElement is an abstract superclass for classes that generate dynamic elements: objects representing HTML or PDF elements whose values can programmatically change at run time. Dynamic elements have a name and one or more _properties_, instance variables holding such things as user-entered data or user-triggerable actions. The properties of a dynamic element are associated with, or "bound" to, the properties of the [WOComponent](WOComponent-2.md) object that represents the page (or portion of a page) in which the dynamic element appears.

At runtime, a dynamic element can extract values from the request, feed those values across the bindings to the owning component, receive back new data, and include that data in the next representation of the page. A dynamic element can also detect if the user has manipulated it (for instance, clicking a button) to signal some intention and then trigger the appropriate action method in the owning WOComponent. The bindings between properties of a dynamic element and properties of a WOComponent are made possible by _associations_, objects that know how to "push" and "pull" values to and from another object using keys. All objects that inherit from NextObject have associative capabilities through NextObjects's implementation of the KeyValueCoding protocol. (In Objective-C, the mechanism is slightly different; see "Differences Between Java and Objective-C," below.)

WODynamicElements must implement the default initializer to initialize their instance variables with the appropriate association objects (passed in). As [WOElement](WOElement-2.md) objects, they must also implement one or more of the three request-handling methods. In the context of request handling, a dynamic element can use its associations to:

- Push request values into the associated properties of their WOComponent ([__takeValuesFromRequest:inContext:__](WOComponent-2.md#apple-ge3tg))
- Invoke action methods of the WOComponent ([__invokeActionForRequest:inContext:__](WOComponent-2.md#apple-geytg))
- Extract values from the WOComponent when composing a dynamic HTML response ([__appendToResponse:inContext:__](WOComponent-2.md#apple-geydgmq))

All dynamic elements must implement [__appendToResponse:inContext:__](WOComponent-2.md#apple-geydgmq). If they accept user input or respond to user actions (such as mouse clicks), they should implement [__takeValuesFromRequest:inContext:__](WOComponent-2.md#apple-ge3tg) and [__invokeActionForRequest:inContext:__](WOComponent-2.md#apple-geytg), respectively.

__Note:__
If you write a dynamic element that appends content to the response (this is typically done by
overriding [__appendToResponse:inContext:__](WOComponent-2.md#apple-geydgmq)), be sure to verify that the request is not client-side:

> ```
> - (void)appendToResponse:(WOResponse *)response inContext:(WOContext *)context {
> ```

> ```
> 	if(![[context request]] isFromClientComponent]){
> ```

> ```
> 		// append content here
> ```

> ```
> 	}
> ```

> ```
> }
> ```

Dynamic elements do not know about their WOComponent object until run time. During request-handling, the application stores components (representing a page and subcomponents on the page) on a stack maintained by the [WOContext](WOContext-2.md) object, with the currently referenced WOComponent on top of the stack. A dynamic element's [WOAssociation](WOAssociation-2.md) retrieves the current WOComponent (through an invocation of WOContext's [__component__](WOContext-2.md#apple-gu3q) method) and reads and writes values from and to the WOComponent using KeyValueCoding methods.

A dynamic element can represent a single HTML or PDF element (such as an editable text field) or a compound element, such as the LoginPanel whose implementation is described below. WebObjects includes a suite of ready-made dynamic elements and the WebObjects Builder application makes these objects available on its palettes. The _Dynamic Elements Reference_ describes WebObjects' dynamic elements and provides examples showing how to use them.

---

## Method Types

**Creation**

**[- __initWithName:associations:template:__](#apple-gu2taoa)**

---

### WODynamicElement

---

## Instance Methods

---

### initWithName:associations:template:

- (id)__initWithName:__ (NSString \*)_aName_ __associations:__ (NSDictionary \*)_someAssociations_ __template:__ (WOElement \*)_anElement_

Returns a dynamic element identified by class _aName_ and initialized with the objects in dictionary _someAssociations_. The dictionary contains [WOAssociation](WOAssociation-2.md) objects, which know how to take values from, and set values in, an "owning" [WOComponent](WOComponent-2.md). To properly initialize a dynamic element, you should use the published keys of the dynamic element to get the associations that belong to the dynamic element; then assign these objects to instance variables. The _anElement_ argument, if not __nil__ , is the root object of a graph of [WOElement](WOElement-2.md)s associated with the dynamic element.

Typically, a key in the _someAssociations_ dictionary is identified with a property of the element, and the value of this key is the name of a property of the associated Component. For example, the value of key "userName" might be bound to "employee.name" in the WOComponent; this designation means that WOComponent has a property called "employee" (possibly referring to an "Employee" object) which in turn has a property called "name". In this case, the binding is two-way; changes in the dynamic element are reflected in the WOComponent property, and changes in the WOComponent property are communicated to the dynamic element. The value of an association can also be a constant, in which case the binding is one-way: WOComponent to dynamic element.

---

[!](WODisplayGroup-2.md)
[!](WOElement-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
