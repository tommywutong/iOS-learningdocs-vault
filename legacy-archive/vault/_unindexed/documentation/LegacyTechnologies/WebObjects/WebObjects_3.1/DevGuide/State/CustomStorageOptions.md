---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/CustomStorageOptions.html
archived_at: '2026-07-15T07:47:44.382176Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](StateInCookies.md)

# Custom State Storage Options

WebObjects provides direct support for storing state in the application, in the page, and in cookies. In addition, you can implement your own state storage---for example, you might want to store state in a file or database. The SessionStores application provides an example of a state storage mechanism that uses the filesystem. Let's take a look at how it's done.

In WebObjects, an application saves and restores sessions by sending the session store object these messages:

- saveSession:
- restoreSession

This is the minimum interface that a custom session store must present to the application object. In the SessionStores example, the custom storage class FileSessionStore presents this interface:

```objc
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
    archiveDirectory = [WOApp pathForResourceNamed:@"SessionArchives" ofType:nil];
    return self;
}

- archiveFileForSessionID:aSessionID {
    return [NSString stringWithFormat:@"%@/%@", archiveDirectory, aSessionID];
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
    restoredSession = [NSUnarchiver unarchiveObjectWithData:archivedSession];
    return restoredSession;
}

- saveSession:aSession {
    id request = [[WOApp context] request];

    // Store data corresponding to session only if necessary.
    if (![aSession isTerminating] && ![request isFromClientComponent]) {
      id sessionData = [NSArchiver archivedDataWithRootObject:aSession];
      id sessionFilePath = [self archiveFileForSessionID:[aSession sessionID]];
      [sessionData writeToFile:sessionFilePath atomically:YES];
    }
}

@end
```

As you can see, when the FileSessionStore receives a __saveSession:__ message, it checks to see if the session object needs to be archived, and if so, it asks NSArchiver to create a binary archive of the session object and all of the components it contains. It then invokes its own __archiveFileForSessionID:__ to determine the path for the archive file. Finally, it writes the data to the file. Notice that the session data is written to a file whose name is the session ID itself.

FileSessionStore __restoreSession__ is responsible for restoring the state for a particular session. An interesting point in the __restoreSession__ method implementation is the __setDistributionEnabled:__ message to the application object. By enabling distribution, you let any instance of the application process handle a request. (See _Serving WebObjects_ for information on using multiple application instances as a means of load balancing.) More specifically, if distribution is enabled, the application instance number is not appended to the response URL. Since session state is store in the file system and not in the application's memory, it's possible for any application instance to handle any request.

[!Table of Contents](ManagingState.book.md)
[!Next Section](StateForCustomObjects.md)
