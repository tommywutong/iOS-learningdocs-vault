---
title: Web Services Core Programming Guide
apple_id: TP30000985
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2009-01-06'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/UsingWebservices/Tasks/Tasks.html
archived_at: '2026-07-15T08:18:28.826196Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Web Services Core Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](About%20Web%20Services.md)

# Using the Web Services Core Framework

The fundamental task in using web services is invoking an operation. This is a moderately complex process. This chapter contains two sections. The first section, [Creating and Invoking Operations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobvfvbuqmjqgewvgvzs), explains the steps and provides illustrative code snippets. The second section, [Example: Calling a SOAP Operation with HTTP Authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobvfvbuqmjqgewvgvzt), is an annotated example with downloadable sample code you can build and run.

To call an XML-RPC or SOAP service on a remote server, you need to create an invocation reference, define the parameters and parameter order, pass in the settings, then invoke the service. The invocation reference includes a URL, an operation name, and a protocol (SOAP or XML-RPC). The parameters and settings vary depending on the selected protocol—SOAP parameters are named, for example, whereas RPC parameters are numbered. SOAP requires a namespace and usually a SOAP action header in the settings as well. In addition, there are debug properties you can set.

The following sections describe the steps in more detail.

You create the `WSMethodInvocationRef` object by using the function `WSMethodInvocationCreate`, which takes a URL (`CFURLRef` or `NSURL`), an operation name (`CFStringRef`), and a protocol. The protocol is one of these `CFStringRef` constants:

- kWSXMLRPCProtocol
- kWSSOAP2001Protocol

Pass in the URL of the service, the name of the operation, and the protocol:

```
NSURL *url = [NSURL URLWithString:@"http://localhost:8888/"];
NSString *methodName = @"echo";
WSMethodInvocationRef mySoapRef = WSMethodInvocationCreate((CFURLRef)url,
                                                 (CFStringRef)methodName,
                                                    kWSSOAP2001Protocol);
```


Create a dictionary of the operation parameters and an array establishing the parameter order, then pass references to the dictionary and array to `WSMethodInvocationSetParameters`:

```
NSDictionary *params = [NSDictionary dictionaryWithObject:@"firstParamName"
                                                          forKey:@"firstParam"];
 NSArray *paramOrder = [NSArray arrayWithObject:@"firstParam"];
 WSMethodInvocationSetParameters(mySoapRef, (CFDictionaryRef)params,
                                            (CFArrayRef)paramOrder);
```


Call `WSMethodInvocationSetProperty` with the appropriate settings for the operation. For example, a SOAP call requires a namespace and a SOAP action header (some SOAP implementations require a header even if it is empty). You might also want to set the request to allow redirects and to turn on the debug properties so that the raw XML is included in the returned dictionary, along with the parsed data.

```
    NSString *namespace = @"http://localhost:8888/";
    NSDictionary *reqHeaders = [NSDictionary dictionaryWithObject:@"" forKey:@"SOAPAction"];
    WSMethodInvocationSetProperty(mySoapRef, kWSSOAPMethodNamespaceURI,
                                             (CFStringRef)namespace);
    WSMethodInvocationSetProperty(mySoapRef, kWSHTTPExtraHeaders,
                                             (CFDictionaryRef)reqHeaders);
    WSMethodInvocationSetProperty(mySoapRef,    kWSHTTPFollowsRedirects,
                                                kCFBooleanTrue);
 // set debug props
    WSMethodInvocationSetProperty(mySoapRef, kWSDebugIncomingBody,
                                             kCFBooleanTrue);
    WSMethodInvocationSetProperty(mySoapRef, kWSDebugIncomingHeaders,
                                             kCFBooleanTrue);
    WSMethodInvocationSetProperty(mySoapRef, kWSDebugOutgoingBody,
                                             kCFBooleanTrue);
    WSMethodInvocationSetProperty(mySoapRef, kWSDebugOutgoingHeaders,
                                             kCFBooleanTrue);
```


Once you’ve created the invocation reference and added the settings and the properties, you can invoke the operation. Typically, you then use the CFNetwork framework to check the status of your post—which saves you the trouble of trying to parse a nonresponse in the event of a challenge or network error—using the constant `kWSHTTPResponseMessage` as an identifier for the web services request.

```
NSDictionary *result = (NSDictionary *)WSMethodInvocationInvoke(mySoapRef);
// get HTTP response from SOAP request so we can see the status code
CFHTTPMessageRef res = (CFHTTPMessageRef)
                       [result objectForKey:(id)kWSHTTPResponseMessage];
```


