---
title: CFNetwork Programming Guide
apple_id: TP30001132
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: CFNetwork
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/CFStreamTasks/CFStreamTasks.html
archived_at: '2026-07-15T08:18:11.163925Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CFNetwork Programming Guide](Introduction%20to%20CFNetwork%20Programming%20Guide.md)


[Next](Communicating%20with%20HTTP%20Servers.md)[Previous](CFNetwork%20Concepts.md)

# Working with Streams

This chapter discusses how to create, open, and check for errors on read and write streams. It also describes how to read from a read stream, how to write to a write stream, how to prevent blocking when reading from or writing to a stream, and how to navigate a stream through a proxy server.

Core Foundation streams can be used for reading or writing files or working with network sockets. With the exception of the process of creating those streams, they behave similarly.

Start by creating a read stream. Listing 2-1 creates a read stream for a file.

__Listing 2-1__  Creating a read stream from a file

```
CFReadStreamRef myReadStream = CFReadStreamCreateWithFile(kCFAllocatorDefault, fileURL);
```

In this listing, the `kCFAllocatorDefault` parameter specifies that the current default system allocator be used to allocate memory for the stream and the `fileURL` parameter specifies the name of the file for which this read stream is being created, such as `file:///Users/joeuser/Downloads/MyApp.sit`.

