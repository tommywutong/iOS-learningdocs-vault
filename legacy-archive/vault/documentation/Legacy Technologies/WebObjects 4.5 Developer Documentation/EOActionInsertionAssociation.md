---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOActionInsertionAssoc.html
archived_at: '2026-07-15T08:11:44.539475Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOActionInsertionAssociation

> **__Inherits
> from:__**
> : [(com.apple.client.eointerface)
> EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) :
> EODelayedObserver (EOControl) :
> Object
> (com.apple.yellow.eointerface)
> EOAssociation :
> EODelayedObserver (EOControl) :
> NSObject

> **__Implements:__**
> : EOObserving (EODelayedObserver)
> : (com.apple.client.eointerface only) java.awt.event.ActionListener
> : (com.apple.client.eointerface only) NSDisposable (EOAssociation)

> **__Package:__**
> : com.apple.client.eointerface
> : com.apple.yellow.eointerface

---

## Class Description

---

An EOActionInsertionAssociation object inserts objects from
one display group into another.

|  |
| --- |
| __Usable With__ |
| (com.apple.client.eointerface) Any object that implements the method `addActionListener` (javax.swing.JButton and javax.swing.JMenuItem, for example)   (com.apple.yellow.eointerface) Any object that responds to `setAction`, typically an NSControl |

|  |
| --- |
| __Aspects__ |
| source | Bound to the EODisplayGroup containing objects to insert. This aspect doesn't use a key. |
| destination | A relationship of the selected object into which objects from the source EODisplayGroup are inserted. Usually bound to a different EODisplayGroup than `source`. |
| enabled | A boolean attribute of the selected object (usually in the destination EODisplayGroup), which determines whether the NSControl is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| target | On receiving an action message from the display object, an EOActionInsertionAssociation inserts objects from the source EODisplayGroup into the destination EODisplayGroup. |

## Example

Suppose an application shows Talent in one display group and
Movies in another. You want a user to be able to select a talent,
select a movie, and then click an Assign Director button that assigns
the selected talent as one of the movie's directors. To do this,
in Interface Builder, control-drag a connection from the button
to the Talent display group. Select EOActionInsertionAssociation
in the Connections inspector, and double-click the association's `source` aspect,
binding it to the Talent display group. Similarly, control-drag
a connection from the button to the Movie display group. Select EOActionAssociation
in the Connections inspector, and bind the association's `destination` aspect
to the "directors" key. Now, when the user clicks the button,
the selected Talent is added to the `directors` relationship
of the selected Movie. If more than one talent is selected, both
are added to the relationship. If more than one Movie is selected,
the selected talent are added to the relationship of the first Movie
in the selection.

## Constructors

---

### EOActionInsertionAssociation

`public EOActionInsertionAssociation(Object  aDisplayObject)`

Creates a new EOActionInsertionAssociation to
monitor and update the value in  _aDisplayObject._

You
normally set up associations in Interface Builder, in which case
you don't need to create them programmatically. However, if you
do create them up programmatically, setting them up is a multi-step
process. After creating an association, you must bind its aspects
and establish its connections.

__See
Also:__  [bindAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe2lomraxg4dfmn2a) (EOAssociation), [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) (EOAssociation)

---

## Instance Methods

---

### actionPerformed

`public void actionPerformed(java.awt.event.ActionEvent  event)`

(com.apple.client.eointerface) Invoked when
the receiver's display object is acted upon. Sends the method
identified by the receiver's action aspect (with an argument,
if the argument aspect is bound) to the selected objects.

---

### breakConnection

`public void breakConnection()`

(com.apple.client.eointerface) See the [breakConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe4tfmfvug33onzswg5djn5xa) method description
in the superclass ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4)).

---

### establishConnection

`public void establishConnection()`

(com.apple.client.eointerface) See the [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) method
description in the superclass ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4)).

---

### isUsableWithObject

`public boolean isUsableWithObject(Object  aDisplayObject)`

(com.apple.client.eointerface) Returns `true` if  _aDisplayObject_ implements
the method `addActionListener`, `false` otherwise.

__See
Also:__  [isUsableWithObject](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxws42vonqwe3dfk5uxi2cpmjvgky3u) ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4))

---

### primaryAspect

`public String primaryAspect()`

(com.apple.client.eointerface) Returns `EOAssociation.` [SourceAspect](EOAssociation.md#apple-ijeugsseizfeo).

__See
Also:__  [primaryAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxa4tjnvqxe6kbonygky3u) ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4))

---

### subjectChanged

`public void subjectChanged()`

(com.apple.client.eointerface) See the [subjectChanged](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg5lcnjswg5cdnbqw4z3fmq) method description
in the superclass ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4)).

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
