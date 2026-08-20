---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSDisposableReg.html
archived_at: '2026-07-15T08:13:55.954492Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSDisposableRegistry

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : NSDisposable: Serializable

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

An NSDisposableRegistry object is a registry of [NSDisposable](NSDisposable.md#apple-ijbesq2gineuc) objects that should be disposed when the registry is disposed. You can add objects to a registry with [addObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruxg4dponqwe3dfkjswo2ltorzhsl3bmrse6ytkmvrxi) and [addObjectsFromRegistry](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruxg4dponqwe3dfkjswo2ltorzhsl3bmrse6ytkmvrxi42gojxw2utfm5uxg5dspe), remove objects with [removeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruxg4dponqwe3dfkjswo2ltorzhsl3smvww65tfj5rguzldoq), and dispose of a registries objects with [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruxg4dponqwe3dfkjswo2ltorzhsl3enfzxa33tmu).

There are two ways in which you might interact with a disposable registry: adding objects to another object's registry and creating a class whose instances manage their own disposable registries. As an example of the former, consider the EOController class (defined in the eoapplication package and used in Direct to Java Client applications). EOController has a disposable registry, which you can access with the EOController method __disposableRegistry__. In EOController's __dispose__ method, it disposes its disposable registry, which in turn disposes all its objects. You can get a controller's registry and add objects to it; they will be disposed along with the EOController. The second way in which you might interact with a disposable registry, then, is to create a class similar to EOController that uses a disposable registry to group objects that should be disposed of along with instances of your class.

## Constructors

---

### NSDisposableRegistry

`public NSDisposableRegistry()`

Creates an empty disposable registry.

---

## Instance Methods

---

### addObject

`public void addObject(NSDisposable anObject)`

Adds _anObject_ to the receiver so that _anObject_ will be disposed when the receiver is disposed.

---

### addObjectsFromRegistry

`public void addObjectsFromRegistry(NSDisposableRegistry aDisposableRegistry)`

Adds the objects in _aDisposableRegistry_ to the receiver, so that _aDisposableRegistry_'s objects will be disposed when the receiver is disposed.

---

### dispose

`public void dispose()`

Conformance to NSDisposable. NSDisposableRegistry's implementation simply sends [dispose](NSDisposable.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstiruxg4dponqwe3dff5sgs43qn5zwk) to all its objects.

__See Also:__ [dispose](NSDisposable.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstiruxg4dponqwe3dff5sgs43qn5zwk) ( [NSDisposable](NSDisposable.md#apple-ijbesq2gineuc))

---

### removeObject

`public void removeObject(NSDisposable anObject)`

Removes _anObject_ from the receiver.

---

### toString

`public String toString()`

Returns a string representation of the receiver.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
