---
title: XML-RPC and SOAP Programming Guide
apple_id: TP30001126
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/soapXMLRPC/chapter4/soapXMLRPC_apps.html
archived_at: '2026-07-15T05:20:45.305944Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [XML-RPC and SOAP Programming Guide](Introduction%20to%20XML-RPC%20and%20SOAP%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Making%20Remote%20Procedure%20Calls%20From%20Scripts.md)

# Making Remote Procedure Calls From Applications

Starting with OS X version 10.1, the Apple Event Manager provides support for using the XML-RPC and SOAP protocols to make remote procedure calls from AppleScript scripts and from applications. This chapter provides sample code that show how to make remote procedure calls from applications or other code.

This chapter assumes you are familiar with the conceptual material in [Introduction to XML-RPC and SOAP Programming Guide](Introduction%20to%20XML-RPC%20and%20SOAP%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temrnkrifqusfiyytami). To test any of the sample code shown in this book, you must have an Internet connection.

To make an XML-RPC call from an application or other code, you create an Apple event that describes the remote procedure call, use the `AESend` function to send it, and extract any returned information from the reply Apple event. This process, along with the Apple Event Manager API you use, is described in [Remote Procedure Calls From Applications](About%20AppleScript%E2%80%99s%20Support%20for%20XML-RPC%20and%20SOAP.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temjnijauuscbjjcei).

This section provides sample code you can use from an application, tool, or other code to send an XML-RPC request to a server. The sample code calls an Internet server that returns the state name for the passed state index. That is, for an index value of 1 it returns Alabama, for 2 it returns Alaska, for 50 it returns Wyoming, and so on.

You can use the sample code in this section in a number of ways. The following steps show one approach: creating a C++ tool with Project Builder:

1. Launch Project Builder.
2. Choose New Project from the File menu.
3. Choose the C++ tool template.
4. Replace the code in the automatically generated main.cpp file with the sample code in [Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusssginbem), [Listing 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusrscjbdeq), and [Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusq2bindeg), in that order.
5. Use Add Frameworks from the Project menu to add `Carbon.framework` to the project.

Once you’ve built the tool, you can run it in Project Builder and examine its output in the Console pane, or run it in a Terminal window.

You can also build this code directly in a Terminal window with the following compile line:

```
cc -g -o xmlrpc xmlrpc.cp -framework Carbon
```

If you want to compile with a C compiler, rather than a C++ compiler, you’ll have to modify the code so that all variables are declared at the beginning of functions, rather than where they are used.

[Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusssginbem) shows include statements, constants, and declarations to place at the beginning of your code file. This code

- includes `Carbon.h` to gain access to the scripting API it needs
- defines a simple error macro that uses `fprintf` to show an error number and line number, then exits the application
- defines constants that specify the server and method name to call to get state name information
- declares a debug function that is defined later

__Listing 3-1__  Includes, constants, and declarations for making an XML-RPC call.

```c
#include <Carbon/Carbon.h>

// Define a simple error macro that just shows the error and line number
#define checkErr(err) \
    while (err != noErr) \
        { fprintf(stderr, "Failed at line %d, error %d\n", __LINE__, err);\
         exit(-1); }

// Define constants for the XML-RPC server and method.
static const char* serverURL = "http://betty.userland.com/RPC2";
static const char* methodName = "examples.getStateName";

// Declare our debug function.
static void dumpDebug(const char* msg, const AppleEvent* replyEvent,
    OSType debugDataKey);
```


[Listing 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusrscjbdeq) shows a `main` function that prepares an XML-RPC Apple event, sends it, and displays information from the reply Apple event. To do so, it performs the following steps:

