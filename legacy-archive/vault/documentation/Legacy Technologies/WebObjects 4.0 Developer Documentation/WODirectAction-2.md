---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WODirectAction.html
archived_at: '2026-07-18T01:28:53.771704Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WOCookie-2.md)
[!](WODisplayGroup-2.md)

---

# WODirectAction

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
WebObjects/WODirectAction.h

---

## Class Description

WODirectAction is an abstract class that defines the interface for direct action classes. You subclass WODirectAction to provide an object that is a repository for action methods.

WODirectAction provides the simplest interface for addig logic and custom code to your WebObjects application. WODirectAction objects are instantiated when a URL requested by a client browser is sent to your WebObjects application. The WODirectActionRequestHandler determines the proper class and action to be invoked and then passes control to your WODirectAction subclass.

In contrast to a WOComponent-based action, a direct action is well-defined by the URL that invokes it. For example, the following URL will invoke the method __findEmployeeAction__  on the subclass of WODirectAtion called Common:

> ```
> http://localhost/cgi-bin/WebObjects/Myapp.woa/wa/Common/findEmployee
> ```

A subclass of WODirectAction is a repository for action methods. New WebObjects applications contain a default implementation of the WODirectAction subclass called DirectAction. The DirectAction class is used when no class is specified in the URL.

In summary, here are some URLs and the actions they invoke:

| __This URL...__ | __Invokes this method...__ |
| ../MyApp.woa/wa/ | __defaultAction__  on class DirectAction |
| ../MyApp.woa/wa/ find | __findAction__  on classDirectAction , if it exists  __defaultAction__  on class find , otherwise |
| ../MyApp.woa/wa/Common/find | __findAction__  on class Common |

```
```

WODirectActionRequestHandler invokes methods only on subclasses on WODirectAction. If the specified class or action doesn't exist, WODirectActionRequestHandler throwsraises an exception.

Need to write section on "The takeValue Convenience Methods"

---

## Method Types

**Creation**

