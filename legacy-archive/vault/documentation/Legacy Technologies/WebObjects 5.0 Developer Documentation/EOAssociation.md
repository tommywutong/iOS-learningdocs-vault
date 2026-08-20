---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface/Classes/EOAssociation.html
archived_at: '2026-07-15T08:13:55.160113Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md) 

# EOAssociation

> **__Inherits from:__**
> : EODelayedObserver (EOControl) : Object

> **__Implements:__**
> : NSDisposable: EOObserving (EOControl)

> **__Package:__**
> : com.webobjects.eointerface

---

### Class at a Glance

---

An EOAssociation maintains a two-way binding between the properties of a display object, such as a text field or combo box, and the properties of one or more enterprise objects contained in one or more EODisplayGroups. You typically create and configure associations in Interface Builder, using the programmatic interface only when you write your own EOAssociation subclasses.

#### Principal Attributes

---

- A display object (such as a text field or combo box)
- Aspects that control different parameters of the display object (such as __value__ and __enabled__)
- One or more EODisplayGroups (no more than one per aspect)
- One or more keys (enteprise object properties) (as many as one key per aspect)

## Class Description

---

EOAssociation defines the mechanism that transfers values between EODisplayGroups and the user interface of an application. An EOAssociation instance is tied to a single display object, a user interface object or other kind of object that manages values intended for display. The EOAssociation takes over certain outlets of the display object and sets its value according to the selection in the EODisplayGroup. An EOAssociation also has various aspects, which define the different parameters of the display object that it controls, such as the value or values displayed and whether the display object is enabled or editable. Each aspect can be bound to an EODisplayGroup with a key denoting a property of the enterprise objects in the EODisplayGroup. The value or values of this property determine the value for the EOAssociation's aspect.

EOAssociation is an abstract class, defining only the general mechanism for binding display objects to EODisplayGroups. You always create instances of its various subclasses, which define behavior specific to different kinds of display objects. For information on the different EOAssociation subclasses you can use, see the following subclass specifications:

|  |  |
| --- | --- |
| __com.webobjects.eointerface.cocoa__ |  |
| EOCocoaButtonPlugin | EOCocoaSimpleTextPlugin |
| EOCocoaCheckBoxPlugin | EOCocoaTableColumnPlugin |
| EOCocoaComboBoxPlugin | EOCocoaTableViewPlugin |
| EOCocoaImageViewPlugin | EOCocoaTextFieldPlugin |
| EOCocoaPopUpButtonPlugin | EOCocoaTextPlugin |
| EOCocoaRadioMatrixPlugin |  |

|  |  |
| --- | --- |
| __com.webobjects.eointerface.swing__ |  |
| EOSwingButtonPlugin | EOSwingQuickTimeViewPlugin |
| EOSwingCheckBoxPlugin | EOSwingTableColumnPlugin |
| EOSwingComboBoxPlugin | EOSwingTablePlugin |
| EOSwingImageViewPlugin | EOSwingTextPlugin |
|  |  |

You normally set up EOAssociations using Interface Builder; each of the class specifications for EOAssociation's subclasses provide an example using Interface Builder to set them up. EOAssociation's programmatic interface is more important when defining custom EOAssociation subclasses. For more information on EOAssociations, see the sections:

- "How EOAssociations Work" (page 41)
- "Setting up an EOAssociation Programmatically" (page 43)
- "Creating a Subclass of EOAssociation" (page 44)

## Constants

---

EOAssociation defines the following String constants to identify the names of association aspects:

|  |  |
| --- | --- |
| ActionAspect | NullAspectSignature |
| ArgumentAspect | ParentAspect |
| AttributeAspectSignature | SelectedIndexAspect |
| AttributeToManyAspectSignature | SelectedObjectAspect |
| AttributeToOneAspectSignature | SelectedTitleAspect |
| AttributeToOneToManyAspectSignature | SourceAspect |
| BackgroundColorAspect | TextColorAspect |
| BoldAspect | TitlesAspect |
| DestinationAspect | ToManyAspectSignature |
| EnabledAspect | ToOneAspectSignature |
| ItalicAspect | ToOneToManyAspectSignature |
| MatchKey1Aspect | URLAspect |
| MatchKey2Aspect | ValueAspect |
| MatchKey3Aspect |  |

