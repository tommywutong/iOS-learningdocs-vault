---
title: DNSServiceDiscovery Mach-Based API
apple_id: TP30001129
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-04-29'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/dns_discovery_mach/reference/reference_mach.html
archived_at: '2026-07-15T08:18:33.184259Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [DNSServiceDiscovery Mach-Based API](Introduction.md)


[Next](Constants%20and%20Data%20Types.md)[Previous](DNSServiceDiscovery%20Tasks.md)

Functions and Callbacks

This section describes the functions that make up the
DNSServiceDiscovery API and provides prototypes of the callbacks
you need to implement. The callbacks are required to handle the
asynchronous replies that many of these functions generate. The
functions and callbacks are organized into the following sections:

- [Registration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqgywtcnzsgm4dk)
- [Mach Port Accessor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqgywtcnrxhe3dk)
- [Service Browser](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqgywtemryge3te)
- [Service Address Resolver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqgywtcnzqgu2tk)
- [Domain Enumeration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqgywtemrzga2do)
- [Reference Record Deallocation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqgywtemryhayts)
- [Dynamic Update](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqgywtenbsgezto)

### Registration

- These functions allow services to register
  with the mDNS responder. Once a service is registered, it can be
  found—either by name or by browsing for services of this type—using multicast
  DNS requests.

  - `[DNSServiceRegistrationCreate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzksmvtws43uojqxi2lpnzbxezlborsq)`
  - `[MyDNSServiceRegistrationReply_handler](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2npfce4u2tmvzhm2ldmvjgkz3jon2heylunfxw4utfobwhsx3imfxgi3dfoi)`
- 

  Allocates and initializes a `dns_service_discovery_ref` record,
  sets up a Mach reply port for the service, and registers the service
  in the specified domain.

  ```
  dns_service_discovery_ref DNSServiceRegistrationCreate(
  const char *name,
  const char *regtype,
  const char *domain,
  uint16_t port,
  const char *txtRecord,
  DNSServiceRegistrationReply callBack,
  void *context);
  ```

  ```
  Parameters
  name
  The name of this service instance (e.g. "Steve's
  Printer").
  regtype
  The service type, such as "
  _printer._tcp.
  "
  For the service type specifications, see RFC 2782 (DNS SRV).
  domain
  The domain in which to register the service,
  such as
  "local."
  Set
  this parameter to ““ (empty string) to use the default domain(s).
  port
  The local IP port on which this service is
  being offered (in network byte order).
  txtRecord
  Optional protocol-specific additional information.
  This parameter is provided to support legacy protocols that have
  no capability negotiation and require text configuration, such as
  LPR printing. If you are creating a new protocol, please not use
  text records.
  callBack
  The
  DNSServiceRegistrationReply_handler
  callback
  function to be called with any flags or errors. See
  “MyDNSServiceRegistrationReply_handler”
  .
  context
  A user specified context which will be passed
  to the callback function.
  ```

  ##### Return Value

  Allocates, initializes,
  and returns a `dns_service_discovery_ref` record,
  an opaque data structure. Use this record to obtain your Mach port
  address from `DNSServiceDiscoveryManPort`.
  This record is also used to identify your service to other functions
  in this API. You are responsible for deallocating the returned record
  when you are finished with it.

  ```
  Discussion
  Use this function to create register a service. Calling this
  function also sets up a Mach reply port for your service. To obtain
  the Mach port address, pass the returned
  dns_service_discovery_ref
  record
  to
  DNSServiceDiscoveryMachPort
  . Deallocating
  the returned record also closes your connection to the Mach reply
  port. Your service needs a network socket and an IP address, and
  should be ready to respond to service requests, when you call this
  function.
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```
- 

  Your application implements this callback function to
  handle replies from `DNSServiceRegistrationCreate`.
  The reply is a `DNSServiceRegistrationReply`.

  ```
  static void reg_reply(
  DNSServiceRegistrationReplyErrorType errorCode,
  void *context)
  ```

  ```
  Parameters
  errorCode
  Any error codes or flags. See
  DNSServiceDiscoveryFlags
  in
  Constants and Data Types
  .
  context
  A user-specified context that will be passed
  to the callback function.
  ```

  ##### Return Value

  Not applicable.

  ```
  Discussion
  This is a prototype for your callback function, to be passed
  in to
  DNSServiceRegistrationCreate
  .
  Your callback is sent a
  DNSServiceRegistrationReply
  ,
  consisting of either no flags, a message conflict flag, or an error
  code. If your requested DNS name is already in use, choose another
  name and re-register. For example, your default service name may
  be in use by another copy of your service on the same network, such
  as an identical printer. If your service has no user interface for
  naming, it is good practice to append a number to your default name
  and retry, incrementing the number as necessary to obtain a unique name.
  A code sample for a service with a user interface follows.
  static void reg_reply(
  DNSServiceRegistrationReplyErrorType errorCode,
  void *context)
  {
  printf("Got a reply from the server: ");
  switch (errorCode)
  {
  case kDNSServiceDiscoveryNoError:
  printf("Name now registered and active\n"); break;
  case kDNSServiceDiscoveryNameConflict:
  printf("Name in use, please choose another\n"); exit(-1);
  default:
  }
  printf("Error %d\n", errorCode); return;
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```

