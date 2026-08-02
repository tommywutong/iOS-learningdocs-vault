---
title: Multiple User Environment Programming Topics
apple_id: 10000180i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPMultipleUsers/Concepts/FastUserSwitching.html
archived_at: '2026-07-15T08:16:24.829807Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Multiple User Environment Programming Topics](Introduction%20to%20Multiple%20User%20Environments.md)


[Next](User%20Switch%20Notifications.md)[Previous](Root%20and%20Login%20Sessions.md)

# Supporting Fast User Switching

Fast user switching lets users share a single machine without having to log out every time they want to access their user account. Users share physical access to the machine, including the same keyboard, mouse, and monitor. However, instead of logging out, a new user simply logs in and switches out the previous user.

Processes in a switched-out login session continue running as before. They can continue processing data, communicating with the system, and drawing to the screen buffer as before. However, because they are switched out, they do not receive input from the keyboard and mouse. Similarly, if they were to check, the monitor would appear to be in sleep mode. As a result, it may benefit some applications to adjust their behavior while in a switched-out state to avoid wasting system resources.

While fast user switching is a convenient feature for users, it does provide several challenges for application developers. Applications that rely on exclusive access to certain resources may need to modify their behavior to live in a fast user switching environment. For example, an application that stores temporary data in `/tmp` may run into problems when a second instance running under a different user tries to modify the same files in that directory.

To support fast user switching, there are certain guidelines you should follow in developing your applications. Most of these guidelines describe safe ways to identify and share system resources. The summary of these guidelines is as follows:

- Incorporate session ID information into the name of any entity that appears in a global namespace, including the following:

  - File names
  - Shared memory regions
  - Semaphores
  - Named pipes
- Accept and handle user switch notifications. See [User Switch Notifications](User%20Switch%20Notifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgiytalkdjjbeurcbi5da) for more information.
- Do not assume you have exclusive access to any resource, especially the following:

  - TCP/IP ports
  - Hardware devices
- Do not assume there is only one instance of a per-user service running.
- Use file-level or range-level locks when accessing files.

Tagging application-specific resources with a session ID is necessary to distinguish them from similar resources created by applications in a different session. The Security layer of the system assigns a unique ID to each login session. Incorporating this ID into cache file or temporary directory names can prevent namespace collisions when creating these files. See [Getting Login Session Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgiydsljrga2demjz) for information on how to get the session ID.

Obtaining shared system resources, such as TCP/IP ports, introduces other problems in a fast user switching environment. For example, if you have a chat connection, do you hold onto the port or give it up when a new user is switched in? How you handle these situations depends on the resource involved and the design of your application. Regardless of how you handle it, you need to know when the user switch occurs, and for that you should read the section [User Switch Notifications](User%20Switch%20Notifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgiytalkdjjbeurcbi5da), which describes the notifications available to applications.

If your application creates a file, shared memory region, or other object that lives in a global namespace, you should brand that object with your unique session ID.

OS X provides access to session information from two different frameworks. The Security framework includes a function for retrieving the session ID along with the basic information about the login session. The Core Graphics framework provides additional information about the login session, including the name of the user and whether the login process has completed.

Because session IDs are unique to a session, use them to identify resources that are session-specific, but which may still be shared by entities in same login session. For example, if your application creates a shared memory region, you could include the session ID in the name of that region. Other applications (including copies of the same application) would be able to access this memory region using the shared name and session information.

You can use session IDs in directory names to group temporary files together and make them easier to find. However, it is still recommended that you use the `mktemp` family of functions to generate random names for the files in that directory.

The Security framework can be linked into any program, whether it resides in the root session or in a login session. This framework includes the function `SessionGetInfo` for getting basic information about the current session, including the session ID and some session attributes.

To get the session ID of the current session, pass the value `callerSecuritySession` as the first parameter to `SessionGetInfo`. If you happen to have the session ID of a different login session, you can use it to get information about the other session. The parameters returned by `SessionGetInfo` are mostly informational and cannot be modified; thus they have no consequences on the security of the login session.

The following example shows you how to call `SessionGetInfo` to get the session ID for the current root or login session.

```c
#include <Security/Security.h>

OSStatus error;
SecuritySessionId mySession;
SessionAttributeBits sessionInfo;

error = SessionGetInfo(callerSecuritySession, &mySession, &sessionInfo);
```

