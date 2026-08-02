---
title: External Accessory Programming Topics
apple_id: TP40009502
resource_type: Guide
platform: iOS
topic: Data Management
technology: ExternalAccessory
published: '2012-02-24'
source_url: https://developer.apple.com/library/archive/featuredarticles/ExternalAccessoryPT/Articles/Connecting.html
archived_at: '2026-07-18T02:28:16.101812Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md) · [External Accessory Programming Topics](About%20External%20Accessories.md)


[Next](Monitoring%20Accessory-Related%20Events.md)[Previous](About%20External%20Accessories.md)

# Connecting to an Accessory

Accessories are not visible through the External Accessory framework until they have been connected by the system and made ready for use. When an accessory does become visible, your app can get the appropriate accessory object and open a session using one or more of the protocols supported by the accessory.

The shared [EAAccessoryManager](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager) object provides the main entry point for apps looking to communicate with accessories. This class contains an array of already connected accessory objects that you can [enumerate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Enumeration.html#//apple_ref/doc/uid/TP40008195-CH17) to see if there is one your app supports. Most of the information in an [EAAccessory](https://developer.apple.com/documentation/externalaccessory/eaaccessory) object (such as the name, manufacturer, and model information) is intended for display purposes only. To determine whether your app can connect to an accessory, you must look at the accessory’s protocols and see if there is one your app supports.

For a given accessory object, only one session at a time is allowed for a specific protocol. The [protocolStrings](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613877-protocolstrings) property of each `EAAccessory` object contains a [dictionary](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10) whose keys are the supported protocols. If you attempt to create a session using a protocol that is already in use, the External Accessory framework closes the existing session before opening the new one.

Listing 1 shows a method that checks the list of connected accessories and grabs the first one that the app supports. It creates a session for the designated protocol and configures the input and output streams of the session. By the time this method returns the session object, it is connected to the accessory and ready to begin sending and receiving data.

__Listing 1__  Creating a communications session for an accessory

```objc
- (EASession *)openSessionForProtocol:(NSString *)protocolString
{
    NSArray *accessories = [[EAAccessoryManager sharedAccessoryManager]
                                   connectedAccessories];
    EAAccessory *accessory = nil;
    EASession *session = nil;

    for (EAAccessory *obj in accessories)
    {
        if ([[obj protocolStrings] containsObject:protocolString])
        {
            accessory = obj;
            break;
        }
    }

    if (accessory)
    {
        session = [[EASession alloc] initWithAccessory:accessory
                                 forProtocol:protocolString];
        if (session)
        {
            [[session inputStream] setDelegate:self];
            [[session inputStream] scheduleInRunLoop:[NSRunLoop currentRunLoop]
                                     forMode:NSDefaultRunLoopMode];
            [[session inputStream] open];
            [[session outputStream] setDelegate:self];
            [[session outputStream] scheduleInRunLoop:[NSRunLoop currentRunLoop]
                                     forMode:NSDefaultRunLoopMode];
            [[session outputStream] open];
            [session autorelease];
        }
    }

    return session;
}
```

After the input and output streams are configured, the final step is to process the stream-related data. Listing 2 shows the fundamental structure of a [delegate’s](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) stream processing code. This method responds to events from both input and output streams of the accessory. As the accessory sends data to your app an event arrives indicating there are bytes available to be read. Similarly, when the accessory is ready to receive data from your app, events arrive indicating that fact. (Of course, your app does not always have to wait for an event to arrive before it can write bytes to the stream. It can also call the stream’s [hasBytesAvailable](https://developer.apple.com/documentation/foundation/inputstream/1409410-hasbytesavailable) method to see if the accessory is still able to receive data.) For more information on streams and handling stream-related events, see _[Stream Programming Guide](../../documentation/Cocoa/Stream%20Programming%20Guide/Introduction%20to%20Stream%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dq2i)_.

__Listing 2__  Processing stream events

```objc
// Handle communications from the streams.
- (void)stream:(NSStream*)theStream handleEvent:(NSStreamEvent)streamEvent
{
    switch (streamEvent)
    {
        case NSStreamHasBytesAvailable:
            // Process the incoming stream data.
            break;

        case NSStreamEventHasSpaceAvailable:
            // Send the next queued command.
            break;

        default:
            break;
    }

}
```

[Next](Monitoring%20Accessory-Related%20Events.md)[Previous](About%20External%20Accessories.md)