1. It calls `AECreateDesc` to create a target address descriptor of type `typeApplicationURL` that specifies the target for the request (a remote server). It uses the constant `serverURL` defined previously to specify the desired Internet server.
2. It calls `AECreateAppleEvent` to create an Apple event with event class `kAERPCClass`, event ID `KAEXMLRPCScheme`, and with the target address descriptor from step 1.
3. It calls `AECreateList` to create the direct object for the Apple event.
4. It calls `AEPutParamPtr` to insert the method name, using the key `keyRPCMethodName` and the constant `methodName` defined previously.
5. It calls `AECreateList` to create a list descriptor for the remote procedure call parameters.
6. It calls `AEPutPtr` to insert the only parameter for the `examples.getStateName` function, the state index, into the parameter list. It passes `typeSInt32` for the type code and an index value of 41. The index number was chosen randomly from the legal values of 1 to 50 (the fifty states).
7. It calls `AEPutParamDesc` to add the parameter list to the Apple event’s direct object.
8. It calls `AEPutParamDesc` to insert the direct object into the Apple event.
9. It calls `AEPutAttributePtr` to turn on debugging by adding an attribute to the event with key `keyXMLDebuggingAttr` and the value `kAEDebugXMLDebugAll`. This step is optional.
10. It initializes a reply Apple event.
11. It calls `AESend` to send the Apple event, passing `kAEWaitReply` to indicate it will wait for a reply.
12. If the previous call succeeds, it calls `AEGetParamPtr` with key `keyDirectObject` and desired type of `typeChar` to extract the direct object of the reply Apple event. For a successful call with state index 41, the returned value is the string “South Dakota”.

    It calls `fprintf` to display the state name. For example

```
    State is South Dakota!
```
13. The main function then calls the function `dumpDebug`, shown in [Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusq2bindeg), once each to display the header and data for the original XML-RPC request and for the reply from the server. [Listing 4-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbussciifcus) shows the possible result of these calls.

__Listing 3-2__  main function to send an XML-RPC Apple event.

```
//------------------------- main ----------------------------------
// Builds and sends an XML-RPC Apple event.
// Sends the Apple event to a server that returns the state
//   name corresponding to the passed number; e.g., the number
//   5 corresponds to the state California.
// Prints the returned state name, then calls function
//   to dump debug information from reply
int main()
{
    OSErr err;
    AEDesc targetAddress;

    // Create the target address.
    //   Using type typeApplicationURL makes it a remote procedure call event.
    err = AECreateDesc(typeApplicationURL, serverURL, strlen(serverURL), &targetAddress);
    checkErr(err);

    // Create an XML-RPC Apple event
    AppleEvent xmlrpcEvent;
    err = AECreateAppleEvent(kAERPCClass, kAEXMLRPCScheme, &targetAddress,
            kAutoGenerateReturnID, kAnyTransactionID, &xmlrpcEvent);
    checkErr(err);
    AEDisposeDesc(&targetAddress);

    // Create the parameters for the event - the direct object is a record
    //   that contains the method name, and a list of parameters
    AEDesc directObject;
    err = AECreateList(NULL, 0, true, &directObject);
    checkErr(err);

    // Insert the method name
    err = AEPutParamPtr(&directObject, keyRPCMethodName, typeChar,
        methodName, strlen(methodName));
    checkErr(err);

    // Create the list for the actual parameters
    AEDesc paramList;
    err = AECreateList(NULL, 0, false, &paramList);
    checkErr(err);

    // Put the state index into the parameter array
    SInt32 stateIndex = 41; // Should correspond to South Dakota
    err = AEPutPtr(&paramList, 0, typeSInt32, &stateIndex,
        sizeof(stateIndex));
    checkErr(err);

    // Put the parameter list into the direct object
    err = AEPutParamDesc(&directObject, keyRPCMethodParam, &paramList);
    checkErr(err);
    AEDisposeDesc(&paramList);

    // Put the direct object into the event
    err = AEPutParamDesc(&xmlrpcEvent, keyDirectObject, &directObject);
    checkErr(err);
    AEDisposeDesc(&directObject);

    // Request all available debugging information. That will include
    //   the header and body for both the XML-RPC request and the reply
    //   from the server.
    SInt32 debugAttr = kAEDebugXMLDebugAll;
    err = AEPutAttributePtr(&xmlrpcEvent, keyXMLDebuggingAttr, typeSInt32,
        &debugAttr, sizeof(debugAttr));

    // Send the event
    AppleEvent replyEvent;
    AEInitializeDescInline(&replyEvent);
    err = AESend(&xmlrpcEvent, &replyEvent, kAEWaitReply, kAENormalPriority,
        kAEDefaultTimeout, NULL, NULL);
    checkErr(err);

    // The direct object of the reply Apple event contains
    // our result (the name of the state)
    char buffer[255];
    Size actualSize;
    err = AEGetParamPtr(&replyEvent, keyDirectObject, typeChar, NULL,
        buffer, sizeof(buffer), &actualSize);
    checkErr(err);

    fprintf(stderr, "State is %.*s!\n", actualSize, buffer);

    // Dump debug information
    dumpDebug("HTTP POST header", &replyEvent, keyAEPOSTHeaderData);
    dumpDebug("XML Request", &replyEvent, keyAEXMLRequestData);
    dumpDebug("HTTP Reply header", &replyEvent, keyAEReplyHeaderData);
    dumpDebug("XML Reply", &replyEvent, keyAEXMLReplyData);

    return 0;
}
```


[Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusq2bindeg) shows a function that extracts debug information from a passed Apple event and displays it with `fprintf`. The information displayed depends on the key passed in the `debugDataKey` parameter. To display debug data, this function:

1. Calls `AEGetParamDesc`, passing the key specified by the `debugDataKey` parameter and the desired type `typeChar`, to extract character data for that debug key.

   The possible debug keys are shown in [Apple Event Manager API for Remote Procedure Calls](About%20AppleScript%E2%80%99s%20Support%20for%20XML-RPC%20and%20SOAP.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temjnijauuqsbizcuo).
2. If step 1 fails, it uses `fprintf` to display an error message.

   Otherwise, it formats the retrieved character data to show tabs, carriage returns, and line feeds, and displays it with `fprintf`.

__Listing 3-3__  A function to display debug information from an XML-RPC reply Apple event.

```
// ------------------------- dumpDebug ----------------------------------
// Extract and display debug information from a reply Apple event.

static void dumpDebug(const char* msg, const AppleEvent* replyEvent,
    OSType debugDataKey)
{
    fprintf(stderr, "%s:\n", msg);

    AEDesc paramDesc;
    OSErr err = AEGetParamDesc(replyEvent, debugDataKey,
                                typeChar, &paramDesc);
    if (err != noErr)
        fprintf(stderr, "\tCan't get debug data %4.4s - %d returned\n",
            &debugDataKey, err);
    else
    {
        int len = AEGetDescDataSize(&paramDesc);
        char* buffer = new char[len];
        AEGetDescData(&paramDesc, buffer, len);

        char* p = buffer;
        char* pEnd = buffer + len;

        while (p < pEnd)
        {
            char* pNext = strpbrk(p, "\r\n");
            if (pNext == NULL)
                pNext = pEnd;
            else
            {
                while (pNext < pEnd && (*pNext == '\r' || *pNext == '\n'))
                {
                    *pNext++ = '\0';
                }
            }
            fprintf(stderr, "\t%.*s\n", pNext - p, p);
            p = pNext;
        }

        AEDisposeDesc(&paramDesc);
        delete[] buffer;
    }
    fprintf(stderr, "\n\n");
}
```

The following listing shows sample output from the `dumpDebug` function for an XML-RPC Apple event.

__Listing 3-4__  Sample header and data from an XML-RPC post and the reply.

```
HTTP POST header:
    POST /RPC2 HTTP/1.0
    User-Agent: OS X; AEServer (1.0)
    Host: betty.userland.com
    Content-Type: text/xml
    Content-length: 216


XML Request:
    <?xml version="1.0" encoding="UTF-8"?>
        <methodCall>
            <methodName>examples.getStateName</methodName>
            <params>
                <param>
                    <value>
                        <i4>41</i4>
                    </value>
                </param>
            </params>
        </methodCall>


HTTP Reply header:
    HTTP/1.1 200 OK
    Connection: close
    Content-Length: 141
    Content-Type: text/xml
    Date: Mon, 13 Aug 2001 03:56:34 GMT
    Server: UserLand Frontier/7.0.1-WinNT


XML Reply:
    <?xml version="1.0"?>
    <methodResponse>
        <params>
            <param>
                <value>South Dakota</value>
                </param>
            </params>
        </methodResponse>
```


