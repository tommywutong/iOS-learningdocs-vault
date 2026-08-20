---
title: CFNetwork Programming Guide
apple_id: TP30001132
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: CFNetwork
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/CFHTTPTasks/CFHTTPTasks.html
archived_at: '2026-07-15T08:18:11.147837Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CFNetwork Programming Guide](Introduction%20to%20CFNetwork%20Programming%20Guide.md)


[Next](Communicating%20with%20Authenticating%20HTTP%20Servers.md)[Previous](Working%20with%20Streams.md)

# Communicating with HTTP Servers

This chapter explains how to create, send, and receive HTTP requests and responses.

An HTTP request is a message consisting of a method for the remote server to execute, the object to operate on (the URL), message headers, and a message body. The methods are usually one of the following: `GET`, `HEAD`, `PUT`, `POST`, `DELETE`, `TRACE`, `CONNECT` or `OPTIONS`. Creating an HTTP request with CFHTTP requires four steps:

1. Generate a CFHTTP message object using the `CFHTTPMessageCreateRequest` function.
2. Set the body of the message using the function `CFHTTPMessageSetBody`.
3. Set the message's headers using the `CFHTTPMessageSetHeaderFieldValue` function.
4. Serialize the message by calling the function `CFHTTPMessageCopySerializedMessage`.

Sample code would look like the code in Listing 3-1.

__Listing 3-1__  Creating an HTTP request

```
CFStringRef bodyString = CFSTR(""); // Usually used for POST data
CFDataRef bodyData = CFStringCreateExternalRepresentation(kCFAllocatorDefault,
                                        bodyString, kCFStringEncodingUTF8, 0);

CFStringRef headerFieldName = CFSTR("X-My-Favorite-Field");
CFStringRef headerFieldValue = CFSTR("Dreams");

CFStringRef url = CFSTR("http://www.apple.com");
CFURLRef myURL = CFURLCreateWithString(kCFAllocatorDefault, url, NULL);

CFStringRef requestMethod = CFSTR("GET");
CFHTTPMessageRef myRequest =
    CFHTTPMessageCreateRequest(kCFAllocatorDefault, requestMethod, myURL,
                               kCFHTTPVersion1_1);

CFDataRef bodyDataExt = CFStringCreateExternalRepresentation(kCFAllocatorDefault, bodyData, kCFStringEncodingUTF8, 0);
CFHTTPMessageSetBody(myRequest, bodyDataExt);
CFHTTPMessageSetHeaderFieldValue(myRequest, headerFieldName, headerFieldValue);
CFDataRef mySerializedRequest = CFHTTPMessageCopySerializedMessage(myRequest);
```

In this sample code, `url` is first converted into a CFURL object by calling `CFURLCreateWithString`. Then `CFHTTPMessageCreateRequest` is called with four parameters: `kCFAllocatorDefault` specifies that the default system memory allocator is to be used to create the message reference, `requestMethod` specifies the method, such as the POST method, `myURL` specifies the URL, such as `http://www.apple.com`, and `kCFHTTPVersion1_1` specifies that message’s HTTP version is to be 1.1.

The message object reference (`myRequest`) returned by `CFHTTPMessageCreateRequest` is then sent to `CFHTTPMessageSetBody` along with the body of the message (`bodyData`). Then call `CFHTTPMessageSetHeaderFieldValue` using the same message object reference along with the name of the header (`headerField`), and the value to be set (`value`). The header parameter is a CFString object such as `Content-Length`, and the value parameter is a CFString object such as `1260`. Finally, the message is serialized by calling `CFHTTPMessageCopySerializedMessage` and should be sent via a write stream to the intended recipient, in this example `http://www.apple.com`.

When the message is no longer needed, release the message object and the serialized message. See Listing 3-2 for sample code.

__Listing 3-2__  Releasing an HTTP request

```
CFRelease(myRequest);
CFRelease(myURL);
CFRelease(url);
CFRelease(mySerializedRequest);
myRequest = NULL;
mySerializedRequest = NULL;
```


The steps for creating an HTTP response are almost identical to those for creating an HTTP request. The only difference is that rather than calling `CFHTTPMessageCreateRequest`, you call the function `CFHTTPMessageCreateResponse` using the same parameters.

To deserialize an incoming HTTP request, create an empty message using the `CFHTTPMessageCreateEmpty` function, passing `TRUE` as the `isRequest` parameter to specify that an empty request message is to be created. Then append the incoming message to the empty message using the function `CFHTTPMessageAppendBytes`. `CFHTTPMessageAppendBytes` deserializes the message and removes any control information it may contain.

Continue to do this until the function `CFHTTPMessageIsHeaderComplete` returns `TRUE`. If you do not check for `CFHTTPMessageIsHeaderComplete` to return `TRUE`, the message may be incomplete and unreliable. A sample of using these two functions can be seen in Listing 3-3.

__Listing 3-3__  Deserializing a message

```
CFHTTPMessageRef myMessage = CFHTTPMessageCreateEmpty(kCFAllocatorDefault, TRUE);
if (!CFHTTPMessageAppendBytes(myMessage, &data, numBytes)) {
    //Handle parsing error
}
```

In the example, `data` is the data that is to be appended and `numBytes` is the length of `data`. You may want to call `CFHTTPMessageIsHeaderComplete` to verify that the header of the appended message is complete.