### Mach Port Accessor

- These functions help the applications programmer
  establish a connection with a Mach reply port.

  - `[DNSServiceDiscoveryMachPort](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzkenfzwg33wmvzhstlbmnufa33soq)`
  - `[DNSServiceDiscovery_handleReply](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzkenfzwg33wmvzhsx3imfxgi3dfkjsxa3dz)`
- 

  Returns a Mach reply port.

  ```
  mach_port_t DNSServiceDiscoveryMachPort(
  dns_service_discovery_ref dnsServiceDiscovery);
  ```

  ```
  Parameters
  registration
  A
  dns_service_discovery_ref
  a
  s returned from
  DNSServiceRegistrationCreate
  .
  ```

  ##### Return Value

  This function returns
  a Mach reply port. A `NULL` value
  indicates that no address was specified or some other error occurred
  which prevented the resolution from being started.

  ```
  Discussion
  This function returns a Mach reply port which will be sent
  messages as appropriate. These messages should be handled by the
  DNSServiceDiscovery_handleReply
  function,
  which needs to be integrated into your run loop. See
  DNSServiceDiscovery_handleReply
  .
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```
- 

  Handles messages from your Mach port.

  ```
  void DNSServiceDiscovery_handleReply(void *replyMsg);
  ```

  ```
  Parameters
  *replyMsg
  The Mach message.
  ```

  ```
  Discussion
  Install this function as a callback to handle messages from
  your Mach port if you are providing a network service and using
  the mDNS responder.
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```

### Service Browser

- These functions allow applications to discover
  network services by browsing:

  - `[DNSServiceBrowserCreate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzkcojxxo43fojbxezlborsq)`
  - `[MyDNSServiceBrowserReply_handler](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2npfce4u2tmvzhm2ldmvbhe33xonsxeutfobwhsx3imfxgi3dfoi)`
