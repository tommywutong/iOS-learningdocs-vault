---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WOAssociation.html
archived_at: '2026-07-18T01:28:51.072660Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WOApplication.md)
[!](WOComponent.md)

---

# WOAssociation

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

The WOAssociation class declares the programmatic interface to objects that represent the values of WebObject attributes, as specified in a declarations file. You rarely need to create subclasses of WOAssociation, except in situations where you need to subclass [WODynamicElement](WODynamicElement.md).

The purpose of a WOAssociation object is to provide a unified interface to values of different types. For example, consider these declarations:

> ```
> TREENAME1:WOString {value = "Ash"};
> ```

> ```
> TREENAME2:WOString {value = treeName};
> ```

> ```
> TREENAME3:WOString {value = selectedTree.name};
> ```

At runtime, the WebObjects parser scans an HTML template and these declarations and creates three WOString dynamic element objects. In the first case, the WOString's `value` attribute is assigned a constant string. In the second, it's associated with the `treeName` variable of the component in which the dynamic element is declared. In the third, `value` is associated with the `name` attribute of the component's `selectedTree` variable. The search path for the value can be arbitrarily deep, depending on the needs of your application:

> ```
> MAYOR:WOString {value = country.state.city.mayor.name};
> ```

To resolve a path such as this, WebObjects accesses each part in turn. First, it looks for the component's `country` variable. If the component responds to a `country` message, it sends one to determine the value; otherwise, it directly accesses the component's `country` instance variable to determine the value. Next, it checks the `country` object for a `state` attribute, using the same strategy of looking for an accessor method named `state` and then, if necessary, accessing the `state` variable's value directly. It continues in this way until the ultimate value is determined.

WOAssociation objects present the WebObjects framework with a unified interface to attribute values, whether their values are static or dynamic. The value attribute for TREENAME1 in the example above will never change during the course of program execution, but the other WOStrings have values that are potentially dynamic, and so will have to be determined at runtime. Since the value of any WOAssociation can be determined by sending it a [`valueInComponent`](#apple-gy4a) message, objects that use WOAssociation objects don't have to be concerned with how values are resolved. The WODynamicElement class makes extensive use of this feature. See the [WODynamicElement](WODynamicElement.md) class specification for more information.

---

## Method Types

**Creation**

**[associationWithKeyPath](#apple-gq4a)

**[associationWithValue](#apple-guza)****

**Obtaining association attributes**

**[isValueConstant](#apple-ha4to)

**[isValueSettable](#apple-gyya)****

**Setting and retrieving value**

**[setValue](#apple-gy2a)

**[valueInComponent](#apple-gy4a)****

#

---

### associationWithKeyPath

public static WOAssociation `associationWithKeyPath`(java.lang.String _aKeyPath_)

Creates and returns a WOAssociation object whose value is determined by evaluating _aKeyPath_. This method is used when a dynamic element's attribute is set to a variable from the component's script. For example, when the WebObjects parser sees a declaration of this sort,

> ```
> TREENAME3:WOString {value = selectedTree.name};
> ```

it invokes `associationWithKeyPath:` to create a WOAssociation whose key is "selectedTree.name". When the resulting WOAssociation is asked for its value, it searches for the value of the `name` attribute of in the current component's `selectedTree` attribute.

If _aKeyPath_ is `null`, the value of the WOAssociation is also `null`.

__See also:__
[`associationWithValue`](#apple-guza)

---

### associationWithValue

public static WOAssociation `associationWithValue`(java.lang.Object _aValue_)

Creates and returns a WOAssociation object whose value is _aValue_, a constant value. This method is used when a dynamic element's attribute is set to a constant. For example, when the WebObjects parser sees a declaration of this sort,

> ```
> TREENAME3:WOString {value = "Time Flies!"};
> ```

it invokes this method to create a WOAssociation whose value is "Time Flies!".

__See also:__
[`associationWithKeyPath`](#apple-gq4a)

---

## Instance Methods

---

### isValueConstant

public boolean `isValueConstant`()

Returns true if the WOAssociation's value is a constant, false otherwise.

__See also:__
[`associationWithValue`](#apple-guza), `[isValueSettable](#apple-gyya)`

---

### isValueSettable

public boolean `isValueSettable`()

Returns false if the receiver's value is constant, true otherwise.

__See also:__
[`associationWithKeyPath`](#apple-gq4a), [`isValueConstant`](#apple-ha4to)

---

### setValue

public void `setValue`(java.lang.Object _aValue_)

public void `setValue`(java.lang.Object _aValue_, WOComponent _aComponent_)

Finds the attribute of _aComponent_ pointed to by the left-hand-side of the receiver and set its value to _aValue_. If _aComponent_ is not given, this method fins the attribute in the current component association with the receiver. This method throws an exception if the receiver's value is not settable. For example, sending a `setValue:inComponent:` message to a WOAssociation created from this declaration,

> ```
> USER:WOTextField {value = userName};
> ```

sets the current component's `userName` variable to the value typed into the WOTextField.

One way in which the WebObjects framework uses this method is to synchronize the values of nested components. When attributes in child and parent components are associated with one another and changes occur in one component, this method is invoked to migrate those changes to the other component. See the reusable components chapter in the _WebObjects Developer's Guide_ for more information.

__See also:__
[`valueInComponent`](#apple-gy4a)

---

### valueInComponent

public java.lang.Object `valueInComponent`(WOComponent _aComponent_)

Returns a value based on the receiver's association and the current component. For example, sending a `value` message to a WOAssociation created from this declaration,

> ```
> DOWNPAYMENT:WOString {value = downpayment};
> ```

returns the value of the current component's `downpayment` variable.

Sending a `value` message to a WOAssociation created from this declaration,

> ```
> DOWNPAYMENT:WOString {value = "$5000.00"};
> ```

returns the value "$5000.00" (independent of the current component).

This method raises an exception if it cannot resolve the WOAssociation's value with the current component.

One way in which the WebObjects framework uses this method is to synchronize the values of nested components. When attributes in child and parent components are associated with one another and changes occur in one component, this method is invoked to migrate those changes to the other component. See the reusable components chapter in the _WebObjects Developer's Guide_ for more information.

__See also:__
[`setValue`](#apple-gy2a)

---

[!](WOApplication.md)
[!](WOComponent.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
