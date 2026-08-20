---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOAssociation.html
archived_at: '2026-07-18T01:28:45.362066Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOArchive-2.md)
[!](EOAssociation-4.md)

---

# EOAssociation

__Inherits From:__
EODelayedObserver (EOControl) : NSObject

__Conforms To:__
NSCoding
EOObserving (EODelayedObserver)
NSObject (NSObject)

__Declared in:__
EOInterface/EOAssociation.h

---

## Class At a Glance:

**---

### Purpose**

An EOAssociation maintains a two-way binding between the properties of a display object, such as a text field or combo box, and the properties of one or more enterprise objects contained in one or more EODisplayGroups. You typically create and configure associations in Interface Builder, using the programmatic interface only when you write your own EOAssociation subclasses. For information on the different kinds of associations you can use, see the following subclass specifications:

| [EOActionAssociation](EOActionAssociation-2.md) | [EOActionCellAssociation](EOActionCellAssociation-2.md) |
| [EOActionInsertionAssociation](EOActionInsertionAssociation-2.md) | [EOColumnAssociation](EOColumnAssociation-2.md) |
| [EOComboBoxAssociation](EOComboBoxAssociation-2.md) | [EOControlAssociation](EOControlAssociation-2.md) |
| [EODetailSelectionAssociation](EODetailSelectionAssociation-2.md) | [EOGenericControlAssociation](EOGenericControlAssociation-2.md) |
| [EOMasterCopyAssociation](EOMasterCopyAssociation-2.md) | [EOMasterDetailAssociation](EOMasterDetailAssociation-2.md) |
| [EOMasterPeerAssociation](EOMasterPeerAssociation-2.md) | [EOMatrixAssociation](EOMatrixAssociation-2.md) |
| [EOPickTextAssociation](EOPickTextAssociation-2.md) | [EOPopUpAssociation](EOPopUpAssociation-2.md) |
| [EORadioMatrixAssociation](EORadioMatrixAssociation-2.md) | [EORecursiveBrowserAssociation](EORecursiveBrowserAssociation-2.md) |
| [EOTableViewAssociation](EOTableViewAssociation-2.md) | [EOTextAssociation](EOTextAssociation-2.md) |

```
```

**---

### Principal Attributes**

- A display object (such as a text field or combo box)
- Aspects that control different parameters of the display object (such as `value` and `enabled`)
- One or more EODisplayGroups (no more than one per aspect)
- One or more keys (enteprise object properties) (as many as one key per aspect)

**---

### Creation**

**Interface Builder