- 

  Returns a list of all network services of a specified
  type in a specified domain.

  ```
  dns_service_discovery_ref DNSServiceBrowserCreate(
  const char *regtype,
  const char *domain,
  DNSServiceBrowserReply callBack,
  void *context);
  ```

  ```
  Parameters
  regtype
  The type of service, as specified by the IANA;
  _printer._tcp
  is
  an example.
  domain
  The domain to search for the specified type
  of service;
  local
  . is
  an example. Pass an empty string ““ to search the default domain.
  callBack
  The
  DNSServiceBrowserReply_handler
  function
  to be called when a service has been found or removed. See
  MyDNSServiceBrowserReply_handler
  .
  context
  A user-specified context that will be passed
  to the callback function.
  ```

  ##### Return Value

  This function allocates
  and returns a `dns_service_discovery_ref` record. The
  caller is responsible for deallocating the record.

  ```
  Discussion
  Use this function to browse for a list of available services
  of a given type in a given domain. The requested service data is
  sent asynchronously to your callback function as a
  DNSServiceBrowserReply
  .
  Your callback may receive a number of calls asynchronously. Do not
  update your user interface (list of available services) while the DNSServiceBrowserReply
  has the “More” flag set, but do not disable the user interface
  or change the cursor while waiting for data. Your callback should
  remain active as long as your service browser is running. To use
  a service found by this function, obtain the actual address information
  for that service by calling
  DNSServiceResolverResolve
  .
  To search for multiple service types, or to search multiple domains,
  make multiple calls to
  DNSServiceBrowserCreate
  .
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```
- 

  Your application implements this callback function to
  handle replies from `DNSServiceBrowserCreate`.
  The reply is a `DNSServiceBrowserReply`.

  ```
  static void MyDNSServiceBrowserReply_handler(
  DNSServiceBrowserReplyResultType resultType,
  const char *replyName,
  const char *replyType,
  const char *replyDomain
  DNSServiceDiscoveryReplyFlags flags,
  void *context)
  ```

  ```
  Parameters
  resultType
  The
  DNSServiceBrowserReplyResultType
  .
  Possible values are
  DNSServiceBrowserReplyAddInstance
  and
  DNSServiceBrowserReplyRemoveInstance
  .
  replyName
  The name of the service instance;
  Sales
  Printer
  is an example.
  replyType
  The type of service;
  _printer._tcp
  is
  an example.
  replyDomain
  The domain of the service;
  local
  .
  is an example.
  flags
  Any error codes or flags. See
  DNSServiceDiscoveryFlags
  in
  Constants and Data Types
  .
  If there are multiple known services, the
  kDNSServiceDiscoveryMoreRepliesImmediately
  flag
  will be set until you have received replies for all of them. Do
  not update the user interface (list of services) while this flag
  is set, but do not disable the user interface or change the cursor
  while waiting for this flag to clear.
  context
  A user-specified context that will be passed
  to the callback function.
  ```

  ##### Return Value

  Not applicable.

  ```
  Discussion
  This is a prototype for your callback function, to be passed
  in to
  DNSServiceBrowserCreate
  . Your
  callback function will be called once for every service instance
  of the specified type found in the domain. It will be called again
  if new instances are added to the domain or known instances are
  removed. The sum of these replies is the current list of service instances.
  Note that you receive individual records; your application is responsible
  for building and maintaining a list.
  This callback should remain active as long as your service
  browser is running. That way the list of available services will
  always be up to date.
  Your callback is sent a
  DNSServiceBrowserReply
  record,
  a structure containing the reply type (add or delete a service instance
  from your list), instance name, service type, and domain, any flags
  or errors, and a context that will be returned to the callback function.
  A simple code sample follows.
  static void browse_reply(DNSServiceBrowserReplyResultType resultType,
  const char *replyName,
  const char *replyType,
  const char *replyDomain
  DNSServiceDiscoveryReplyFlags flags,
  void *context)
  {
  char *op =
  (resultType == DNSServiceBrowserReplyAddInstance) ? Found" : "Removed";
  printf("Service \"%s\", type \"%s\", domain \"%s\" %s", replyName, replyType,  replyDomain, op);
  if (flags) printf(" Flags: %X", flags);
  printf("\n");
  }
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```

### Service Address Resolver

- These functions resolve the current IP address
  and port of a given service instance.

  - `[DNSServiceResolverResolve](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzksmvzw63dwmvzfezltn5whmzi)`
  - `[MyDNSServiceResolverReply_handler](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2npfce4u2tmvzhm2ldmvjgk43pnr3gk4ssmvygy6k7nbqw4zdmmvza)`