Similarly, you can create a pair of streams based on a network service by calling [CFStreamCreatePairWithSocketToCFHost](https://developer.apple.com/documentation/cfnetwork/1426831-cfstreamcreatepairwithsockettocf) (described in [Using a Run Loop to Prevent Blocking](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydemzqfu3demrtgm)) or [CFStreamCreatePairWithSocketToNetService](https://developer.apple.com/documentation/cfnetwork/1426794-cfstreamcreatepairwithsockettone) (described in _[NSNetServices and CFNetServices Programming Guide](../NSNetServices%20and%20CFNetServices%20Programming%20Guide/About%20NSNetServices%20and%20CFNetServices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomzw)_).

Now that you have created the stream, you can open it. Opening a stream causes the stream to reserve any system resources that it requires, such as the file descriptor needed to open the file. Listing 2-2 is an example of opening the read stream.

__Listing 2-2__  Opening a read stream

```
if (!CFReadStreamOpen(myReadStream)) {
    CFStreamError myErr = CFReadStreamGetError(myReadStream);
    // An error has occurred.
        if (myErr.domain == kCFStreamErrorDomainPOSIX) {
        // Interpret myErr.error as a UNIX errno.
        } else if (myErr.domain == kCFStreamErrorDomainMacOSStatus) {
        // Interpret myErr.error as a MacOS error code.
            OSStatus macError = (OSStatus)myErr.error;
        // Check other error domains.
    }
}
```

The `CFReadStreamOpen` function returns `TRUE` to indicate success and `FALSE` if the open fails for any reason. If `CFReadStreamOpen` returns `FALSE`, the example calls the `CFReadStreamGetError` function, which returns a structure of type `CFStreamError` consisting of two values: a domain code and an error code. The domain code indicates how the error code should be interpreted. For example, if the domain code is `kCFStreamErrorDomainPOSIX`, the error code is a UNIX `errno` value. The other error domains are `kCFStreamErrorDomainMacOSStatus`, which indicates that the error code is an `OSStatus` value defined in `MacErrors.h`, and `kCFStreamErrorDomainHTTP`, which indicates that the error code is the one of the values defined by the `CFStreamErrorHTTP` enumeration.

Opening a stream can be a lengthy process, so the `CFReadStreamOpen` and `CFWriteStreamOpen` functions avoid blocking by returning `TRUE` to indicate that the process of opening the stream has begun. To check the status of the open, call the functions `CFReadStreamGetStatus` and `CFWriteStreamGetStatus`, which return `kCFStreamStatusOpening` if the open is still in progress, `kCFStreamStatusOpen` if the open is complete, or `kCFStreamStatusErrorOccurred` if the open has completed but failed. In most cases, it doesn’t matter whether the open is complete because the CFStream functions that read and write will block until the stream is open.

To read from a read stream, call the function `CFReadStreamRead`, which is similar to the UNIX `read()` system call. Both take buffer and buffer length parameters. Both return the number of bytes read, `0` if at the end of stream or file, or `-1` if an error occurred. Both block until at least one byte can be read, and both continue reading as long as they can do so without blocking. Listing 2-3 is an example of reading from the read stream.

__Listing 2-3__  Reading from a read stream (blocking)

```
CFIndex numBytesRead;
do {
    UInt8 buf[myReadBufferSize]; // define myReadBufferSize as desired
    numBytesRead = CFReadStreamRead(myReadStream, buf, sizeof(buf));
    if( numBytesRead > 0 ) {
        handleBytes(buf, numBytesRead);
    } else if( numBytesRead < 0 ) {
        CFStreamError error = CFReadStreamGetError(myReadStream);
        reportError(error);
    }
} while( numBytesRead > 0 );
```


When all data has been read, you should call the `CFReadStreamClose` function to close the stream, thereby releasing system resources associated with it. Then release the stream reference by calling the function `CFRelease`. You may also want to invalidate the reference by setting it to `NULL`. See Listing 2-4 for an example.

__Listing 2-4__  Releasing a read stream

```
CFReadStreamClose(myReadStream);
CFRelease(myReadStream);
myReadStream = NULL;
```


Working with write streams is similar to working with read streams. One major difference is that the function `CFWriteStreamWrite` does not guarantee to accept all of the bytes that you pass it. Instead, `CFWriteStreamWrite` returns the number of bytes that it accepted. You'll notice in the sample code shown in Listing 2-5 that if the number of bytes written is not the same as the total number of bytes to be written, the buffer is adjusted to accommodate this.

__Listing 2-5__  Creating, opening, writing to, and releasing a write stream

```
CFWriteStreamRef myWriteStream =
        CFWriteStreamCreateWithFile(kCFAllocatorDefault, fileURL);
if (!CFWriteStreamOpen(myWriteStream)) {
    CFStreamError myErr = CFWriteStreamGetError(myWriteStream);
    // An error has occurred.
    if (myErr.domain == kCFStreamErrorDomainPOSIX) {
    // Interpret myErr.error as a UNIX errno.
    } else if (myErr.domain == kCFStreamErrorDomainMacOSStatus) {
        // Interpret myErr.error as a MacOS error code.
        OSStatus macError = (OSStatus)myErr.error;
        // Check other error domains.
    }
}
UInt8 buf[] = “Hello, world”;
CFIndex bufLen = (CFIndex)strlen(buf);

while (!done) {
    CFIndex bytesWritten = CFWriteStreamWrite(myWriteStream, buf, (CFIndex)bufLen);
    if (bytesWritten < 0) {
        CFStreamError error = CFWriteStreamGetError(myWriteStream);
        reportError(error);
    } else if (bytesWritten == 0) {
        if (CFWriteStreamGetStatus(myWriteStream) == kCFStreamStatusAtEnd) {
            done = TRUE;
        }
    } else if (bytesWritten != bufLen) {
        // Determine how much has been written and adjust the buffer
        bufLen = bufLen - bytesWritten;
        memmove(buf, buf + bytesWritten, bufLen);

        // Figure out what went wrong with the write stream
        CFStreamError error = CFWriteStreamGetError(myWriteStream);
        reportError(error);

    }
}
CFWriteStreamClose(myWriteStream);
CFRelease(myWriteStream);
myWriteStream = NULL;
```


When using streams to communicate, there is always a chance, especially with socket-based streams, that a data transfer could take a long time. If you are implementing your streams synchronously your entire application will be forced to wait on the data transfer. Therefore, it is highly recommended that your code use alternate methods to prevent blocking.

There are two ways to prevent blocking when reading from or writing to a CFStream object:

- Using a run loop — Register to receive stream-related events and schedule the stream on a run loop. When a stream-related event occurs, your callback function (specified by the registration call) is called.
- Polling — For read streams, find out if there are bytes to read before reading from the stream. For write streams, find out whether the stream can be written to without blocking before writing to the stream.

Each of these approaches is described in the following sections.

The preferred way to use streams is with a run loop. A run loop executes on your main program thread. It waits for events to occur, then calls whatever function is associated with a given event.

In the case of network transfers, your callback functions are executed by the run loop when the event you registered for occurs. This allows you to not have to poll your socket stream, which would slow down the thread.

To learn more about run loops in general, read _[Threading Programming Guide](../../Cocoa/Threading%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2i)_.

This example begins by creating a socket read stream:

```
CFStreamCreatePairWithSocketToCFHost(kCFAllocatorDefault, host, port,
                                   &myReadStream, NULL);
```

where the CFHost object reference, `host`, specifies the remote host with which the read stream is to be made and the `port` parameter specifies the port number that the host uses. The `CFStreamCreatePairWithSocketToCFHost` function returns the new read stream reference in `myReadStream`. The last parameter, `NULL`, indicates that the caller does not want to create a write stream. If you wanted to create a write steam, the last parameter would be, for example, `&myWriteStream`.

Before opening the socket read stream, create a context that will be used when you register to receive stream-related events:

```
CFStreamClientContext myContext = {0, myPtr, myRetain, myRelease, myCopyDesc};
```

The first parameter is `0` to specify the version number. The `info` parameter, `myPtr`, is a pointer to data you want to be passed to your callback function. Usually, `myPtr` is a pointer to a structure you’ve defined that contains information relating to the stream. The `retain` parameter is a pointer to a function to retain the `info` parameter. So if you set it to your function `myRetain`, as in the code above, CFStream will call `myRetain(myPtr)` to retain the `info` pointer. Similarly, the `release` parameter, `myRelease`, is a pointer to a function to release the info parameter. When the stream is disassociated from the context, CFStream would call `myRelease(myPtr)`. Finally, `copyDescription` is a parameter to a function to provide a description of the stream. For example, if you were to call `CFCopyDesc(myReadStream)` with the stream client context shown above, CFStream would call `myCopyDesc(myPtr)`.

The client context also allows you the option of setting the `retain`, `release`, and `copyDescription` parameters to `NULL`. If you set the `retain` and `release` parameters to `NULL`, then the system will expect you to keep the memory pointed to by the `info` pointer alive until the stream itself is destroyed. If you set the `copyDescription` parameter to `NULL`, then the system will provide, if requested, a rudimentary description of what is in the memory pointed to by the `info` pointer.

With the client context set up, call the function `CFReadStreamSetClient` to register to receive stream-related events. `CFReadStreamSetClient` requires that you specify the callback function and the events you want to receive. The following example in Listing 2-6 specifies that the callback function wants to receive the `kCFStreamEventHasBytesAvailable`, `kCFStreamEventErrorOccurred`, and `kCFStreamEventEndEncountered` events. Then schedule the stream on a run loop with the `CFReadStreamScheduleWithRunLoop` function. See Listing 2-6 for an example of how to do this.

__Listing 2-6__  Scheduling a stream on a run loop

```
CFOptionFlags registeredEvents = kCFStreamEventHasBytesAvailable |
        kCFStreamEventErrorOccurred | kCFStreamEventEndEncountered;
if (CFReadStreamSetClient(myReadStream, registeredEvents, myCallBack, &myContext))
{
    CFReadStreamScheduleWithRunLoop(myReadStream, CFRunLoopGetCurrent(),
                                    kCFRunLoopCommonModes);
}
```

With the stream scheduled on the run loop, you are ready to open the stream as shown in Listing 2-7.

__Listing 2-7__  Opening a nonblocking read stream

```
if (!CFReadStreamOpen(myReadStream)) {
    CFStreamError myErr = CFReadStreamGetError(myReadStream);
    if (myErr.error != 0) {
    // An error has occurred.
        if (myErr.domain == kCFStreamErrorDomainPOSIX) {
        // Interpret myErr.error as a UNIX errno.
            strerror(myErr.error);
        } else if (myErr.domain == kCFStreamErrorDomainMacOSStatus) {
            OSStatus macError = (OSStatus)myErr.error;
            }
        // Check other domains.
    } else
        // start the run loop
        CFRunLoopRun();
}
```

Now, wait for your callback function to be executed. In your callback function, check the event code and take appropriate action. See Listing 2-8.

__Listing 2-8__  Network events callback function

```
void myCallBack (CFReadStreamRef stream, CFStreamEventType event, void *myPtr) {
    switch(event) {
        case kCFStreamEventHasBytesAvailable:
            // It is safe to call CFReadStreamRead; it won’t block because bytes
            // are available.
            UInt8 buf[BUFSIZE];
            CFIndex bytesRead = CFReadStreamRead(stream, buf, BUFSIZE);
            if (bytesRead > 0) {
                handleBytes(buf, bytesRead);
            }
            // It is safe to ignore a value of bytesRead that is less than or
            // equal to zero because these cases will generate other events.
            break;
        case kCFStreamEventErrorOccurred:
            CFStreamError error = CFReadStreamGetError(stream);
            reportError(error);
            CFReadStreamUnscheduleFromRunLoop(stream, CFRunLoopGetCurrent(),
                                              kCFRunLoopCommonModes);
            CFReadStreamClose(stream);
            CFRelease(stream);
            break;
        case kCFStreamEventEndEncountered:
            reportCompletion();
            CFReadStreamUnscheduleFromRunLoop(stream, CFRunLoopGetCurrent(),
                                              kCFRunLoopCommonModes);
            CFReadStreamClose(stream);
            CFRelease(stream);
            break;
    }
}
```

When the callback function receives the `kCFStreamEventHasBytesAvailable` event code, it calls `CFReadStreamRead` to read the data.

When the callback function receives the `kCFStreamEventErrorOccurred` event code, it calls `CFReadStreamGetError` to get the error and its own error function (`reportError`) to handle the error.

When the callback function receives the `kCFStreamEventEndEncountered` event code, it calls its own function (`reportCompletion`) for handling the end of data and then calls the `CFReadStreamUnscheduleFromRunLoop` function to remove the stream from the specified run loop. Then the `CFReadStreamClose` function is run to close the stream and `CFRelease` to release the stream reference.

In general, polling a network stream is inadvisable. However, in certain rare circumstances, it can be useful to do so. To poll a stream, you first check to see if the streams are ready for reading or writing, then perform a read or write operation on the stream.

When writing to a write stream, you can determine if the stream is ready to accept data by calling [CFWriteStreamCanAcceptBytes](https://developer.apple.com/documentation/corefoundation/1539684-cfwritestreamcanacceptbytes). If it returns `TRUE`, then you can be assured that a subsequent call to the [CFWriteStreamWrite](https://developer.apple.com/documentation/corefoundation/1539680-cfwritestreamwrite) function will send data immediately without blocking.

Similarly, for a read stream, before calling [CFReadStreamRead](https://developer.apple.com/documentation/corefoundation/1539700-cfreadstreamread), call the function [CFReadStreamHasBytesAvailable](https://developer.apple.com/documentation/corefoundation/1539638-cfreadstreamhasbytesavailable).

Listing 2-9 is a polling example for a read stream.

__Listing 2-9__  Polling a read stream

```
while (!done) {
    if (CFReadStreamHasBytesAvailable(myReadStream)) {
        UInt8 buf[BUFSIZE];
        CFIndex bytesRead = CFReadStreamRead(myReadStream, buf, BUFSIZE);
        if (bytesRead < 0) {
            CFStreamError error = CFReadStreamGetError(myReadStream);
            reportError(error);
        } else if (bytesRead == 0) {
            if (CFReadStreamGetStatus(myReadStream) == kCFStreamStatusAtEnd) {
                done = TRUE;
            }
        } else {
            handleBytes(buf, bytesRead);
        }
    } else {
        // ...do something else while you wait...
    }
}
```

Listing 2-10 is a polling example for a write stream.

__Listing 2-10__  Polling a write stream

```
UInt8 buf[] = “Hello, world”;
UInt32 bufLen = strlen(buf);

while (!done) {
    if (CFWriteStreamCanAcceptBytes(myWriteStream)) {
        int bytesWritten = CFWriteStreamWrite(myWriteStream, buf, strlen(buf));
        if (bytesWritten < 0) {
            CFStreamError error = CFWriteStreamGetError(myWriteStream);
            reportError(error);
        } else if (bytesWritten == 0) {
            if (CFWriteStreamGetStatus(myWriteStream) == kCFStreamStatusAtEnd)
            {
                done = TRUE;
            }
        } else if (bytesWritten != strlen(buf)) {
            // Determine how much has been written and adjust the buffer
            bufLen = bufLen - bytesWritten;
            memmove(buf, buf + bytesWritten, bufLen);

            // Figure out what went wrong with the write stream
            CFStreamError error = CFWriteStreamGetError(myWriteStream);
            reportError(error);
        }
    } else {
        // ...do something else while you wait...
    }
}
```


There are two ways to apply firewall settings to a stream. For most streams, you can retrieve the proxy settings using the `SCDynamicStoreCopyProxies` function and then apply the result to the stream by setting the `kCFStreamHTTPProxy` (or `kCFStreamFTPProxy`) property. The `SCDynamicStoreCopyProxies` function is part of the System Configuration framework, so you need to include `<SystemConfiguration/SystemConfiguration.h>` in your project to use the function. Then just release the proxy dictionary reference when you are done with it. The process would look like that in Listing 2-11.

__Listing 2-11__  Navigating a stream through a proxy server

```
CFDictionaryRef proxyDict = SCDynamicStoreCopyProxies(NULL);
CFReadStreamSetProperty(readStream, kCFStreamPropertyHTTPProxy, proxyDict);
```

However, if you need to use the proxy settings often for multiple streams, it becomes a bit more complicated. In this case retrieving the firewall settings of a user's machine requires five steps:

1. Create a single, persistent handle to a dynamic store session, `SCDynamicStoreRef`.
2. Put the handle to the dynamic store session into the run loop to be notified of proxy changes.
3. Use `SCDynamicStoreCopyProxies` to retrieve the latest proxy settings.
4. Update your copy of the proxies when told of the changes.
5. Clean up the `SCDynamicStoreRef` when you are through with it.

To create the handle to the dynamic store session, use the function `SCDynamicStoreCreate` and pass an allocator, a name to describe your process, a callback function and a dynamic store context, `SCDynamicStoreContext`. This is run when initializing your application. The code would be similar to that in Listing 2-12.

__Listing 2-12__  Creating a handle to a dynamic store session

```
SCDynamicStoreContext context = {0, self, NULL, NULL, NULL};
systemDynamicStore = SCDynamicStoreCreate(NULL,
                                          CFSTR("SampleApp"),
                                          proxyHasChanged,
                                          &context);
```

After creating the reference to the dynamic store, you need to add it to the run loop. First, take the dynamic store reference and set it up to monitor for any changes to the proxies. This is accomplished with the functions `SCDynamicStoreKeyCreateProxies` and `SCDynamicStoreSetNotificationKeys`. Then, you can add the dynamic store reference to the run loop with the functions `SCDynamicStoreCreateRunLoopSource` and `CFRunLoopAddSource`. Your code should look like that in Listing 2-13.

__Listing 2-13__  Adding a dynamic store reference to the run loop

```
// Set up the store to monitor any changes to the proxies
CFStringRef proxiesKey = SCDynamicStoreKeyCreateProxies(NULL);
CFArrayRef keyArray = CFArrayCreate(NULL,
                                    (const void **)(&proxiesKey),
                                    1,
                                    &kCFTypeArrayCallBacks);
SCDynamicStoreSetNotificationKeys(systemDynamicStore, keyArray, NULL);
CFRelease(keyArray);
CFRelease(proxiesKey);

// Add the dynamic store to the run loop
CFRunLoopSourceRef storeRLSource =
    SCDynamicStoreCreateRunLoopSource(NULL, systemDynamicStore, 0);
CFRunLoopAddSource(CFRunLoopGetCurrent(), storeRLSource, kCFRunLoopCommonModes);
CFRelease(storeRLSource);
```

Once the dynamic store reference has been added to the run loop, use it to preload the proxy dictionary the current proxy settings by calling `SCDynamicStoreCopyProxies`. See Listing 2-14 for how to do this.

__Listing 2-14__  Loading the proxy dictionary

```
gProxyDict = SCDynamicStoreCopyProxies(systemDynamicStore);
```

As a result of adding the dynamic store reference to the run loop, each time the proxies are changed your callback function will be run. Release the current proxy dictionary and reload it with the new proxy settings. A sample callback function would look like the one in Listing 2-15.

__Listing 2-15__  Proxy callback function

```
void proxyHasChanged() {
    CFRelease(gProxyDict);
    gProxyDict = SCDynamicStoreCopyProxies(systemDynamicStore);
}
```

Since all of the proxy information is up-to-date, apply the proxies. After creating your read or write stream, set the `kCFStreamPropertyHTTPProxy` proxy by calling the functions `CFReadStreamSetProperty` or `CFWriteStreamSetProperty`. If your stream was a read stream called `readStream`, your function call would be like that in Listing 2-16.

__Listing 2-16__  Adding proxy information to a stream

```
CFReadStreamSetProperty(readStream, kCFStreamPropertyHTTPProxy, gProxyDict);
```

When you are all done with using the proxy settings, make sure to release the dictionary and dynamic store reference, and to remove the dynamic store reference from the run loop. See Listing 2-17.

__Listing 2-17__  Cleaning up proxy information

```
if (gProxyDict) {
    CFRelease(gProxyDict);
}

// Invalidate the dynamic store's run loop source
// to get the store out of the run loop
CFRunLoopSourceRef rls = SCDynamicStoreCreateRunLoopSource(NULL, systemDynamicStore, 0);
CFRunLoopSourceInvalidate(rls);
CFRelease(rls);
CFRelease(systemDynamicStore);
```

[Next](Communicating%20with%20HTTP%20Servers.md)[Previous](CFNetwork%20Concepts.md)