Because network delays tend to be unpredictably long, you normally want to invoke operations asynchronously, using `WSMethodInvocationScheduleWithRunLoop`, and providing a callback on your run loop to handle the response. You can re-schedule the invocation after it completes. Set your callback using `WSMethodInvocationSetCallBack`.

If there are no network, transport, or web services faults, the invocation returns a method response dictionary, either synchronously or on your callback. (Set your callback using `WSMethodInvocationSetCallBack`). If you know what the keys are for the values you want, you can retrieve the returned data from the dictionary using the keys.

Alternatively, you can request the `kWSMethodInvocationResult` and parse the XML yourself. If you prefer, you can pass in an expected result parameter name before invoking the operation, in which case `kWSMethodInvocationResult` will be an alias to the parameter that you want.

Because the response dictionary may contain the raw XML as well as the deserialized data, there may be more than one instance of the data in the dictionary.

If the CFTypes for the data you are working with have corresponding WSTypes, invoking the operation automatically serializes the outbound data from the dictionary into XML and deserializes the returned data from XML into a dictionary. If you need to work with more complex data types, you can write your own serializer and deserializer callbacks. These callbacks are called when the method invocation encounters the specified data type in an outbound dictionary or an inbound XML response.

Set the callbacks using `WSMethodInvocationAddSerializationOverride` and `WSMethodInvocationAddDeserializationOverride`.

