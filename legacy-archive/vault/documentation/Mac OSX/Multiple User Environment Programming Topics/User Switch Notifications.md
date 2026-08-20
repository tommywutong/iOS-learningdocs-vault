---
title: Multiple User Environment Programming Topics
apple_id: 10000180i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPMultipleUsers/Concepts/UserSwitchNotifications.html
archived_at: '2026-07-15T08:16:26.691361Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Multiple User Environment Programming Topics](Introduction%20to%20Multiple%20User%20Environments.md)


[Next](Document%20Revision%20History.md)[Previous](Supporting%20Fast%20User%20Switching.md)

# User Switch Notifications

When a user switch occurs, OS X generates events for all interested applications. Events are sent to applications in a login session whenever the login session is activated or deactivated. If a login session is not being activated or deactivated, it receives no events. You can use the activation events to perform the following kinds of tasks:

- Halt or restart sound playback
- Halt or restart animations
- Give up or acquire shared resources
- Put your application into a quiescent state to improve overall system performance

For Carbon applications, user switch notifications come through the Carbon Event Manager. Applications can register to receive the `kEventSystemUserSessionActivated` and `kEventSystemUserSessionDeactivated` events if they want to know when a switch occurs. The following example shows you how to register for these events:

```
pascal OSStatus switchEventsHandler (EventHandlerCallRef nextHandler,
                                        EventRef switchEvent,
                                        void* userData)
{
    if (GetEventKind(switchEvent)== kEventSystemUserSessionDeactivated)
    {
        // Perform deactivation tasks here.
    }
    else
    {
        // Perform activation tasks here.
    }

    return noErr;
}

void SwitchEventsRegister()
{
    EventTypeSpec switchEventTypes[2];
    EventHandlerUPP switchEventHandler;

    switchEventTypes[0].eventClass = kEventClassSystem;
    switchEventTypes[0].eventKind = kEventSystemUserSessionDeactivated;
    switchEventTypes[1].eventClass = kEventClassSystem;
    switchEventTypes[1].eventKind = kEventSystemUserSessionActivated;

    switchEventHandler = NewEventHandlerUPP(switchEventsHandler);
    InstallApplicationEventHandler(switchEventHandler, 2,
                                    switchEventTypes, NULL, NULL);
}
```


For Cocoa applications, user switch notifications come through the NSWorkspace shared notification center. The user-switch events themselves are defined in NSWorkspace and are `NSWorkspaceSessionDidBecomeActiveNotification` and `NSWorkspaceSessionDidResignActiveNotification`. To register for these notifications, your application (or its delegate) would provide a handler method and then register that handler by adding itself as an observer of the notification. The following sample methods illustrate how to do this:

```objc
- (void) switchHandler:(NSNotification*) notification
{
    if ([[notification name] isEqualToString:
                NSWorkspaceSessionDidResignActiveNotification])
    {
        // Perform deactivation tasks here.
    }
    else
    {
        // Perform activation tasks here.
    }
}

// Register the handler
- (void) applicationDidFinishLaunching:(NSNotification*) aNotification
{
    [[[NSWorkspace sharedWorkspace] notificationCenter]
            addObserver:self
            selector:@selector(switchHandler:)
            name:NSWorkspaceSessionDidBecomeActiveNotification
            object:nil];

    [[[NSWorkspace sharedWorkspace] notificationCenter]
            addObserver:self
            selector:@selector(switchHandler:)
            name:NSWorkspaceSessionDidResignActiveNotification
            object:nil];
}
```


User switch notifications are sent to applications at the same time the switch occurs. Because the switch occurs relatively quickly, this is normally not a problem. However, it is possible for an application to receive its activation event before other applications have received their deactivation events. This could lead to potential race conditions between applications releasing and acquiring shared resources.

To avoid race conditions, applications in the session being deactivated should continue to release any shared resources as soon as possible. Applications in the session being activated should delay the acquisition of any shared resources until those resources are actually used. Not only can this help avoid potential race conditions, it can also improve overall system performance. If your application needs a particular resource right away but encounters errors while trying to acquire it, set a timer and try to acquire the resource again a short time later.

Shutdown and restart sequences do not generate any special notifications to switched out login sessions. Without fast user switching enabled, the normal sequence is to notify the user’s applications about the impending termination and give them a chance to abort the sequence. However, with fast user switching enabled, only the applications for the active user are prompted. Applications in switched out login sessions are killed without the chance to save any changes; otherwise, there is the potential that a process in one of those sessions could hang the system.

If other users are logged in, the system warns the initiator of a shutdown or restart sequence that those users might lose unsaved changes. This warning only appears when other users are logged in. The user is prompted for an administrative password to ensure that there is a good reason to shutdown or restart the machine. As long as the user has a valid administrator password, the sequence proceeds.

For more information about the shutdown and restart sequence for the active login session, see _[Daemons and Services Programming Guide](../Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_.

[Next](Document%20Revision%20History.md)[Previous](Supporting%20Fast%20User%20Switching.md)

