---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WODirectAction.html
archived_at: '2026-07-18T01:28:51.466140Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WOCookie.md)
[!](WODisplayGroup.md)

---

# WODirectAction

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

WODirectAction is an abstract class that defines the interface for direct action classes. You subclass WODirectAction to provide an object that is a repository for action methods.

WODirectAction provides the simplest interface for addig logic and custom code to your WebObjects application. WODirectAction objects are instantiated when a URL requested by a client browser is sent to your WebObjects application. The WODirectActionRequestHandler determines the proper class and action to be invoked and then passes control to your WODirectAction subclass.

In contrast to a WOComponent-based action, a direct action is well-defined by the URL that invokes it. For example, the following URL will invoke the method `findEmployeeAction` on the subclass of WODirectAtion called Common:

> ```
> http://localhost/cgi-bin/WebObjects/Myapp.woa/wa/Common/findEmployee
> ```

A subclass of WODirectAction is a repository for action methods. New WebObjects applications contain a default implementation of the WODirectAction subclass called DirectAction. The DirectAction class is used when no class is specified in the URL.

In summary, here are some URLs and the actions they invoke:

| __This URL...__ | __Invokes this method...__ |
| ../MyApp.woa/wa/ | `defaultAction` on class DirectAction |
| ../MyApp.woa/wa/ find | `findAction` on classDirectAction , if it exists  `defaultAction` on class find , otherwise |
| ../MyApp.woa/wa/Common/find | `findAction` on class Common |

```
```

WODirectActionRequestHandler invokes methods only on subclasses on WODirectAction. If the specified class or action doesn't exist, WODirectActionRequestHandler throwsraises an exception.

---

## Method Types

**Constructors**

**[WODirectAction](#apple-ge3dqobw)**

**Obtaining attributes**

**[request](#apple-g42a)**

**Obtaining a session**

**[existingSession](#apple-gu2a)

**[session](#apple-g44a)****

**Obtaining a page**

**[pageWithName](#apple-gm3tmmi)**

**Performing an action**

**[performActionNamed](#apple-g4ya)**

**Value assignment**

**[takeFormValueArraysForKeyArray](#apple-haza)

**[takeFormValuesForKeyArray](#apple-gqydemy)****

**Debugging**

**[debugString](#apple-ge3dqojt)

**[logString](#apple-ge3dsmbw)****

---

## Constructors

---

### WODirectAction

public `WODirectAction`()

public `WODirectAction`(WORequest _aWORequest_)

Subclasses must override to provide any additional initialization.

#

---

### debugString

public static void `debugString`(java.lang.String _aString_)

This method is similar to [`logString`](#apple-ge3dsmbw) except that you can control whether it displays output with the `WODebuggingEnabled` user default option. If `WODebuggingEnabled` is YES, then the [`debugString`](#apple-ge3dqojt) messages display their output. If `WODebuggingEnabled` is NO, the [`debugString`](#apple-ge3dqojt) messages don\xd5 t display their output.

---

### logString

public static void `logString`(java.lang.String _aString_)

Prints a message to the standard error device (stderr). The message can include formatted variable data using String's concatenation feature, for example:

> ```
> int i = 500;
> ```

> ```
> float f = 2.045;
> ```

> ```
> WOComponent.logString("Amount = " + i + ", Rate = " + f ", Total = " + i*f);
> ```

---

## Instance Methods

---

### existingSession

public WOSession `existingSession`()

Restores the session based on the request. If the request did not have a session ID or the session ID referred to a non-existent session, then this method returns `null`. To determine if a session failed to restore, check the request's session ID to see if it non-`null` and if so, call this method to check its result.

__See also:__
[`session`](#apple-g44a)

---

### pageWithName

public WOComponent `pageWithName`(java.lang.String _aComponentName_)

Returns the WOComponent with the specified name.

---

### performActionNamed

public WOActionResults `performActionNamed`(java.lang.String _anActionName_)

Performs the action with the specified name and returns the result of that action. The default implementation appends \xd2 Action\xd3 to _anActionName_ and tries to invoke resulting method name. Override this method to change how actions are dispatched.

---

### request

public WORequest `request`()

Returns the WORequest object that initiated the action.

---

### session

public WOSession `session`()

Returns the current session. If there is no session, this method first tries to restore the session that the request\xd5 s session ID refers to. If the request has no session IDwhich is a possibility if the application is written entirely with direct actionsthis method creates a new session and returns it. If the session ID refers to a session that doesn\xd5 t exist or cannot be restored, this method throws an exception.

__See also:__
[`existingSession`](#apple-gu2a)

---

### takeFormValueArraysForKeyArray

public void `takeFormValueArraysForKeyArray`(NSArray _aKeyArray_)

Performs takeValueForKey on each key in _aKeyArray_ using values from the receiver\xd5 s request.

This method uses an NSArray for each form value. This is useful when a user can select multiple items for a form value, such as a WOBrowser. If a form value contains only one item, this method uses an NSArray with one object. To use single objects as form values, use [`takeFormValuesForKeyArray`](#apple-gqydemy).

---

### takeFormValuesForKeyArray

public void `takeFormValuesForKeyArray`(NSArray _aKeyArray_)

Performs takeValueForKey on the each key in _aKeyArray_ using values from the receiver\xd5 s request.

This method uses an a single object for each form value. If a form value contains more than one item, such as a WOBrowser, this method uses the first item in the array. To use arrays of objects as form values, use [`takeFormValueArraysForKeyArray`](#apple-haza).

---

### 

---

[!](WOCookie.md)
[!](WODisplayGroup.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
