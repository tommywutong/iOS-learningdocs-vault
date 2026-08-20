---
title: CFNetwork Programming Guide
apple_id: TP30001132
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: CFNetwork
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/CFFTPTasks/CFFTPTasks.html
archived_at: '2026-07-15T08:18:10.300840Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CFNetwork Programming Guide](Introduction%20to%20CFNetwork%20Programming%20Guide.md)


[Next](Using%20Network%20Diagnostics.md)[Previous](Communicating%20with%20Authenticating%20HTTP%20Servers.md)

# Working with FTP Servers

This chapter explains how to use some of the basic features of the CFFTP API. Managing the FTP transactions is performed asynchronously, while managing the file transfer is implemented synchronously.

Using CFFTP is very similar to using CFHTTP because they are both based on CFStream. As with any other API that uses CFStream asynchronously, downloading a file with CFFTP requires that you create a read stream for the file, and a callback function for that read stream. When the read stream receives data, the callback function will be run and you will need to appropriately download the bytes. This procedure should normally be performed using two functions: one to set up the streams and one to act as the callback function.

Begin by creating a read stream using the `CFReadStreamCreateWithFTPURL` function and passing it the URL string of the file to be downloaded on the remote server. An example of a URL string might be `ftp://ftp.example.com/file.txt`. Note that the string contains the server name, the path, and the file. Next, create a write stream for the local location where the file will be downloaded. This is accomplished using the `CFWriteStreamCreateWithFile` function, passing the path where the file will be downloaded.

Since the write stream and the read stream need to stay in sync, it is a good idea to create a structure that contains all of the common information, such as the proxy dictionary, the file size, the number of bytes written, the number of bytes left over, and a buffer. This structure might look like that in Listing 5-1.

__Listing 5-1__  A stream structure

```
typedef struct MyStreamInfo {

    CFWriteStreamRef  writeStream;
    CFReadStreamRef   readStream;
    CFDictionaryRef   proxyDict;
    SInt64            fileSize;
    UInt32            totalBytesWritten;
    UInt32            leftOverByteCount;
    UInt8             buffer[kMyBufferSize];

} MyStreamInfo;
```

Initialize your structure with the read stream and write stream you just created. You can then define the `info` field of your stream client context (`CFStreamClientContext`) to point to your structure. This will become useful later.

