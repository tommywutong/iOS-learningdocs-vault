---
title: Services Implementation Guide
apple_id: 10000101i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SysServices/Articles/providing.html
archived_at: '2026-07-15T07:19:54.746507Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Services Implementation Guide](Introduction.md)


[Next](Using%20Services.md)[Previous](Services%20Properties.md)

# Providing a Service

Providing a service consists of the following steps:

1. Deciding what the service will do
2. Implementing the service method
3. Registering the service provider
4. Advertising the service by adding it to your application’s property list file
5. Installing the service

For the purposes of this chapter, suppose you have decided to work on a program to read USENET news and have an object with a method to encrypt and decrypt articles, such as the one in Listing 1. News articles containing offensive material are often encrypted with this algorithm, called ROT13, in which letters are shifted halfway through the alphabet. Since this feature is generally useful as a simple encryption scheme, it can be exported to other applications.

__Listing 1__  Text encryption method

```objc
- (NSString *)rotateLettersInString:(NSString *)aString {
    NSString *newString;
    NSUInteger length;
    unichar *buf;
    unsigned i;

    length = [aString length];
    buf = malloc( (length + 1) * sizeof(unichar) );
    [aString getCharacters:buf];
    buf[length] = (unichar)0; // not really needed....
    for (i = 0; i < length; i++) {
        if (buf[i] >= (unichar)'a' && buf[i] <= (unichar) 'z') {
            buf[i] += 13;
            if (buf[i] > 'z') buf[i] -= 26;
        } else if (buf[i] >= (unichar)'A' && buf[i] <= (unichar) 'Z') {
            buf[i] += 13;
            if (buf[i] > 'Z') buf[i] -= 26;
        }
    }
    newString = [NSString stringWithCharacters:buf length:length];
    free(buf);
    return newString;
}
```


To offer the encryption facility as a service, write a method such as the one in Listing 2.

__Listing 2__  Service method

```objc
- (void)simpleEncrypt:(NSPasteboard *)pboard
    userData:(NSString *)userData error:(NSString **)error {

     // Test for strings on the pasteboard.
     NSArray *classes = [NSArray arrayWithObject:[NSString class]];
     NSDictionary *options = [NSDictionary dictionary];

     if (![pboard canReadObjectForClasses:classes options:options]) {
          *error = NSLocalizedString(@"Error: couldn't encrypt text.",
               @"pboard couldn't give string.");
          return;
     }

     // Get and encrypt the string.
     NSString *pboardString = [pboard stringForType:NSPasteboardTypeString];
     NSString *newString = [self rotateLettersInString:pboardString];
     if (!newString) {
          *error = NSLocalizedString(@"Error: couldn't encrypt text.",
               @"self couldn't rotate letters.");
          return;
     }

     // Write the encrypted string onto the pasteboard.
     [pboard clearContents];
     [pboard writeObjects:[NSArray arrayWithObject:newString]];
}
```

The method providing the service is of the form _messageName_`:userData:error:` and takes the values shown in Listing 2. The method itself takes data from the pasteboard as needed, operates on it, and writes any results back to the pasteboard. In case of an error, the method simply sets the pointer given by the error argument to a non-nil `NSString` and returns. The error message is logged to the console. The _userData_ parameter is not used here.

Now you have an object with methods that allow it to perform a service for another application. Next, you need to register the object at run time so the services facility knows which object to have perform the service.

You create and register your object in the `applicationDidFinishLaunching:` application delegate method (or equivalent) with the `setServicesProvider:` method of the `NSApplication` class. If your object is called `encryptor`, you create and register it with this code fragment:

```
EncryptoClass *encryptor;
encryptor = [[EncryptoClass alloc] init];
[NSApp setServicesProvider:encryptor];
```

If you are writing a Foundation tool, which lacks an `NSApplication` object, register the service object with the `NSRegisterServicesProvider` function. Its declaration is the following:

```
void NSRegisterServicesProvider(id provider, NSString *portName)
```

where _provider_ is the object that provides the services, and _portName_ is the same value you specify for the `NSPortName` entry in the `NSServices` property of the application’s information property list (`Info.plist`) file. After making this function call, you must enter the run loop to respond to service requests.

You can register only one service provider per application. If you have more than one service to provide, a single object must provide the interface to all of the services.

Service requests can arrive immediately after you register the object, in some circumstances even before exiting `applicationDidFinishLaunching:`. Therefore, register your service provider only when you are completely ready to process requests.

For the system to know that your application provides a service, you must advertise that fact. You do this by adding an entry to your application project’s `Info.plist` file as described in [Services Properties](Services%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha2telkdjbceurcgjfbq). The entry you add is called the service specification. In our example, the `NSServices` property looks like this:

```
    <key>NSServices</key>
    <array>
        <dict>
            <key>NSKeyEquivalent</key>
            <dict>
                <key>default</key>
                <string>E</string>
            </dict>
            <key>NSMenuItem</key>
            <dict>
                <key>default</key>
                <string>Encrypt Text</string>
            </dict>
            <key>NSMessage</key>
            <string>simpleEncrypt</string>
            <key>NSPortName</key>
            <string>NewsReader</string>
            <key>NSRequiredContext</key>
            <dict/>
            <key>NSRestricted</key>
            <false/>
            <key>NSSendTypes</key>
            <array>
                <string>NSStringPboardType</string>
            </array>
            <key>NSReturnTypes</key>
            <array>
                <string>NSStringPboardType</string>
            </array>
        </dict>
    </array>
```


A service can be offered as part of an application, such as Mail, or as a standalone service—one without a user interface that is intended for use only in the Services menu.

- To build an application that offers a service, use the extension `.app` and install it in the `Applications` folder (or a subfolder).
- To build a standalone service, use the extension `.service` and store it in `Library/Services`.

In either case, you should install it in one of the four file-system domains—System, Network, Local, and User. (See [File-System Domains](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/Domains.html#//apple_ref/doc/uid/20002281) in _File System Overview_ for details.)

The list of available services on the computer is built each time a user logs in. If your service is installed in an `Applications` directory, you need to log out and log back in before the service becomes available. If it’s installed in a `Library/Services` directory, this is not necessary. You can force an update of the list of services without logging out by calling the following function:

```
void NSUpdateDynamicServices(void)
```


When you test your program, it may be useful to trigger an immediate rescan of Services, as if [NSUpdateDynamicServices](https://developer.apple.com/documentation/appkit/1428762-nsupdatedynamicservices) had been called. You can do this from the command line using the `pbs` tool:

```
/System/Library/CoreServices/pbs
```

It may also be useful to be sure that the system has recognized the Service. You can also use the `pbs` tool to list the registered Services by specifying the `dump_pboard` option:

```
/System/Library/CoreServices/pbs -dump_pboard
```

If your Service is recognized by `pbs`, but does not appear in the Services menu, you can use the `NSDebugServices` user default to help determine why. For example, to determine why Mail’s Services appear or do not appear in TextEdit, you can launch TextEdit with the `NSDebugServices` option and pass it the bundle identifier of Mail:

```
/Applications/TextEdit.app/Contents/MacOS/TextEdit -NSDebugServices com.apple.mail
```

When the Services menu is opened, it will log information to the console about why the service does or does not appear.

[Next](Using%20Services.md)[Previous](Services%20Properties.md)

