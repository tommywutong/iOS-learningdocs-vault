---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOQuickTimeAssociation.html
archived_at: '2026-07-15T08:11:44.940485Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOQuickTimeAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl)
> : Object

> **__Implements:__**
> : EOObserving (EODelayedObserver)

> **__Package:__**
> : com.apple.client.eointerface

---

## Class Description

---

EOQuickTimeAssociation associates the contents of its [URLAspect](EOAssociation.md#apple-ijeugskjifbuo)'s display group with an EOQuickTimeView.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eointerface package. |

|  |
| --- |
| __Usable With__ |
| EOQuickTimeView |

|  |
| --- |
| __Aspects__ |
| URLAspect | A URL for the location of the QuickTime movie. |

## Constructors

---

### EOQuickTimeAssociation

`public EOQuickTimeAssociation(Object  aDisplayObject)`

Creates a new EOQuickTimeAssociation
to monitor and update the value in  _aDisplayObject,_
an EOQuickTimeView.

You normally set up associations
in Interface Builder, in which case you don't need to create them programmatically.
However, if you do create them up programmatically, setting them
up is a multi-step process. After creating an association, you must
bind its aspects and establish its connections.

__See
Also:__  [bindAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe2lomraxg4dfmn2a) (EOAssociation), [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) (EOAssociation)

---

## Instance Methods

---

### breakConnection

`public void breakConnection()`

See the [breakConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe4tfmfvug33onzswg5djn5xa) method description
in the superclass [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4).

---

### isUsableWithObject

`public boolean isUsableWithObject(Object  aDisplayObject)`

Returns `true` if  _aDisplayObject_ is
an instance of EOQuickTimeView, `false` otherwise.

__See
Also:__  [isUsableWithObject](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxws42vonqwe3dfk5uxi2cpmjvgky3u) ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4))

---

### primaryAspect

`public String primaryAspect()`

Returns `EOAssociation.` [URLAspect](EOAssociation.md#apple-ijeugskjifbuo).

__See
Also:__  [primaryAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxa4tjnvqxe6kbonygky3u) ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4))

---

### subjectChanged

`public void subjectChanged()`

See the [subjectChanged](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg5lcnjswg5cdnbqw4z3fmq) method description
in the superclass [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4).

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
