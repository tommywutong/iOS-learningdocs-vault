---
title: Internet Connect Speed
apple_id: DTS10002280
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: SystemConfiguration
published: '2011-08-01'
source_url: https://developer.apple.com/library/archive/qa/qa1165/_index.html
archived_at: '2026-07-18T02:30:11.796135Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1165

# Internet Connect Speed

## Q:  On Mac OS X, how do I get the modem connection speed? I want to get the same value that Internet Connect displays.

A: You can get this information from the System Configuration framework dynamic store. When the modem connects, the PPP controller stores the connection speed in the `kSCPropNetModemConnectSpeed` property of the `kSCEntNetModem` entity of the network service state. The code in Listing 1 prints this information for every connected modem service.

__Listing 1__  Getting the modem connection speed

```
static void PrintConnectionSpeed(const void *key,                                   const void *value,                                   void *context)     // A CFDictionaryApplyFunction callback. The key is the SCF      // dynamic store key for a modem network service entity. The      // value is the entity dictionary. This extracts the connection      // speed property from that entity and prints it. {     CFStringRef       dynStoreKey;     CFDictionaryRef   entityDict;     CFNumberRef       connectionSpeed;     #pragma unused(context)      dynStoreKey = (CFStringRef) key;     entityDict  = (CFDictionaryRef) value;      assert( CFGetTypeID(dynStoreKey) == CFStringGetTypeID() );     assert( CFGetTypeID(entityDict) == CFDictionaryGetTypeID() );      connectionSpeed = (CFNumberRef) CFDictionaryGetValue(entityDict,                                         kSCPropNetModemConnectSpeed);     if (connectionSpeed == NULL) {         // A disconnected modem entity has no connection speed          // property. In this example, we simply ignore it.     } else {         CFStringRef str;          assert( CFGetTypeID(connectionSpeed) == CFNumberGetTypeID() );          str = CFStringCreateWithFormat(NULL, NULL,                                         CFSTR("%@ = %@"),                                         dynStoreKey,                                         connectionSpeed);         assert(str != NULL);          CFShow(str);          CFQRelease(str);     } }  int main (int argc, const char * argv[]) {     OSStatus            err;     SCDynamicStoreRef   store;     CFStringRef         pattern;     CFArrayRef          patterns;     CFDictionaryRef     dictOfModemEntities;      dictOfModemEntities = NULL;     pattern  = NULL;     patterns = NULL;      // Connect to the dynamic store.      store = SCDynamicStoreCreate(NULL, CFSTR("ConnectionSpeedTest"),                                                          NULL, NULL);     err = MoreSCError(store);      // Set pattern to "State:/Network/Service/[^/]+/Modem" and      // then put it into a CFArray.      if (err == noErr) {         pattern = SCDynamicStoreKeyCreateNetworkServiceEntity(NULL,                                          kSCDynamicStoreDomainState,                                          kSCCompAnyRegex,                                         kSCEntNetModem);         err = MoreSCError(pattern);     }     if (err == noErr) {         patterns = CFArrayCreate(NULL, (const void **) &pattern, 1,                                              &kCFTypeArrayCallBacks);         err = CFQError(patterns);     }      // Get all of the modem network service entities from the      // dynamic store and print the results.      if (err == noErr) {         dictOfModemEntities = SCDynamicStoreCopyMultiple(store,                                                      NULL, patterns);         err = MoreSCError(dictOfModemEntities);     }     if (err == noErr) {         CFDictionaryApplyFunction(dictOfModemEntities,                                          PrintConnectionSpeed, NULL);     }      // Clean up.      CFQRelease(store);     CFQRelease(pattern);     CFQRelease(patterns);     CFQRelease(dictOfModemEntities);      return (err != noErr); }
```

This code uses three helper functions (`CFQError`, `CFQRelease`, `MoreSCError`) from the DTS "MoreSCF" sample code.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-08-01 | Reformatted content and made minor editorial changes. |
| 2003-03-26 | New document that describes how to get the modem connection speed from the System Configuration framework dynamic store. |

