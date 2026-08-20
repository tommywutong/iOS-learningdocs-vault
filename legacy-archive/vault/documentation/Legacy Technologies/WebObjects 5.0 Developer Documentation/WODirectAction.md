---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WODirectAction.html
archived_at: '2026-07-15T08:15:15.486880Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WODirectAction

> __Inherits from:__ Object

> __Implements:__ NSKeyValueCodingNSKeyValueCoding.ErrorHandlingNSKeyValueCodingAdditionsNSValidation

> __Package:__ com.webobjects.appserver

---

## Class Description

---

WODirectAction is an abstract class that defines the interface for direct action classes. You subclass WODirectAction to provide an object that is a repository for action methods.

WODirectAction provides the simplest interface for adding logic and custom code to your WebObjects application. WODirectAction objects are instantiated when a URL requested by a client browser is sent to your WebObjects application. The WODirectActionRequestHandler determines the proper class and action to be invoked and then passes control to your WODirectAction subclass.

In contrast to a WOComponent-based action, a direct action is well-defined by the URL that invokes it. For example, the following URL will invoke the method __findEmployeeAction__ on the subclass of WODirectAtion called Common:

```
http://localhost/cgi-bin/WebObjects/Myapp.woa/wa/Common/findEmployee
```

A subclass of WODirectAction is a repository for action methods. New WebObjects applications contain a default implementation of the WODirectAction subclass called DirectAction. The DirectAction class is used when no class is specified in the URL.

In summary, here are some URLs and the actions they invoke:

|  |  |
| --- | --- |
| __This URL...__ | __Invokes this method...__ |
| ../MyApp.woa/wa/ | __defaultAction__ on class DirectAction |
| ../MyApp.woa/wa/ find | __findAction__ on classDirectAction , if it exists __defaultAction__ on class find , otherwise |
| ../MyApp.woa/wa/Common/find | __findAction__ on class Common |

WODirectActionRequestHandler invokes methods only on subclasses on WODirectAction. If the specified class or action doesn't exist, WODirectActionRequestHandler throws an exception.

## Interfaces Implemented

---

> NSKeyValueCoding [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65dbnnsvmylmovsum33sjnsxs)[valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65tbnr2wkrtpojfwk6i)NSKeyValueCodingAdditions [takeValueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65dbnnsvmylmovsum33sjnsxsudborua)[valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65tbnr2wkrtpojfwk6kqmf2gq)NSKeyValueCoding.ErrorHandling [handleQueryWithUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc62dbnzsgyzkrovsxe6kxnf2gqvlomjxxk3tejnsxs)[handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc62dbnzsgyzkumfvwkvtbnr2wkrtpojkw4ytpovxgis3fpe)[unableToSetNullForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65lomfrgyzkun5jwk5coovwgyrtpojfwk6i)NSValidation [validateTakeValueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65tbnruwiylumvkgc23fkzqwy5lfizxxes3fpfigc5di)[validateValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65tbnruwiylumvlgc3dvmvdg64slmv4q)

## Method Types

---

> Constructors[WODirectAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc6v2piruxezldorawg5djn5xa)Obtaining attributes[canAccessFieldsDirectly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjojswg5cbmn2gs33of5rwc3sbmnrwk43tizuwk3deoncgs4tfmn2gy6i)[request](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc64tfof2wk43u)Obtaining a context[context](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc6y3pnz2gk6du)Obtaining a session[existingSession](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc6zlynfzxi2lom5jwk43tnfxw4)[session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc643fonzws33o)Obtaining a page[pageWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc64dbm5svo2lunbhgc3lf)Performing an action[performActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc64dfojtg64tnifrxi2lpnzhgc3lfmq)Value assignment[takeFormValueArraysForKeyArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65dbnnsum33snvlgc3dvmvaxe4tbpfzum33sjnsxsqlsojqxs)[takeFormValuesForKeyArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65dbnnsum33snvlgc3dvmvzum33sjnsxsqlsojqxs)Debugging[debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjojswg5cbmn2gs33of5sgkytvm5jxi4tjnztq)[logString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjojswg5cbmn2gs33of5wg6z2torzgs3th)Other[defaultAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc6zdfmzqxk3duifrxi2lpny)

## Constructors

---

### WODirectAction

`public WODirectAction(WORequest aWORequest)`

Subclasses must override to provide any additional initialization.

---

## Static Methods

---

### __canAccessFieldsDirectly__

`public static boolean canAccessFieldsDirectly()`

WODirectAction's implementation of this static method returns `true`, indicating that key/value coding is allowed to access fields in this object if an appropriate method isn't present.

---

### debugString

`public static void debugString(String aString)`

