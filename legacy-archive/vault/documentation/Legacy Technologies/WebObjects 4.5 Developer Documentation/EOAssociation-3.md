---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOAssociation.html
archived_at: '2026-07-15T08:11:45.351120Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOAssociation

> **__Inherits
> from:__**
> : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOAssociation.h

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
  (such as __value__ and __enabled__)
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

|  |  |
| --- | --- |
| [EOActionAssociation](EOActionAssociation.md#apple-ivhucy3unfxw4qltonxwg2lboruw63q) | [EOActionCellAssociation](EOActionCellAssociation-2.md#apple-ivhucy3unfxw4q3fnrwec43tn5rwsylunfxw4) |
| [EOActionInsertionAssociation](EOActionInsertionAssociation-2.md#apple-ivhucy3unfxw4sloonsxe5djn5xec43tn5rwsylunfxw4) | [EOColumnAssociation](EOColumnAssociation.md#apple-ivhug33movww4qltonxwg2lboruw63q) |
| [EOComboBoxAssociation](EOComboBoxAssociation-2.md#apple-ivhug33nmjxue33yifzxg33dnfqxi2lpny) | [EOControlAssociation](EOControlAssociation-2.md#apple-ivhug33oorzg63cbonzw6y3jmf2gs33o) |
| [EODetailSelectionAssociation](EODetailSelectionAssociation-2.md#apple-ivhuizlumfuwyu3fnrswg5djn5xec43tn5rwsylunfxw4) | [EOGenericControlAssociation](EOGenericControlAssociation-2.md#apple-ivhuozlomvzgsy2dn5xhi4tpnraxg43pmnuwc5djn5xa) |
| [EOMasterCopyAssociation](EOMasterCopyAssociation-2.md#apple-ivhu2yltorsxeq3pob4uc43tn5rwsylunfxw4) | [EOMasterDetailAssociation](EOMasterDetailAssociation.md#apple-ivhu2yltorsxerdforqws3cbonzw6y3jmf2gs33o) |
| [EOMasterPeerAssociation](EOMasterPeerAssociation-2.md#apple-ivhu2yltorsxeudfmvzec43tn5rwsylunfxw4) | [EOMatrixAssociation](EOMatrixAssociation.md#apple-ivhu2yluojuxqqltonxwg2lboruw63q) |
| [EOPickTextAssociation](EOPickTextAssociation-2.md#apple-ivhva2ldnnkgk6duifzxg33dnfqxi2lpny) | [EOPopUpAssociation](EOPopUpAssociation-2.md#apple-ivhva33qkvyec43tn5rwsylunfxw4) |
| [EORadioMatrixAssociation](EORadioMatrixAssociation-2.md#apple-ivhveylenfxu2yluojuxqqltonxwg2lboruw63q) | [EORecursiveBrowserAssociation](EORecursiveBrowserAssociation-2.md#apple-ivhvezldovzhg2lwmvbhe33xonsxeqltonxwg2lboruw63q) |
| [EOTableViewAssociation](EOTableViewAssociation-2.md#apple-ivhviylcnrsvm2lfo5axg43pmnuwc5djn5xa) | [EOTextAssociation](EOTextAssociation-2.md#apple-ivhvizlyoraxg43pmnuwc5djn5xa) |

You normally set up EOAssociations using Interface Builder;
each of the class specifications for EOAssociation's subclasses
provide an example using Interface Builder to set them up. EOAssociation's
programmatic interface is more important when defining custom EOAssociation subclasses.
For more information on EOAssociations, see the sections:

- ["How EOAssociations Work"](EOAssociation-4.md#apple-infemrcdivbuc)
- ["Setting up an EOAssociation Programmatically"](EOAssociation-4.md#apple-infemqsfivbeq)
- ["Creating a Subclass of EOAssociation"](EOAssociation-4.md#apple-infemqsiirdek)

## Adopted Protocols

---

> NSCoding: __- encodeWithCoder:__
> : __- initWithCoder:__

## Method Types

---

> **Declaring capabilities**
> : [+ aspects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3bonygky3uom)
> : [+ aspectSignatures](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3bonygky3uknuwo3tbor2xezlt)
> : [+ objectKeysTaken](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3pmjvgky3ujnsxs42umfvwk3q) (Yellow
> Box)
> : [+ isUsableWithObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3jonkxgylcnrsvo2lunbhwe2tfmn2du)
> : [+ associationClassesSuperseded](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3bonzw6y3jmf2gs33oinwgc43tmvzvg5lqmvzhgzlemvsa)
> : [+ displayName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3enfzxa3dbpfhgc3lf)
> : [+ primaryAspect](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3qojuw2ylspfaxg4dfmn2a)
> : [- canBindAspect:displayGroup:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5rwc3scnfxgiqltobswg5b2mruxg4dmmf4uo4tpovydu23fpe5a)
>
> **Getting all possible
> EOAssociations for a display object**
> : [+ associationClassesForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3bonzw6y3jmf2gs33oinwgc43tmvzum33sj5rguzldoq5a)
>
> **Creating and configuring
> instances**
> : [- initWithObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5uw42luk5uxi2cpmjvgky3uhi)
> : [- bindAspect:displayGroup:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5rgs3teifzxazldoq5gi2ltobwgc6khojxxk4b2nnsxsoq)
> : [- establishConnection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sxg5dbmjwgs43iinxw43tfmn2gs33o)
> : [- breakConnection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5rhezlbnnbw63tomvrxi2lpny)
> : [- copyMatchingBindingsFromAssociation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5rw64dzjvqxiy3infxgoqtjnzsgs3thondhe33nifzxg33dnfqxi2lpny5a)
>
> **Getting the display object**
> : [- object](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5xwe2tfmn2a)
>
> **Examining bindings**
> : [- displayGroupForAspect:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sgs43qnrqxsr3sn52xartpojaxg4dfmn2du)
> : [- displayGroupKeyForAspect:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sgs43qnrqxsr3sn52xas3fpfdg64sbonygky3uhi)
>
> **Updating values**
> : [- subjectChanged](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zxkytkmvrxiq3imfxgozle)
> : [- endEditing](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sw4zcfmruxi2lom4)
>
> **Accessing enterprise
> object values**
> : [- setValue:forAspect:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwk5cwmfwhkzj2mzxxeqltobswg5b2)
> : [- setValue:forAspect:atIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwk5cwmfwhkzj2mzxxeqltobswg5b2mf2es3temv4du)
> : [- valueForAspect:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of53gc3dvmvdg64sbonygky3uhi)
> : [- valueForAspect:atIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of53gc3dvmvdg64sbonygky3uhjqxislomrsxqoq)
>
> **Handling validation errors**
> : [- shouldEndEditingForAspect:invalidInput:errorDescription:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwq33vnrsek3teivsgs5djnztum33sifzxazldoq5gs3twmfwgszcjnzyhk5b2mvzhe33sirsxgy3snfyhi2lpny5a)
> : [- shouldEndEditingForAspect:invalidInput:errorDescription:index:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwq33vnrsek3teivsgs5djnztum33sifzxazldoq5gs3twmfwgszcjnzyhk5b2mvzhe33sirsxgy3snfyhi2lpny5gs3temv4du)

## Constructors

---

## Class Methods

---

### aspects

`+ (NSArray *)aspects`

Overridden by subclasses to return the
names of the receiving class's aspects as an array of string objects.
Subclasses should include their superclass's aspects and add their
own when overriding this method.

---

### aspectSignatures

`+ (NSArray *)aspectSignatures`

Overridden by subclasses to return the signatures
of the receiver's aspects, an array of string objects matching
its aspects array index for index. Each signature string can contain
the following characters:

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

---

### associationClassesForObject:

`+ (NSArray *)associationClassesForObject:(id)aDisplayObject`

Returns the subclasses of EOAssociation
usable with _aDisplayObject_. Sends [isUsableWithObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3jonkxgylcnrsvo2lunbhwe2tfmn2du) to every
loaded subclass of EOAssociation, adding those that respond YES to
the array. Subclasses shouldn't override this method; override __isUsableWithObject:__ instead.

---

### associationClassesSuperseded

`+ (NSArray *)associationClassesSuperseded`

Overridden by subclasses to return the
other EOAssociation classes that the receiver supplants. This allows
a subclass to mask its superclasses from the Connection Inspector's
pop-up list in Interface Builder, since the subclass always includes
the aspects and functionality of its superclasses. For example,
EOPopUpAssociation supersedes EOControlAssociation, because EOPopUpAssociation
is always more appropriate to use with pop-up buttons.

---

### displayName

`+ (NSString *)displayName`

Returns the name used by Interface Builder
in the Connection Inspector's pop-up list. EOAssociation's implementation
simply returns the name of the receiving class.

---

### isUsableWithObject:

`+ (BOOL)isUsableWithObject:(id)aDisplayObject`

Overridden by subclasses to return YES if
instances of the receiving class are usable with _aDisplayObject_, NO if
they aren't. The receiving class can examine any relevant characteristic
of _aDisplayObject_-its class, configuration
(such as whether an NSMatrix operates in radio mode), and so on.

---

### objectKeysTaken

`+ (NSArray *)objectKeysTaken`

Overridden by subclasses to return the
names of display object outlets that instances assume control of, such
as "target" and "delegate". Interface Builder uses this
information to disable connections from these outlets in its Connections
Inspector.

---

### primaryAspect

`+ (NSString *)primaryAspect`

Overridden by subclasses to return the
default aspect, usually one denoting the displayed value, which by
convention is named "value". EOAssociation's implementation
returns nil.

---

## Instance Methods

---

### bindAspect:displayGroup:key:

`- (void)bindAspect:(NSString
*)aspectName
displayGroup:(EODisplayGroup *)aDisplayGroup
key:(NSString *)key`

Defines the receiver's link between its display
object and _aDisplayGroup_. _aspectName_ is
the name of the aspect it observer in its display object, and _key_ is
the name of the property it observes in _aDisplayGroup_. Invoke [establishConnection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sxg5dbmjwgs43iinxw43tfmn2gs33o) after
this method to finish setting up the binding. See ["Setting up an EOAssociation Programmatically"](EOAssociation-4.md#apple-infemqsfivbeq) in
the class description for more information.

__See
Also:__  [- initWithObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5uw42luk5uxi2cpmjvgky3uhi), [- establishConnection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sxg5dbmjwgs43iinxw43tfmn2gs33o)

---

### breakConnection

`- (void)breakConnection`

Removes the receiver from its EODisplayGroup
and display object. This causes it to be released, so be sure to
retain the EOAssociation before invoking this method if you want
to keep it for another use. Subclasses should override this method
to remove the receiver from any outlets of the display object, such
as target or delegate, and invoke __super__'s
implementation at the end.

__See Also:__  [- establishConnection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sxg5dbmjwgs43iinxw43tfmn2gs33o)

---

### canBindAspect:displayGroup:key:

`- (BOOL)canBindAspect:(NSString
*)aspectName
displayGroup:(EODisplayGroup *)aDisplayGroup
key:(NSString *)key`

Overridden by subclasses to return YES if the
receiver can tie an aspect named _aspectName_ from
its display object to the property identified by _key_ in _aDisplayGroup_, NO if
it can't. _aspectName_ should name an
aspect supported by the receiver's class.

Interface Builder
uses this information to disable aspects in its Connections Inspector.
Subclasses can override this method to base their answers on other
binds already made, or on characteristics of the receiver's display
object or of _aDisplayGroup_. EOAssociation's
implementation always returns YES.

__See
Also:__  [- localKeys](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwy33dmfwewzlzom) (EODisplayGroup), __-__ __attributeKeys__ (EOClassDescription), __-__ __toOneRelationshipKeys__ (EOClassDescription), __-__ __toManyRelationshipKeys__ (EOClassDescription)

---

### copyMatchingBindingsFromAssociation:

`- (void)copyMatchingBindingsFromAssociation:(EOAssociation
*)anAssociation`

Duplicates the bindings of _anAssociation_ in
the receiver. For each aspect of _anAssociation_ that
has an EODisplayGroup, invokes [bindAspect:displayGroup:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5rgs3teifzxazldoq5gi2ltobwgc6khojxxk4b2nnsxsoq) with
the EODisplayGroup and key for that aspect.

---

### displayGroupForAspect:

`- (EODisplayGroup *)displayGroupForAspect:(NSString
*)aspectName`

Returns the EODisplayGroup bound to the receiver
for _aspectName_, or nil if there's
no such object.

__See Also:__  [- displayGroupKeyForAspect:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sgs43qnrqxsr3sn52xas3fpfdg64sbonygky3uhi)

---

### displayGroupKeyForAspect:

`- (NSString *)displayGroupKeyForAspect:(NSString
*)aspectName`

Returns the EODisplayGroup key bound to the
receiver for _aspectName_, or nil if
there's no EODisplayGroup.

__See Also:__  [- displayGroupForAspect:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sgs43qnrqxsr3sn52xartpojaxg4dfmn2du)

---

### endEditing

`- (BOOL)endEditing`

Overridden by subclasses to pass the value of
the receiver's display object to the EODisplayGroup, by invoking [setValue:forAspect:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwk5cwmfwhkzj2mzxxeqltobswg5b2) with
the display object's value and the appropriate aspect (typically "value").
Returns YES if successful, NO if not-specifically if [setValue:forAspect:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwk5cwmfwhkzj2mzxxeqltobswg5b2) returns NO.
The receiver should also send an __associationDidEndEditing:__ message
to its EODisplayGroup.

Subclasses whose display objects immediately
pass their changes back to the EOAssociation-such as a button
or pop-up list-need not override this method. It's only needed
when the display object's value is edited rather than simply set.

EOAssociation's
implementation does nothing but return YES.

---

### establishConnection

`- (void)establishConnection`

Overridden by subclasses to attach the receiver
to the outlets of its display object, and to otherwise configure
the display object (such as by setting its action method). EOAssociation's
implementation subscribes the receiver as an observer of its EODisplayGroups and
causes the display object to retain the receiver. Subclasses should
invoke __super__'s implementation after establishing
their own connections.

See ["Setting up an EOAssociation Programmatically"](EOAssociation-4.md#apple-infemqsfivbeq) in
the class description for more information.

__See
Also:__  [- breakConnection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5rhezlbnnbw63tomvrxi2lpny)

---

### initWithObject:

`- (id)initWithObject:(id)aDisplayObject`

Initializes the receiver to monitor and update
the value in _aDisplayObject_, which
is typically a user-interface object or an EODisplayGroup. This
is the designated initializer for the EOAssociation class. Returns __self__.

Because
of the way that EOAssociations are set up, this method doesn't
retain _aDisplayObject_. See ["Setting up an EOAssociation Programmatically"](EOAssociation-4.md#apple-infemqsfivbeq) in
the class description for more information.

__See
Also:__  [- bindAspect:displayGroup:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5rgs3teifzxazldoq5gi2ltobwgc6khojxxk4b2nnsxsoq), [- establishConnection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sxg5dbmjwgs43iinxw43tfmn2gs33o)

---

### object

`- (id)object`

Returns the receiver's display object.

__See
Also:__  [- initWithObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5uw42luk5uxi2cpmjvgky3uhi)

---

### setValue:forAspect:

`- (BOOL)setValue:(id)value
forAspect:(NSString *)aspectName`

Sets a value of the selected enterprise object
in the EODisplayGroup bound to _aspectName_.
Retrieves the display group and key bound to _aspectName_,
and sends the display group a [setSelectedObjectValue:forKey:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldorswit3cnjswg5cwmfwhkzj2mzxxes3fpe5a) message
with _value_ and the key as arguments.
Returns YES if successful, or if there's no display group bound
to _aspectName_. Returns NO if there's
an display group and it doesn't accept the new value.

__See
Also:__  [- valueForAspect:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of53gc3dvmvdg64sbonygky3uhi)

---

### setValue:forAspect:atIndex:

`- (BOOL)setValue:(id)value
forAspect:(NSString *)aspectName
atIndex:(unsigned int)index`

Sets a value of the enterprise object at _index_ in
the EODisplayGroup bound to _aspectName_.
Retrieves the display group and key bound to _aspectName_,
and sends the display group a [setValue:forObjectAtIndex:key:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy5lfhjtg64spmjvgky3uif2es3temv4du23fpe5a) message
with _value_, _index_,
and the key as arguments. Returns YES if successful, or if there's
no display group bound to _aspectName_.
Returns NO if there's a display group and it doesn't accept
the new value.

__See Also:__  [- valueForAspect:atIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of53gc3dvmvdg64sbonygky3uhjqxislomrsxqoq)

---

### shouldEndEditingForAspect:invalidInput:errorDescription:

`- (BOOL)shouldEndEditingForAspect:(NSString
*)aspectName
invalidInput:(NSString *)inputString
errorDescription:(NSString *)errorDescription`

Invoked by subclasses when the display object
fails to validate its input, this method informs the EODisplayGroup
bound to _aspectName_ with an [association:failedToValidateValue:forKey:object:errorDescription:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4otgmfuwyzlekrxvmylmnfsgc5dfkzqwy5lfhjtg64slmv4tu33cnjswg5b2mvzhe33sirsxgy3snfyhi2lpny5a) message,
using the display group's selected object. Returns the result
of that message, or YES if there's no display group.

For
example, an association bound to an NSControl object (Application
Kit) receives a control:didFailToFormatString:errorDescription: delegate
message when the control's formatter fails to format the input
string. Its implementation of that method invokes __shouldEndEditingForAspect:invalidInput:errorDescription:__.

__See
Also:__  [- shouldEndEditingForAspect:invalidInput:errorDescription:index:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwq33vnrsek3teivsgs5djnztum33sifzxazldoq5gs3twmfwgszcjnzyhk5b2mvzhe33sirsxgy3snfyhi2lpny5gs3temv4du)

---

### shouldEndEditingForAspect:invalidInput:errorDescription:index:

`- (BOOL)shouldEndEditingForAspect:(NSString
*)aspectName
invalidInput:(NSString *)inputString
errorDescription:(NSString *)errorDescription
index:(unsigned int)index`

Works in the same manner as [shouldEndEditingForAspect:invalidInput:errorDescription:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwq33vnrsek3teivsgs5djnztum33sifzxazldoq5gs3twmfwgszcjnzyhk5b2mvzhe33sirsxgy3snfyhi2lpny5a),
but allows you to specify a particular object by _index_ rather
than implicitly specifying the selected object.

---

### subjectChanged

`- (void)subjectChanged`

Overridden by subclasses to update state based
when an EODisplayGroup's selection or contents changes. This method
is invoked automatically anytime a display group that's bound
to the receiver changes. The receiver can query its display group
with [selectionChanged](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxi2lpnzbwqylom5swi) and [contentsChanged](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwg33oorsw45dtinugc3thmvsa) messages to determine
how it needs to update.

---

### valueForAspect:

`- (id)valueForAspect:(NSString
*)aspectName`

Returns a value of the selected enterprise object
in the EODisplayGroup bound to _aspectName_.
Retrieves the display group and key bound to _aspectName_,
and sends the display group a [selectedObjectValueForKey:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldorlgc3dvmvdg64slmv4tu) message
with the key. Returns nil if there's no display group or key bound
to _aspectName_.

__See
Also:__  [- setValue:forAspect:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwk5cwmfwhkzj2mzxxeqltobswg5b2)

---

### valueForAspect:atIndex:

`- (id)valueForAspect:(NSString
*)aspectName
atIndex:(unsigned int)index`

Returns a value of the enterprise object at _index_ in
the EODisplayGroup bound to _aspectName_.
Retrieves the display group and key bound to _aspectName_,
and sends the display group a [valueForObjectAtIndex:key:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxmylmovsum33sj5rguzldoraxislomrsxqotlmv4tu) message
with _index_ and the key. Returns nil if
there's no display group or key bound to _aspectName_.

__See
Also:__  [- setValue:forAspect:atIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwk5cwmfwhkzj2mzxxeqltobswg5b2mf2es3temv4du)

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
