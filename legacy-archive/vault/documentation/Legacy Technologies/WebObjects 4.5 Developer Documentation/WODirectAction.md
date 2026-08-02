---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Classes/WODirectAction.html
archived_at: '2026-07-15T08:11:46.816439Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WODirectAction

> __Inherits
> from:__  NSObject

> __Package:__ com.apple.yellow.webobjects

---

## Class Description

---

WODirectAction is an abstract class that defines the interface
for direct action classes. You subclass WODirectAction to provide
an object that is a repository for action methods.

WODirectAction provides the simplest interface for addig logic
and custom code to your WebObjects application. WODirectAction objects
are instantiated when a URL requested by a client browser is sent to
your WebObjects application. The WODirectActionRequestHandler determines
the proper class and action to be invoked and then passes control
to your WODirectAction subclass.

In contrast to a WOComponent-based action, a direct action
is well-defined by the URL that invokes it. For example, the following
URL will invoke the method __findEmployeeAction__ on
the subclass of WODirectAtion called Common:

> ```
> http://localhost/cgi-bin/WebObjects/Myapp.woa/wa/Common/findEmployee
> ```

A subclass of WODirectAction is a repository for action methods.
New WebObjects applications contain a default implementation of
the WODirectAction subclass called DirectAction. The DirectAction
class is used when no class is specified in the URL.

In summary, here are some URLs and the actions they invoke:

|  |  |
| --- | --- |
| __This URL...__ | __Invokes this method...__ |
| ../MyApp.woa/wa/ | __defaultAction__ on class DirectAction |
| ../MyApp.woa/wa/ find | __findAction__ on classDirectAction , if it exists __defaultAction__ on class find , otherwise |
| ../MyApp.woa/wa/Common/find | __findAction__ on class Common |

WODirectActionRequestHandler invokes methods only on subclasses
on WODirectAction. If the specified class or action doesn't exist,
WODirectActionRequestHandler throws an exception.

## Method Types

---

> **Constructors**
> : [WODirectAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc6v2piruxezldorawg5djn5xa)
>
> **Obtaining attributes**
> : [request](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc64tfof2wk43u)
>
> **Obtaining a session**
> : [existingSession](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc6zlynfzxi2lom5jwk43tnfxw4)
> : [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc643fonzws33o)
>
> **Obtaining a page**
> : [pageWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc64dbm5svo2lunbhgc3lf)
>
> **Performing an action**
> : [performActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc64dfojtg64tnifrxi2lpnzhgc3lfmq)
>
> **Value assignment**
> : [takeFormValueArraysForKeyArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65dbnnsum33snvlgc3dvmvaxe4tbpfzum33sjnsxsqlsojqxs)
> : [takeFormValuesForKeyArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65dbnnsum33snvlgc3dvmvzum33sjnsxsqlsojqxs)
>
> **Debugging**
> : [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjojswg5cbmn2gs33of5sgkytvm5jxi4tjnztq)
> : [logString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjojswg5cbmn2gs33of5wg6z2torzgs3th)

## Constructors

---

### WODirectAction

`public WODirectAction(WORequest aWORequest)`

Subclasses must override to provide any additional
initialization.

---

## Static Methods

---

### debugString

`public static void debugString(String aString)`

This method is similar to [logString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjojswg5cbmn2gs33of5wg6z2torzgs3th) except that you can control
whether it displays output with the __WODebuggingEnabled__ user
default option. If __WODebuggingEnabled__ is
YES, then the [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjojswg5cbmn2gs33of5sgkytvm5jxi4tjnztq) messages display
their output. If __WODebuggingEnabled__ is
NO, the [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjojswg5cbmn2gs33of5sgkytvm5jxi4tjnztq) messages
don't display their output.

---

### logString

`public static void logString(String aString)`

Prints a message to the standard error device
(stderr). The message can include formatted variable data using
String's concatenation feature, for example:
> ```
> int i = 500;
>
> float f = 2.045;
>
> WOComponent.logString("Amount = " + i + ", Rate = " + f ", Total = " + i*f);
> ```

---

## Instance Methods

---

### existingSession

`public WOSession existingSession()`

Restores the session based on the request.
If the request did not have a session ID or the session ID referred
to a non-existent session, then this method returns null. To determine
if a session failed to restore, check the request's session ID
to see if it non-null and if so, call this method to check its result.

__See
Also:__  [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc643fonzws33o)

---

### pageWithName

`public WOComponent pageWithName(String aComponentName)`

Returns the WOComponent with the specified name.

---

### performActionNamed

`public WOActionResults performActionNamed(String anActionName)`

Performs the action with the specified name
and returns the result of that action. The default implementation
appends "Action" to _anActionName_ and
tries to invoke resulting method name. Override this method to change
how actions are dispatched.

---

### request

`public WORequest request()`

Returns the WORequest object that initiated
the action.

---

### session

`public WOSession session()`

Returns the current session. If there is no
session, this method first tries to restore the session that the request's
session ID refers to. If the request has no session ID-which is
a possibility if the application is written entirely with direct
actions-this method creates a new session and returns it. If the
session ID refers to a session that doesn't exist or cannot be
restored, this method throws an exception.

__See
Also:__  [existingSession](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc6zlynfzxi2lom5jwk43tnfxw4)

---

### takeFormValueArraysForKeyArray

`public void takeFormValueArraysForKeyArray(NSArray aKeyArray)`

Performs takeValueForKey on
each key in _aKeyArray_ using values
from the receiver's request.

This method uses an NSArray
for each form value. This is useful when a user can select multiple
items for a form value, such as a WOBrowser. If a form value contains
only one item, this method uses an NSArray with one object. To use
single objects as form values, use [takeFormValuesForKeyArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65dbnnsum33snvlgc3dvmvzum33sjnsxsqlsojqxs).

__See
Also:__  takeFormValueArraysForKeys:

---

### takeFormValuesForKeyArray

`public void takeFormValuesForKeyArray(NSArray aKeyArray)`

Performs takeValueForKey on
the each key in _aKeyArray_ using values
from the receiver's request.

This method uses an a single
object for each form value. If a form value contains more than one
item, such as a WOBrowser, this method uses the first item in the
array. To use arrays of objects as form values, use [takeFormValueArraysForKeyArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65dbnnsum33snvlgc3dvmvaxe4tbpfzum33sjnsxsqlsojqxs).

__See
Also:__  takeFormValuesForKeys:

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
