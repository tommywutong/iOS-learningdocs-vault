---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/CustomStorageOptions.html
archived_at: '2026-07-15T07:52:15.365924Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](StateInCookies.md)

### Custom State-Storage Options

If the provided state-storage strategies are insufficient for your needs, you can implement your own state storage. For example, you might want to store state in a file or database. The SessionStores application provides an example of a state-storage mechanism that uses the file system. Let's take a look at how it's done.
In WebObjects, an application saves and restores sessions by sending the session store object these messages:

- saveSession:
- restoreSession

This is the minimum interface that a custom session store must present to the application object. In the WebScript version of the SessionStores example, the custom storage class FileSessionStore presents this interface:

```objc
    // WebScript StateStorage FileSessionStore.wos
    @interface FileSessionStore:NSObject  {
        id archiveDirectory;
    }
    - init;
    - archiveFileForSessionID:aSessionID;
    - archiveForSessionID:aSessionID;
    - restoreSession;
    - saveSession:aSession;
    @end
```


These methods have the following implementation:

```objc
    @implementation FileSessionStore

    - init {
        self = [super init];
        archiveDirectory = [WOApp pathForResourceNamed:@"SessionArchives"
            ofType:nil];
        return self;
    }

    - archiveFileForSessionID:aSessionID {
        return [NSString stringWithFormat:@"%@/%@", archiveDirectory,
            aSessionID];
    }

    - archiveForSessionID:aSessionID {
        id archiveFile = [self archiveFileForSessionID:aSessionID];
        return [NSData dataWithContentsOfFile:archiveFile];
    }

    - restoreSession {

        id request = [[WOApp context] request];
        id archivedSession;
        id restoredSession;

        // Allow requests in this session to go to any application instance.
        [[WOApp context] setDistributionEnabled:YES];

        // Get archived session (as an NSData object)
        archivedSession = [self archiveForSessionID:[request sessionID]];

        // Unarchive session
        restoredSession = [NSUnarchiver
            unarchiveObjectWithData:archivedSession];

        return restoredSession;
    }

    - saveSession:aSession {
        id request = [[WOApp context] request];

        // Store data corresponding to session only if necessary.
        if (![aSession isTerminating] && ![request isFromClientComponent]) {
            id sessionData = [NSArchiver
                archivedDataWithRootObject:aSession];
            id sessionFilePath = [self archiveFileForSessionID:[aSession
                sessionID]];

            [sessionData writeToFile:sessionFilePath atomically:YES];
        }
    }

    @end
```


As you can see, when the FileSessionStore receives a saveSession: message, it checks whether the session object needs to be archived, and if so, it asks NSArchiver to create a binary archive of the session object and all of the components it contains. It then invokes its own archiveFileForSessionID: to determine the path for the archive file. Finally, it writes the data to the file. Notice that the session data is written to a file whose name is the session ID itself.
In this implementation, restoreSession restores the state for a particular session. An interesting point in the restoreSession method implementation is the setDistributionEnabled: message to the WOContext object (Context in Java). This method enables application load balancing. As you learned in the earlier section ["State in the Server"](StateInServer.md#apple-g4ztc), when state is stored in the server, all requests from a particular session must access the same application instance on the same machine. In this example, because session state is stored in the file system and not in the application's memory, any application instance can handle any request. The __setDistributionEnabled:__ method enables application load balancing by allowing any application instance to respond to any request.

Note that the Foundation classes NSArchiver and NSUnarchiver aren't provided in the Java next.util package and that the WebSession and Component classes don't implement the Serializable or the Externalizable interface. For these reasons, you can't implement storing state in the file system in Java. If you want to store Java objects in the file system, you can do so if they implement the Coding interface, but you must write your equivalent of the FileSessionStore class in WebScript or Objective-C.

[!Table of Contents](StateTOC.md) [!Next Section](StateForCustomObjects.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
