---
title: Core Foundation Release Notes for OS X v10.9
apple_id: TP40000994
resource_type: Release Note
platform: macOS
topic: null
technology: CoreFoundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/releasenotes/CoreFoundation/RN-CoreFoundation/index.html
archived_at: '2026-07-18T02:50:22.951843Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Core Foundation Release Notes for OS X v10.9

Document Generated: 2013-11-08 18:52:43 -0800

OS X Release Notes Copyright © 2013 Apple Inc. All Rights Reserved.

### OS X 10.9 Release Notes CoreFoundation Framework

CoreFoundation (aka CF) is a framework that provides C APIs for strings, collections, user preferences, property lists, plug-ins, bundles, notifications, runloop, and so forth. These APIs are designed with portability, performance, and consistency in mind, and are available to Cocoa and Carbon applications.

CoreFoundation is accessible directly as a public framework. But it is also within the CoreServices umbrella framework and is very often pulled into your application simply by linking against CoreServices or one of the higher-level umbrellas, such as Cocoa, which bring in CoreServices.

### CFURL

The "file" URL scheme is defined so that no authority, an empty host, and "localhost" all mean the end-user's machine. To reduce memory use, file URL objects created with file system paths or from file system representation no longer include the host string "localhost".

This change means CFURLCopyHostName no longer returns the string "localhost" for file URLs and will instead return NULL, and CFURLGetByteRangeForComponent will return kCFNotFound for kCFURLComponentHost.

The use of kCFURLHFSPathStyle is deprecated. The Carbon File Manager, which uses HFS style paths, is deprecated. HFS style paths are unreliable because they can arbitrarily refer to multiple volumes if those volumes have identical volume names. You should instead use kCFURLPOSIXPathStyle wherever possible.

CFURLIsFileReferenceURL() has been added to allow identification of file reference URLs.

CFURLCreateFromFSRef() and CFURLGetFSRef() are deprecated because the Carbon File Manager is deprecated.

URL objects created from URL strings where the URL string length was exactly 1 can no longer be created with characters not allowed in URL strings. This change affects CFURL's CFURLCreateWithString(), and the NSURL methods -initWithString:, -initWithString:relativeToURL:, +URLWithString:, and +URLWithString:relativeToURL:.

The descriptions of long URLs with the data scheme may be truncated if the data URL is very large.

### CFURLAccess

CFURLAccess has been deprecated. The suggested replacement for URLs with network schemes (http, https, ftp, data) is NSURLConnection, or better yet, the new NSURLSession APIs. The suggested replacement for URLs with the file scheme are the foundation classes NSFileManager, NSFileHandle and NSURL, or the CoreFoundation classes CFStream and CFURL.

### CFPreferences support for Security Application Groups (Sandboxing)

For applications that are part of a Security Application Group, domains matching the name of a security application group entitlement on the app will be shared among all applications in the group, and stored in the group container (this only applies to kCFPreferencesCurrentUser).

### Behavioral changes to CFPreferencesGetAppBooleanValue and CFPreferencesGetAppIntegerValue

CFPreferences has been updated to match NSUserDefault's behavior in parsing. Specifically, "1" and "0" will now be interpreted as their corresponding boolean values if looked up via CFPreferencesGetAppBooleanValue, boolean values will be interpreted as 0 or 1 when looked up via CFPreferencesGetAppIntegerValue, and float or double values will be truncated when returned from CFPreferencesGetAppIntegerValue. However, in the case of float to int, the "exists and has valid format" out argument will be false.

### CFString

The options argument for CFStringFold was changed from CFOptionFlags to CFStringCompareFlags.

For applications built against the 10.9 SDK, backing store for CFString objects with 8-bit content has been changed to ASCII, which means more requests to CFStringGetCStringPtr() will succeed. It also means that more CFString objects may end up with UTF-16 backing store. This change may, in rare circumstances, cause compatibility problems, since some CFStringGetCStringPtr() calls that used to succeed may now return NULL. (However, a large number of those may already have been returning NULL in other user languages.)

### CFStringGetCStringPtr Warning

Following up on the previous paragraph, we want to provide a gentle reminder that the function CFStringGetCStringPtr() may return NULL for a variety of reasons that may vary from release to release, or actually from user language to user language, and due to other factors that are outside of the control of the application.

Just because you observe CFStringGetCStringPtr() returning a non-NULL value for a given string, it does not mean that it will not return NULL for the same string in the future or under different circumstances.

So, please, anytime you call CFStringGetCStringPtr(), follow it with a call to CFStringGetCString() in case of a NULL return:

```
char buffer[BUFSIZE];
const char *ptr = CFStringGetCStringPtr(str, encoding);
if (ptr == NULL) {
    if (CFStringGetCString(str, buffer, BUFSIZE, encoding)) ptr = buffer;
}
```

Or better yet just call CFStringGetCString() without bothering with CFStringGetCStringPtr().

Note that CFStringGetCString() may also fail, but that will happen deterministically, and only on two circumstances: The conversion from the UniChar contents of CFString to the specified encoding is not possible, or the buffer is too small.