To make a SOAP request from an application or other code, you create an Apple event that describes the request, use the `AESend` function to send it, and extract any returned information from the reply Apple event. This process, along with the Apple Event Manager API you use, is described in [Remote Procedure Calls From Applications](About%20AppleScript%E2%80%99s%20Support%20for%20XML-RPC%20and%20SOAP.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temjnijauuscbjjcei).

This section provides sample code for sending a SOAP request to a server. Like the sample code in [Making an XML-RPC Call](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusr2jjjcue), it makes a request to an Internet server that returns the state name for the passed state index. That is, for an index value of 1 it returns Alabama, for 2 it returns Alaska, and so on. In this case, however, the sample code calls the `getStateName` method, a SOAP method on an entirely different server.

You can use the sample code in this task in a number of ways. The following steps show how to create a C++ tool with Project Builder:

1. Launch Project Builder.
2. Choose New Project from the File menu.
3. Choose the C++ tool template.
4. Replace the code in the automatically generated main.cpp file with the sample code in [Listing 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusqsci5bus), [Listing 4-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusskgivees), [Listing 4-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusskfi5ceg), and [Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusq2bindeg), in that order.
5. Use Add Frameworks from the Project menu to add `Carbon.framework` to the project.

Once you’ve built the tool, you can run it in Project Builder and examine its output in the Console pane, or run it in a Terminal window.

You can also build this code directly in a Terminal window with the following compile line:

```
cc -g -o soap soap.cp -framework Carbon
```

If you want to compile with a C compiler, rather than a C++ compiler, you’ll have to modify the code so that all variables are declared at the beginning of functions, rather than where they are used.

[Listing 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusqsci5bus) shows include statements, constants, and declarations to place at the beginning of your code file. This code

- includes Carbon.h to gain access to the scripting API it needs
- defines a simple error macro that uses `fprintf` to show an error number and line number, then exits the application
- defines constants that specify the server and method name to call to get state name information
- declares a function (defined later) that creates a parameter list record
- declares a debug function that is defined later

__Listing 3-5__  Includes, constants, and declarations for making a SOAP request.

```c
#include <Carbon/Carbon.h>

#define checkErr(err) \
    while (err != noErr) \
    { fprintf(stderr, "Failed at line %d, error %d\n", __LINE__, err); \
    exit(-1); }

static const char* serverURL = "http://www.soapware.org/examples";
static const char* methodName = "getStateName";
static const char* methodNameSpaceURI = "http://www.soapware.org/";

static OSStatus createUserRecord(AEDesc* desc, const char* paramName,
    OSType dataType, const void* data, UInt32 dataSize);
static void dumpDebug(const char* msg, const AppleEvent* reply,
    OSType debugDataKey);
```


[Listing 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusrscjbdeq) shows a `main` function that prepares a SOAP request Apple event, sends it, and displays information from the reply Apple event. To do so, it performs the following steps:

1. It calls `AECreateDesc` to create a target address descriptor of type `typeApplicationURL` that specifies the target for the request (a remote server). It uses the constant `serverURL` defined previously to specify the desired Internet server.
2. It calls `AECreateAppleEvent` to create an Apple event with event class `kAERPCClass`, event ID `kAESOAPScheme`, and with the target address descriptor from step 1.
3. It calls `AECreateList` to create the direct object for the Apple event.
4. It calls `AEPutParamPtr` to insert the method name, using the key `keyRPCMethodName` and the constant `methodName` defined previously.
5. It calls the function `createUserRecord`, shown in [Listing 4-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusskfi5ceg), to create an `AEDesc` record that stores the parameter name and value for a method that has one of each.
6. It calls `AEPutParamDesc` to add the parameter record to the Apple event’s direct object.
7. It calls `AEPutParamPtr` to insert the method namespace URI, using the key `keySOAPMethodNameSpaceURI` and the constant `methodNameSpaceURI` defined previously.
8. It calls `AEPutParamDesc` to insert the direct object into the Apple event.
9. It calls `AEPutAttributePtr` to turn on debugging by adding an attribute to the event with key `keyXMLDebuggingAttr` and the value `kAEDebugXMLDebugAll`. This step is optional.
10. It initializes a reply Apple event.
11. It calls `AESend` to send the Apple event, passing `kAEWaitReply` to indicate it will wait for a reply.
12. If the previous call succeeds, it calls `AEGetParamPtr` with key `keyDirectObject` and desired type of `typeChar` to extract the direct object of the reply Apple event. For a successful call with state index 41, the returned value is the string “South Dakota”.

    It calls `fprintf` to display the state name. For example

