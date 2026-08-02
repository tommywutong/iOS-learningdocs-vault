---
title: DNSServiceDiscovery Mach-Based API
apple_id: TP30001129
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-04-29'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/dns_discovery_mach/tasks/tasks_mach.html
archived_at: '2026-07-15T08:18:33.216894Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [DNSServiceDiscovery Mach-Based API](Introduction.md)


[Next](reference_mach.md)[Previous](Bonjour%20Overview.md)

# DNSServiceDiscovery Tasks

The DNSServiceDiscovery API helps you to perform
three main tasks:

- registering a service
- browsing for services
- resolving the current address of a service instance

In support of these main tasks, this API can directly assist
you in performing two subsidiary tasks:

- enumerating domains (finding recommended service
  domains)
- updating registrations (changing your DNS registration data
  dynamically)

The next few paragraphs describe some things you should know
about this API before attempting any of the tasks.

Most functions in this API do not return all of their data
using their function return or parameter block. Instead, they require
you to provide a callback function that can handle data sent asynchronously.
This data is in the form of a reply type, such as a `DNSServiceRegistrationReply`.
There are separate reply types for registration, enumeration, browsing,
resolving addresses, and updating registration records. These reply
types can be found in the section [Constants and Data Types](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/dns_discovery_mach/reference/reference_mach2.html#//apple_ref/doc/uid/TP30001129-CH1g-207632).

Your callback function may be called multiple times in response
to a single function call on your part. For example, you might request
a list of available services. Your callback would be called once
for each available service that matches your request, then called
again whenever a matching service is added or removed.

Some functions return error codes or status flags in the usual
way, but many do not. In these cases, any error codes or status
flags are sent to your callback function as part of the asynchronous
reply, along with—or instead of—any returned data.

Most of the functions in this API use a common set of parameters
to describe services. You will need to supply some or all of these
parameters, depending on the purpose of your call. In many cases,
you will provide some parameters, such as the domain and type of
service, and your callback function will receive data corresponding
to other parameters, such as the service name and IP address of
a matching service.

Here is a list of the common parameters used to describe a
service.

- Name—human readable name of the service, such
  as “`Sales Laser Printer`”
- Registration type—the type of service, such as “`_printer._tcp`”
- Domain—the domain for the service, typically “`local.`”
  but you can usually pass an empty string ““ to specify the default
  domain

- Port—the port number for the service
- Text record—an optional field containing any additional
  information that may be needed to use the service, such as a print
  queue name

When your service starts up, you need to register with the
mDNS responder daemon so that applications can discover your service.
This section provides a general overview of the process, followed
by a set of step-by-step instructions and some sample code.

Before registering your service, you need to create a network
socket and obtain an IP address (this can be a link-local IP address
or a universal IP address). Your service should be active and ready
respond to service requests when you register.

The first step in registration is to allocate and initialize
a `dns_service_discovery_ref` record for
your service. This is an opaque type, so you call a create function
to allocate it and initialize it with your chosen DNS name and service
type. Your service type is passed as a standard DNS resource, as
defined by the IANA. You can find the definition at [http://www.iana.org/assignments/dns-parameters](http://www.iana.org/assignments/dns-parameters).

If the DNS name you’ve chosen is already in local use, you’ll
need to choose another name and try again, until you choose a locally-unique
name.

When you register successfully, a Mach reply port is set up
for your service.

The `dns_service_discovery_ref` record
returned to you contains the Mach reply port address, which you
extract using an accessor function.

You need to handle incoming Mach messages by passing them
to a special message-handling function provided by this API. One
way to do this is to generate a Mach reference that uses the message-handling
function in a callback, create a runloop source from it, and add
it to your `CFRunLoop`,
(assuming you have one). In any event, you need to implement some
method for passing incoming Mach messages to this message-handling function.

You have now registered your service; it is announced to the
local network and its access information (IP address, port, and
so on) can be found using multicast DNS, either by name or by browsing
for services.

Here are the actual programming steps:

1. Allocate and initialize a `dns_service_discovery_ref` record
   by calling `DNSServiceRegistrationCreate.`You will be returned a `dns_service_discovery_ref` record
   and a Mach reply port will be set up.
2. Extract your Mach port address by calling `DNSServiceDiscoveryMachPort`.
3. Put a mechanism in place to receive Mach messages and route
   them to `[DNSServiceDiscovery_handleReply](../reference/reference_mach.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxuitstknsxe5tjmnsui2ltmnxxmzlspfpwqylomrwgkutfobwhs)`.
   If you are using a `CFRunLoop`,
   for example, you would do something like this:

   __Listing 2-1__  Sample code for registration

```
// create a callback wrapper for the DNSServiceDiscovery_handleReply
// function
    static void MyHandleMachMessage(
                CFMachPortRef port, void *msg, CFIndex size, void *info)
    {
    DNSServiceDiscovery_handleReply(msg);
    }
// Create a port reference, use it to create a runloop source,
// and add it to the current runloop
static int AddDNSServiceClientToRunLoop(dns_service_discovery_ref client)
{
mach_port_t port = DNSServiceDiscoveryMachPort(client);
if (!port)
    return(-1);
else
    {
    CFMachPortContext  context    = { 0, 0, NULL, NULL, NULL };
    Boolean shouldFreeInfo;
    CFMachPortRef cfMachPort =
        CFMachPortCreateWithPort(kCFAllocatorDefault, port,
        MyHandleMachMessage, &context, &shouldFreeInfo);

    CFRunLoopSourceRef rls = CFMachPortCreateRunLoopSource(NULL,
        cfMachPort, 0);

    CFRunLoopAddSource(CFRunLoopGetCurrent(), rls,kCFRunLoopDefaultMode);
    CFRelease(rls);
    return(0);
    }
}
```

Additional registration sample code can be found in the file `SamplemDNSClient.c`

Browsing for services using this API is fairly simple. You
can find out what services of a given type are available in a given
domain with a single function call.

To browse for available services, take the following step:

1. Call `DNSServiceBrowserCreate`,
   passing in the domain to search and the type of service you’re
   interested in.

You can pass an empty string ““ as the domain to browse—this
automatically selects the default domain.

This function sends a separate reply to your callback function
for every service instance that matches the specified type and domain,
with additional calls when services are added or removed.

To create a list of available services, your application code
must record each reply from `DNSServiceBrowserCreate`,
concatenating them with sufficient logic to account for deletions.

To browse in multiple domains, or for multiple service types,
make one call to `DNSServiceBrowserCreate` for
each domain and service type of interest. Again, it is up to your
application code to keep track of the replies.

Don’t disable the user interface or change the cursor while
waiting for the replies from `DNSServiceBrowserCreate`.
This task should be running in the background all the time. You normally
call `DNSServiceBrowserCreate` only
once per session. Whenever the list of services changes, data is
sent to the callback function that you provide, so you can simply
leave the callback active, and your list will always be up to date.
This information typically changes infrequently, so the callback
shouldn’t use much CPU time.

Calling the browser-create function allocates a `dns_service_discovery_ref` record,
so if you choose to deactivate your callback and repeat the search
as needed, be sure to deallocate the record using `[DNSServiceDiscoveryDeallocate](../reference/reference_mach.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxuitstknsxe5tjmnsui2ltmnxxmzlspfcgkylmnrxwgylumu)` before
calling `[DNSServiceBrowserCreate](../reference/reference_mach.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxuitstknsxe5tjmnsue4tpo5zwk4sdojswc5df)` again.
Otherwise, you will “leak” a record for every search.

The actual IP address and port of a given service instance
are more ephemeral than the list of available services. You should
resolve the current address of a service instance just prior to
actually using the service, each time you use it. See the next section, [Resolving the Current Address of a Service Instance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqguwtcnbtge3ts).

Browsing sample code can be found in the file `SamplemDNSClient.c`

Once you have the name, service type, and domain of a service,
you can find the address (and any other access information you may
need, such as a print queue name) by calling `DNSServiceResolverResolve`.

To resolve the current address of a service instance, perform
the following steps:

1. If you have not already done so, obtain a valid
   name, service type, and domain by calling `DNSServiceBrowserCreate`.
2. Call `DNSServiceResolverResolve`,
   passing in the service name, domain, and type. Your callback function
   will be called once, asynchronously, when the service address has been
   resolved.

Your callback will receive a `DNSServiceResolverReply` containing
the current IP address, port, and other information you need to
access the service.

One of the less obvious pieces of information you need is
the IP address of the host computer’s network interface. You need
this because link-local addresses are not globally unique URLs—they
are unique only on the local network. If the host computer has more than
one network interface, such as an Ethernet card and an Airport card,
it can be connected to more than one local network. If you know
which interface is in use, you know which local network the service
is on, and the link-local address is fully scoped.

Resolver sample code can be found in the file `SamplemDNSClient.c`

While Bonjour is typically used to register and browse
for services in the `local.` domain,
it is also possible to register your service or browse for available
services in other domains. You can obtain a list of recommended
domains for registration or browsing by calling `DNSServiceDomainEnumerationCreate`.

To obtain a list of recommended domains, take the following
step:

1. Call `DNSServiceDomainEnumerationCreate`,
   passing in a Boolean that tells the function whether you intend
   to register or browse. You will receive a list of recommended search
   domains, including the default domain (typically “`local.`”).
   The list is sent asynchronously to your callback function.

Your callback will be called for each recommended domain and
whenever a domain is added or removed. Your application code is
responsible for assembling these replies into a list.

Your callback will be passed a `DNSServiceDomainEnumerationReply` struct,
which contains a domain name with flags indicating whether the domain
should be added, removed, or made the default. Another flag indicates
whether the list is now complete or more is coming.

The `DNSServiceDomainEnumerationCreate` function
also allocates and returns a `dns_service_discovery_ref` record
to serve as your client ID. You are responsible for deallocating
it.

Enumeration sample code can be found in the file `SamplemDNSClient.c`

You will probably never need to update your registration dynamically,
as Bonjour automatically handles the common cases, such as waking,
sleeping, shutting down, and changing IP addresses.

An exception would be the need to update the text record associated
with a service. If a text field contains a queue name, for example,
and the queue name changes, you would need to update the text record
for the service.

To update your DNS information, call `DNSServiceRegistrationUpdateRecord`,
passing in an updated DNS resource record. This function calls for
a reference returned from `DNSServiceDiscoveryAddRecord`,
but you can pass a zero in this field to update the record returned
by `[DNSServiceRegistrationCreate](../reference/reference_mach.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxuitstknsxe5tjmnsvezlhnfzxi4tboruw63sdojswc5df)`, which
is your primary record.

Registration update sample code can be found in the file `SamplemDNSClient.c`

[Next](reference_mach.md)[Previous](Bonjour%20Overview.md)

