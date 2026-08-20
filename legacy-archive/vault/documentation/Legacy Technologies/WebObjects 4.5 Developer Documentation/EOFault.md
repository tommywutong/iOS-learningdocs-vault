---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOFault.html
archived_at: '2026-07-15T08:11:39.731974Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOFault

> **__Inherits
> from:__**
> : none (EOFault is a root class)

> __Declared in:__ : EOControl/EOFault.h

---

## Class Description

---

EOFault and EOFaultHandler form a general mechanism for substituting
placeholder objects that convert themselves into regular objects.
An EOFault is most commonly used by the Access Layer to represent
an object not yet fetched from the database, but that must nonetheless
exist as an instance in the application-typically because it's
the destination of a relationship. EOFault is a completely general class;
there's no need to create subclasses to customize fault handling.
Instead, you create subclasses of EOFaultHandler to accommodate
different means of converting faults into regular objects.

The faulting mechanism provides for continuity of an object's __id__ even
when that object's state isn't yet available. An EOFault simply
holds the place for an ultimate "real" object, handling all
methods that it can without causing the state to be loaded. When
an EOFault receives a message that it can't handle, it calls upon
its EOFaultHandler to _fire_ it, converting
it into a "real" object. This often involves accessing the external,
persistent state of the object.

## Creating an EOFault

Rather than allocating and initializing an EOFault, you turn
an existing object into one using EOFault's [makeObjectIntoFault:withHandler:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c63lbnnsu6ytkmvrxisloorxumylvnr2du53jorueqylomrwgk4r2) class
method. When you do so, you must provide an EOFaultHandler that
will later help the fault to fire. [makeObjectIntoFault:withHandler:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c63lbnnsu6ytkmvrxisloorxumylvnr2du53jorueqylomrwgk4r2) preserves
the __id__ of the original object, overlaying
its __isa__ pointer with that of the EOFault
class and slipping the EOFaultHandler among its instance variables.
Once this is done, the original object is an EOFault that will fire
when accessed.

The EOFaultHandler should be considered completely private
property of the EOFault once you've created it. You should neither
retain the EOFaultHandler or send it any other messages, instead
dealing exclusively with the newly created EOFault or the EOFault
class itself.

## EOFault Behavior

EOFault implements many basic object methods in a manner that
doesn't cause the receiver to fire. The following methods all
behave as though normal for the original object:

|  |  |
| --- | --- |
| [- retain](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpojsxiyljny) | [- isMemberOfClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpnfzu2zlnmjsxet3ginwgc43thi) |
| [- release](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpojswyzlbonsq) | [- conformsToProtocol:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmnxw4ztpojwxgvdpkbzg65dpmnxwyoq) |
| [- autorelease](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmf2xi33smvwgkyltmu) | [- isProxy](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpnfzva4tppb4q) |
| [- retainCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpojsxiyljnzbw65looq) | [- methodSignatureForSelector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpnvsxi2dpmrjwsz3omf2hk4tfizxxeu3fnrswg5dpoi5a) |
| [- class](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmnwgc43t) | [- respondsToSelector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpojsxg4dpnzshgvdpknswyzldorxxeoq) |
| [- superclass](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpon2xazlsmnwgc43t) | [- zone](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bppjxw4zi) |
| [- isKindOfClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpnfzuw2lomrhwmq3mmfzxgoq) | [- doesNotRecognizeSelector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrxwk42on52fezldn5tw42l2mvjwk3dfmn2g64r2) |

[doesNotRecognizeSelector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrxwk42on52fezldn5tw42l2mvjwk3dfmn2g64r2) is a special
case here, in that it's only invoked if the selector in question
isn't found for the original class. Normally, methods not implemented
by EOFault, but implemented by the original class, cause the receiver
to fire as described below.

These methods don't cause the receiver to fire, but also
don't hide the presence of the EOFault class:

|  |  |
| --- | --- |
| [- description](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrsxgy3snfyhi2lpny) | [- descriptionWithLocale:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrsxgy3snfyhi2lpnzlws5dijrxwgylmmu5a) |
| [- descriptionWithIndent:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrsxgy3snfyhi2lpnzlws5dijfxgizlooq5a) | [- descriptionWithLocale:indent:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrsxgy3snfyhi2lpnzlws5dijrxwgylmmu5gs3temvxhioq) |
| [- eoDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmvxuizltmnzgs4dunfxw4) | [- eoShallowDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmvxvg2dbnrwg652emvzwg4tjob2gs33o) |