This method is similar to [logString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjojswg5cbmn2gs33of5wg6z2torzgs3th) except that you can control whether it displays output with the __WODebuggingEnabled__ user default option. If __WODebuggingEnabled__ is true, then the [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjojswg5cbmn2gs33of5sgkytvm5jxi4tjnztq) messages display their output. If __WODebuggingEnabled__ is false, the [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjojswg5cbmn2gs33of5sgkytvm5jxi4tjnztq) messages don't display their output.

---

### logString

`public static void logString(String aString)`

Prints a message to the standard error device (stderr). The message can include formatted variable data using String's concatenation feature, for example:

```
int i = 500;

float f = 2.045;

WOComponent.logString("Amount = " + i + ", Rate = " + f ", Total = " + i*f);
```

---

## Instance Methods

---

### __context__

`public WOContext context()`

Returns the WODirectAction's context.

---

### __defaultAction__

`public WOActionResults defaultAction()`

Returns a WOActionResults object that is the result of sending __generateResponse()__ to the page named "Main".

---

### existingSession

`public WOSession existingSession()`

Restores the session based on the request. If the request did not have a session ID or the session ID referred to a non-existent session, then this method returns null. To determine if a session failed to restore, check the request's session ID to see if it non-null and if so, call this method to check its result.

__See Also:__ [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc643fonzws33o)

---

### handleQueryWithUnboundKey

`public Object handleQueryWithUnboundKey(String key)`

Conformance to NSKeyValueCoding.ErrorHandling.

---

### handleTakeValueForUnboundKey

`public void handleTakeValueForUnboundKey(Object value, String key)`

Conformance to NSKeyValueCoding.ErrorHandling.

---

### pageWithName

`public WOComponent pageWithName(String aComponentName)`

Returns the WOComponent with the specified name.

---

### performActionNamed

`public WOActionResults performActionNamed(String anActionName)`

Performs the action with the specified name and returns the result of that action. The default implementation appends "Action" to _anActionName_ and tries to invoke resulting method name. Override this method to change how actions are dispatched.

---

### request

`public WORequest request()`

Returns the WORequest object that initiated the action.

---

### session

`public WOSession session()`

Returns the current session. If there is no session, this method first tries to restore the session that the request's session ID refers to. If the request has no session ID-which is a possibility if the application is written entirely with direct actions-this method creates a new session and returns it. If the session ID refers to a session that doesn't exist or cannot be restored, this method throws an exception.

__See Also:__ [existingSession](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc6zlynfzxi2lom5jwk43tnfxw4)

---

### takeFormValueArraysForKeyArray

`public void takeFormValueArraysForKeyArray(NSArray aKeyArray)`

Performs [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65dbnnsvmylmovsum33sjnsxs)on each key in _aKeyArray_ using values from the receiver's request.

This method uses an NSArray for each form value. This is useful when a user can select multiple items for a form value, such as a WOBrowser. If a form value contains only one item, this method uses an NSArray with one object. To use single objects as form values, use [takeFormValuesForKeyArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65dbnnsum33snvlgc3dvmvzum33sjnsxsqlsojqxs).

---

### takeFormValuesForKeyArray

`public void takeFormValuesForKeyArray(NSArray aKeyArray)`

Performs [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65dbnnsvmylmovsum33sjnsxs) on the each key in _aKeyArray_ using values from the receiver's request.

This method uses an a single object for each form value. If a form value contains more than one item, such as a WOBrowser, this method uses the first item in the array. To use arrays of objects as form values, use [takeFormValueArraysForKeyArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxezldorawg5djn5xc65dbnnsum33snvlgc3dvmvaxe4tbpfzum33sjnsxsqlsojqxs).

---

### takeValueForKey

`public void takeValueForKey(Object value, String key)`

Conformance to NSKeyValueCoding.

---

### takeValueForKeyPath

`public void takeValueForKeyPath(Object value, String keyPath)`

Conformance to NSKeyValueCodingAdditions.

---

### __toString__

`public String toString()`

Returns a String containing a string representation of the receiver.

---

### unableToSetNullForKey

`public void unableToSetNullForKey(String key)`

Conformance to NSKeyValueCoding.ErrorHandling.

---

### validateTakeValueForKeyPath

`public Object validateTakeValueForKeyPath( Object value, String keyPath) throws NSValidation.ValidationException`

Conformance to NSValidation.

---

### validateValueForKey

`public Object validateValueForKey( Object value, String key) throws NSValidation.ValidationException`

Conformance to NSValidation.

---

### valueForKey

`public Object valueForKey(String key)`

Conformance to NSKeyValueCoding.

---

### valueForKeyPath

`public Object valueForKeyPath(String keyPath)`

Conformance to NSKeyValueCodingAdditions.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
