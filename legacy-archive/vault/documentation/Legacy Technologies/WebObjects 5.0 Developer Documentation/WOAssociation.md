---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WOAssociation.html
archived_at: '2026-07-15T08:15:15.326706Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOAssociation

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : Cloneable

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

The WOAssociation class declares the programmatic interface to objects that represent the values of WebObject attributes, as specified in a declarations file. You rarely need to create subclasses of WOAssociation, except in situations where you need to subclass WODynamicElement.

The purpose of a WOAssociation object is to provide a unified interface to values of different types. For example, consider these declarations:

> ```
> TREENAME1:WOString {value = "Ash"};
> TREENAME2:WOString {value = treeName};
> TREENAME3:WOString {value = selectedTree.name};
> ```

At runtime, the WebObjects parser scans an HTML template and these declarations and creates three WOString dynamic element objects. In the first case, the WOString's __value__ attribute is assigned a constant string. In the second, it's associated with the __treeName__ variable of the component in which the dynamic element is declared. In the third, __value__ is associated with the __name__ attribute of the component's __selectedTree__ variable. The search path for the value can be arbitrarily deep, depending on the needs of your application:

> ```
> MAYOR:WOString {value = country.state.city.mayor.name};
> ```

To resolve a path such as this, WebObjects accesses each part in turn. First, it looks for the component's __country__ variable. If the component responds to a __country__ message, it sends one to determine the value; otherwise, it directly accesses the component's __country__ instance variable to determine the value. Next, it checks the __country__ object for a __state__ attribute, using the same strategy of looking for an accessor method named __state__ and then, if necessary, accessing the __state__ variable's value directly. It continues in this way until the ultimate value is determined.

WOAssociation objects present the WebObjects framework with a unified interface to attribute values, whether their values are static or dynamic. The value attribute for TREENAME1 in the example above will never change during the course of program execution, but the other WOStrings have values that are potentially dynamic, and so will have to be determined at runtime. Since the value of any WOAssociation can be determined by sending it a [valueInComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxxmylmovsus3sdn5wxa33omvxhi) message, objects that use WOAssociation objects don't have to be concerned with how values are resolved. The WODynamicElement class makes extensive use of this feature. See the WODynamicElement class specification for more information.

## Method Types

---

> **Creation**
> : [associationWithKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6qltonxwg2lboruw63rpmfzxg33dnfqxi2lpnzlws5dijnsxsudborua): [associationWithValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6qltonxwg2lboruw63rpmfzxg33dnfqxi2lpnzlws5dikzqwy5lf)
>
> **Obtaining association attributes**
> : [bindingInComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxwe2lomruw4z2jnzbw63lqn5xgk3tu): [booleanValueInComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxwe33pnrswc3swmfwhkzkjnzbw63lqn5xgk3tu): [isValueConstant](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxws42wmfwhkzkdn5xhg5dbnz2a): [isValueConstantInComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxws42wmfwhkzkdn5xhg5dbnz2es3sdn5wxa33omvxhi): [isValueSettable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxws42wmfwhkzktmv2hiylcnrsq): [isValueSettableInComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxws42wmfwhkzktmv2hiylcnrsus3sdn5wxa33omvxhi): [keyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxwwzlzkbqxi2a)
>
> **Setting and retrieving value**
> : [setValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxxgzlukzqwy5lf): [valueInComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxxmylmovsus3sdn5wxa33omvxhi)
>
> **Debugging**
> : [setDebugEnabledForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxxgzluirswe5lhivxgcytmmvsem33sijuw4zdjnztq)

## Constructors

---

### WOAssociation

`protected WOAssociation()`

Description forthcoming.

---

## Static Methods

---

### associationWithKeyPath

`public static WOAssociation associationWithKeyPath(String aKeyPath)`

Creates and returns a WOAssociation object whose value is determined by evaluating _aKeyPath_. This method is used when a dynamic element's attribute is set to a variable from the component's script. For example, when the WebObjects parser sees a declaration of this sort,
> ```
> TREENAME3:WOString {value = selectedTree.name};
> ```

it invokes __associationWithKeyPath__ to create a WOAssociation whose key is "selectedTree.name". When the resulting WOAssociation is asked for its value, it searches for the value of the __name__ attribute of in the current component's __selectedTree__ attribute.

If _aKeyPath_ is null, the value of the WOAssociation is also null.

__See Also:__ [associationWithValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6qltonxwg2lboruw63rpmfzxg33dnfqxi2lpnzlws5dikzqwy5lf)

---

### associationWithValue

`public static WOAssociation associationWithValue(Object aValue)`

Creates and returns a WOAssociation object whose value is _aValue_, a constant value. This method is used when a dynamic element's attribute is set to a constant. For example, when the WebObjects parser sees a declaration of this sort,
> ```
> TREENAME3:WOString {value = "Time Flies!"};
> ```

