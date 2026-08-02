---
title: Distributed Objects Programming Topics
apple_id: 10000102i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2017-06-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Tasks/invocations.html
archived_at: '2026-07-15T07:15:03.767852Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Distributed Objects Programming Topics](Introduction%20to%20Distributed%20Objects.md)


[Next](Document%20Revision%20History.md)[Previous](Making%20Substitutions%20During%20Message%20Encoding.md)

For interprocess communication, you should use XPC instead; see _[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_ for more information.

# Using NSInvocation

Creating an `NSInvocation` object requires several steps. Consider this method of the custom class `MyCalendar`:

```
– (BOOL)updateAppointmentsForDate:(NSDate *)aDate
```

`updateAppointmentsForDate:` takes an `NSDate` object as its only argument, and returns `YES` or `NO` depending on whether the appointments could be updated without conflicts. The following code fragment sets up an `NSInvocation` object for it:

```
SEL theSelector;
NSMethodSignature *aSignature;
NSInvocation *anInvocation;

theSelector = @selector(updateAppointmentsForDate:);
aSignature = [MyCalendar instanceMethodSignatureForSelector:theSelector];
anInvocation = [NSInvocation invocationWithMethodSignature:aSignature];
[anInvocation setSelector:theSelector];
```

The first two lines get the `NSMethodSignature` object for the `updateAppointmentsForDate:` method. The last two lines actually create the `NSInvocation` object and set its selector. Note that the selector can be set to any selector matching the signature of `updateAppointmentsForDate:`. Any of these methods can be used with _anInvocation_:

```
– (BOOL)clearAppointmentsForDate:(NSDate *)aDate
– (BOOL)isAvailableOnDate:(NSDate *)aDate
– (BOOL)setMeetingTime:(NSDate *)aDate
```

Before being dispatched, _anInvocation_ must have its target and arguments set:

```
MyCalendar *userDatebook;    /* Assume this exists. */
NSDate *todaysDate;          /* Assume this exists. */

[anInvocation setTarget:userDatebook];
[anInvocation setArgument:&todaysDate atIndex:2];
```

`setArgument:atIndex:` sets the specified argument to the value supplied. Every method has two hidden arguments, the _target_ and _selector_ (whose indices are `0` and `1`), so the first argument that needs to be set is actually at index `2`. In this case, _todaysDate_ is the `NSDate` argument to `updateAppointmentsForDate:`.

To dispatch the `NSInvocation` object, send an `invoke` or `invokeWithTarget:` message. `invoke` only produces a result if the `NSInvocation` object has a target set. Once dispatched, the `NSInvocation` object contains the return value of the message, which `getReturnValue:` produces:

```
BOOL result;

[anInvocation invoke];
[anInvocation getReturnValue:&result];
```

`NSInvocation` does not support invocations of methods with either variable numbers of arguments or `union` arguments.

Because an `NSInvocation` object does not always need to retain its arguments, by default it does not do so. This can cause object arguments as well as the target to become invalid if they are automatically released. If you plan to cache an `NSInvocation` object or dispatch it repeatedly during the execution of your application, you should send it a `retainArguments` message. This method retains the target and all object arguments, and copies C strings so that they are not lost because another object frees them.

Suppose the `NSInvocation` object created above is being used in a time-management application that allows multiple users to set appointments for others, such as group meetings. This application might allow a user’s calendar to be automatically updated every few minutes, so that the user always knows what his schedule looks like. Such automatic updating can be accomplished by setting up `NSTimer` objects with `NSInvocation` objects.

Given the `NSInvocation` object above, this is as simple as invoking one NSTimer method:

```
[NSTimer scheduledTimerWithInterval:600
        invocation:anInvocation
        repeats:YES];
```

This line of code sets up an `NSTimer` object to dispatch _anInvocation_ every 10 minutes (600 seconds). Note that an `NSTimer` object always instructs its `NSInvocation` object to retain its arguments; thus, you do not need to send `retainArguments` yourself. See _[Timer Programming Topics](../Timer%20Programming%20Topics/Introduction%20to%20Timers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3dc2i)_ for more information on timers.

[Next](Document%20Revision%20History.md)[Previous](Making%20Substitutions%20During%20Message%20Encoding.md)