```
    State is South Dakota!
```
13. The main function then calls the function `dumpDebug`, shown in [Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusq2bindeg), once each to display the header and data for the original XML-RPC request and for the reply from the server. [Listing 4-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusrsbifeec) shows the possible result of these calls.

__Listing 3-6__  main function to send a SOAP Apple event.

```
//------------------------- main ----------------------------------
// Builds and sends a SOAP request Apple event.
// Sends the Apple event to a server that returns the state
//   name corresponding to the passed number; e.g., the number
//   5 corresponds to the state California.
// Prints the returned state name, then calls function
//   to dump debug information from reply
int main()
{
    OSErr err;
    AEDesc targetAddress;

    // Create the target address
    //   Using type typeApplicationURL makes it a remote procedure
    //   call event.
    err = AECreateDesc(typeApplicationURL, serverURL, strlen(serverURL),
        &targetAddress);
    checkErr(err);

    // Create a SOAP request Apple event
    AppleEvent event;
    err = AECreateAppleEvent(kAERPCClass, kAESOAPScheme, &targetAddress,
        kAutoGenerateReturnID, kAnyTransactionID, &event);
    checkErr(err);
    AEDisposeDesc(&targetAddress);

    // Create the parameters for the event - the direct object is a
    // record that contains the method name, and a list of parameters

    AEDesc directObject;
    err = AECreateList(NULL, 0, true, &directObject);
    checkErr(err);

    // Put the method name
    err = AEPutParamPtr(&directObject, keyRPCMethodName, typeChar,
        methodName, strlen(methodName));
    checkErr(err);

    // The parameters for a SOAP request are a record. We use the
    // "AppleScript" format for records that contain user readable
    // names, and call a helper routine to construct this record.
    AEDesc paramRecord;
    SInt32 stateIndex = 41;
    err = createUserRecord(&paramRecord, "statenum", typeSInt32,
        &stateIndex, sizeof(stateIndex));
    checkErr(err);

    // Put the parameter record into the direct object
    err = AEPutParamDesc(&directObject, keyRPCMethodParam,
        &paramRecord);
    checkErr(err);
    AEDisposeDesc(&paramRecord);

    // Additional pieces for soap are the SOAP schema, method
    //      namespaceURI and SOAPAction.
    // If the SOAP schema is not explicitly specified, it defaults
    //      to kSOAP1999Schema for the 1999 schema
    //      (corresponding to the 1.1 specification).
    // If the SOAPAction is not explicitly specified, it will be
    //    the path part of the URL (in this case, "/examples")

    err = AEPutParamPtr(&directObject, keySOAPMethodNameSpaceURI,
        typeChar, methodNameSpaceURI, strlen(methodNameSpaceURI));
    checkErr(err);

    // Put the direct object into the event
    err = AEPutParamDesc(&event, keyDirectObject, &directObject);
    checkErr(err);
    AEDisposeDesc(&directObject);

    // Request debugging information
    SInt32 debugAttr = kAEDebugXMLDebugAll;
    err = AEPutAttributePtr(&event, keyXMLDebuggingAttr, typeSInt32,
        &debugAttr, sizeof(debugAttr));

    // Send the event
    AppleEvent reply;
    AEInitializeDescInline(&reply);
    err = AESend(&event, &reply, kAEWaitReply, kAENormalPriority,
        kAEDefaultTimeout, NULL, NULL);
    checkErr(err);

    // The direct object contains our result (the name of the state)
    char buffer[255];
    Size actualSize;
    err = AEGetParamPtr(&reply, keyDirectObject, typeChar, NULL,
        buffer, sizeof(buffer), &actualSize);
    checkErr(err);

    fprintf(stderr, "State is %.*s!\n", actualSize, buffer);

    // Dump debug information
    dumpDebug("HTTP POST header", &reply, keyAEPOSTHeaderData);
    dumpDebug("XML Request", &reply, keyAEXMLRequestData);
    dumpDebug("HTTP Reply header", &reply, keyAEReplyHeaderData);
    dumpDebug("XML Reply", &reply, keyAEXMLReplyData);

    return 0;
}
```