- 

  Finds the current IP address and port for a service instance,
  as returned to your `DNSServiceBrowserReply_handler` callback
  function after a call to `DNSServiceBrowserCreate`.

  ```
  dns_service_discovery_ref DNSServiceResolverResolve(
  const char *name,
  const char *regtype,
  const char *domain,
  DNSServiceResolverReply callBack,
  void *context);
  ```

  ```
  Parameters
  name
  The name of the service instance, as returned
  from
  DNSServiceBrowserCreate
  .
  regtype
  The type of service, as returned from
  DNSServiceBrowserCreate
  .
  domain
  The domain in which to find the service, as
  returned from
  DNSServiceBrowserCreate
  .
  callBack
  The
  DNSServiceResolverReply_handler
  function
  to be called when the specified address has been resolved. See
  MyDNSServiceResolverReply_handler
  .
  context
  A user specified context which will be passed
  to the callback function.
  ```

  ##### Return Value

  This function returns
  a `dns_service_discovery_ref` record,
  an opaque data type. The requested service address data is sent
  to your callback function asynchronously as a `[DNSServiceResolverReply](reference_mach2.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxuitstknsxe5tjmnsvezltn5whmzlskjsxa3dz)`.

  ```
  Discussion
  Use this function to resolve the current IP address of a service
  after you have obtained its name, service type, and domain from
  DNSServiceBrowserCreate
  .
  The IP address can change dynamically, and services can be removed
  or unplugged at any time, so call this function immediately before
  using any network service, and call it each time you use the service.
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```
- 

  Your application implements this callback function to
  handle replies from `DNSServiceResolverResolve`.

  ```
  static void MyDNSServiceResolverReply_handler(struct
  sockaddr *interface,
  struct sockaddr *address,
  const char *txtRecord,
  DNSServiceDiscoveryReplyFlags flags,
  void *context)
  ```

  ```
  Parameters
  interface
  A
  sockaddr
  containing
  the IP address of the host’s network interface. If the host is
  connected to more than one local network, such as an ethernet LAN and
  a wireless LAN, this identifies which network contains the service.
  address
  A
  sockaddr
  containing
  the link-local IP address and port number of the service.
  txtrecord
  A character string containing any additional
  information, such as a print queue name. If there is no additional
  information, this is an empty string.
  flags
  Any error codes or flags. See
  DNSServiceDiscoveryFlags
  in
  Constants and Data Types
  .
  context
  A user-specified context that will be passed
  to the callback function.
  ```

  ##### Return Value

  Not applicable.

  ```
  Discussion
  This is a prototype for your callback function, to be passed
  in to
  DNSServiceResolverResolve
  . Your
  function will be called when the service address has been resolved.
  Your callback will receive a
  DNSServiceResolverReply
  record.
  This struct contains the host interface IP address, the service
  IP address and port, an optional text record with any additional
  demultiplexing information, any flags or errors, and a context that
  will be returned to the callback function.
  A code sample follows.
  static void resolve_reply(struct sockaddr *interface,
  struct sockaddr *address,
  const char *txtRecord,
  DNSServiceDiscoveryReplyFlags flags,
  void *context)
  {
  if (address->sa_family (!= AF_INET)
  printf("Unknown address family %d\n", address->sa_family);
  else
  {
  struct sockaddr_in *ip = (struct sockaddr_in *)address;
  union { uint32_t l; u_char b[4]; } addr = { ip->sin_addr.s_addr };
  union { uint16_t s; u_char b[2]; } port = { ip->sin_port };
  uint16_t PortAsNumber = ((uint16_t)port.b[0]) << 8 | port.b[1];
  const char *src = txtRecord;
  printf("Service can be reached at %d.%d.%d.%d:%u", addr.b[0],
  addr.b[1], addr.b[2], addr.b[3], PortAsNumber);
  while (*src)
  {
  char txtInfo[256];
  char *dst = txtInfo;
  const char *const lim = &txtInfo[sizeof(txtInfo)];
  while (*src && *src != 1 && dst < lim-1) *dst++ = *src++;
  *dst++ = 0;
  printf(" TXT \"%s\"", txtInfo);
  if (*src == 1) src++;
  }
  if (flags) printf(" Flags: %X", flags);
  printf("\n");
  }
  }
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```

### Domain Enumeration

- These functions list the recommended and default
  domains for registration or browsing:

  - `[DNSServiceDomainEnumerationCreate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzken5wwc2loivxhk3lfojqxi2lpnzbxezlborsq)`
  - `[MyDNSServiceDomainEnumerationReply_handler](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2npfce4u2tmvzhm2ldmvcg63lbnfxek3tvnvsxeylunfxw4utfobwhsx3imfxgi3dfoi)`