## Interfaces Implemented

---

> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwi2ltobxxgzi)
>
> :
>
> : EOObserving:

## Method Types

---

> **All methods**
>
> : [EOAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxukt2bonzw6y3jmf2gs33o): [associationClassesForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmfzxg33dnfqxi2lpnzbwyyltonsxgrtpojhwe2tfmn2a): [registerAssociationClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpojswo2ltorsxeqltonxwg2lboruw63sdnrqxg4y): [aspectSignatures](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwc43qmvrxiu3jm5xgc5dvojsxg): [aspects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwc43qmvrxi4y): [bindAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe2lomraxg4dfmn2a): [breakConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe4tfmfvug33onzswg5djn5xa): [copyMatchingBindingsFromAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwg33qpfgwc5ddnbuw4z2cnfxgi2lom5zum4tpnvaxg43pmnuwc5djn5xa): [displayGroupForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwi2ltobwgc6khojxxk4cgn5zec43qmvrxi): [displayGroupKeyForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwi2ltobwgc6khojxxk4clmv4um33sifzxazldoq): [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk3teivsgs5djnztq): [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny): [isConnected](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxws42dn5xg4zldorswi): [isEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxws42fnzqwe3dfmq): [isEnabledAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxws42fnzqwe3dfmraxislomrsxq): [isExplicitlyDisabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxws42fpbygy2ldnf2gy6kenfzwcytmmvsa): [isUsableWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxws42vonqwe3dfk5uxi2cpmjvgky3u): [object](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxw6ytkmvrxi): [objectKeysTaken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxw6ytkmvrxis3fpfzviyllmvxa): [primaryAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxa4tjnvqxe6kbonygky3u): [priority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxa4tjn5zgs5dz): [setExplicitlyDisabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzluiv4ha3djmnuxi3dziruxgylcnrswi): [setObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzluj5rguzldoq): [setValueForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5a): [setValueForAspectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5cborew4zdfpa): [shouldEndEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg2dpovwgirlomrcwi2lunfxgo): [shouldEndEditingAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg2dpovwgirlomrcwi2lunfxgoqlujfxgizly): [subjectChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg5lcnjswg5cdnbqw4z3fmq): [valueForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxmylmovsum33sifzxazldoq): [valueForAspectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxmylmovsum33sifzxazldoraxislomrsxq)

## Constructors

---

### EOAssociation

`public EOAssociation(Object anObject)`

Description forthcoming.

---

## Static Methods

---

### associationClassesForObject

`public static NSArray associationClassesForObject(Object anObject)`

Description forthcoming.

---

### registerAssociationClass

`public static void registerAssociationClass(Class aClass)`

Description forthcoming.

---

## Instance Methods

---

### aspectSignatures

`public NSArray aspectSignatures()`

Overridden by subclasses to return the signatures of the receiver's aspects, an array of string objects matching its aspects array index for index. The signature strings can be any of:

|  |  |
| --- | --- |
| __Constant__ | __The Aspect Can Be Bound to__ |
| [AttributeAspectSignature](#apple-ijeugskdireus) | Attributes |
| [AttributeToOneAspectSignature](#apple-ijeugssejjeeg) | Attributes and to-one relationships |
| [AttributeToManyAspectSignature](#apple-ijeugrkkivdeo) | Attributes and to-many relationships |
| [AttributeToOneToManyAspectSignature](#apple-ijeugssjizeee) | Attributes, to-one relationships, and to-many relationships |
| [ToOneAspectSignature](#apple-ijeugrchjfcuo) | To-one relationships |
| [ToOneToManyAspectSignature](#apple-ijeugrcfjbauu) | To-one and to-many relationships |
| [ToManyAspectSignature](#apple-ijeugr2di5deo) | To-many relationships |
| [NullAspectSignature](#apple-ijeugqsci5beg) | An EODisplayGroup without a key (the key is irrelevant). |

Interface Builder uses aspect signatures to enable and disable keys in its Connections inspectors.

EOAssociation's implementation of this method returns an array of `AttributeToOneToManyAspectSignature` strings.

---

### aspects

`public NSArray aspects()`

Overridden by subclasses to return the names of the receiving class's aspects as an array of string objects. Subclasses should include their superclass's aspects and add their own when overriding this method.

---

### bindAspect

`public void bindAspect( String aspectName, EODisplayGroup anEODisplayGroup, String key )`

Defines the receiver's link between its display object and _aEODisplayGroup_. _aspectName_ is the name of the aspect it observes in its display object, and _key_ is the name of the property it observes in _aEODisplayGroup_. Invoke [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) after this method to finish setting up the binding. See "Setting up an EOAssociation Programmatically" (page 43) in the class description for more information.

---

### breakConnection

`public void breakConnection()`

Removes the receiver from its EODisplayGroup and display object. Subclasses should override this method to remove the receiver from any outlets of the display object and invoke __super__'s implementation at the end.

__See Also:__ [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny)

---

### copyMatchingBindingsFromAssociation

`public void copyMatchingBindingsFromAssociation(EOAssociation anEOAssociation)`

Description forthcoming.

---

### displayGroupForAspect

`public EODisplayGroup displayGroupForAspect(String aspectName)`

Returns the EODisplayGroup bound to the receiver for _aspectName_, or null if there's no such object.

__See Also:__ [displayGroupKeyForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwi2ltobwgc6khojxxk4clmv4um33sifzxazldoq)

---

### displayGroupKeyForAspect

`public String displayGroupKeyForAspect(String aspectName,)`

Returns the EODisplayGroup key bound to the receiver for _aspectName_, or null if there's no EODisplayGroup.

__See Also:__ [displayGroupForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwi2ltobwgc6khojxxk4cgn5zec43qmvrxi)

---

### dispose

`public void dispose()`

Description forthcoming.

---

### endEditing

`public boolean endEditing()`

Overridden by subclasses to pass the value of the receiver's display object to the EODisplayGroup, by invoking [setValueForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5a) with the display object's value and the appropriate aspect (typically "value"). Returns true if successful, false if not-specifically if [setValueForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5a) returns false.

Subclasses whose display objects immediately pass their changes back to the EOAssociation-such as a button or pop-up list-need not override this method. It's only needed when the display object's value is edited rather than simply set.

EOAssociation's implementation does nothing but return true.

---

### establishConnection

`public void establishConnection()`

Overridden by subclasses to attach the receiver to the outlets of its display object, and to otherwise configure the display object (such as by setting its action method). EOAssociation's implementation subscribes the receiver as an observer of its EODisplayGroups. Subclasses should invoke __super__'s implementation after establishing their own connections.

See "Setting up an EOAssociation Programmatically" (page 43) in the class description for more information.

---

### isConnected

`public boolean isConnected()`

Description forthcoming.

---

### isEnabled

`protected boolean isEnabled()`

Returns `false` if the receiver has explicitly disabled its display object or if the receiver's `EnabledAspect` (if bound) resolves to `false`; `true` otherwise.

---

### isEnabledAtIndex

`protected boolean isEnabledAtIndex(int index)`

Returns `false` if the receiver has explicitly disabled its display object or if the receiver's `EnabledAspect` (if bound) resolves to `false` for _index_; `true` otherwise.

---

### isExplicitlyDisabled

`public boolean isExplicitlyDisabled()`

Returns `true` if the receiver has explicitly disabled its display object, `false` otherwise.

---

### isUsableWithObject

`public boolean isUsableWithObject(Object anObject)`

Overridden by subclasses to return true if instances of the receiving class are usable with _anObject_ false if they aren't. The receiving class can examine any relevant characteristic of _anObject_-its class, configuration (such as whether an NSMatrix operates in radio mode), and so on.

---

### object

`public Object object()`

Description forthcoming.

---

### objectKeysTaken

`public NSArray objectKeysTaken()`

Overridden by subclasses to return the names of display object outlets that instances assume control of. Interface Builder uses this information to disable connections from these outlets in its Connections Inspector.

---

### primaryAspect

`public String primaryAspect()`

Overridden by subclasses to return the default aspect, usually one denoting the displayed value, which by convention is named "value". EOAssociation's implementation returns null.

---

### priority

`public int priority()`

Returns the receiver's change notification priority. For more information, see the EODelayedObserver class specification (EOControl).

---

### setExplicitlyDisabled

`public void setExplicitlyDisabled(boolean flag)`

Sets according to _flag_ whether or not the association is explicitly disabled. An association is "explicitly disabled" when the display object shouldn't be editable, such as in the case where the display object simply displays the results of a search.

---

### setObject

`public void setObject(Object anObject)`

Description forthcoming.

---

### setValueForAspect

`public boolean setValueForAspect( Object value, String aspectName)`

Sets a value of the selected enterprise object in the EODisplayGroup bound to _aspectName_. Retrieves the display group and key bound to _aspectName_, and sends the display group a setSelectedObjectValue message with _value_ and the key as arguments. Returns true if successful, or if there's no display group bound to _aspectName_. Returns false if there's an display group and it doesn't accept the new value.

__See Also:__ [valueForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxmylmovsum33sifzxazldoq)

---

### setValueForAspectAtIndex

`public boolean setValueForAspectAtIndex( Object value, String aspectName, int index)`

Sets a value of the enterprise object at _index_ in the EODisplayGroup bound to _aspectName_. Retrieves the display group and key bound to _aspectName_, and sends the display group a setValueForObjectAtIndex message with _value_, _index_, and the key as arguments. Returns true if successful, or if there's no display group bound to _aspectName_. Returns false if there's a display group and it doesn't accept the new value.

__See Also:__ [valueForAspectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxmylmovsum33sifzxazldoraxislomrsxq)

---

### shouldEndEditing

`public boolean shouldEndEditing( String aspectName, String inputString, String errorDescription)`

Invoked by subclasses when the display object fails to validate its input, this method informs the EODisplayGroup bound to _aspectName_ with an associationFailedToValidateValue message, using the display group's selected object. Returns the result of that message, or true if there's no display group.

For example, an association bound to an NSControl object (Cocoa) receives a controlDidFailToFormatStringErrorDescription delegate message when the control's formatter fails to format the input string. Its implementation of that method invokes __shouldEndEditing__.

---

### shouldEndEditingAtIndex

`public boolean shouldEndEditingAtIndex( String aspectName, String inputString, String errorDescription, int index)`

Works in the same manner as [shouldEndEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg2dpovwgirlomrcwi2lunfxgo), but allows you to specify a particular object by _index_ rather than implicitly specifying the selected object.

---

### subjectChanged

`public void subjectChanged()`

Overridden by subclasses to update state based when an EODisplayGroup's selection or contents changes. This method is invoked automatically anytime a display group that's bound to the receiver changes. The receiver can query its display group with selectionChanged and contentsChanged messages to determine how it needs to update.

---

### valueForAspect

`public Object valueForAspect(String aspectName)`

Returns a value of the selected enterprise object in the EODisplayGroup bound to _aspectName_. Retrieves the display group and key bound to _aspectName_, and sends the display group a selectedObjectValueForKey message with the key. Returns null if there's no display group or key bound to _aspectName_.

__See Also:__ [setValueForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5a)

---

### valueForAspectAtIndex

`public Object valueForAspectAtIndex( String aspectName, int index)`

Returns a value of the enterprise object at _index_ in the EODisplayGroup bound to _aspectName_. Retrieves the display group and key bound to _aspectName_, and sends the display group a valueForObjectAtIndex message with _index_ and the key. Returns null if there's no display group or key bound to _aspectName_.

__See Also:__ [valueForAspectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxmylmovsum33sifzxazldoraxislomrsxq)

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