it invokes this method to create a WOAssociation whose value is "Time Flies!".

__See Also:__ [associationWithKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6qltonxwg2lboruw63rpmfzxg33dnfqxi2lpnzlws5dijnsxsudborua)

---

## Instance Methods

---

### bindingInComponent

`public abstract String bindingInComponent(WOComponent aComponent)`

This abstract method is implemented by WOAssociation subclasses to return, as a String, the binding string as seen in the declarations file.

---

### booleanValueInComponent

`public boolean booleanValueInComponent(WOComponent aComponent)`

Returns the value of the association as a boolean. This method returns `false` if the binding is to a boolean variable or constant with a value of `false`, the binding is to a null value, the binding is to a numeric value equivalent to zero, the binding is to a string that can be interpreted as a number whose value is zero, or the binding is to a string whose value is "false" or "no" (independent of case). Otherwise, this method returns `true`.

---

### isValueConstant

`public boolean isValueConstant()`

Returns true if the WOAssociation's value is a constant, false otherwise.

__See Also:__ [associationWithValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6qltonxwg2lboruw63rpmfzxg33dnfqxi2lpnzlws5dikzqwy5lf), [isValueSettable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxws42wmfwhkzktmv2hiylcnrsq)

---

### isValueConstantInComponent

`public boolean isValueConstantInComponent(WOComponent aComponent)`

Returns false when the association is "constant." Use this for checking bindings at runtime.

__See Also:__ [associationWithValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6qltonxwg2lboruw63rpmfzxg33dnfqxi2lpnzlws5dikzqwy5lf), [isValueSettableInComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxws42wmfwhkzktmv2hiylcnrsus3sdn5wxa33omvxhi)

---

### isValueSettable

`public boolean isValueSettable()`

Returns false if the receiver's value is constant, true otherwise.

__See Also:__ [associationWithKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6qltonxwg2lboruw63rpmfzxg33dnfqxi2lpnzlws5dijnsxsudborua), [isValueConstant](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxws42wmfwhkzkdn5xhg5dbnz2a)

---

### isValueSettableInComponent

`public boolean isValueSettableInComponent(WOComponent aComponent)`

Returns true when the association is "settable." Use this for checking bindings at runtime.

__See Also:__ [associationWithKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6qltonxwg2lboruw63rpmfzxg33dnfqxi2lpnzlws5dijnsxsudborua), [isValueConstant](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxws42wmfwhkzkdn5xhg5dbnz2a)

---

### __keyPath__

`public abstract String keyPath()`

This abstract method is implemented by WOAssociation subclasses to return, as a String, the keypath that the association binds to the component attribute-if there is one. If the association doesn't contain a keypath, as is the case when the association binds a constant value, the string "<none>" is returned.

---

### setDebugEnabledForBinding

`public void setDebugEnabledForBinding(String aBindingName, String aDeclarationName, String aDeclarationType)`

Enables logging whenever binding values are pushed to or pulled from the parent component. The three String parameters are included in the log, and allow you to specify the binding name, the declaration name, and the declaration type, respectively.

---

### setValue

`public void setValue( Object aValue, WOComponent aComponent)`

Finds the attribute of _aComponent_ pointed to by the left-hand-side of the receiver and sets its value to _aValue_. This method throws an exception if the receiver's value is not settable. For example, sending a __setValue__ message to a WOAssociation created from this declaration,

> ```
> USER:WOTextField {value = userName};
> ```

sets the current component's __userName__ variable to the value typed into the WOTextField.

One way in which the WebObjects framework uses this method is to synchronize the values of nested components. When attributes in child and parent components are associated with one another and changes occur in one component, this method is invoked to migrate those changes to the other component. See the reusable components chapter in the _WebObjects Developer's Guide_ for more information.

__See Also:__ [valueInComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxxmylmovsus3sdn5wxa33omvxhi)

---

### toString

`public String toString()`

Description forthcoming.

---

### valueInComponent

`public Object valueInComponent(WOComponent aComponent)`

Returns a value based on the receiver's association and the current component. For example, sending a __value__ message to a WOAssociation created from this declaration,
> ```
> DOWNPAYMENT:WOString {value = downpayment};
> ```

returns the value of the current component's __downpayment__ variable.

Sending a __value__ message to a WOAssociation created from this declaration,

> ```
> DOWNPAYMENT:WOString {value = "$5000.00"};
> ```

returns the value "$5000.00" (independent of the current component).

This method raises an exception if it cannot resolve the WOAssociation's value with the current component.

One way in which the WebObjects framework uses this method is to synchronize the values of nested components. When attributes in child and parent components are associated with one another and changes occur in one component, this method is invoked to migrate those changes to the other component. See the reusable components chapter in the _WebObjects Developer's Guide_ for more information.

__See Also:__ [setValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxxgzlukzqwy5lf)

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