**[- initWithObject:](#apple-giytinbs) Designated initializer.****

---

## Class Description

EOAssociation defines the mechanism that transfers values between EODisplayGroups and the user interface of an application. An EOAssociation instance is tied to a single __display object__, a user interface object or other kind of object that manages values intended for display. The EOAssociation takes over certain outlets of the display object and sets its value according to the selection in the EODisplayGroup. An EOAssociation also has various __aspects__, which define the different parameters of the display object that it controls, such as the value or values displayed and whether the display object is enabled or editable. Each aspect can be bound to an EODisplayGroup with a key denoting a property of the enterprise objects in the EODisplayGroup. The value or values of this property determine the value for the EOAssociation's aspect.

EOAssociation is an abstract class, defining only the general mechanism for binding display objects to EODisplayGroups. You always create instances of its various subclasses, which define behavior specific to different kinds of display objects. See the listing in the Class at a Glance section for standard EOAssociation subclasses.

You normally set up EOAssociations using Interface Builder; each of the class specifications for EOAssociation's subclasses provide an example using Interface Builder to set them up. EOAssociation's programmatic interface is more important when defining custom EOAssociation subclasses. For more information on EOAssociations, see the sections:

- [How EOAssociations Work](EOAssociation-4.md#apple-gq2da)
- [Setting up an EOAssociation Programmatically](EOAssociation-4.md#apple-gq2te)
- [Creating a Subclass of EOAssociation](EOAssociation-4.md#apple-gq2to)

---

# Adopted Protocols

**NSCoding - encodeWithCoder:**

**- initWithCoder:**

---

## Method Types

**Declaring capabilities**

**[+ aspects](#apple-gm2dgnq)

**[+ aspectSignatures](#apple-guztc)

**[+ objectKeysTaken](#apple-g4ytgoa)[+ isUsableWithObject:](#apple-gu2dq)

**[+ associationClassesSuperseded](#apple-gu2de)[+ displayName](#apple-gu2dk)

**[+ primaryAspect](#apple-gu2ti)

**[- canBindAspect:displayGroup:key:](#apple-gu3dm)************

**Getting all possible EOAssociations for a display object**

**[+ associationClassesForObject:](#apple-giytanrt)**

**Creating and configuring instances**

**[- initWithObject:](#apple-giytinbs)

**[- bindAspect:displayGroup:key:](#apple-gu2tq)

**[- establishConnection](#apple-gu4dq)

**[- breakConnection](#apple-gu3de)

**[- copyMatchingBindingsFromAssociation:](#apple-gu3tc)**********

**Getting the display object**

**[- object](#apple-gu4tq)**

**Examining bindings**

**[- displayGroupForAspect:](#apple-gu3tk)

**[- displayGroupKeyForAspect:](#apple-gu3ts)****

**Updating values**

**[- subjectChanged](#apple-gyytq)

**[- endEditing](#apple-gu4dg)****

**Accessing enterprise object values**

**[- setValue:forAspect:](#apple-gyyde)

**[- setValue:forAspect:atIndex:](#apple-gyydm)

**[- valueForAspect:](#apple-gyzdc)

**[- valueForAspect:atIndex:](#apple-gyzdk)********

**Handling validation errors**

**[- shouldEndEditingForAspect:invalidInput:errorDescription:](#apple-gyyta)

**[- shouldEndEditingForAspect:invalidInput:errorDescription:index:](#apple-gyytk)****

---

## Class Methods

---

### aspects

+ (NSArray \*)`aspects`

Overridden by subclasses to return the names of the receiving class's aspects as an array of string objects. Subclasses should include their superclass's aspects and add their own when overriding this method.

---

### aspectSignatures

+ (NSArray \*)`aspectSignatures`

Overridden by subclasses to return the signatures of the receiver's aspects, an array of string objects matching its aspects array index for index. Each signature string can contain the following characters:

| __Signature Character__ | __Meaning__ |
| A | The aspect can be bound to attributes. |
| 1 (one) | The aspect can be bound to to-one relationships. |
| M | The aspect can be bound to to-many relationships. |

```
```

An aspect signature string of "A1", for example, means the corresponding aspect can be bound to either attributes or to-one relationships. An empty signature indicates that the corresponding aspect can be bound to an EODisplayGroup without a key (that is, the key is irrelevant). Interface Builder uses aspect signatures to enable and disable keys in its Connections inspectors.

EOAssociation's implementation of this method returns an array of "A1M" of the length of its aspects array.

---

### associationClassesForObject:

+ (NSArray \*)`associationClassesForObject:`(id)_aDisplayObject_

Returns the subclasses of EOAssociation usable with _aDisplayObject_. Sends `[isUsableWithObject:](#apple-gu2dq)` to every loaded subclass of EOAssociation, adding those that respond YES to the array. Subclasses shouldn't override this method; override `isUsableWithObject:` instead.

---

### associationClassesSuperseded

+ (NSArray \*)`associationClassesSuperseded`

Overridden by subclasses to return the other EOAssociation classes that the receiver supplants. This allows a subclass to mask its superclasses from the Connection Inspector's pop-up list in Interface Builder, since the subclass always includes the aspects and functionality of its superclasses. For example, EOPopUpAssociation supersedes EOControlAssociation, because for pop-up buttons an EOPopUpAssociation is always more appropriate to use.

---

### displayName

+ (NSString \*)`displayName`

Returns the name used by Interface Builder in the Connection Inspector's pop-up list. EOAssociation's implementation simply returns the name of the receiving class.

---

### isUsableWithObject:

+ (BOOL)`isUsableWithObject:`(id)_aDisplayObject_

Overridden by subclasses to return YES if instances of the receiving class are usable with _aDisplayObject_, NO if they aren't. The receiving class can examine any relevant characteristic of _aDisplayObject_-its class, configuration (such as whether an NSMatrix operates in radio mode), and so on.

---

### objectKeysTaken

+ (NSArray \*)`objectKeysTaken`

Overridden by subclasses to return the names of display object outlets that instances assume control of, such as "target" and "delegate". Interface Builder uses this information to disable connections from these outlets in its Connections Inspector.

---

### primaryAspect

+ (NSString \*)`primaryAspect`

Overridden by subclasses to return the default aspect, usually one denoting the displayed value, which by convention is named "value". EOAssociation's implementation returns `nil`.

---

## Instance Methods

---

### bindAspect:displayGroup:key:

- (void)`bindAspect:`(NSString \*)_aspectName_`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_`key:`(NSString \*)_key_

Defines the receiver's link between its display object and _aDisplayGroup_. _aspectName_ is the name of the aspect it observer in its display object, and _key_ is the name of the property it observes in _aDisplayGroup_. Invoke [`establishConnection`](#apple-gu4dq) after this method to finish setting up the binding. See "[Setting up an EOAssociation Programmatically](EOAssociation-4.md#apple-gq2te)" in the class description for more information.

__See also:__
[- `initWithObject:`](#apple-giytinbs), [- `establishConnection`](#apple-gu4dq)

---

### breakConnection

- (void)`breakConnection`

Removes the receiver from its EODisplayGroup and display object. This causes it to be released, so be sure to retain the EOAssociation before invoking this method if you want to keep it for another use. Subclasses should override this method to remove the receiver from any outlets of the display object, such as target or delegate, and invoke `super`'s implementation at the end.

__See also:__
[- `establishConnection`](#apple-gu4dq)

---

### canBindAspect:displayGroup:key:

- (BOOL)`canBindAspect:`(NSString \*)_aspectName_`displayGroup:`(EODisplayGroup \*)_aDisplayGroup_`key:`(NSString \*)_key_

Overridden by subclasses to return YES if the receiver can tie an aspect named _aspectName_ from its display object to the property identified by _key_ in _aDisplayGroup_, NO if it can't. _aspectName_ should name an aspect supported by the receiver's class.

Interface Builder uses this information to disable aspects in its Connections Inspector. Subclasses can override this method to base their answers on other binds already made, or on characteristics of the receiver's display object or of _aDisplayGroup_. EOAssociation's implementation always returns YES.

__See also:__
[- `localKeys`](EODisplayGroup.md#apple-ge2dcmq) (EODisplayGroup), - __attributeKeys__ (EOClassDescription),
- __toOneRelationshipKeys__
(EOClassDescription),
- __toManyRelationshipKeys__
(EOClassDescription)

---

### copyMatchingBindingsFromAssociation:

- (void)`copyMatchingBindingsFromAssociation:`(EOAssociation \*)_anAssociation_

Duplicates the bindings of _anAssociation_ in the receiver. For each aspect of _anAssociation_ that has an EODisplayGroup, invokes `[bindAspect:displayGroup:key:](#apple-gu2tq)` with the EODisplayGroup and key for that aspect.

---

### displayGroupForAspect:

- (EODisplayGroup \*)`displayGroupForAspect:`(NSString \*)_aspectName_

Returns the EODisplayGroup bound to the receiver for _aspectName_, or `nil` if there's no such object.

__See also:__
[- `displayGroupKeyForAspect:`](#apple-gu3ts)

---

### displayGroupKeyForAspect:

- (NSString \*)`displayGroupKeyForAspect:`(NSString \*)_aspectName_

Returns the EODisplayGroup key bound to the receiver for _aspectName_, or `nil` if there's no EODisplayGroup.

__See also:__
[- `displayGroupForAspect:`](#apple-gu3tk)

---

### endEditing

- (BOOL)`endEditing`

Overridden by subclasses to pass the value of the receiver's display object to the EODisplayGroup, by invoking `[setValue:forAspect:](#apple-gyyde)` with the display object's value and the appropriate aspect (typically "value"). Returns YES if successful, NO if not-specifically if `[setValue:forAspect:](#apple-gyyde)` returns NO. The receiver should also send an `associationDidEndEditing:` message to its EODisplayGroup.

Subclasses whose display objects immediately pass their changes back to the EOAssociation-such as a button or pop-up list-need not override this method. It's only needed when the display object's value is edited rather than simply set.

EOAssociation's implementation does nothing but return YES.

---

### establishConnection

- (void)`establishConnection`

Overridden by subclasses to attach the receiver to the outlets of its display object, and to otherwise configure the display object (such as by setting its

---

action
method). EOAssociation's implementation subscribes the receiver as an observer of its EODisplayGroups and causes the display object to retain the receiver. Subclasses should invoke `super`'s implementation after establishing their own connections.

See "[Setting up an EOAssociation Programmatically](EOAssociation-4.md#apple-gq2te)" in the class description for more information.

__See also:__
[- `breakConnection`](#apple-gu3de)

---

### initWithObject:

- (id)`initWithObject:`(id)_aDisplayObject_

Initializes the receiver to monitor and update the value in _aDisplayObject_, which is typically a user-interface object or an EODisplayGroup. This is the designated initializer for the EOAssociation class. Returns `self`.

__Note:__
Because of the way that EOAssociations are set up, this method doesn't retain _aDisplayObject_. See
"[Setting up an EOAssociation Programmatically](EOAssociation-4.md#apple-gq2te)" in the class description for more information.

__See also:__
[- `bindAspect:displayGroup:key:`](#apple-gu2tq), [- `establishConnection`](#apple-gu4dq)

---

### object

- (id)`object`

Returns the receiver's display object.

__See also:__
[- `initWithObject:`](#apple-giytinbs)

---

### setValue:forAspect:

- (BOOL)`setValue:`(id)_value_`forAspect:`(NSString \*)_aspectName_

Sets a value of the selected enterprise object in the EODisplayGroup bound to _aspectName_. Retrieves the display group and key bound to _aspectName_, and sends the display group a [`setSelectedObjectValue:forKey:`](EODisplayGroup.md#apple-geytqmzq) message with _value_ and the key as arguments. Returns YES if successful, or if there's no display group bound to _aspectName_. Returns NO if there's an display group and it doesn't accept the new value.

__See also:__
[- `valueForAspect:`](#apple-gyzdc)

---

### setValue:forAspect:atIndex:

- (BOOL)`setValue:`(id)_value_`forAspect:`(NSString \*)_aspectName_`atIndex:`(unsigned int)_index_

Sets a value of the enterprise object at _index_ in the EODisplayGroup bound to _aspectName_. Retrieves the display group and key bound to _aspectName_, and sends the display group a [`setValue:forObjectAtIndex:key:`](EODisplayGroup.md#apple-ge2tioi) message with _value_, _index_, and the key as arguments. Returns YES if successful, or if there's no display group bound to _aspectName_. Returns NO if there's a display group and it doesn't accept the new value.

__See also:__
[- `valueForAspect:atIndex:`](#apple-gyzdk)

---

### shouldEndEditingForAspect:invalidInput:errorDescription:

- (BOOL)`shouldEndEditingForAspect:`(NSString \*)_aspectName_`invalidInput:`(NSString \*)_inputString_`errorDescription:`(NSString \*)_errorDescription_

Invoked by subclasses when the display object fails to validate its input, this method informs the EODisplayGroup bound to _aspectName_ with an [`association:failedToValidateValue:forKey:object:errorDescription:`](EODisplayGroup.md#apple-gi3dcoa) message, using the display group's selected object. Returns the result of that message, or YES if there's no display group.

For example, an association bound to an NSControl object (Application Kit) receives a

---

control:didFailToFormatString:errorDescription:
delegate message when the control's formatter fails to format the input string. Its implementation of that method invokes `shouldEndEditingForAspect:invalidInput:errorDescription:`.

__See also:__
[- `shouldEndEditingForAspect:invalidInput:errorDescription:index:`](#apple-gyytk)

---

### shouldEndEditingForAspect:invalidInput:errorDescription:index:

- (BOOL)`shouldEndEditingForAspect:`(NSString \*)_aspectName_`invalidInput:`(NSString \*)_inputString_`errorDescription:`(NSString \*)_errorDescription_`index:`(unsigned int)_index_

Works in the same manner as `[shouldEndEditingForAspect:invalidInput:errorDescription:](#apple-gyyta)`, but allows you to specify a particular object by _index_ rather than implicitly specifying the selected object.

---

### subjectChanged

- (void)`subjectChanged`

Overridden by subclasses to update state based when an EODisplayGroup's selection or contents changes. This method is invoked automatically anytime a display group that's bound to the receiver changes. The receiver can query its display group with [`selectionChanged`](EODisplayGroup.md#apple-ge2dima) and [`contentsChanged`](EODisplayGroup.md#apple-geztgnq) messages to determine how it needs to update.

---

### valueForAspect:

- (id)`valueForAspect:`(NSString \*)_aspectName_

Returns a value of the selected enterprise object in the EODisplayGroup bound to _aspectName_. Retrieves the display group and key bound to _aspectName_, and sends the display group a [`selectedObjectValueForKey:`](EODisplayGroup.md#apple-ge2dgnq) message with the key. Returns `nil` if there's no display group or key bound to _aspectName_.

__See also:__
[- `setValue:forAspect:`](#apple-gyyde)

---

### valueForAspect:atIndex:

- (id)`valueForAspect:`(NSString \*)_aspectName_`atIndex:`(unsigned int)_index_

Returns a value of the enterprise object at _index_ in the EODisplayGroup bound to _aspectName_. Retrieves the display group and key bound to _aspectName_, and sends the display group a [`valueForObjectAtIndex:key:`](EODisplayGroup.md#apple-ge2tony) message with _index_ and the key. Returns `nil` if there's no display group or key bound to _aspectName_.

__See also:__
[- `setValue:forAspect:atIndex:`](#apple-gyydm)

---

[!](EOArchive-2.md)
[!](EOAssociation-4.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
