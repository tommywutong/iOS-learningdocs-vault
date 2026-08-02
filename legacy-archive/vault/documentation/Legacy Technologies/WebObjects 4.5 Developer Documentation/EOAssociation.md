---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOAssociation.html
archived_at: '2026-07-15T08:11:44.555398Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOAssociation

> **__Inherits
> from:__**
> : (com.apple.client.eointerface)
> EODelayedObserver (EOControl) :
> Object
> (com.apple.yellow.eointerface)
> EODelayedObserver (EOControl) :
> NSObject

> **__Implements:__**
> : EOObserving (EODelayedObserver)
> : (com.apple.client.eointerface only) NSDisposable

> **__Package:__**
> : com.apple.client.eointerface
> : com.apple.yellow.eointerface

---

### Class at a Glance

---

An EOAssociation maintains a two-way binding
between the properties of a display object, such as a text field
or combo box, and the properties of one or more enterprise objects
contained in one or more EODisplayGroups. You typically create and
configure associations in Interface Builder, using the programmatic
interface only when you write your own EOAssociation subclasses.

#### Principal Attributes

---

- A display object (such as a text field or combo
  box)
- Aspects that control different parameters of the display object
  (such as `value` and `enabled`)
- One or more EODisplayGroups (no more than one per aspect)
- One or more keys (enteprise object properties) (as many as
  one key per aspect)

## Class Description

---

EOAssociation defines the mechanism that transfers values
between EODisplayGroups and the user interface of an application.
An EOAssociation instance is tied to a single display object, a
user interface object or other kind of object that manages values
intended for display. The EOAssociation takes over certain outlets
of the display object and sets its value according to the selection
in the EODisplayGroup. An EOAssociation also has various aspects,
which define the different parameters of the display object that
it controls, such as the value or values displayed and whether the
display object is enabled or editable. Each aspect can be bound
to an EODisplayGroup with a key denoting a property of the enterprise
objects in the EODisplayGroup. The value or values of this property
determine the value for the EOAssociation's aspect.

EOAssociation is an abstract class, defining only the general
mechanism for binding display objects to EODisplayGroups. You always
create instances of its various subclasses, which define behavior specific
to different kinds of display objects. For information on the different
EOAssociation subclasses you can use, see the following subclass
specifications:

|  |
| --- |
| __com.apple.client.eointerface Associations__ |
| [EOActionAssociation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOActionAssociation.html#EOActionAssociation) | [EOActionInsertionAssociation](EOActionInsertionAssociation.md#apple-ivhucy3unfxw4sloonsxe5djn5xec43tn5rwsylunfxw4) |
| [EOComboBoxAssociation](EOComboBoxAssociation.md#apple-ivhug33nmjxue33yifzxg33dnfqxi2lpny) | [EOMasterDetailAssociation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOMasterDetailAssoc.html#EOMasterDetailAssociation) |
| [EOTableAssociation](EOTableAssociation.md#apple-ivhviylcnrsuc43tn5rwsylunfxw4) | [EOTableColumnAssociation](EOTableColumnAssociation.md#apple-ivhviylcnrsug33movww4qltonxwg2lboruw63q) |
| [EOTableViewAssociation](EOTableViewAssociation.md#apple-ivhviylcnrsvm2lfo5axg43pmnuwc5djn5xa) | [EOTextAssociation](EOTextAssociation.md#apple-ivhvizlyoraxg43pmnuwc5djn5xa) |

|  |
| --- |
| __com.apple.yellow.eointerface Associations__ |
| [EOActionAssociation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOActionAssociation.html#EOActionAssociation) | [EOActionCellAssociation](EOActionCellAssociation.md#apple-ivhucy3unfxw4q3fnrwec43tn5rwsylunfxw4) |
| [EOActionInsertionAssociation](EOActionInsertionAssociation.md#apple-ivhucy3unfxw4sloonsxe5djn5xec43tn5rwsylunfxw4) | [EOColumnAssociation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOColumnAssociation.html#EOColumnAssociation) |
| [EOComboBoxAssociation](EOComboBoxAssociation.md#apple-ivhug33nmjxue33yifzxg33dnfqxi2lpny) | [EOControlAssociation](EOControlAssociation.md#apple-ivhug33oorzg63cbonzw6y3jmf2gs33o) |
| [EODetailSelectionAssociation](EODetailSelectionAssociation.md#apple-ivhuizlumfuwyu3fnrswg5djn5xec43tn5rwsylunfxw4) | [EOGenericControlAssociation](EOGenericControlAssociation.md#apple-ivhuozlomvzgsy2dn5xhi4tpnraxg43pmnuwc5djn5xa) |
| [EOMasterCopyAssociation](EOMasterCopyAssociation.md#apple-ivhu2yltorsxeq3pob4uc43tn5rwsylunfxw4) | [EOMasterDetailAssociation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOMasterDetailAssoc.html#EOMasterDetailAssociation) |
| [EOMasterPeerAssociation](EOMasterPeerAssociation.md#apple-ivhu2yltorsxeudfmvzec43tn5rwsylunfxw4) | [EOMatrixAssociation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOMatrixAssociation.html#EOMatrixAssociation) |
| [EOPickTextAssociation](EOPickTextAssociation.md#apple-ivhva2ldnnkgk6duifzxg33dnfqxi2lpny) | [EOPopUpAssociation](EOPopUpAssociation.md#apple-ivhva33qkvyec43tn5rwsylunfxw4) |
| [EORadioMatrixAssociation](EORadioMatrixAssociation.md#apple-ivhveylenfxu2yluojuxqqltonxwg2lboruw63q) | [EORecursiveBrowserAssociation](EORecursiveBrowserAssociation.md#apple-ivhvezldovzhg2lwmvbhe33xonsxeqltonxwg2lboruw63q) |
| [EOTableViewAssociation](EOTableViewAssociation.md#apple-ivhviylcnrsvm2lfo5axg43pmnuwc5djn5xa) | [EOTextAssociation](EOTextAssociation.md#apple-ivhvizlyoraxg43pmnuwc5djn5xa) |

You normally set up EOAssociations using Interface Builder;
each of the class specifications for EOAssociation's subclasses
provide an example using Interface Builder to set them up. EOAssociation's
programmatic interface is more important when defining custom EOAssociation subclasses.
For more information on EOAssociations, see the sections:

- ["How EOAssociations Work"](EOAssociation-2.md#apple-infemrcdivbuc)
- ["Setting up an EOAssociation Programmatically"](EOAssociation-2.md#apple-infemqsfivbeq)
- ["Creating a Subclass of EOAssociation"](EOAssociation-2.md#apple-infemqsiirdek)

## Constants

---

(com.apple.client.eointerface only) EOAssociation defines
the following String constants to identify the names of association
aspects:

|  |  |  |
| --- | --- | --- |
| ActionAspect | EnabledAspect | SourceAspect |
| ArgumentAspect | ParentAspect | TitlesAspect |
| BoldAspect | SelectedObjectAspect | ValueAspect |
| DestinationAspect | SelectedTitleAspect | URLAspect |
| ItalicAspect |  |  |

(com.apple.client.eointerface only) The class defines additional
String constants to identify association signatures (see the method
description [aspectSignatures](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmfzxazldorjwsz3omf2hk4tfom) for
more information):

|  |  |
| --- | --- |
| AttributeAspectSignature | NullAspectSignature |
| AttributeToOneAspectSignature | ToOneAspectSignature |
| AttributeToOneToManyAspectSignature | ToOneToManyAspectSignature |
| AttributeToManyAspectSignature | ToManyAttributeSignature |

## Interfaces Implemented

---

> NSDisposable: `dispose`

## Method Types

---

> **Declaring capabilities**
> : [aspects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmfzxazldorzq) (com.apple.yellow.eointerface static
> method)
> : [aspects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwc43qmvrxi4y) (com.apple.client.eointerface instance
> method)
> : [aspectSignatures](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmfzxazldorjwsz3omf2hk4tfom) (com.apple.yellow.eointerface static
> method)
> : [aspectSignatures](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwc43qmvrxiu3jm5xgc5dvojsxg) (com.apple.client.eointerface instance
> method)
> : [objectKeysTaken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpn5rguzldorfwk6ltkrqwwzlo) (com.apple.yellow.eointerface)
> : [isUsableWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpnfzvk43bmjwgkv3jorue6ytkmvrxi) (com.apple.yellow.eointerface static
> method)
> : [isUsableWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxws42vonqwe3dfk5uxi2cpmjvgky3u) (com.apple.client.eointerface instance
> method)
> : [associationClassesSuperseded](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmfzxg33dnfqxi2lpnzbwyyltonsxgu3vobsxe43fmrswi) (com.apple.yellow.eointerface static
> method)
> : [associationClassesSuperseded](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwc43tn5rwsylunfxw4q3mmfzxgzltkn2xazlsonswizle) (com.apple.client.eointerface instance
> method)
> : [displayName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmruxg4dmmf4u4ylnmu) (com.apple.yellow.eointerface static
> method)
> : [displayName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwi2ltobwgc6komfwwk) (com.apple.client.eointerface instance
> method)
> : [primaryAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpobzgs3lboj4uc43qmvrxi) (com.apple.yellow.eointerface static
> method)
> : [primaryAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxa4tjnvqxe6kbonygky3u) (com.apple.client.eointerface instance
> method)
> : [canBindAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwgyloijuw4zcbonygky3u)
>
> **Getting all possible
> EOAssociations for a display object**
> : [associationClassesForObject:](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmfzxg33dnfqxi2lpnzbwyyltonsxgrtpojhwe2tfmn2du)
>
> **Getting the display object**
> : [object](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxw6ytkmvrxi)
>
> **Examining bindings**
> : [displayGroupForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwi2ltobwgc6khojxxk4cgn5zec43qmvrxi)
> : [displayGroupKeyForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwi2ltobwgc6khojxxk4clmv4um33sifzxazldoq)
>
> **Updating values**
> : [subjectChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg5lcnjswg5cdnbqw4z3fmq)
> : [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk3teivsgs5djnztq)
>
> **Accessing enterprise
> object values**
> : [setValueForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5a)
> : [setValueForAspectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5cborew4zdfpa)
> : [valueForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxmylmovsum33sifzxazldoq)
> : [valueForAspectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxmylmovsum33sifzxazldoraxislomrsxq)
>
> **Handling validation errors**
> : [shouldEndEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg2dpovwgirlomrcwi2lunfxgo)
> : [shouldEndEditingAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg2dpovwgirlomrcwi2lunfxgoqlujfxgizly)

## Constructors

---

### EOAssociation

`public EOAssociation(Object  aDisplayObject)`

Never use this method to create an EOAssociation.
EOAssociation is conceptually an abstract class, and you'd never
use instances of it. Instead, use subclasses of EOAssociation. Instances
of the subclasses can be created programmatically with a constructor
of this same form. For more information, see the constructor description
for the subclass you want to use. For a list of the subclasses,
see the ["Class Description"](#apple-ijeugskki5deo).

---

## Static Methods

---

### aspects

`public static NSArray aspects()`

(com.apple.yellow.eointerface only) Overridden
by subclasses to return the names of the receiving class's aspects
as an array of string objects. Subclasses should include their superclass's
aspects and add their own when overriding this method.

__See
Also:__  [aspects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwc43qmvrxi4y) instance
method

---

### aspectSignatures

`public static NSArray aspectSignatures()`

(com.apple.yellow.eointerface only) Overridden
by subclasses to return the signatures of the receiver's aspects,
an array of string objects matching its aspects array index for
index. Each signature string can contain the following characters:

|  |  |
| --- | --- |
| __Signature Character__ | __Meaning__ |
| A | The aspect can be bound to attributes. |
| 1 (one) | The aspect can be bound to to-one relationships. |
| M | The aspect can be bound to to-many relationships. |

An aspect signature string of "A1", for example,
means the corresponding aspect can be bound to either attributes
or to-one relationships. An empty signature indicates that the corresponding
aspect can be bound to an EODisplayGroup without a key (that is,
the key is irrelevant). Interface Builder uses aspect signatures
to enable and disable keys in its Connections inspectors.

EOAssociation's
implementation of this method returns an array of "A1M" of the
length of its aspects array.

__See Also:__  [aspectSignatures](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwc43qmvrxiu3jm5xgc5dvojsxg) instance
method

---

### associationClassesForObject:

`public static NSArray associationClassesForObject(Object  aDisplayObject)`

Returns the subclasses of EOAssociation
usable with  _aDisplayObject._ Sends [isUsableWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpnfzvk43bmjwgkv3jorue6ytkmvrxi) to every
loaded subclass of EOAssociation, adding those that respond true to
the array. Subclasses shouldn't override this method; override `isUsableWithObject` instead.

---

### associationClassesSuperseded

`public static NSArray associationClassesSuperseded()`

(com.apple.yellow.eointerface only) Overridden
by subclasses to return the other EOAssociation classes that the
receiver supplants. This allows a subclass to mask its superclasses
from the Connection Inspector's pop-up list in Interface Builder,
since the subclass always includes the aspects and functionality
of its superclasses. For example, EOPopUpAssociation supersedes EOControlAssociation,
because EOPopUpAssociation is always more appropriate to use with
pop-up buttons.

__See Also:__  [associationClassesSuperseded](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwc43tn5rwsylunfxw4q3mmfzxgzltkn2xazlsonswizle) instance
method

---

### displayName

`public static String displayName()`

(com.apple.yellow.eointerface only) Returns
the name used by Interface Builder in the Connection Inspector's
pop-up list. EOAssociation's implementation simply returns the
name of the receiving class.

__See Also:__  [displayName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwi2ltobwgc6komfwwk) instance
method

---

### isUsableWithObject

`public static boolean isUsableWithObject(Object  aDisplayObject)`

(com.apple.yellow.eointerface only) Overridden
by subclasses to return true if instances of the receiving class
are usable with  _aDisplayObject,_ false if
they aren't. The receiving class can examine any relevant characteristic
of  _aDisplayObject_ -its class, configuration
(such as whether an NSMatrix operates in radio mode), and so on.

__See
Also:__  [isUsableWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxws42vonqwe3dfk5uxi2cpmjvgky3u) instance
method

---

### objectKeysTaken

`public static NSArray objectKeysTaken()`

(com.apple.yellow.eointerface only) Overridden
by subclasses to return the names of display object outlets that
instances assume control of, such as "target" and "delegate".
Interface Builder uses this information to disable connections from
these outlets in its Connections Inspector.

__See
Also:__  [objectKeysTaken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxw6ytkmvrxis3fpfzviyllmvxa) instance
method

---

### primaryAspect

`public static String primaryAspect()`

(com.apple.yellow.eointerface only) Overridden
by subclasses to return the default aspect, usually one denoting
the displayed value, which by convention is named "value". EOAssociation's implementation
returns null.

__See Also:__  [primaryAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxa4tjnvqxe6kbonygky3u) instance
method

---

## Instance Methods

---

### aspects

`public NSArray aspects()`

(com.apple.client.eointerface only) Overridden
by subclasses to return the names of the receiving class's aspects,
as string objects. Subclasses should include their superclass's
aspects and add their own when overriding this method.

__See
Also:__  [aspects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmfzxazldorzq) static
method

---

### aspectSignatures

`public NSArray aspectSignatures()`

(com.apple.client.eointerface only) Overridden
by subclasses to return the signatures of the receiver's aspects,
an array of string objects matching its aspects array index for
index. The signature strings can be any of:

|  |  |
| --- | --- |
| __Constant__ | __The Aspect Can Be Bound to__ |
| [AttributeAspectSignature](#apple-ijeugrkfi5fec) | Attributes |
| [AttributeToOneAspectSignature](#apple-ijeugq2ci5buo) | Attributes and to-one relationships |
| [AttributeToManyAspectSignature](#apple-ijeugr2iivauc) | Attributes and to-many relationships |
| [AttributeToOneToManyAspectSignature](#apple-ijeugq2bizcem) | Attributes, to-one relationships, and to-many relationships |
| [ToOneAspectSignature](#apple-ijeugqshifaus) | To-one relationships |
| [ToOneToManyAspectSignature](#apple-ijeugr2fi5duq) | To-one and to-many relationships |
| [ToManyAttributeSignature](#apple-ijeugrckifduc) | To-many relationships |
| [NullAspectSignature](#apple-ijeugrkdjbcum) | An EODisplayGroup without a key (the key is irrelevant). |

Interface Builder uses aspect signatures to enable
and disable keys in its Connections inspectors.

EOAssociation's
implementation of this method returns an array of `AttributeToOneToManyAspectSignature` strings.

__See
Also:__  [aspectSignatures](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmfzxazldorjwsz3omf2hk4tfom) static method

---

### associationClassesSuperseded

`public NSArray associationClassesSuperseded()`

(com.apple.client.eointerface only) Overridden
by subclasses to return the other EOAssociation classes that the
receiver supplants. This allows a subclass to mask its superclasses
from the Connection Inspector's pop-up list in Interface Builder,
since the subclass always includes the aspects and functionality
of its superclasses. For example, EOPopUpAssociation supersedes EOControlAssociation,
because EOPopUpAssociation is always more appropriate to use with
pop-up buttons.

__See Also:__  [associationClassesSuperseded](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmfzxg33dnfqxi2lpnzbwyyltonsxgu3vobsxe43fmrswi) static
method

---

### bindAspect

`public void bindAspect(
String  aspectName,
EODisplayGroup  aDisplayGroup,
String  key)`

Defines the receiver's link between its display
object and  _aDisplayGroup._  _aspectName_ is
the name of the aspect it observer in its display object, and  _key_ is
the name of the property it observes in  _aDisplayGroup._ Invoke [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) after
this method to finish setting up the binding. See ["Setting up an EOAssociation Programmatically"](EOAssociation-2.md#apple-infemqsfivbeq) in the class description for more information.

__See
Also:__  [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny)

---

### breakConnection

`public void breakConnection()`

Removes the receiver from its EODisplayGroup
and display object. Subclasses should override this method to remove
the receiver from any outlets of the display object and invoke `super`'s implementation
at the end.

__See Also:__  [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny)

---

### canBindAspect

`public boolean canBindAspect(
String  aspectName,
EODisplayGroup  aDisplayGroup,
String  key)`

Overridden by subclasses to return true if the
receiver can tie an aspect named  _aspectName_ from
its display object to the property identified by  _key_ in  _aDisplayGroup,_ false if
it can't.  _aspectName_ should name
an aspect supported by the receiver's class.

Interface Builder
uses this information to disable aspects in its Connections Inspector.
Subclasses can override this method to base their answers on other
binds already made, or on characteristics of the receiver's display
object or of  _aDisplayGroup._ EOAssociation's
implementation always returns true.

__See
Also:__  [localKeys](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc63dpmnqwys3fpfzq) (EODisplayGroup), `attributeKeys` (EOClassDescription), `toOneRelationshipKeys` (EOClassDescription), `toManyRelationshipKeys` (EOClassDescription)

---

### copyMatchingBindingsFromAssociation

`public void copyMatchingBindingsFromAssociation(EOAssociation  anAssociation)`

Duplicates the bindings of  _anAssociation_ in
the receiver. For each aspect of  _anAssociation_ that
has an EODisplayGroup, invokes [bindAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe2lomraxg4dfmn2a) with the EODisplayGroup
and key for that aspect.

---

### displayGroupForAspect

`public EODisplayGroup displayGroupForAspect(String  aspectName)`

Returns the EODisplayGroup bound to the receiver
for  _aspectName,_ or null if there's
no such object.

__See Also:__  [displayGroupKeyForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwi2ltobwgc6khojxxk4clmv4um33sifzxazldoq)

---

### displayGroupKeyForAspect

`public String displayGroupKeyForAspect(String  aspectName)`

Returns the EODisplayGroup key bound to the
receiver for  _aspectName,_ or null if
there's no EODisplayGroup.

__See Also:__  [displayGroupForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwi2ltobwgc6khojxxk4cgn5zec43qmvrxi)

---

### displayName

`public String displayName()`

(com.apple.client.eointerface only) Returns
the name used for display purposes. EOAssociation's implementation
simply returns the name of the receiver's class.

__See
Also:__  [displayName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmruxg4dmmf4u4ylnmu) static
method

---

### endEditing

`public boolean endEditing()`

Overridden by subclasses to pass the value of
the receiver's display object to the EODisplayGroup, by invoking [setValueForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5a) with
the display object's value and the appropriate aspect (typically "value").
Returns true if successful, false if not-specifically if [setValueForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5a) returns false.
The receiver should also send an `associationDidEndEditing:` message
to its EODisplayGroup.

Subclasses whose display objects immediately
pass their changes back to the EOAssociation-such as a button
or pop-up list-need not override this method. It's only needed
when the display object's value is edited rather than simply set.

EOAssociation's
implementation does nothing but return true.

---

### establishConnection

`public void establishConnection()`

Overridden by subclasses to attach the receiver
to the outlets of its display object, and to otherwise configure
the display object (such as by setting its action method). EOAssociation's
implementation subscribes the receiver as an observer of its EODisplayGroups.
Subclasses should invoke `super`'s implementation
after establishing their own connections.

See ["Setting up an EOAssociation Programmatically"](EOAssociation-2.md#apple-infemqsfivbeq) in the class description for more information.

__See
Also:__  [breakConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe4tfmfvug33onzswg5djn5xa)

---

### isEnabled

`protected boolean isEnabled()`

(com.apple.client.eointerface only) Returns `false` if
the receiver has explicitly disabled its display object or if the
receiver's `EnabledAspect` (if
bound) resolves to `false`; `true` otherwise.

---

### isEnabledAtIndex

`protected boolean isEnabledAtIndex(int  index)`

(com.apple.client.eointerface only) Returns `false` if
the receiver has explicitly disabled its display object or if the
receiver's `EnabledAspect` (if
bound) resolves to `false` for
index; `true` otherwise.

---

### isExplicitlyDisabled

`public boolean isExplicitlyDisabled()`

(com.apple.client.eointerface only) Returns `true` if
the receiver has explicitly disabled its display object, `false` otherwise.

---

### isUsableWithObject

`public boolean isUsableWithObject(Object  aDisplayObject)`

(com.apple.client.eointerface only) Overridden
by subclasses to return `true` if instances
of the receiving class are usable with  _aDisplayObject,_ `false` if
they aren't. The receiving class can examine any relevant characteristic
of  _aDisplayObject_ -its class, configuration,
and so on. EOAssociation's implementation returns `false`.

__See
Also:__  [isUsableWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpnfzvk43bmjwgkv3jorue6ytkmvrxi) static
method

---

### object

`public Object object()`

Returns the receiver's display object.

---

### objectKeysTaken

`public NSArray objectKeysTaken()`

(com.apple.client.eointerface only) Overridden
by subclasses to return the names of display object outlets that
instances assume control of. Interface Builder uses this information
to disable connections from these outlets in its Connections Inspector.

__See
Also:__  [objectKeysTaken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpn5rguzldorfwk6ltkrqwwzlo) static
method

---

### primaryAspect

`public String primaryAspect()`

(com.apple.client.eointerface only) Overridden
by subclasses to return the default aspect, usually one denoting
the displayed value, which by convention is named "value". EOAssociation's implementation
returns `null`.

__See
Also:__  [primaryAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpobzgs3lboj4uc43qmvrxi) static
method

---

### priority

`public int priority()`

Returns the receiver's change notification
priority. For more information, see the EODelayedObserver class
specification (EOControl).

---

### setAutoCreated

`public void setAutoCreated(boolean  aBoolean)`

(com.apple.client.eointerface only) This method
is provided for internal use and is intentionally undocumented.
You should never need to invoke or customize this method.

---

### setExplicitlyDisabled

`public void setExplicitlyDisabled(boolean  flag)`

(com.apple.client.eointerface only) Sets according
to  _flag_ whether or not the association
is explicitly disabled. This method and its counterpart [isExplicitlyDisabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxws42fpbygy2ldnf2gy6kenfzwcytmmvsa) are
used by objects in the com.apple.client.eoapplication and com.apple.client.eogeneration
packages for Direct to Java Client applications. An association
is "explicitly disabled" when the display object shouldn't
be editable, such as in the case where the display object simply
displays the results of a search.

---

### setValueForAspect

`public boolean setValueForAspect(
Object  value,
String  aspectName)`

Sets a value of the selected enterprise object
in the EODisplayGroup bound to  _aspectName._
Retrieves the display group and key bound to  _aspectName,_
and sends the display group a [setSelectedObjectValue](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gkzcpmjvgky3ukzqwy5lf) message
with  _value_ and the key as arguments.
Returns true if successful, or if there's no display group bound
to  _aspectName._ Returns false if there's
an display group and it doesn't accept the new value.

__See
Also:__  [valueForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxmylmovsum33sifzxazldoq)

---

### setValueForAspectAtIndex

`public boolean setValueForAspectAtIndex(
Object  value,
String  aspectName,
int  index)`

Sets a value of the enterprise object at  _index_ in
the EODisplayGroup bound to  _aspectName._
Retrieves the display group and key bound to  _aspectName,_
and sends the display group a [setValueForObjectAtIndex](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3dvmvdg64spmjvgky3uif2es3temv4a) message
with  _value,_  _index,_
and the key as arguments. Returns true if successful, or if there's
no display group bound to  _aspectName._
Returns false if there's a display group and it doesn't accept
the new value.

__See Also:__  [valueForAspectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxmylmovsum33sifzxazldoraxislomrsxq)

---

### shouldEndEditing

`public boolean shouldEndEditing(
String  aspectName,
String  inputString,
String  errorDescription)`

Invoked by subclasses when the display object
fails to validate its input, this method informs the EODisplayGroup
bound to  _aspectName_ with an [associationFailedToValidateValue](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63sgmfuwyzlekrxvmylmnfsgc5dfkzqwy5lf) message,
using the display group's selected object. Returns the result
of that message, or true if there's no display group.

For
example, an association bound to an NSControl object (Application
Kit) receives a controlDidFailToFormatStringErrorDescription delegate
message when the control's formatter fails to format the input
string. Its implementation of that method invokes `shouldEndEditing`.

__See
Also:__  [shouldEndEditingAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg2dpovwgirlomrcwi2lunfxgoqlujfxgizly)

---

### shouldEndEditingAtIndex

`public boolean shouldEndEditingAtIndex(
String  aspectName,
String  inputString,
String  errorDescription,
int  index)`

Works in the same manner as [shouldEndEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg2dpovwgirlomrcwi2lunfxgo),
but allows you to specify a particular object by  _index_ rather
than implicitly specifying the selected object.

---

### subjectChanged

`public void subjectChanged()`

Overridden by subclasses to update state based
when an EODisplayGroup's selection or contents changes. This method
is invoked automatically anytime a display group that's bound
to the receiver changes. The receiver can query its display group
with [selectionChanged](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5djn5xeg2dbnztwkza) and [contentsChanged](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6y3pnz2gk3tuonbwqylom5swi) messages to determine
how it needs to update.

---

### valueForAspect

`public Object valueForAspect(String  aspectName)`

Returns a value of the selected enterprise object
in the EODisplayGroup bound to  _aspectName._
Retrieves the display group and key bound to  _aspectName,_
and sends the display group a [selectedObjectValueForKey](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2fmylmovsum33sjnsxs) message
with the key. Returns null if there's no display group or key bound
to  _aspectName._

__See
Also:__  [setValueForAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5a)

---

### valueForAspectAtIndex

`public Object valueForAspectAtIndex(
String  aspectName,
int  index)`

Returns a value of the enterprise object at  _index_  in
the EODisplayGroup bound to  _aspectName._
Retrieves the display group and key bound to  _aspectName,_
and sends the display group a [valueForObjectAtIndex](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65tbnr2wkrtpojhwe2tfmn2ec5cjnzsgk6a) message
with  _index_ and the key. Returns null if
there's no display group or key bound to  _aspectName._

__See
Also:__  [setValueForAspectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5cborew4zdfpa)

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