The session ID itself is an integer value that persists for the duration of the login session; see [Identifying Login Sessions](Root%20and%20Login%20Sessions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgiydqljrga3tiojy) for additional information. The attribute bits parameter is an integer bitmask value that provides additional information about the session, such as whether it is the root session and whether it has an available console. See the header files for a description of the available bit constants.

The Core Graphics framework relies on the presence of the window server and thus is available only to applications running in a login session. This framework includes the `CGSessionCopyCurrentDictionary` function for getting information about the current login session, including the user ID and name.

The following example shows you how to get login session information using the `CGSessionCopyCurrentDictionary` function. This function returns a dictionary with several keys that you can read to get the information you need.

```c
#include <CoreFoundation/CoreFoundation.h>
#include <ApplicationServices/ApplicationServices.h>

CFStringRef shortUserName;
CFNumberRef userUID;
CFBooleanRef userIsActive;
CFBooleanRef loginCompleted;

int MyCGGetSessionInfo
{
    CFDictionaryRef sessionInfoDict;

    sessionInfoDict = CGSessionCopyCurrentDictionary();
    if (sessionInfoDict == NULL)
    {
        printf(“Unable to get session dictionary.”);
        return(1);
    }

    shortUserName = CFDictionaryGetValue(sessionInfoDict,
                                        kCGSessionUserNameKey);
    userUID = CFDictionaryGetValue(sessionInfoDict,
                                        kCGSessionUserIDKey);
    userIsActive = CFDictionaryGetValue(sessionInfoDict,
                                        kCGSessionOnConsoleKey);
    loginCompleted = CFDictionaryGetValue(sessionInfoDict,
                                        kCGSessionLoginDoneKey);
}
```


Prior to the introduction of fast user switching, distributed notifications sent using either the Core Foundation or Cocoa interfaces were delivered to any process that registered as an observer. With the introduction of fast user switching in OS X v10.3, the existing interfaces have changed to limit distribution to registered processes in the current login session. This change should not affect the behavior of most applications. For those applications that might be affected, new interfaces have been added for distributing notifications across login session boundaries.

If you need to send a distributed notification to other processes, you should generally do so only to processes in the current login session. However, there may be cases where you need to send a notification to all processes, regardless of their corresponding login session. For example, changes to system-global settings affect all applications that rely on those settings.

In Core Foundation, the `CFNotificationCenterPostNotificationWithOptions` function allows you to post notifications to all login sessions. To use this function for global notifications, pass the `kCFNotificationPostToAllSessions` constant to the `options` parameter.

In Cocoa, the `postNotificationName:object:userInfo:options:` method of the NSDistributedNotificationCenter object allows you to post notifications to all login sessions. To use this function for global notifications, pass the `NSNotificationPostToAllSessions` constant to the `options` parameter.

The use of global notifications should be minimized whenever possible. If you need to identify the login session that originated a notification, put its session ID into the user information dictionary of the notification. For more information on getting the session ID, see [Getting Login Session Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgiydsljrga2demjz).

The handler for a global notification must be prepared to handle that notification even when it comes from a different login session. If your handler assumes the notification originated in the same login session, your application could experience problems in a fast user switched environment. Fortunately, existing methods for distributing notifications limit the scope of delivery to the current login session. Applications that need to send global notifications must be modified to send those notifications explicitly with interfaces introduced in OS X version 10.3.

If you set up your application to receive a particular global notification, keep in mind that you may not need to handle all instances of that notification. For example, a daemon in the root session might use a global notification to communicate with a process in the active session. In this situation, use of a global notification is preferable because the daemon does not have any knowledge of programs in the login sessions. By broadcasting to all sessions, the notification is guaranteed to reach the active session. Applications in inactive sessions would simply ignore the notification.

If the need arises, you can tell OS X not to run your application in more than one login session. This option should be avoided if possible; however, if you are unable to get your application running suitably in multiple login sessions, you might consider using it.

To disable multiple-session support for your application, include the LSMultipleInstancesProhibited key in your application’s information property list. If this key is present and set to true, Launch Services denies attempts to launch a second instance of your application, in any login session. This key works both for launching your application across multiple sessions and for launching a second instance of your application in the same session. In both cases, Launch Services returns an error to the calling process indicating the reason for the failure.

For details on how to use the LSMultipleInstancesProhibited key, see “Property List Key Reference” in _[Runtime Configuration Guidelines](../Runtime%20Configuration%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3ta2i)_.

[Next](User%20Switch%20Notifications.md)[Previous](Root%20and%20Login%20Sessions.md)