The following common methods, along with any others not explicitly
mentioned in this section, do cause the receiving EOFault to fire.

- [- dealloc](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrswc3dmn5rq)
- [- self](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bponswyzq)
- [- forwardInvocation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmzxxe53bojses3twn5rwc5djn5xdu)

When an EOFault receives one of these messages, it fires in
one of a few different ways. [dealloc](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrswc3dmn5rq) invokes the [- clearFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c6y3mmvqxertbovwhioq) class
method to revert the receiver back to its original state, then reinvokes __dealloc__ to
clean up instance variables and deallocate the object. The other
methods all send a special message, [completeInitializationOfObject:](EOFaultHandler-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33nobwgk5dfjfxgs5djmfwgs6tboruw63spmzhwe2tfmn2du),
to the EOFaultHandler to transform the EOFault into a regular object,
possibly different from its original state. In addition, [forwardInvocation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmzxxe53bojses3twn5rwc5djn5xdu) sends
a __shouldPerformInvocation:__ to the EOFaultHandler
first, which allows it to perform the method itself without causing
the EOFault to be transformed. If the EOFaultHandler returns YES,
though, the EOFault then sends it a __completeInitializationOfObject:__ message.

## Examining an EOFault

Three additional EOFault methods allow you to explicitly check
whether an object is an EOFault without causing it to fire, and
to get its original class and EOFaultHandler if it is an EOFault.
These methods are:

- [+ isFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c62ltizqxk3duhi)
- [+ targetClassForFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c65dbojtwk5cdnrqxg42gn5zemylvnr2du)
- [+ handlerForFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c62dbnzsgyzlsizxxertbovwhioq)

You can use these methods to base some decisions on whether
an object is an EOFault, though you should rarely need to do so.

## Method Types

---

> **Creating and examining
> faults**
> : [+ makeObjectIntoFault:withHandler:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c63lbnnsu6ytkmvrxisloorxumylvnr2du53jorueqylomrwgk4r2)
> : [+ isFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c62ltizqxk3duhi)
> : [+ clearFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c6y3mmvqxertbovwhioq)
> : [+ handlerForFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c62dbnzsgyzlsizxxertbovwhioq)
> : [+ targetClassForFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c65dbojtwk5cdnrqxg42gn5zemylvnr2du)
> : [+ respondsToSelector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpojsxg4dpnzshgvdpknswyzldorxxeoq)
>
> **Checking class information**
> : [- class](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmnwgc43t)
> : [- isKindOfClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpnfzuw2lomrhwmq3mmfzxgoq)
> : [- isMemberOfClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpnfzu2zlnmjsxet3ginwgc43thi)
> : [- respondsToSelector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpojsxg4dpnzshgvdpknswyzldorxxeoq)
> : [- conformsToProtocol:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmnxw4ztpojwxgvdpkbzg65dpmnxwyoq)
> : [- methodSignatureForSelector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpnvsxi2dpmrjwsz3omf2hk4tfizxxeu3fnrswg5dpoi5a)
>
> **Run-time support**
> : [- forwardInvocation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmzxxe53bojses3twn5rwc5djn5xdu)
> : [- doesNotRecognizeSelector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrxwk42on52fezldn5tw42l2mvjwk3dfmn2g64r2)
>
> **Getting a fault's description**
> : [- description](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrsxgy3snfyhi2lpny)
> : [- descriptionWithIndent:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrsxgy3snfyhi2lpnzlws5dijfxgizlooq5a)
> : [- descriptionWithLocale:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrsxgy3snfyhi2lpnzlws5dijrxwgylmmu5a)
> : [- descriptionWithLocale:indent:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrsxgy3snfyhi2lpnzlws5dijrxwgylmmu5gs3temvxhioq)
> : [- eoDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmvxuizltmnzgs4dunfxw4)
> : [- eoShallowDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmvxvg2dbnrwg652emvzwg4tjob2gs33o)
>
> **Reference-counting**
> : [- retain](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpojsxiyljny)
> : [- release](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpojswyzlbonsq)
> : [- retainCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpojsxiyljnzbw65looq)
> : [- autorelease](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmf2xi33smvwgkyltmu)
> : [- dealloc](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrswc3dmn5rq)
>
> **Miscellaneous object
> methods**
> : [- self](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bponswyzq)
> : [- isProxy](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpnfzva4tppb4q)
> : [- superclass](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpon2xazlsmnwgc43t)
> : [- zone](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bppjxw4zi)