Open your write stream with the [CFWriteStreamOpen](https://developer.apple.com/documentation/corefoundation/1539753-cfwritestreamopen) function so you can begin writing to the local file. To make sure the stream opens properly, call the function `CFWriteStreamGetStatus` and check whether it returns either `kCFStreamStatusOpen` or `kCFStreamStatusOpening`.

With the write stream open, associate a callback function with the read stream. Call the function [CFReadStreamSetClient](https://developer.apple.com/documentation/corefoundation/1539670-cfreadstreamsetclient) and pass the read stream, the network events your callback function should receive, the callback function's name and the `CFStreamClientContext` object. By having earlier set the `info` field of the stream client context, your structure will now be sent to your callback function whenever it is run.

Some FTP servers may require a user name, and some may also require a password. If the server you are accessing needs a user name for authentication, call the [CFReadStreamSetProperty](https://developer.apple.com/documentation/corefoundation/1539615-cfreadstreamsetproperty) function and pass the read stream, `kCFStreamPropertyFTPUserName` for the property, and a reference to a `CFString` object containing the user name. In addition, if you need to set a password, set the `kCFStreamPropertyFTPPassword` property.

Some network configurations may also use FTP proxies. You obtain the proxy information in different ways depending on whether your code is running in OS X or iOS.

- In OS X, you can retrieve the proxy settings in a dictionary by calling the [SCDynamicStoreCopyProxies](https://developer.apple.com/documentation/systemconfiguration/1517088-scdynamicstorecopyproxies) function and passing it `NULL`.
- In iOS, you can retrieve the proxy settings by calling [CFNetworkCopyProxiesForURL](https://developer.apple.com/documentation/cfnetwork/1426639-cfnetworkcopyproxiesforurl).

These functions return a dynamic store reference. You can use this value to set the `kCFStreamPropertyFTPProxy` property of the read stream. This sets the proxy server, specifies the port, and returns a Boolean value indicating whether passive mode is enforced for the FTP stream.

In addition to the properties mentioned, there are a number of other properties available for FTP streams. The complete list follows.

- `kCFStreamPropertyFTPUserName` — user name to use to log in (settable and retrievable; do not set for anonymous FTP connections)
- `kCFStreamPropertyFTPPassword` — password to use to log in (settable and retrievable; do not set for anonymous FTP connections)
- `kCFStreamPropertyFTPUsePassiveMode` — whether to use passive mode (settable and retrievable)
- `kCFStreamPropertyFTPResourceSize` — the expected size of an item that is being downloaded, if available (retrievable; available only for FTP read streams)
- `kCFStreamPropertyFTPFetchResourceInfo` — whether to require that resource information, such as size, be required before starting a download (settable and retrievable); setting this property may impact performance
- `kCFStreamPropertyFTPFileTransferOffset` — file offset at which to start a transfer (settable and retrievable)
- `kCFStreamPropertyFTPAttemptPersistentConnection` — whether to try to reuse connections (settable and retrievable)
- `kCFStreamPropertyFTPProxy` — CFDictionary type that holds key-value pairs of proxy dictionary (settable and retrievable)
- `kCFStreamPropertyFTPProxyHost` — name of an FTP proxy host (settable and retrievable)
- `kCFStreamPropertyFTPProxyPort` — port number of an FTP proxy host (settable and retrievable)

After the correct properties have been assigned to the read stream, open the stream using the `CFReadStreamOpen` function. Assuming that this does not return an error, all the streams have been properly set up.

Your callback function will receive three parameters: the read stream, the type of event, and your `MyStreamInfo` structure. The type of event determines what action must be taken.

The most common event is `kCFStreamEventHasBytesAvailable`, which is sent when the read stream has received bytes from the server. First, check how many bytes have been read by calling the `CFReadStreamRead` function. Make sure the return value is not less than zero (an error), or equal to zero (download has completed). If the return value is positive, then you can begin writing the data in the read stream to disk via the write stream.

Call the `CFWriteStreamWrite` function to write the data to the write stream. Sometimes `CFWriteStreamWrite` can return without writing all of the data from the read stream. For this reason, set up a loop to run as long as there is still data to be written. The code for this loop is in Listing 5-2, where `info` is the `MyStreamInfo` structure from [Setting up the Streams](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzsfvbuqojnknlte). This method of writing to the write stream uses blocking streams. You can achieve better performance by making the write stream event driven, but the code is more complex.

__Listing 5-2__  Writing data to a write stream from the read stream

```swift
bytesRead = CFReadStreamRead(info->readStream, info->buffer, kMyBufferSize);

//...make sure bytesRead > 0 ...

bytesWritten = 0;
while (bytesWritten < bytesRead) {
    CFIndex result;

    result = CFWriteStreamWrite(info->writeStream, info->buffer + bytesWritten, bytesRead - bytesWritten);
    if (result <= 0) {
        fprintf(stderr, "CFWriteStreamWrite returned %ld\n", result);
        goto exit;
    }
    bytesWritten += result;
}
info->totalBytesWritten += bytesWritten;
```

Repeat this entire procedure as long as there are available bytes in the read stream.

The other two events you need to watch out for are `kCFStreamEventErrorOccurred` and `kCFStreamEventEndEncountered`. If an error occurs, retrieve the error using `CFReadStreamGetError` and then exit. If the end of the file occurs, then your download has completed and you can exit.

Make sure to remove all your streams after everything is completed and no other process is using the streams. First, close the write stream and set the client to `NULL`. Then unschedule the stream from the run loop and release it. Remove the streams from the run loop when you are done.

Uploading a file is similar to downloading a file. As with downloading a file, you need a read stream and a write stream. However, when uploading a file, the read stream will be for the local file and the write stream will be for the remote file. Follow the instructions in [Setting up the Streams](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzsfvbuqojnknlte), but wherever it refers to the read stream, adapt the code for a write stream and visa versa.

In the callback function, rather than looking for the `kCFStreamEventHasBytesAvailable` event, now look for the event `kCFStreamEventCanAcceptBytes`. First, read bytes from the file using the read stream and place the data into the buffer in `MyStreamInfo`. Then, run the `CFWriteStreamWrite` function to push bytes from the buffer into the write stream. `CFWriteStreamWrite` returns the number of bytes that have been written to the stream. If the number of bytes written to the stream is fewer than the number read from the file, calculate the leftover bytes and store them back into the buffer. During the next write cycle, if there are leftover bytes, write them to the write stream rather than loading new data from the read stream. Repeat this whole procedure as long as the write stream can accept bytes (`CFWriteStreamCanAcceptBytes`). See this loop in code in Listing 5-3.

__Listing 5-3__  Writing data to the write stream

```swift
do {
    // Check for leftover data
    if (info->leftOverByteCount > 0) {
        bytesRead = info->leftOverByteCount;
    } else {
        // Make sure there is no error reading from the file
        bytesRead = CFReadStreamRead(info->readStream, info->buffer,
                                     kMyBufferSize);
        if (bytesRead < 0) {
            fprintf(stderr, "CFReadStreamRead returned %ld\n", bytesRead);
            goto exit;
        }
        totalBytesRead += bytesRead;
    }

    // Write the data to the write stream
     bytesWritten = CFWriteStreamWrite(info->writeStream, info->buffer, bytesRead);
    if (bytesWritten > 0) {

        info->totalBytesWritten += bytesWritten;

        // Store leftover data until kCFStreamEventCanAcceptBytes event occurs again
        if (bytesWritten < bytesRead) {
            info->leftOverByteCount = bytesRead - bytesWritten;
            memmove(info->buffer, info->buffer + bytesWritten,
                    info->leftOverByteCount);
        } else {
            info->leftOverByteCount = 0;
        }
    } else {
        if (bytesWritten < 0)
            fprintf(stderr, "CFWriteStreamWrite returned %ld\n", bytesWritten);
        break;
    }

} while (CFWriteStreamCanAcceptBytes(info->writeStream));
```

Also account for the `kCFStreamEventErrorOccurred` and `kCFStreamEventEndEncountered` events as you do when downloading a file.

To create a directory on a remote server, set up a write stream as if you were going to be uploading a file. However, provide a directory path, not a file, for the `CFURL` object that is passed to the `CFWriteStreamCreateWithFTPURL` function. End the path with a forward slash. For example, a proper directory path would be `ftp://ftp.example.com/newDirectory/`, not `ftp://ftp.example.com/newDirectory/newFile.txt`. When the callback function is executed by the run loop, it sends the event `kCFStreamEventEndEncountered`, which means the directory has been created (or `kCFStreamEventErrorOccurred` if something went wrong).

Only one level of directories can be created with each call to `CFWriteStreamCreateWithFTPURL`. Also, a directory is created only if you have the correct permissions on the server.

Downloading a directory listing via FTP is slightly different from downloading or uploading a file. This is because the incoming data has to be parsed. First, set up a read stream to get the directory listing. This should be done as it was for downloading a file: create the stream, register a callback function, schedule the stream with the run loop (if necessary, set up user name, password and proxy information), and finally open the stream. In the following example you do not need both a read and a write stream when retrieving the directory listing, because the incoming data is going to the screen rather than a file.

In the callback function, watch for the `kCFStreamEventHasBytesAvailable` event. Prior to loading data from the read stream, make sure there is no leftover data in the stream from the previous time the callback function was run. Load the offset from the `leftOverByteCount` field of your `MyStreamInfo` structure. Then, read data from the stream, taking into account the offset you just calculated. The buffer size and number of bytes read should be calculated too. This is all accomplished in Listing 5-4.

__Listing 5-4__  Loading data for a directory listing

```swift
// If previous call had unloaded data
int offset = info->leftOverByteCount;

// Load data from the read stream, accounting for the offset
bytesRead = CFReadStreamRead(info->readStream, info->buffer + offset,
                             kMyBufferSize - offset);
if (bytesRead < 0) {
    fprintf(stderr, "CFReadStreamRead returned %ld\n", bytesRead);
    break;
} else if (bytesRead == 0) {
    break;
}
bufSize = bytesRead + offset;
totalBytesRead += bufSize;
```

After the data has been read to a buffer, set up a loop to parse the data. The data that is parsed is not necessarily the entire directory listing; it could (and probably will) be chunks of the listing. Create the loop to parse the data using the function `CFFTPCreateParsedResourceListing`, which should be passed the buffer of data, the size of the buffer, and a dictionary reference. It returns the number of bytes parsed. As long as this value is greater than zero, continue to loop. The dictionary that `CFFTPCreateParsedResourceListing` creates contains all the directory listing information; more information about the keys is available in [Setting up the Streams](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzsfvbuqojnknlte).

It is possible for `CFFTPCreateParsedResourceListing` to return a positive value, but not create a parse dictionary. For example, if the end of the listing contains information that cannot be parsed, `CFFTPCreateParsedResourceListing` will return a positive value to tell the caller that data has been consumed. However, `CFFTPCreateParsedResourceListing` will not create a parse dictionary since it could not understand the data.

If a parse dictionary is created, recalculate the number of bytes read and the buffer size as shown in Listing 5-5.

__Listing 5-5__  Loading the directory listing and parsing it

```swift
do
{
    bufRemaining = info->buffer + totalBytesConsumed;

    bytesConsumed = CFFTPCreateParsedResourceListing(NULL, bufRemaining,
                                                     bufSize, &parsedDict);
    if (bytesConsumed > 0) {

        // Make sure CFFTPCreateParsedResourceListing was able to properly
        // parse the incoming data
        if (parsedDict != NULL) {
            // ...Print out data from parsedDict...
            CFRelease(parsedDict);
        }

        totalBytesConsumed += bytesConsumed;
        bufSize -= bytesConsumed;
        info->leftOverByteCount = bufSize;

    } else if (bytesConsumed == 0) {

        // This is just in case. It should never happen due to the large buffer size
        info->leftOverByteCount = bufSize;
        totalBytesRead -= info->leftOverByteCount;
        memmove(info->buffer, bufRemaining, info->leftOverByteCount);

    } else if (bytesConsumed == -1) {
        fprintf(stderr, "CFFTPCreateParsedResourceListing parse failure\n");
        // ...Break loop and cleanup...
    }

} while (bytesConsumed > 0);
```

When the stream has no more bytes available, clean up all the streams and remove them from the run loop.

[Next](Using%20Network%20Diagnostics.md)[Previous](Communicating%20with%20Authenticating%20HTTP%20Servers.md)

