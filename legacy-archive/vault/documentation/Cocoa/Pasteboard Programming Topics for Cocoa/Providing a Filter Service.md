---
title: Pasteboard Programming Topics for Cocoa
apple_id: 10000068i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2009-01-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CopyandPaste/Articles/pbCreatingFilters.html
archived_at: '2026-07-15T07:13:51.946277Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Pasteboard Programming Topics for Cocoa](Introduction%20to%20Pasteboards%20Programming%20Topics.md)


[Next](Document%20Revision%20History.md)[Previous](Filter%20Services.md)

# Providing a Filter Service

You implement a filter service very much like a system service. See [System Services](../Services%20Implementation%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydc2i) for details on how services generally work. The following sections focus on issues specific to filter services.

Like system services, filter services are defined with an `NSServices` property in the filter’s information property list file (`Info.plist`). Filter services, though, do not show up in the Services menu, so you do not need to have `NSMenuItem` and `NSKeyEquivalent` entries in the definition.

Because data is moving both in and out of the filter service, you must have entries for both `NSSendTypes` and `NSReturnTypes` in the filter definition. You indicate send and return types as either `NSTypedFilenamesPboardType:`_fileType_ when you want file names and `NSTypedFileContentsPboardType:`_fileType_ when you want file contents, where _fileType_ is either a file name extension or an encoded HFS type, for example:

```
NSSendTypes = (NSTypedFilenamesPboardType:tiff);
NSSendTypes = (NSTypedFileContentsPboardType:’MooV’);
```

Finally, instead of an NSMessage entry, which identifies the method to invoke, filter services contain an equivalent `NSFilter` entry. The invoked method is _filterName_`:userData:error:`, where _filterName_ is the value of the `NSFilter` entry. The method accepts a pasteboard, converts the contents of the pasteboard to the requested type or types, and returns the converted data on the pasteboard.

The method identified by the `NSFilter` property is sent to the filter application’s service provider object, which you register with the pasteboard server using the function `NSRegisterServicesProvider` when the filter service is launched. This function’s declaration is:

```
void NSRegisterServicesProvider(id provider, NSString *name)
```

_provider_ is the object that provides the services, and _name_ is the same value you specify for the `NSPortName` entry in the services specification. `NSPortName` is usually the filter application’s name. After calling `NSRegisterServicesProvider`, the filter service must enter the run loop to respond to service requests. The filter’s `main` function may look like this:

```
int main (int argc, const char *argv[])
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    ServiceTest *serviceProvider = [[ServiceTest alloc] init];

    NSRegisterServicesProvider(serviceProvider, @"SimpleService");

    NS_DURING
        [[NSRunLoop currentRunLoop] run];
    NS_HANDLER
        NSLog(@"Received exception: %@", localException);
    NS_ENDHANDLER

    [serviceProvider release];
    [pool release];
    return 0;
}
```

If the _serviceProvider_ object implements the method `convertData:userData:error:`, the filter’s `Info.plist` file may contain the following service specification:

```
NSServices = (
    {
        NSFilter = "convertData";
        NSPortName = SimpleService;
        NSSendTypes = (NSTypedFilenamesPboardType:gif);
        NSReturnTypes = (NSTIFFPboardType);
    }
);
```

The filter service bundle should have a `.service` extension and be installed in the `Library/Services` directory in one of the file system domains—System, Network, Local, or User. (See _System Overview_ for details on file-system domains.) The list of available services is created each time a user logs into the computer, so you must log out and back in before a newly-installed service is available.

A filter service can use data-transfer mechanisms other than the pasteboard, indicated by an optional entry in the filter service specification. The key is `NSInputMechanism`, and it can have a value of `NSUnixStdio`, `NSMapFile`, or `NSIdentity`. If you specify an input mechanism, the value for the `NSFilter` entry is ignored (though it is still required).

`NSUnixStdio` allows you to turn nearly any command-line program into a filter service. Instead of sending an Objective-C message to an object in your filter service program, the services facility simply runs the executable specified in the service specification with the contents of the pasteboard as the argument (which must be of `NSFilenamesPboardType` or `NSTypedFilenamesPboardType`). If there is more than one filename on the pasteboard, only the first is used. The output of the filter program (on `stdout`) is captured by the services facility and put on a pasteboard for use by the requestor of the filter. Note that the program must be relaunched every time the service is invoked; if you are creating a filter service from scratch it is more efficient to package it as an application that can remain running. Here is a sample service specification for a program that converts GIF images to TIFF:

```
NSServices = (
    {
        NSFilter = "";
        NSPortName = gif2tiff;
        NSInputMechanism = NSUnixStdio;
        NSSendTypes = (NSTypedFilenamesPboardType:gif);
        NSReturnTypes = (NSTIFFPboardType);
    }
);
```


`NSMapFile` defines an “empty” service for data in files, used when you invoke NSPasteboard’s `pasteboardByFilteringFile:` class method. Its value must be an `NSFilenamesPboardType` or an `NSTypedFilenamesPboardType`. When the filter service is invoked for a file, the services facility merely puts the contents of the file on the pasteboard. This input mechanism is useful for file types with nonstandard or special extensions whose format is nonetheless the same as a standard type. For example, if you have defined an image format based on a subset of TIFF and given it a file extension of `stif`, you can define a service that maps the `stif` file extension to `NSTIFFPboardType`:

```
NSServices = (
    {
        NSFilter = "";
        NSInputMechanism = NSMapFile;
        NSSendTypes = (NSTypedFilenamesPboardType:stif);
        NSReturnTypes = (NSTIFFPboardType);
    }
);
```

`NSMapFile` does not result in any program being executed, so its service specification lacks the `NSPortName` entry.

`NSIdentity` defines an empty service for data in memory, used when you invoke NSPasteboard’s `pasteboardByFilteringData:ofType:` class method. It declares that the send type is effectively identical to the return type—though the reverse is not necessarily true. For example, you can define a service that filters your custom image format in memory with this service specification:

```
NSServices = (
    {
        NSFilter = "";
        NSInputMechanism = NSIdentity;
        NSSendTypes = (MyCustomImagePboardType);
        NSReturnTypes = (NSTIFFPboardType);
    }
);
```

`NSIdentity` does not result in any program being executed, so its service specification lacks the `NSPortName` entry.

[Next](Document%20Revision%20History.md)[Previous](Filter%20Services.md)

