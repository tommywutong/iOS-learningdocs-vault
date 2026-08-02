---
title: NSNetServices and CFNetServices Programming Guide
apple_id: TP40002736
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSNetServiceProgGuide/Articles/CFNetServices.html
archived_at: '2026-07-15T08:18:19.317775Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [NSNetServices and CFNetServices Programming Guide](About%20NSNetServices%20and%20CFNetServices.md)


[Next](Browsing%20for%20Domains.md)[Previous](Connecting%20to%20and%20Monitoring%20Network%20Services.md)

# Using CFNetServices

`CFNetServices` is an API in the `CFNetwork` framework (Core Foundation level) that allows you to publish or search for network services.

At a high level, the `CFNetServices` API provides access to Bonjour through three objects:

- `CFNetService`—An object that represents a single service on the network. A `CFNetService` object has a name, a type, a domain, and a port number. Service types used by `CFNetServices` are maintained at [http://www.dns-sd.org/servicetypes.html](http://www.dns-sd.org/servicetypes.html).
- `CFNetServiceBrowser`—An object used to discover domains and discover network services within domains.
- `CFNetServiceMonitor`—An object used to monitor services for changes to their TXT records.

Publishing a service on the network involves two tasks: creating a service and registering a service. The next two sections describe what is required to perform these two tasks.

To create a `CFNetService` object, call [CFNetServiceCreate](https://developer.apple.com/documentation/cfnetwork/1426628-cfnetservicecreate) and provide the following information about the service:

- __Name.__ The human-readable name of the service (such as “`Sales Laser Printer`”)
- __Service Type.__ The type of service, such as “`_printer._tcp`“;
- __Domain.__ The domain for the service, typically the empty string (`CFSTR("")`)for default domain(s), or `local.` for the local domain only
- __Port.__ The port number the service listens on

If you are implementing a protocol that relies on data stored in DNS text records, you can associate that information with a `CFNetService` object by calling [CFNetServiceSetTXTData](https://developer.apple.com/documentation/cfnetwork/1426670-cfnetservicesettxtdata)).

Associate a callback function with your `CFNetService` object by calling [CFNetServiceSetClient](https://developer.apple.com/documentation/cfnetwork/1426447-cfnetservicesetclient). Your callback function is called to report errors that occur while your service is running and to report on the status of publication.

If you want the service to run asynchronously, you must also schedule the service on a run loop by calling [CFNetServiceScheduleWithRunLoop](https://developer.apple.com/documentation/cfnetwork/1426730-cfnetserviceschedulewithrunloop); otherwise, the service will run synchronously. For more information about the modes in which a service can run, see[Asynchronous and Synchronous Modes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi3tmlkci5beeskgirba).

Listing A-1 shows how to create a `CFNetService` object.

__Listing A-1__  Creating a `CFNetService` object

```
    CFStringRef serviceType = CFSTR("_printer._tcp");
    CFStringRef serviceName = CFSTR("Sales Laser Printer");
    CFStringRef theDomain = CFSTR("");
    int chosenPort = 515;

    CFNetServiceRef netService = CFNetServiceCreate(NULL, theDomain, serviceType, serviceName, chosenPort);
```


To make a service available on the network, call [CFNetServiceRegisterWithOptions](https://developer.apple.com/documentation/cfnetwork/1426790-cfnetserviceregisterwithoptions). (This operation is also known as “publishing” a service.) The service can then be found by clients until you unregister the service by calling [CFNetServiceCancel](https://developer.apple.com/documentation/cfnetwork/1426533-cfnetservicecancel).

See Listing A-2 for sample code on this subject.

__Listing A-2__  Registering an asynchronous service

```
void registerCallback (
   CFNetServiceRef theService,
   CFStreamError* error,
   void* info)
{
    // ...
}

void startBonjour (CFNetServiceRef netService) {
   CFStreamError error;
   CFNetServiceClientContext clientContext = { 0, NULL, NULL, NULL, NULL };

   CFNetServiceSetClient(netService, registerCallback, &clientContext);
   CFNetServiceScheduleWithRunLoop(netService, CFRunLoopGetCurrent(), kCFRunLoopCommonModes);
   CFOptionFlags options = 0; // or kCFNetServiceFlagNoAutoRename

   if (CFNetServiceRegisterWithOptions(netService, options, &error) == false) {
     CFNetServiceUnscheduleFromRunLoop(netService, CFRunLoopGetCurrent(),kCFRunLoopCommonModes);
     CFNetServiceSetClient(netService, NULL, NULL);
     CFRelease(netService);
     fprintf(stderr, "could not register Bonjour service");
   }
}
```


To browse for services represented by a `CFNetService` object, call [CFNetServiceBrowserCreate](https://developer.apple.com/documentation/cfnetwork/1426560-cfnetservicebrowsercreate) and provide a pointer to a callback function that will be called as services are found.

If you want searches to be conducted asynchronously, you must also schedule the browser on a run loop by calling [CFNetServiceBrowserScheduleWithRunLoop](https://developer.apple.com/documentation/cfnetwork/1426904-cfnetservicebrowserschedulewithr).

To browse for services, you can call [CFNetServiceBrowserSearchForServices](https://developer.apple.com/documentation/cfnetwork/1426405-cfnetservicebrowsersearchforserv) and specify the services to search for. For the domain parameter, you have two options. It is recommended that you pass the empty string (`CFSTR("")`) as the domain, allowing you to discover services in any domain on which your system is registered. Alternatively, you can specify a domain to search in. Your callback function will be called and passed a `CFNetService` object representing a matching service. The `CFNetServiceBrowser` object continues searching until your app stops the search by calling [CFNetServiceBrowserStopSearch](https://developer.apple.com/documentation/cfnetwork/1426523-cfnetservicebrowserstopsearch).

For each `CFNetService` object that your callback function receives, you can call [CFNetServiceResolveWithTimeout](https://developer.apple.com/documentation/cfnetwork/1426563-cfnetserviceresolvewithtimeout) to update the service with the IP address for the service. Then call [CFNetServiceGetAddressing](https://developer.apple.com/documentation/cfnetwork/1426743-cfnetservicegetaddressing) to get an array of `CFDataRef` objects, one for each IP address associated with the service. Each `CFDataRef` object, in turn, contains a `sockaddr` structure with an IP address.

A good example of how to browse for services can be seen in Listing A-3.

__Listing A-3__  Browsing asynchronously for services

```
void MyBrowseCallBack (
   CFNetServiceBrowserRef browser,
   CFOptionFlags flags,
   CFTypeRef domainOrService,
   CFStreamError* error,
   void* info)
{
    // ...
}

static Boolean MyStartBrowsingForServices(CFStringRef type, CFStringRef domain) {
     CFNetServiceClientContext clientContext = { 0, NULL, NULL, NULL, NULL };
     CFStreamError error;
     Boolean result;

     assert(type != NULL);

     CFNetServiceBrowserRef gServiceBrowserRef = CFNetServiceBrowserCreate(kCFAllocatorDefault, MyBrowseCallBack, &clientContext);
     assert(gServiceBrowserRef != NULL);

     CFNetServiceBrowserScheduleWithRunLoop(gServiceBrowserRef, CFRunLoopGetCurrent(), kCFRunLoopCommonModes);

     result = CFNetServiceBrowserSearchForServices(gServiceBrowserRef, domain, type, &error);
     if (result == false) {

         // Something went wrong, so let's clean up.
         CFNetServiceBrowserUnscheduleFromRunLoop(gServiceBrowserRef, CFRunLoopGetCurrent(), kCFRunLoopCommonModes);         CFRelease(gServiceBrowserRef);
         gServiceBrowserRef = NULL;

         fprintf(stderr, "CFNetServiceBrowserSearchForServices returned (domain = %ld, error = %d)\n", (long)error.domain, error.error);
     }

     return result;
}
```


After you have a name, type, and domain, you can resolve the service to retrieve its hostname and port. As with registering a service, resolving a service also requires a `CFNetServiceRef` object. If you already have one (typically obtained through a browse operation callback), you don’t need to take any further action. Otherwise, you can create one yourself by calling `CFNetServiceCreate`.

If you plan to resolve a service asynchronously, associate the newly created `CFNetServiceRef` object with a callback function, which will receive a `CFNetServiceRef` object and a pointer to a `CFStreamError` object. You can set this callback by calling [CFNetServiceSetClient](https://developer.apple.com/documentation/cfnetwork/1426447-cfnetservicesetclient). Be sure to call [CFNetServiceScheduleWithRunLoop](https://developer.apple.com/documentation/cfnetwork/1426730-cfnetserviceschedulewithrunloop) afterward to add the service to a run loop (which is typically the result of a call to [CFRunLoopGetCurrent](https://developer.apple.com/documentation/corefoundation/1542428-cfrunloopgetcurrent)).

After setting up the run loop, call [CFNetServiceResolve](https://developer.apple.com/documentation/cfnetwork/1574815-cfnetserviceresolve). If this call returns an error, you should clean up all the references you created. Otherwise, just wait for your callback functions to be called.

An example of resolving a service with `CFNetService` is in Listing A-4.

__Listing A-4__  Resolving a service asynchronously

```
void MyResolveCallback (
   CFNetServiceRef theService,
   CFStreamError* error,
   void* info)
{
    // ...
}

static void MyResolveService(CFStringRef name, CFStringRef type, CFStringRef domain)
{
    CFNetServiceClientContext context = { 0, NULL, NULL, NULL, NULL };
    CFTimeInterval duration = 0; // use infinite timeout
    CFStreamError error;

    CFNetServiceRef gServiceBeingResolved = CFNetServiceCreate(kCFAllocatorDefault, domain, type, name, 0);
    assert(gServiceBeingResolved != NULL);

    CFNetServiceSetClient(gServiceBeingResolved, MyResolveCallback, &context);
    CFNetServiceScheduleWithRunLoop(gServiceBeingResolved, CFRunLoopGetCurrent(), kCFRunLoopCommonModes);

    if (CFNetServiceResolveWithTimeout(gServiceBeingResolved, duration, &error) == false) {

         // Something went wrong, so let's clean up.
         CFNetServiceUnscheduleFromRunLoop(gServiceBeingResolved, CFRunLoopGetCurrent(), kCFRunLoopCommonModes);
         CFNetServiceSetClient(gServiceBeingResolved, NULL, NULL);
         CFRelease(gServiceBeingResolved);
         gServiceBeingResolved = NULL;

         fprintf(stderr, "CFNetServiceResolve returned (domain = %ld, error = %d)\n", (long)error.domain, error.error);
}

    return;
}
```


`CFNetServiceMonitor` lets you watch services for changes to `TXT` records.

In the app that is publishing a service, you can provide a custom `TXT` record by calling [CFNetServiceSetTXTData](https://developer.apple.com/documentation/cfnetwork/1426670-cfnetservicesettxtdata). The most straightforward way to provide spec-compliant data is by calling [CFNetServiceCreateTXTDataWithDictionary](https://developer.apple.com/documentation/cfnetwork/1426572-cfnetservicecreatetxtdatawithdic) and passing it a dictionary of values to publish.

In the app that needs to monitor a service, perform the following steps:

1. After you have a `CFNetServiceRef` object for the service you wish to monitor, create a monitor reference (`CFNetServiceMonitorRef`) by calling [CFNetServiceMonitorCreate](https://developer.apple.com/documentation/cfnetwork/1426665-cfnetservicemonitorcreate).
2. Schedule the monitor reference on a run loop with [CFNetServiceMonitorScheduleWithRunLoop](https://developer.apple.com/documentation/cfnetwork/1426880-cfnetservicemonitorschedulewithr). (You can obtain the default run loop by calling [CFRunLoopGetCurrent](https://developer.apple.com/documentation/corefoundation/1542428-cfrunloopgetcurrent).)
3. Start the monitor by calling [CFNetServiceMonitorStart](https://developer.apple.com/documentation/cfnetwork/1426842-cfnetservicemonitorstart), passing it the monitor reference and a callback function to handle the resulting data. Be sure to check the return value to ensure that the monitor started successfully.
4. In the callback function, the most straightforward way to handle the `TXT` data is by calling [CFNetServiceCreateDictionaryWithTXTData](https://developer.apple.com/documentation/cfnetwork/1426852-cfnetservicecreatedictionarywith) to obtain a dictionary containing the original key-value pairs.

When you no longer need to monitor a service, call [CFNetServiceMonitorStop](https://developer.apple.com/documentation/cfnetwork/1426696-cfnetservicemonitorstop) (to stop the monitoring), [CFNetServiceMonitorUnscheduleFromRunLoop](https://developer.apple.com/documentation/cfnetwork/1426400-cfnetservicemonitorunschedulefro) (to unschedule your monitor from its run loop), and [CFNetServiceMonitorInvalidate](https://developer.apple.com/documentation/cfnetwork/1426906-cfnetservicemonitorinvalidate) (to destroy the monitor reference).

Several `CFNetServices` functions can operate in asynchronous or synchronous mode. Scheduling a `CFNetService` or `CFNetServiceBrowser` object on a run loop causes the service or browser to operate in asynchronous mode. If a `CFNetService` or `CFNetServiceBrowser` object is not scheduled on a run loop, it operates in synchronous mode. Operating in asynchronous mode changes the behavior of its functions.

Although it is possible to use the synchronous modes of these functions, keep in mind that it is unacceptable to block the user interface or other functions of your program while you wait for synchronous functions to return. Because network operations may take an arbitrary amount of time to complete, it is highly recommended that you use the asynchronous modes of each function.

Table A-1 describes the differences in behavior between synchronous and asynchronous modes.

__Table A-1__  Behavior of certain `CFNetServices` functions in asynchronous and synchronous mode

| Function | Asynchronous mode | Synchronous mode |
| `CFNetServiceRegisterWithOptions` | Starts the registration and returns. The callback function for the `CFNetService` is called to report any errors that occur while the service is running. The service is available on the network until your app cancels the registration. | Blocks until your app cancels the service from another thread or until an error occurs, at which point the function returns. If an error occurs, the error is returned through the provided error structure. The service is available on the network until your app cancels the registration or an error occurs. |
| `CFNetServiceResolveWithTimeout` | Starts the resolution and returns. The callback function for the `CFNetService` is called to report any errors that occur during resolution. The resolution operation runs until the specified timeout is reached or, if the timeout was specified as zero, until it is canceled. | Blocks until at least one IP address is found for the service, an error occurs, the time specified as the timeout parameter is reached, or your app cancels the resolution, at which point the function returns. If an error occurs, the error is returned through the provided error structure. The resolution operation continues to run until your app cancels it or an error occurs. |
| `CFNetServiceBrowserSearchForDomains` | Starts the search and returns. The callback function for the `CFNetServiceBrowser` is called for each domain that is found and when any error occurs while browsing. Browsing continues to run until your app stops the browsing. | Blocks until an error occurs or your app calls `CFNetServiceBrowserStopSearch`, at which time the callback function for the `CFNetServiceBrowser` is called for each domain that was found. Any error is returned through the provided error structure. Browsing continues until your app stops the browsing operation. |
| `CFNetServiceBrowserSearchForServices` | Starts the search and returns. The callback function for the `CFNetServiceBrowser` is called for each `CFNetService` that is found and when any error occurs while browsing. Browsing continues to run until your app stops the browsing. | Blocks until an error occurs or until your app calls `CFNetServiceBrowserStopSearch`, at which time the callback function for the `CFNetServiceBrowser` is called for each `CFNetService` that was found. Any error is returned in the provided error structure. Browsing continues until your app stops the browsing. |

To shut down a service that is running in asynchronous mode, your app unschedules the service from all run loops that it may be scheduled on. The app then calls [CFNetServiceSetClient](https://developer.apple.com/documentation/cfnetwork/1426447-cfnetservicesetclient) with the `clientCB` parameter set to `NULL` to disassociate your callback function from the `CFNetService` object. Finally, the app calls [CFNetServiceCancel](https://developer.apple.com/documentation/cfnetwork/1426533-cfnetservicecancel) to stop the service.

To shut down a service that is running in synchronous mode, your app only needs to call `CFNetServiceCancel` from another thread.

Listing A-5 shows a good example of shutting down an asynchronous `CFNetService` resolve operation that has not timed out.

__Listing A-5__  Canceling an asynchronous `CFNetService` resolve operation

```
void MyCancelResolve(CFNetServiceRef gServiceBeingResolved)
{
     assert(gServiceBeingResolved != NULL);
     CFNetServiceUnscheduleFromRunLoop(gServiceBeingResolved, CFRunLoopGetCurrent(), kCFRunLoopCommonModes);
     CFNetServiceSetClient(gServiceBeingResolved, NULL, NULL);
     CFNetServiceCancel(gServiceBeingResolved);
     CFRelease(gServiceBeingResolved);
     gServiceBeingResolved = NULL;
     return;
}
```

To shut down a browser that is running in asynchronous mode, your app unschedules the browser from all run loops that it may be scheduled on and then calls [CFNetServiceBrowserInvalidate](https://developer.apple.com/documentation/cfnetwork/1426399-cfnetservicebrowserinvalidate). Then your app calls [CFNetServiceBrowserStopSearch](https://developer.apple.com/documentation/cfnetwork/1426523-cfnetservicebrowserstopsearch). If the browser is running in synchronous mode, you only need to call `CFNetServiceBrowserStopSearch`. An example of these functions can be seen in Listing A-6.

__Listing A-6__  Stop browsing for services

```
static void MyStopBrowsingForServices(CFNetServiceBrowserRef gServiceBrowserRef)
{
     CFStreamError streamerror;
     assert(gServiceBrowserRef != NULL);
     CFNetServiceBrowserStopSearch(gServiceBrowserRef, &streamerror);
     CFNetServiceBrowserUnscheduleFromRunLoop(gServiceBrowserRef, CFRunLoopGetCurrent(), kCFRunLoopCommonModes);
     CFNetServiceBrowserInvalidate(gServiceBrowserRef);
     CFRelease(gServiceBrowserRef);
     gServiceBrowserRef = NULL;
     return;
}
```

[Next](Browsing%20for%20Domains.md)[Previous](Connecting%20to%20and%20Monitoring%20Network%20Services.md)

