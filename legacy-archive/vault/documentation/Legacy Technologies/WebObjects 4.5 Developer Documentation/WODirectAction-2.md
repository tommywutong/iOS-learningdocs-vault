---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WODirectAction.html
archived_at: '2026-07-15T08:11:47.490642Z'
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

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  WebObjects/WODirectAction.h

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
WODirectActionRequestHandler raises an exception.

## Method Types

---

> **Creation**
> : [- initWithRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxws3tjorlws5dikjsxc5lfon2du)
>
> **Obtaining attributes**
> : [- request](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxezlrovsxg5a)
>
> **Obtaining a session**
> : [- existingSession](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxwk6djon2gs3thknsxg43jn5xa)
> : [- session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxgzltonuw63q)
>
> **Obtaining a page**
> : [- pageWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxaylhmvlws5dijzqw2zj2)
>
> **Performing an action**
> : [- performActionNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxazlsmzxxe3kbmn2gs33ojzqw2zlehi)
>
> **Value assignment**
> : [- takeFormValueArraysForKeyArray:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxiyllmvdg64tnkzqwy5lfifzheylzondg64slmv4uc4tsmf4tu)
> : [- takeFormValueArraysForKeys:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxiyllmvdg64tnkzqwy5lfifzheylzondg64slmv4xgoq)
> : [- takeFormValuesForKeyArray:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxiyllmvdg64tnkzqwy5lfondg64slmv4uc4tsmf4tu)
> : [- takeFormValuesForKeys:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxiyllmvdg64tnkzqwy5lfondg64slmv4xgoq)
>
> **Debugging**
> : [- debugWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxwizlcovtvo2lunbdg64tnmf2du)
> : [- logWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxwy33hk5uxi2cgn5zg2yluhi)

## Instance Methods

---

### debugWithFormat:

`- (void)debugWithFormat:(NSString
*)aFormatString,...`

This method is similar to [logWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxwy33hk5uxi2cgn5zg2yluhi) except
that you can control whether it displays output with the __WODebuggingEnabled__ user
default option. If __WODebuggingEnabled__ is
YES, then the [debugWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxwizlcovtvo2lunbdg64tnmf2du) messages
display their output. If __WODebuggingEnabled__ is
NO, the [debugWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxwizlcovtvo2lunbdg64tnmf2du) messages don't display
their output.

__See Also:__  [- debugWithFormat:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkytvm5lws5diizxxe3lboq5a) ( [- WOApplication](WOApplication-2.md#apple-k5huc4dqnruwgylunfxw4))

---

### existingSession

`- (WOSession*)existingSession`

Restores the session based on the request.
If the request did not have a session ID or the session ID referred
to a non-existent session, then this method returns nil. To determine
if a session failed to restore, check the request's session ID
to see if it non-nil and if so, call this method to check its result.

__See
Also:__  [- session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxgzltonuw63q)

---

### initWithRequest:

`- initWithRequest:(WORequest
*)aRequest`

This is the designated initializer for all subclasses
of WODirectAction. Whne you create a subclass, you must override
this method to provide any additional initialization.

---

### logWithFormat:

`- (void)logWithFormat:(NSString
*)aFormatString,...`

Prints a message to the standard error device
(stderr). The message can include formatted variable data using
printf-style conversion specifiers, for example:
> ```
> id i = 500;
> id f = 2.045;
> [self logWithFormat:@"Amount = %@, Rate = %@, Total = %@", i, f, i*f];
> ```

Note
that in WebScript, all variables are objects, so the only conversion
specifier allowed is __%@__ as shown above.
In compiled Objective-C code, all __printf__ conversion
specifiers are allowed. The equivalent method in Java is __logString__.

__See
Also:__  [- logWithFormat:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5wg6z2xnf2gqrtpojwwc5b2) ( [- WOApplication](WOApplication-2.md#apple-k5huc4dqnruwgylunfxw4))

---

### pageWithName:

`- (WOComponent *)pageWithName:(NSString
*)aComponentName`

Returns the WOComponent with the specified name.

---

### performActionNamed:

`- (id <WOActionResults>)performActionNamed:(NSString
*)anActionName`

Performs the action with the specified name
and returns the result of that action. The default implementation
appends "Action" to _anActionName_ and
tries to invoke resulting method name. Override this method to change
how actions are dispatched.

---

### request

`- (WORequest *)request`

Returns the WORequest object that initiated
the action.

---

### session

`- (WOSession *)session`

Returns the current session. If there is no
session, this method first tries to restore the session that the request's
session ID refers to. If the request has no session ID-which is
a possibility if the application is written entirely with direct
actions-this method creates a new session and returns it. If the
session ID refers to a session that doesn't exist or cannot be
restored, this method raises an exception.

__See
Also:__  [- existingSession](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxwk6djon2gs3thknsxg43jn5xa)

---

### takeFormValueArraysForKeyArray:

`- (void)takeFormValueArraysForKeyArray:(NSArray
*)aKeyArray`

Performs __takeValue:forKey:__ on
each key in _aKeyArray_ using values
from the receiver's request.

This method uses an NSArray
for each form value. This is useful when a user can select multiple
items for a form value, such as a WOBrowser. If a form value contains
only one item, this method uses an NSArray with one object. To use
single objects as form values, use [takeFormValuesForKeyArray:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxiyllmvdg64tnkzqwy5lfondg64slmv4uc4tsmf4tu).

__See
Also:__  [takeFormValueArraysForKeys:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxiyllmvdg64tnkzqwy5lfifzheylzondg64slmv4xgoq)

---

### takeFormValueArraysForKeys:

`- (void)takeFormValueArraysForKeys:(NSString
*)aFirstKey,...`

Performs __takeValue:forKey:__ on
the specified keys using values from the receiver's request. The
last key must be nil.

This method uses an NSArray for each
form value. This is useful when a user can select multiple items for
a form value, such as a WOBrowser. If a form value contains only
one item, this method uses an NSArray with one object. To use single
objects as form values, use [takeFormValuesForKeys:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxiyllmvdg64tnkzqwy5lfondg64slmv4xgoq).

__See
Also:__  [takeFormValueArraysForKeyArray:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxiyllmvdg64tnkzqwy5lfifzheylzondg64slmv4uc4tsmf4tu)

---

### takeFormValuesForKeyArray:

`- (void)takeFormValuesForKeyArray:(NSArray
*)aKeyArray`

Performs __takeValue:forKey:__ on
the each key in _aKeyArray_ using values
from the receiver's request.

This method uses an a single
object for each form value. If a form value contains more than one
item, such as a WOBrowser, this method uses the first item in the
array. To use arrays of objects as form values, use [takeFormValueArraysForKeyArray:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxiyllmvdg64tnkzqwy5lfifzheylzondg64slmv4uc4tsmf4tu).

__See
Also:__  [takeFormValuesForKeys:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxiyllmvdg64tnkzqwy5lfondg64slmv4xgoq)

---

### takeFormValuesForKeys:

`- (void)takeFormValuesForKeys:(NSString
*)aFirstKey,...`

Performs __takeValue:forKey:__ on
the specified keys using values from the receiver's request. The
last key must be nil.

This method uses an a single object for
each form value. If a form value contains more than one item, such
as a WOBrowser, this method uses the first item in the array. To
use arrays of objects as form values, use [takeFormValueArraysForKeys:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxiyllmvdg64tnkzqwy5lfifzheylzondg64slmv4xgoq).

__See
Also:__  [takeFormValuesForKeyArray:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzgky3uifrxi2lpnyxxiyllmvdg64tnkzqwy5lfondg64slmv4uc4tsmf4tu)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
