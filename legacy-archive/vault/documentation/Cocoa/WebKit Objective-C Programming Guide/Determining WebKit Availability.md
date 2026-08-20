---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/WebKitAvail.html
archived_at: '2026-07-15T07:14:56.285575Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Accessing%20WebKit%20From%20Carbon%20Applications.md)

# Determining WebKit Availability

On OS X v10.2, the WebKit framework and the URL Loading system is only available on systems that have installed Safari 1.0. This article explains how a Mach-O application that use the WebKit framework or the URL Loading system, can run effectively on versions of OS X that don't have Safari 1.0 installed.

If a user runs your application on a system that does not have the appropriate frameworks installed it will fail to launch, or crash at some point during execution. In order to prevent this you must take some precautions in your project.

The URL Loading system is available as of version 462.6 of the Foundation framework. To determine if the classes are available you can test the `NSFoundationVersionNumber` of the installed Foundation framework.

The example code in Listing 1 will return `YES` if the URL Loading system is available.

__Listing 1__  Determining if the URL Loading system is available

```objc
+ (BOOL)isURLLoadingAvailable
{
    return (NSFoundationVersionNumber >= 462.6);
}
```


An application can test for the availability of WebKit by attempting to create a bundle for the framework using `NSBundle`. If the framework exists, the application can use the `load` method to dynamically load the framework.

The example code in Listing 2 will return `YES` if the framework is installed and loads successfully.

__Listing 2__  Determining if the WebKit framework is available

```objc
+ (BOOL)isWebKitAvailable
{
    static BOOL _webkitAvailable=NO;
    static BOOL _initialized=NO;

    if (_initialized)
        return _webkitAvailable;

    NSBundle* webKitBundle;
    webKitBundle = [NSBundle bundleWithPath:@"/System/Library/Frameworks/WebKit.framework"];
    if (webKitBundle) {
        _webkitAvailable = [webKitBundle load];
    }
    _initialized=YES;

    return _webkitAvailable;
}
```


Simply testing the version of the Foundation framework or if the WebKit framework is installed is not sufficient. If the application contains WebKit or URL Loading system symbols it can fail before it's able to execute the test code and inform the user of the problem.

The application must ensure that the main bundle does not include any symbols that may not be available at launch.

One solution is to separate your WebKit dependent code into a bundle and load it only after determining that the framework is available.

You start by creating a new Bundle target in your application's Xcode project. This target should contain all your code that directly references WebKit classes, globals and types and is should be set to link against WebKit.framework.

Your main application target in Project Builder should specify that it is dependent on the bundle and copy it to the application directory at compile time. Your application then checks the availability of the WebKit framework and, if present, uses `NSBundle` or `CFBundle` to dynamically load the code.

OS X v10.2 introduced support for weak linking in Mach-O applications. It works in a similar manner to the traditional Mac OS' Code Fragment Manager’s weak, or soft imports.

Due to the dynamic nature of Objective-C it is possible to avoid using linked symbols for class names by creating an instance of a class using the [NSClassFromString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSClassFromString) function.

```
Class webDownloadClass=NSClassFromString(@"WebDownload");
WebDownload *download=[[webDownloadClass alloc] initWithRequest:theRequest delegate:self];
```

This is equivalent to the following code that explicitly uses the [WebDownload](https://developer.apple.com/documentation/webkit/webdownload) class.

```
WebDownload *download=[[WebDownload alloc] initWithRequest:theRequest delegate:self];
```

Depending on your usage, it may also be necessary to dynamically load WebKit constants using `CFBundle` after determining that the framework is available. The example code in Listing 3 demonstrates testing for the framework and loading a WebKit constant using [CFBundleCreate](https://developer.apple.com/documentation/corefoundation/1537154-cfbundlecreate).

__Listing 3__  Loading WebKit constants dynamically using CFBundle

```
 CFURLRef url = CFURLCreateWithFileSystemPath(NULL,
                          CFSTR("/System/Library/Frameworks/WebKit.framework"),
                          kCFURLPOSIXPathStyle, TRUE);
    CFBundleRef bundle = CFBundleCreate(NULL, url);
    if (bundle != NULL) {
        NSString **WebHistoryItemsAddedNotificationPointer =
              (NSString **)CFBundleGetDataPointerForName(bundle,
                                 CFSTR("WebHistoryItemsAddedNotification"));
        if (WebHistoryItemsAddedNotificationPointer != NULL) {
            NSLog(@"looked up WebHistoryItemsAddedNotification");
            NSLog(@"location is %x, value is %@", *WebHistoryItemsAddedNotificationPointer, *WebHistoryItemsAddedNotificationPointer);
        } else {
            NSLog(@"found WebKit, but couldn't get the pointer");
        }
    } else {
        NSLog(@"no WebKit installed");
    }
```

See Also: _[SDK Compatibility Guide](../../Developer%20Tools/SDK%20Compatibility%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2i)_.

[Next](Document%20Revision%20History.md)[Previous](Accessing%20WebKit%20From%20Carbon%20Applications.md)