- 

  Lists the recommended domains in which to register a service
  or browse for services.

  ```
  dns_service_discovery_ref DNSServiceDomainEnumerationCreate(
  int registrationDomains,
  DNSServiceDomainEnumerationReply callBack,
  void *context);
  ```

  ```
  Parameters
  registrationDomains
  A Boolean indicating whether you are looking
  for recommended registration domains (equivalent to the AppleTalk
  zone list in the AppleTalk Control Panel) or recommended browsing
  domains (equivalent to the AppleTalk zone list in the Chooser).
  callBack
  The
  DNSServiceDomainEnumerationReply_handler
  function
  to be called when domains are found or removed See
  “MyDNSServiceDomainEnumerationReply_handler”
  .
  context
  A user-specified context that will be passed
  to the callback function.
  ```

  ##### Return Value

  This function allocates
  and returns a `dns_service_discovery_ref` record. The
  caller is responsible for deallocating the record. This record does
  not contain the requested domain data—that information is sent
  to your callback function asynchronously.

  ```
  Discussion
  You can use this function obtain a list of recommended domains
  in which to register your service or a list of recommended domains
  in which to browse for services. This is not necessary if you want
  to simply register in or search the default domain. You can pass
  an empty string ““ as the domain parameter for the registration
  and browser functions, and they will use the default domain without
  requiring you to look it up. Use this function if you need to do
  something more complex.
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```
- 

  Your application implements this callback function to
  handle replies from `DNSServiceDomainEnumerationCreate`.
  The reply is a `DNSServiceDomainEnumerationReply`.

  ```
  static void regdom_reply(
  DNSServiceDomainEnumerationReplyResultType resultType,
  const char *replyDomain,
  DNSServiceDiscoveryReplyFlags flags,
  void *context)
  ```

  ```
  Parameters
  resultType
  The
  DNSServiceDomainEnumerationReplyResultType
  .
  Possible values are
  DNSServiceDomainEnumerationReplyAddDomain
  ,
  DNSServiceDomainEnumerationReplyAddDomainDefault
  ,
  or
  DNSServiceDomainEnumerationReplyRemoveDomain
  .
  replyDomain
  A domain in which to register or browse;
  local
  .
  is an example.
  flags
  Any error codes or flags. See
  DNSServiceDiscoveryFlags
  in
  Constants and Data Types
  .
  If there are multiple recommended domains, the
  kDNSServiceDiscoveryMoreRepliesImmediately
  flag
  will be set until you have received replies for all of them.
  context
  A user-specified context that will be passed
  to the callback function.
  ```

  ##### Return Value

  Not applicable.

  ```
  Discussion
  This is a prototype for your callback function, to be passed
  in to
  DNSServiceDomainEnumerationCreate
  .
  Your callback function will be called once for every recommended
  domain. It will be called again if domains are added or removed,
  or if the default changes. The sum of these replies is the current
  list of recommended domains.
  Your callback is sent a
  DNSServiceDomainEnumerationReply
  record,
  a struct containing the reply type (add or delete a domain from
  your list), a domain name, any flags or errors, and a context that
  will be returned to the callback function. A code sample follows.
  #define DomainMsg(X) (
  (X) == DNSServiceDomainEnumerationReplyAddDomain
  ? "Added"               :        \
  (X) == DNSServiceDomainEnumerationReplyAddDomainDefault
  ? "(Default)"               :        \
  (X) == DNSServiceDomainEnumerationReplyRemoveDomain
  ? "Removed"             : "Unknown")
  static void regdom_reply(
  DNSServiceDomainEnumerationReplyResultType resultType,
  const char *replyDomain,
  DNSServiceDiscoveryReplyFlags flags,
  void *context)
  {
  printf("Recommended Registration or Browse Domain %s %s", replyDomain,  DomainMsg(resultType));
  if (flags) printf(" Flags: %X", flags);
  printf("\n");
  }
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```

### Reference Record Deallocation

- This function described in this section deallocates
  a `dns_service_discovery_ref` record
  and disconnects any associated Mach port.

  - `[DNSServiceDiscoveryDeallocate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzkenfzwg33wmvzhsrdfmfwgy33dmf2gk)`
- 

  Deallocates a `dns_service_discovery_ref` record
  and closes the connection to the server.

  ```
  void DNSServiceDiscoveryDeallocate(
  dns_service_discovery_ref dnsServiceDiscovery);
  ```

  ```
  Parameters
  dnsServiceDiscovery_ref
  A
  dns_service_discovery_ref
  record
  as returned from calling
  DNSServiceRegistrationCreate
  ,
  DNSServiceBrowserCreate
  ,
  or
  DNSServiceDomainEnumerationCreate
  .
  ```

  ##### Return Value

  None.

  ```
  Discussion
  You are responsible for deallocating
  dns_service_discovery_ref
  records
  returned by creation or enumeration calls. For registration or browsing,
  you typically make a single creation call, and the returned record
  remains active until your application terminates. In these cases,
  it is not necessary to deallocate the record. The enumeration function
  can also be called once, and the callback left active, or it can
  be called as needed. In the latter case, you should deallocate the
  record before calling the enumeration function again to prevent a
  memory leak.
  A Mach reply port is set up for your application when you
  call
  DNSServiceRegistrationCreate
  .
  Deallocating the returned
  dns_service_discovery_ref
  disconnects
  your application from the Mach port and unregisters your service.
  You can use this technique if you need to unregister and re-register
  your service without shutting down your application.
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```

### Dynamic Update

- These functions provide the ability to add
  to, update, or delete registration information stored in the mDNS
  responder dynamically, after you have registered and while your service
  is running. An example would be updating the text record associated
  with a printer to indicate a change in printing capabilities. Bonjour
  automatically handles most update tasks, such as sleep/wake and
  location changes, so these functions are rarely needed.

  - `[DNSServiceRegistrationAddRecord](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzksmvtws43uojqxi2lpnzawizcsmvrw64te)`
  - `[DNSServiceRegistrationRemoveRecord](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzksmvtws43uojqxi2lpnzjgk3lpozsvezldn5zgi)`
  - `[DNSServiceRegistrationUpdateRecord](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzksmvtws43uojqxi2lpnzkxazdborsvezldn5zgi)`