## Class Methods

---

### clearFault:

`+ (void)clearFault:(id)aFault`

Restores _aFault_ to
its status prior to the __makeObjectIntoFault:withHandler:__ message
that created it. Raises an NSInvalidArgumentException if _aFault_ isn't
an EOFault.

You rarely use this method. Faults typically fire
automatically when accessed, using EOFaultHandler's [completeInitializationOfObject:](EOFaultHandler-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33nobwgk5dfjfxgs5djmfwgs6tboruw63spmzhwe2tfmn2du) method.
See the EOFaultHandler class specification for more information.

---

### handlerForFault:

`+ (EOFaultHandler *)handlerForFault:(id)aFault`

Returns the EOFaultHandler that will help _aFault_ to
fire. Returns __nil__ if _aFault_ isn't
an EOFault.

---

### isFault:

`+ (BOOL)isFault:(id)anObject`

Returns `YES` if _anObject_ is
an EOFault, `NO` otherwise.

---

### makeObjectIntoFault:withHandler:

`+ (void)makeObjectIntoFault:(id)anObject
withHandler:(EOFaultHandler *)aFaultHandler`

Converts _anObject_ into
an EOFault, assigning _aFaultHandler_ as
the object that stores its original state and later converts the
EOFault back into a normal object (typically by fetching data from
an external repository). The new EOFault becomes the owner of _aFaultHandler_;
you shouldn't assign it to another object.

---

### respondsToSelector:

`+ (BOOL)respondsToSelector:(SEL)aSelector`

Returns `YES` if
the receiving class responds to _aSelector_, `NO` otherwise.

---

### targetClassForFault:

`+ (Class)targetClassForFault:(id)aFault`

Returns the original class of the object that
was turned into _aFault_, or __nil__ if _aFault_ isn't
an EOFault. When the EOFault fires, it's guaranteed to be an instance
of this class or possibly of a subclass. To get the actual class,
you must send a [class](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmnwgc43t) message
to the EOFault, which may fire to determine its actual class membership.

---

## Instance Methods

---

### autorelease

`- (id)autorelease`

Performs as NSObject's __autorelease__ method.

---

### class

`- (Class)class`

Returns the class of the object that the receiving
EOFault will become. This may cause the EOFault to fire in order
to determine its actual class membership.

__See
Also:__  [- classForFault:](EOFaultHandler-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg3dbonzum33sizqxk3duhi) (EOFaultHandler), [+ targetClassForFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c65dbojtwk5cdnrqxg42gn5zemylvnr2du)

---

### conformsToProtocol:

`- (BOOL)conformsToProtocol:(Protocol
*)aProtocol`

Returns `YES` if
the object that the receiving EOFault will become conforms to _aProtocol_, `NO` if
it doesn't. This may cause the EOFault to fire in order to determine
its actual class membership.

__See Also:__  [- conformsToProtocol:forFault:](EOFaultHandler-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33omzxxe3ltkrxva4tporxwg33mhjtg64sgmf2wy5b2) (EOFaultHandler)

---

### dealloc

`- (void)dealloc`

Invokes the [clearFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c6y3mmvqxertbovwhioq) class method to revert
the receiving EOFault to its original class membership and state,
then reinvokes __dealloc__.

---

### description

`- (NSString *)description`

Sends [descriptionForObject:](EOFaultHandler-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwizltmnzgs4dunfxw4rtpojhwe2tfmn2du) to
the receiver's EOFaultHandler and returns the result.

---

### descriptionWithIndent:

`- (NSString *)descriptionWithIndent:(unsigned
int)indentLevel`

Invokes [description](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrsxgy3snfyhi2lpny) and returns the result.

---

### descriptionWithLocale:

`- (NSString *)descriptionWithLocale:(NSDictionary
*)locale`

Invokes [description](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrsxgy3snfyhi2lpny) and returns the result.

---

### descriptionWithLocale:indent:

`- (NSString *)descriptionWithLocale:(NSDictionary
*)locale
indent:(unsigned int)indentLevel`

Invokes [description](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrsxgy3snfyhi2lpny) and returns the result.

---

### doesNotRecognizeSelector:

`- (void)doesNotRecognizeSelector:(SEL)aSelector`

Raises an NSInvalidArgumentException.

---

### eoDescription

`- (NSString *)eoDescription`

Invokes [description](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrsxgy3snfyhi2lpny) and returns the result.