```
if (CFHTTPMessageIsHeaderComplete(myMessage)) {
    // Perform processing.
}
```

With the message deserialized, you can now call any of the following functions to extract information from the message:

- `CFHTTPMessageCopyBody` to get a copy of the message’s body
- `CFHTTPMessageCopyHeaderFieldValue` to get a copy of a specific header field value
- `CFHTTPMessageCopyAllHeaderFields` to get a copy of all of the message’s header fields
- `CFHTTPMessageCopyRequestURL` to get a copy of the message’s URL
- `CFHTTPMessageCopyRequestMethod` to get a copy of the message’s request method

When you no longer need the message, release and dispose of it properly.

Just as creating an HTTP request is very similar to creating an HTTP response, deserializing an incoming HTTP request is also very similar to deserializing an incoming HTTP response. The only important difference is that when calling `CFHTTPMessageCreateEmpty`, you must pass `FALSE` as the `isRequest` parameter to specify that the message to be created is a response message.

You can use a CFReadStream object to serialize and send CFHTTP requests. When you use a CFReadStream object to send a CFHTTP request, opening the stream causes the message to be serialized and sent in one step. Using a CFReadStream object to send CFHTTP requests makes it easy to get the response to the request because the response is available as a property of the stream.

To use a CFReadStream object to serialize and send an HTTP request, first create a CFHTTP request and set the message body and headers as described in [Creating a CFHTTP Request](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzsfvbuqnjnknltc). Then create a CFReadStream object by calling the function `CFReadStreamCreateForHTTPRequest` and passing the request you just created. Finally, open the read stream with `CFReadStreamOpen`.

When `CFReadStreamCreateForHTTPRequest` is called, it makes a copy of the CFHTTP request object that it is passed. Thus, if necessary, you could release the CFHTTP request object immediately after calling `CFReadStreamCreateForHTTPRequest`.

Because the read stream opens a socket connection with the server specified by the `myUrl` parameter when the CFHTTP request was created, some amount of time must be allowed to pass before the stream is considered to be open. Opening the read stream also causes the request to be serialized and sent.

A sample of how to serialize and send an HTTP request can be seen in Listing 3-4.

__Listing 3-4__  Serializing an HTTP request with a read stream

```
CFStringRef url = CFSTR("http://www.apple.com");
CFURLRef myURL = CFURLCreateWithString(kCFAllocatorDefault, url, NULL);
CFStringRef requestMethod = CFSTR("GET");

CFHTTPMessageRef myRequest = CFHTTPMessageCreateRequest(kCFAllocatorDefault,
        requestMethod, myUrl, kCFHTTPVersion1_1);
CFHTTPMessageSetBody(myRequest, bodyData);
CFHTTPMessageSetHeaderFieldValue(myRequest, headerField, value);

CFReadStreamRef myReadStream = CFReadStreamCreateForHTTPRequest(kCFAllocatorDefault, myRequest);

CFReadStreamOpen(myReadStream);
```


After you schedule the request on a run loop, you will eventually get a header complete callback. At this point, you can call [CFReadStreamCopyProperty](https://developer.apple.com/documentation/corefoundation/1539715-cfreadstreamcopyproperty) to get the message response from the read stream:


```
CFHTTPMessageRef myResponse = (CFHTTPMessageRef)CFReadStreamCopyProperty(myReadStream, kCFStreamPropertyHTTPResponseHeader);
```

You can get the complete status line from the response message by calling the function `CFHTTPMessageCopyResponseStatusLine`:

```
CFStringRef myStatusLine = CFHTTPMessageCopyResponseStatusLine(myResponse);
```

Or get just the status code from the response message by calling the function `CFHTTPMessageGetResponseStatusCode`:

```
UInt32 myErrCode = CFHTTPMessageGetResponseStatusCode(myResponse);
```


If the status code returned by the function `CFHTTPMessageGetResponseStatusCode` is 401 (the remote server requires authentication information) or 407 (a proxy server requires authentication), you need to append authentication information to the request and send it again. Please read [Communicating with Authenticating HTTP Servers](Communicating%20with%20Authenticating%20HTTP%20Servers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzsfvbuqobnknltc) for information on how to handle authentication.

When `CFReadStreamCreateForHTTPRequest` creates a read stream, automatic redirection for the stream is disabled by default. If the uniform resource locator, or URL, to which the request is sent is redirected to another URL, sending the request will result in an error whose status code ranges from 300 to 307. If you receive a redirection error, you need to close the stream, create the stream again, enable automatic redirection for it, and open the stream. See Listing 3-5.

__Listing 3-5__  Redirecting an HTTP stream

```
CFReadStreamClose(myReadStream);
CFReadStreamRef myReadStream =
    CFReadStreamCreateForHTTPRequest(kCFAllocatorDefault, myRequest);
if (CFReadStreamSetProperty(myReadStream, kCFStreamPropertyHTTPShouldAutoredirect, kCFBooleanTrue) == false) {
    // something went wrong, exit
}
CFReadStreamOpen(myReadStream);
```

You may want to enable automatic redirection whenever you create a read stream.

Once a request has been sent, it is not possible to prevent the remote server from acting on it. However, if you no longer care about the response data, you can close the stream.

[Next](Communicating%20with%20Authenticating%20HTTP%20Servers.md)[Previous](Working%20with%20Streams.md)