- 

  Request that the mDNS Responder append an additional record
  to the DNS resource information associated with your service.

  ```
  DNSRecordReference DNSServiceRegistrationAddRecord(
  dns_service_discovery_ref dnsServiceDiscovery,
  uint16_t rrtype,
  uint16_t rdlen,
  const char *rdata,
  uint32_t ttl);
  ```

  ```
  Parameters
  dnsServiceDiscovery
  The
  dns_service_discovery_ref
  for
  your service, as returned from a
  DNSServiceRegistrationCreate
  call.
  rrtype
  A standard DNS Resource Record Type, as defined
  at
  http://www.iana.org/assignments/dns-parameters
  .
  rdlen
  Length of the data block to follow (
  rdata
  ).
  rdata
  Opaque binary Resource Record data—up to
  64 kB of whatever you need to store.
  ttl
  Time-to-live for the added record. The TTL
  can be set to any signed 32-bit value.
  ```

  ##### Return Value

  A `DNSRecordReference`,
  an opaque reference that can be passed to `[DNSServiceRegistrationUpdateRecord](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxuitstknsxe5tjmnsvezlhnfzxi4tboruw63svobsgc5dfkjswg33smq)` or `[DNSServiceRegistrationRemoveRecord](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxuitstknsxe5tjmnsvezlhnfzxi4tboruw63ssmvww65tfkjswg33smq)` to
  update or remove this record. If an error occurs, this value will
  be zero or negative.

  ```
  Discussion
  This function appends a resource record to your existing DNS
  service registry. This should not be necessary for existing services.
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```
- 

  Request that the mDNS responder remove a record from your
  service’s registration information.

  ```
  DNSServiceRegistrationReplyErrorType DNSServiceRegistrationRemoveRecord(
  dns_service_discovery_ref ref,
  DNSRecordReference reference);
  ```

  ```
  Parameters
  ref
  A
  dns_service_discovery_ref
  as
  returned from a
  DNSServiceRegistrationCreate
  call
  reference
  A
  dnsRecordReference
  as
  returned from calling
  DNSServiceRegistrationAddRecord
  .
  To remove your primary record, as returned from DNSServiceRegistrationCreate,
  pass a zero in this parameter.
  ```

  ##### Return Value

  A `DNSServiceRegistrationReplyErrorType.` If
  an error occurs, this value will be nonzero.

  ```
  Discussion
  Call this function to remove a record from your service’s
  DNS registration information. You do not need to do this in the
  ordinary course of events. If you remove your primary record, you
  effectively unregister your service, but this is a side effect,
  not a design feature—it does not deallocate your registration
  record or disconnect your Mach port, for example.
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```
- 

  Request the mDNS responder to update a DNS record for
  your service. Most services will never need to do this.

  ```
  DNSServiceRegistrationReplyErrorType DNSServiceRegistrationUpdateRecord(
  dns_service_discovery_ref ref,
  DNSRecordReference reference,
  uint16_t rdlen,
  const char *rdata,
  uint32_t ttl);
  ```

  ```
  Parameters
  ref
  A
  dns_service_discovery_ref
  as
  returned by
  DNSServiceRegistrationCreate
  .
  reference
  A
  dnsRecordReference
  as
  returned by
  DNSServiceRegistrationAddRecord
  .
  To update information in your primary record, as returned from,
  set this parameter to zero. You might do this, for example, if you
  need to update the text field for a legacy protocol while a service
  is running.
  rdlen
  Length of the data block to follow (
  rdata
  ).
  rdata
  Opaque binary resource record data, containing
  up to 64 kB of whatever data you choose.
  ttl
  Time to live for the updated record. The TTL
  can be set to any signed 32-bit value.
  ```

  ##### Return Value

  A value of type `DNSServiceRegistrationReplyErrorType`.
  If an error occurs, this value will be non-zero.

  ```
  Discussion
  You might use this function to update a text record associated
  with your service, if you are supporting a legacy protocol and the
  information stored in the text record changes. Otherwise, you are
  unlikely to have use for this function.
  Sample code:
  SamplemDNSClient.c
  ```

  ```
  Version Notes
  Introduced in OS X version 10.2.
  ```

[Next](Constants%20and%20Data%20Types.md)[Previous](DNSServiceDiscovery%20Tasks.md)