This example calls a SOAP method over HTTP. Web services commonly require authentication, so this example sends the SOAP request and, if challenged, authenticates. You can download the sample code from [http://developer.apple.com/internet/webservices/SOAP_AuthExample.dmg](https://developer.apple.com/internet/webservices/SOAP_AuthExample.dmg).

As shown in the example code, begin by declaring or fetching the data that makes up the parameters and other details of the SOAP request, including the SOAP method name, method namespace, request parameters, request parameter order, and SOAP action HTTP header. The SOAP method in this case is named `echo` and takes a single string parameter named `param`. If the call is successful, the method echoes the string parameter ("I hear an echo.”) in the SOAP response. Create a dictionary of parameters and their names for SOAP calls (for XML-RPC calls, use ordinal numbers for the parameters instead of names) and an array containing the parameters in order.

```
// SOAP request settings
NSURL *url = [NSURL URLWithString:@"http://localhost:8888/"];
NSString *method = @"echo";
NSString *namespace = @"http://localhost:8888/";

// SOAP request params
NSDictionary *params = [NSDictionary dictionaryWithObject:@"I hear an echo."
                                                   forKey:@"param"];
NSArray *paramOrder = [NSArray arrayWithObject:@"param"];

// SOAP request http headers -- some server implementations require even empty SOAPAction headers
NSDictionary *reqHeaders = [NSDictionary dictionaryWithObject:@"" forKey:@"SOAPAction"];
```

It's generally easier to work with Cocoa objects, as shown, and cast the objects to Core Foundation types when necessary. This approach takes advantage of the toll-free bridging between Cocoa and Core Foundation, and makes many common tasks—such as memory management—easier. That said, you can make the same calls from C or C++.

The URL for this example points to the SOAP server running on port 8888 on the local host. Values for the method namespace and SOAPAction HTTP headers are also declared. Many SOAP server implementations require the presence of an empty SOAP action header even if the method itself does not specifically require a header value. Creating a dictionary with an empty value for the `SOAPAction` key and attaching it to the SOAP request forces an empty SOAP action header to be sent along with the request.

Next, a SOAP request is created from the settings above. A SOAP request is represented as a `WSMethodInvocationRef` type.

```
// create SOAP request
WSMethodInvocationRef soapReq = createSOAPRequest(url, method, namespace, params, paramOrder, reqHeaders);
```

Next, creation of the SOAP request is delegated to the `createSOAPRequest` function, which returns a `WSMethodInvocationRef` object.

```
// Custom function to create SOAP request
WSMethodInvocationRef createSOAPRequest(NSURL *url,
                                        NSString *method,
                                        NSString *namespace,
                                        NSDictionary *params,
                                        NSArray *paramOrder,
                                        NSDictionary *reqHeaders)
{
    WSMethodInvocationRef soapReq = WSMethodInvocationCreate((CFURLRef)url,
                                                             (CFStringRef)method,
                                                             kWSSOAP2001Protocol);
    // set SOAP params
    WSMethodInvocationSetParameters(soapReq, (CFDictionaryRef)params, (CFArrayRef)paramOrder);
    // set method namespace
    WSMethodInvocationSetProperty(soapReq, kWSSOAPMethodNamespaceURI, (CFStringRef)namespace);
    // Add HTTP headers (with SOAPAction header)
    WSMethodInvocationSetProperty(soapReq, kWSHTTPExtraHeaders, (CFDictionaryRef)reqHeaders);
    // for good measure, make the request follow redirects.
    WSMethodInvocationSetProperty(soapReq,    kWSHTTPFollowsRedirects, kCFBooleanTrue);
    // set debug props
    WSMethodInvocationSetProperty(soapReq, kWSDebugIncomingBody,    kCFBooleanTrue);
    WSMethodInvocationSetProperty(soapReq, kWSDebugIncomingHeaders, kCFBooleanTrue);
    WSMethodInvocationSetProperty(soapReq, kWSDebugOutgoingBody,    kCFBooleanTrue);
    WSMethodInvocationSetProperty(soapReq, kWSDebugOutgoingHeaders, kCFBooleanTrue);
   return soapReq;
}
```

Note that in addition to creating the SOAP request, several debug properties of the `WSMethodInvocationRef` object are also set to true. This causes the raw XML contents of the SOAP request and response messages to be included in the result dictionary returned from executing the SOAP request. Viewing this raw XML can be extremely helpful in debugging SOAP client code.

The next step is to invoke the initial SOAP request. Do this using the `WSMethodInvocationInvoke` function, which returns a dictionary containing the SOAP response and other debug information.

Since the service accessed requires HTTP basic authentication, expect the HTTP headers of the SOAP response to contain authentication challenge information. To respond to the authentication challenge, retrieve the HTTP response from the result dictionary using the `kWSHTTPResponseMessage` key. The HTTP response is represented by a `CFHTTMessageRef` object.

```
// invoke SOAP request
NSDictionary *result = (NSDictionary *)WSMethodInvocationInvoke(soapReq);
// get HTTP response from SOAP request so we can see response HTTP status code
CFHTTPMessageRef res = (CFHTTPMessageRef)[result objectForKey:(id)kWSHTTPResponseMessage];
```

Now check for an HTTP response code of 401 or 407, which would signal an HTTP authentication challenge. If an authentication challenge is returned, you must:

1. Extract the HTTP response headers from the first SOAP response. These headers contain the necessary authentication challenge information.
2. Create a new `CFHTTMessageRef` object to represent a new HTTP request.
3. Gather user name and password information by prompting the user or by querying some external data source.
4. Combine the user name and password with the authentication challenge information from the initial SOAP response to create credentials.
5. Attach the credentials to the newly-created HTTP request.
6. Create a new SOAP request and combine it with the new HTTP request to produce a SOAP request with the necessary authentication credentials attached.
7. Invoke the new SOAP request.

```
// get status
int resStatusCode = CFHTTPMessageGetResponseStatusCode(res);
// if response status code indicates auth challenge, attempt to add authorization
while (401 == resStatusCode || 407 == resStatusCode) {
CFHTTPAuthenticationRef auth = CFHTTPAuthenticationCreateFromResponse(kCFAllocatorDefault, res);
// extract details of the auth challenge to display
// when prompting the user for username and password information
NSString *scheme = [(NSString *)CFHTTPAuthenticationCopyMethod(auth) autorelease];
NSString *realm  = [(NSString *)CFHTTPAuthenticationCopyRealm(auth)  autorelease];
NSArray *domains = [(NSArray *)CFHTTPAuthenticationCopyDomains(auth) autorelease];
NSLog(@"Providing auth info for \nscheme: %@\n, realm: %@\n, domains: %@",       scheme, realm, domains);
// Replace with a user prompt or fetch data from remote source
NSString *username = @"uName";
NSString *password = @"pWord";
// create custom http request with authorization
NSString *reqMethod = @"POST";
CFHTTPMessageRef req = CFHTTPMessageCreateRequest(kCFAllocatorDefault,
                                                  (CFStringRef)reqMethod,
                                                  (CFURLRef)url,
                                                  kCFHTTPVersion1_1);
// add auth creds to request.
Boolean success = CFHTTPMessageAddAuthentication(req,
                                                 res,
                                                 (CFStringRef)username,
                                                 (CFStringRef)password,
                                                 NULL,
                                                 false);
if (!success) {
    NSLog(@"failed to add auth to request");
    return EXIT_FAILURE;
}
// create a new SOAP request
soapReq = createSOAPRequest(url, method, namespace, params, paramOrder, reqHeaders);
// add HTTP request auth creds to SOAP request
WSMethodInvocationSetProperty(soapReq, kWSHTTPMessage, req);
// send SOAP request again
result = (NSDictionary *)WSMethodInvocationInvoke(soapReq);
NSLog(@"result: %@", result);
```

At this point, the console should reflect the string you sent to the SOAP server. You have successfully invoked a service, responded to HTTP authentication challenge, serialized your outbound query, and deserialized the response.

[Next](Document%20Revision%20History.md)[Previous](About%20Web%20Services.md)

