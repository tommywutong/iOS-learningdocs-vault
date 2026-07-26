---
title: CFFileDescriptor
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cffiledescriptor
source_url: 'https://developer.apple.com/documentation/corefoundation/cffiledescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cffiledescriptor.json'
content_hash: 'sha256:5af4b1a798a00193'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFFileDescriptor

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFFileDescriptor
```

## Overview

The CFFileDescriptor provides an opaque type to monitor file descriptors for read and write activity via CFRunLoop.

You use CFFileDescriptor to monitor file descriptors for read and write activity via CFRunLoop using callbacks. Each call back is one-shot, and must be re-enabled if you want to get another one.

You can re-enable the callback in the callback function itself, but you must completely service the file descriptor before doing so. For example, if you create a CFFileDescriptor for a pipe and get a callback because there are bytes to be read, then if you don’t read all of the bytes but nevertheless re-enable the CFFileDescriptor for read activity, you’ll get called back again immediately.

You can monitor kqueue file descriptors for read activity to find out when an event the kqueue is filtering for has occurred. You are responsible for understanding the use of the kevent() API and inserting and removing filters from the kqueue file descriptor yourself.

The following example takes a UNIX process ID as argument, and watches up to 20 seconds, and reports if the process terminates in that time:

```objc
// cc test.c -framework CoreFoundation -O
#include <CoreFoundation/CoreFoundation.h>
#include <unistd.h>
#include <sys/event.h>
static void noteProcDeath(CFFileDescriptorRef fdref, CFOptionFlags callBackTypes, void *info) {
    struct kevent kev;
    int fd = CFFileDescriptorGetNativeDescriptor(fdref);
    kevent(fd, NULL, 0, &kev, 1, NULL);
    // take action on death of process here
    printf("process with pid '%u' died\n", (unsigned int)kev.ident);
    CFFileDescriptorInvalidate(fdref);
    CFRelease(fdref); // the CFFileDescriptorRef is no longer of any use in this example
}
// one argument, an integer pid to watch, required
int main(int argc, char *argv[]) {
    if (argc < 2) exit(1);
    int fd = kqueue();
    struct kevent kev;
    EV_SET(&kev, atoi(argv[1]), EVFILT_PROC, EV_ADD|EV_ENABLE, NOTE_EXIT, 0, NULL);
    kevent(fd, &kev, 1, NULL, 0, NULL);
    CFFileDescriptorRef fdref = CFFileDescriptorCreate(kCFAllocatorDefault, fd, true, noteProcDeath, NULL);
    CFFileDescriptorEnableCallBacks(fdref, kCFFileDescriptorReadCallBack);
    CFRunLoopSourceRef source = CFFileDescriptorCreateRunLoopSource(kCFAllocatorDefault, fdref, 0);
    CFRunLoopAddSource(CFRunLoopGetMain(), source, kCFRunLoopDefaultMode);
    CFRelease(source);
    // run the run loop for 20 seconds
    CFRunLoopRunInMode(kCFRunLoopDefaultMode, 20.0, false);
    return 0;
}
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a CFFileDescriptor

- [CFFileDescriptorCreate](<cffiledescriptorcreate(__________).md>) — Creates a new CFFileDescriptor.

### Getting Information About a File Descriptor

- [CFFileDescriptorGetNativeDescriptor](<cffiledescriptorgetnativedescriptor(__).md>) — Returns the native file descriptor for a given CFFileDescriptor.
- [CFFileDescriptorIsValid](<cffiledescriptorisvalid(__).md>) — Returns a Boolean value that indicates whether the native file descriptor for a given CFFileDescriptor is valid.
- [CFFileDescriptorGetContext](<cffiledescriptorgetcontext(____).md>) — Gets the context for a given CFFileDescriptor.

### Invalidating a File Descriptor

- [CFFileDescriptorInvalidate](<cffiledescriptorinvalidate(__).md>) — Invalidates a CFFileDescriptor object.

### Managing Callbacks

- [CFFileDescriptorEnableCallBacks](<cffiledescriptorenablecallbacks(____).md>) — Enables callbacks for a given CFFileDescriptor.
- [CFFileDescriptorDisableCallBacks](<cffiledescriptordisablecallbacks(____).md>) — Disables callbacks for a given CFFileDescriptor.

### Creating a Run Loop Source

- [CFFileDescriptorCreateRunLoopSource](<cffiledescriptorcreaterunloopsource(______).md>) — Creates a new runloop source for a given CFFileDescriptor.

### Getting the CFFileDescriptor Type ID

- [CFFileDescriptorGetTypeID](<cffiledescriptorgettypeid().md>) — Returns the type identifier for the CFFileDescriptor opaque type.

### Data Types

- [CFFileDescriptorNativeDescriptor](cffiledescriptornativedescriptor.md) — Defines a type for the native file descriptor.
- [CFFileDescriptorCallBack](cffiledescriptorcallback.md) — Defines a structure for a callback for a CFFileDescriptor.
- [CFFileDescriptorContext](cffiledescriptorcontext.md) — Defines a structure for the context of a CFFileDescriptor.

### Constants

- [Callback Identifiers](1477595-callback-identifiers.md) — Constants that identify the read and write callbacks.

## See Also

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