[Listing 4-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusskfi5ceg) shows a function that creates a record containing the parameter name and value for a SOAP method with one parameter.

To prepare a parameter list record, this function performs the following steps:

1. It calls `AECreateList` to create a list descriptor record for the SOAP request parameters.
2. It calls `AECreateList` again to create a list descriptor for the parameter name and value.
3. Calls `AEPutPtr` to insert the passed parameter name in the parameter name and value list, with the type `typeChar`.
4. Calls `AEPutPtr` again to insert the passed parameter data in the parameter name and value list, with the type specified the passed type.
5. It calls `AEPutParamDesc` to add the parameter name and value list to the parameter list record.

If you need to create a parameter list record for a SOAP request with multiple parameters, you can define a function with a variable length argument list. The function can iterate over the arguments, performing steps 3 and 4 (adding the name and data) for each pair of parameter arguments.

__Listing 3-7__  A function to create a parameter list record for a SOAP request Apple event.

```
// -------------------- createUserRecord -----------------------------
// Creates a record containing the parameters for a SOAP request.
// Uses the "AppleScript" format for records that contain user readable
// names.

static OSStatus createUserRecord(AEDesc* desc, const char* paramName,
    OSType dataType, const void* data, UInt32 dataSize)
{
    OSErr err = AECreateList(0, NULL, true, desc);
    if (err == noErr) {
        AEDesc termsList;
        err = AECreateList(0, NULL, false, &termsList);

        if (err == noErr)
            err = AEPutPtr(&termsList, 0, typeChar,
                paramName, strlen(paramName));
        if (err == noErr)
            err = AEPutPtr(&termsList, 0, dataType,
                data, dataSize);

        if (err == noErr)
            err = AEPutParamDesc(desc, keyASUserRecordFields,
                &termsList);

        AEDisposeDesc(&termsList);
    }
    return err;
}
```


The sample code to display debug information from a SOAP request Apple event uses the same `dumpDebug` function as the sample code for making an XML-RPC call. That code is shown in [Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusq2bindeg). However, because the XML-RPC and SOAP protocols are different, the requests, the Apple events that represent them, and the debug output are all different. Listing [Listing 4-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnijbusrsbifeec) shows sample output from the `dumpDebug` function for a SOAP request Apple event.

__Listing 3-8__  Sample header and data from a SOAP post and the reply.

```
HTTP POST header:
    POST /examples HTTP/1.0
    Host: www.soapware.org
    SOAPAction: "/examples"
    User-Agent: OS X; AEServer (1.0)
    Content-Type: text/xml
    Content-length: 538


XML Request:
    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope
        xmlns:xsd="http://www.w3.org/1999/XMLSchema"
        xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance"
        SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
        xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
        <SOAP-ENV:Body>
            <m:getStateName xmlns:m="http://www.soapware.org/">
                    <statenum xsi:type="xsd:int">41</statenum>
            </m:getStateName>
        </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>


HTTP Reply header:
    HTTP/1.1 200 OK
    Connection: close
    Content-Length: 499
    Content-Type: text/xml; charset="us-ascii"
    Date: Mon, 13 Aug 2001 05:07:46 GMT
    Server: UserLand Frontier/7.0.1-WinNT


XML Reply:
    <?xml version="1.0"?>
    <SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
        xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-ENV="http://
        schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/1999/XMLSchema"
        xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance">
        <SOAP-ENV:Body>
            <getStateNameResponse>
                <Result xsi:type="xsd:string">South Dakota</Result>
                </getStateNameResponse>
            </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>
```

[Next](Document%20Revision%20History.md)[Previous](Making%20Remote%20Procedure%20Calls%20From%20Scripts.md)