__See
Also:__  [- eoDescription](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sw6rdfonrxe2lqoruw63q) ( [EOEnterpriseObject](EOEnterpriseObject-3.md#apple-ijaueqsdjbfeq))

---

### eoShallowDescription

`- (NSString *)eoShallowDescription`

Invokes [description](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpmrsxgy3snfyhi2lpny) and returns the result.

__See
Also:__  [- eoShallowDescription](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5sw6u3imfwgy33xirsxgy3snfyhi2lpny) ( [EOEnterpriseObject](EOEnterpriseObject-3.md#apple-ijaueqsdjbfeq))

---

### forwardInvocation:

`- (void)forwardInvocation:(NSInvocation
*)anInvocation`

Causes the receiving EOFault to fire, if allowed
by its EOFaultHandler, and forward _anInvocation_ to
its new incarnation. Sends a [shouldPerformInvocation:](EOFaultHandler-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixxg2dpovwgiudfojtg64tnjfxhm33dmf2gs33ohi) to
the receiver's EOFaultHandler first, giving it a chance to bypass
the conversion. If the EOFaultHandler returns `NO`,
returns immediately. If it returns `YES`,
sends a [completeInitializationOfObject:](EOFaultHandler-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33nobwgk5dfjfxgs5djmfwgs6tboruw63spmzhwe2tfmn2du) message
to the EOFaultHandler with __self__ as the argument.
Once the receiver has fired it invokes _anInvocation_.

---

### isKindOfClass:

`- (BOOL)isKindOfClass:(Class)aClass`

Returns `YES` if _aClass_ is
the class, or a superclass, of the object that the receiving EOFault
will become, `NO` otherwise.
This may cause the EOFault to fire in order to determine its actual
class membership.

__See Also:__  [- isMemberOfClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpnfzu2zlnmjsxet3ginwgc43thi), [- isKindOfClass:forFault:](EOFaultHandler-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixws42lnfxgit3ginwgc43thjtg64sgmf2wy5b2) (EOFaultHandler)

---

### isMemberOfClass:

`- (BOOL)isMemberOfClass:(Class)aClass`

Returns `YES` if _aClass_ is
the class of the object that the receiving EOFault will become, `NO` otherwise.
This may cause the EOFault to fire in order to determine its actual
class membership.

__See Also:__  [- isKindOfClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpnfzuw2lomrhwmq3mmfzxgoq), [- isMemberOfClass:forFault:](EOFaultHandler-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixws42nmvwwezlsj5teg3dbonztuztpojdgc5lmoq5a) (EOFaultHandler)

---

### isProxy

`- (BOOL)isProxy`

Returns `NO`.

---

### methodSignatureForSelector:

`- (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector`

Returns a method signature for _aSelector_ for
the object that the receiving EOFault will become, or __nil__ if
one can't be found. This may cause the EOFault to fire in order
to determine its actual class membership.

__See
Also:__  [- methodSignatureForSelector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5bpnvsxi2dpmrjwsz3omf2hk4tfizxxeu3fnrswg5dpoi5a) (EOFaultHandler)

---

### release

`- (void)release`

Performs as NSObject's __release__ method.

---

### respondsToSelector:

`- (BOOL)respondsToSelector:(SEL)aSelector`

Returns `YES` if
the object that the receiving EOFault will become responds to _aSelector_, `NO` otherwise. This
may cause the EOFault to fire in order to determine its actual class
membership.

__See Also:__  [- respondsToSelector:forFault:](EOFaultHandler-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixxezltobxw4zdtkrxvgzlmmvrxi33shjtg64sgmf2wy5b2) (EOFaultHandler)

---

### retain

`- (id)retain`

Performs as NSObject's __retain__ method.

---

### retainCount

`- (unsigned int)retainCount`

Performs as NSObject's __retainCount__ method.

---

### self

`- (id)self`

Fires the receiver and returns `self`.
This is the recommended way to simply fire an EOFault.

---

### superclass

`- (Class)superclass`

Returns the superclass of the object that the
receiving EOFault will become. This may cause the EOFault to fire
in order to determine its actual class membership.

__See
Also:__  [- classForFault:](EOFaultHandler-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg3dbonzum33sizqxk3duhi) ( [EOFaultHandler](EOFaultHandler-2.md#apple-ivhumylvnr2eqylomrwgk4q))

---

### zone

`- (NSZone *)zone`

Performs as NSObject's `zone` method.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