**[- initWithRequest:](#apple-ge3dkoju)**

**Obtaining attributes**

**[- request](#apple-g42a)**

**Obtaining a session**

**[- existingSession](#apple-gu2a)

**[- session](#apple-g44a)****

**Obtaining a page**

**[- pageWithName:](#apple-gm3tmmi)**

**Performing an action**

**[- performActionNamed:](#apple-g4ya)**

**Value assignment**

**[- takeFormValueArraysForKeyArray:](#apple-haza)

**[- takeFormValueArraysForKeys:](#apple-ge3donzr)

**[- takeFormValuesForKeyArray:](#apple-gqydemy)

**[- takeFormValuesForKeys:](#apple-ge3dqmzv)********

**Debugging**

**[- debugWithFormat:](#apple-ge3dkmjt)

**[- logWithFormat:](#apple-ge3dmmbq)****

---

## Instance Methods

---

### debugWithFormat:

- (void)`debugWithFormat:`(NSString \*)_aFormatString,..._

This method is similar to [__logWithFormat:__](#apple-ge3dmmbq) except that you can control whether it displays output with the __WODebuggingEnabled__  user default option. If __WODebuggingEnabled__  is YES, then the [__debugWithFormat:__](#apple-ge3dkmjt) messages display their output. If __WODebuggingEnabled__  is NO, the [__debugWithFormat:__](#apple-ge3dkmjt) messages don\xd5 t display their output.

__See also:__
[- __debugWithFormat:__](WOApplication-2.md#apple-g43tgma) ([- __WOApplication__](WOApplication-2.md))

---

### existingSession

- (WOSession\*)__existingSession__

Restores the session based on the request. If the request did not have a session ID or the session ID referred to a non-existent session, then this method returns __nil__ . To determine if a session failed to restore, check the request's session ID to see if it non-__nil__  and if so, call this method to check its result.

__See also:__
[- __session__](#apple-g44a)

---

### initWithRequest:

- `initWithRequest:`(WORequest \*)_aRequest_

This is the designated initializer for all subclasses of WODirectAction. Whne you create a subclass, you must override this method to provide any additional initialization.

---

### logWithFormat:

- (void)`logWithFormat:`(NSString \*)_aFormatString,..._

Prints a message to the standard error device (stderr). The message can include formatted variable data using printf-style conversion specifiers, for example:

> ```
> id i = 500;
> ```

> ```
> id f = 2.045;
> ```

> ```
> [self logWithFormat:@"Amount = %@, Rate = %@, Total = %@", i, f, i*f];
> ```

Note that in WebScript, all variables are objects, so the only conversion specifier allowed is __%@__  as shown above. In compiled Objective-C code, all __printf__  conversion specifiers are allowed. The equivalent method in Java is __logString__ .

__See also:__
[- __logWithFormat:__](WOApplication-2.md#apple-geytanbrha) ([- __WOApplication__](WOApplication-2.md))

---

### pageWithName:

- (WOComponent \*)`pageWithName:`(NSString \*)_aComponentName_

Returns the WOComponent with the specified name.

---

### performActionNamed:

- (id <WOActionResults>)`performActionNamed:`(NSString \*)_anActionName_

Performs the action with the specified name and returns the result of that action. The default implementation appends \xd2 Action\xd3 to _anActionName_ and tries to invoke resulting method name. Override this method to change how actions are dispatched.

---

### request

- (WORequest \*)`request`

Returns the WORequest object that initiated the action.

---

### session

- (WOSession \*)`session`

Returns the current session. If there is no session, this method first tries to restore the session that the request\xd5 s session ID refers to. If the request has no session IDwhich is a possibility if the application is written entirely with direct actionsthis method creates a new session and returns it. If the session ID refers to a session that doesn\xd5 t exist or cannot be restored, this method raises an exception.

__See also:__
[- __existingSession__](#apple-gu2a)

---

### takeFormValueArraysForKeyArray:

- (void)`takeFormValueArraysForKeyArray:`(NSArray \*)_aKeyArray_

Performs __takeValue:forKey:__  on each key in _aKeyArray_ using values from the receiver\xd5 s request.

This method uses an NSArray for each form value. This is useful when a user can select multiple items for a form value, such as a WOBrowser. If a form value contains only one item, this method uses an NSArray with one object. To use single objects as form values, use [__takeFormValuesForKeyArray:__](#apple-gqydemy).

__See also:__
[__takeFormValueArraysForKeys:__](#apple-ge3donzr)

---

### takeFormValueArraysForKeys:

- (void)`takeFormValueArraysForKeys:`(NSString \*)_aFirstKey,..._

Performs __takeValue:forKey:__  on the specified keys using values from the receiver\xd5 s request. The last key must be nil.

This method uses an NSArray for each form value. This is useful when a user can select multiple items for a form value, such as a WOBrowser. If a form value contains only one item, this method uses an NSArray with one object. To use single objects as form values, use [__takeFormValuesForKeys:__](#apple-ge3dqmzv).

__See also:__
[__takeFormValueArraysForKeyArray:__](#apple-haza)

---

### takeFormValuesForKeyArray:

- (void)`takeFormValuesForKeyArray:`(NSArray \*)_aKeyArray_

Performs __takeValue:forKey:__  on the each key in _aKeyArray_ using values from the receiver\xd5 s request.

This method uses an a single object for each form value. If a form value contains more than one item, such as a WOBrowser, this method uses the first item in the array. To use arrays of objects as form values, use [__takeFormValueArraysForKeyArray:__](#apple-haza).

__See also:__
[__takeFormValuesForKeys:__](#apple-ge3dqmzv)

---

### takeFormValuesForKeys:

- (void)`takeFormValuesForKeys:`(NSString \*)_aFirstKey,..._

Performs __takeValue:forKey:__  on the specified keys using values from the receiver\xd5 s request. The last key must be nil.

This method uses an a single object for each form value. If a form value contains more than one item, such as a WOBrowser, this method uses the first item in the array. To use arrays of objects as form values, use [__takeFormValueArraysForKeys:__](#apple-ge3donzr).

__See also:__
[__takeFormValuesForKeyArray:__](#apple-gqydemy)

---

###

---

[!](WOCookie-2.md)
[!](WODisplayGroup-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
