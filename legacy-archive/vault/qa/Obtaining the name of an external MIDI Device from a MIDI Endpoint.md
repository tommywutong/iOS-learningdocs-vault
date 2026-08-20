---
title: Obtaining the name of an external MIDI Device from a MIDI Endpoint
apple_id: DTS10003394
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreMIDI
published: '2014-03-24'
source_url: https://developer.apple.com/library/archive/qa/qa1374/_index.html
archived_at: '2026-07-18T02:30:27.505179Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1374

# Obtaining the name of an external MIDI Device from a MIDI Endpoint

## Q:  How do I get the name of an external MIDI Device from a MIDI Endpoint?

A: CoreMIDI supports external MIDI devices with multiple ports, for example a synthesizer with more than one MIDI input. External MIDI devices can have multiple endpoints and entities. Therefore, instead of querying just the MIDI Object for the device name, the MIDI endpoints, entities and external devices must all be checked to obtain the appropriate device name.

Since the release of OS X 10.4, MIDIServices.h has included the property `kMIDIPropertyDisplayName` which can be used for this purpose. This property provides the Apple-recommended user-visible name for an endpoint, by combining the device and endpoint names for you. For objects other than endpoints, the display name is the same as the name.

__Listing 1__  Getting an endpoint display name.

```
// ____________________________________________________________________________
// Obtain the name of an endpoint without regard for whether it has connections.
// The result should be released by the caller.
static CFStringRef GetEndpointDisplayName(MIDIEndpointRef endpoint)
{
    CFStringRef result = CFSTR(""); // default

    MIDIObjectGetStringProperty(endpoint, kMIDIPropertyDisplayName, &result);

    return result;
}
```


__Listing 2__  Getting an endpoint name following connections.

```
// Obtain the name of an endpoint, following connections.
// The result should be released by the caller.
static CFStringRef CreateConnectedEndpointName(MIDIEndpointRef endpoint)
{
    CFMutableStringRef result = CFStringCreateMutable(NULL, 0);
    CFStringRef str;
    OSStatus err;

    // Does the endpoint have connections?
    CFDataRef connections = NULL;
    int nConnected = 0;
    bool anyStrings = false;
    err = MIDIObjectGetDataProperty(endpoint, kMIDIPropertyConnectionUniqueID, &connections);
    if (connections != NULL) {
        // It has connections, follow them
        // Concatenate the names of all connected devices
        nConnected = CFDataGetLength(connections) / sizeof(MIDIUniqueID);
        if (nConnected) {
            const SInt32 *pid = reinterpret_cast<const SInt32 *>(CFDataGetBytePtr(connections));
            for (int i = 0; i < nConnected; ++i, ++pid) {
               MIDIUniqueID id = EndianS32_BtoN(*pid);
               MIDIObjectRef connObject;
               MIDIObjectType connObjectType;
               err = MIDIObjectFindByUniqueID(id, &connObject, &connObjectType);
               if (err == noErr) {
                if (connObjectType == kMIDIObjectType_ExternalSource  ||
                                                      connObjectType == kMIDIObjectType_ExternalDestination) {
                   // Connected to an external device's endpoint (10.3 and later).
                   str = EndpointName(static_cast<MIDIEndpointRef>(connObject), true);
                } else {
                     // Connected to an external device (10.2) (or something else, catch-all)
                  str = NULL;
                  MIDIObjectGetStringProperty(connObject, kMIDIPropertyName, &str);
                }
                if (str != NULL) {
                    if (anyStrings)
                        CFStringAppend(result, CFSTR(", "));
                    else anyStrings = true;
                    CFStringAppend(result, str);
                    CFRelease(str);
                }
               }
            }
        }
        CFRelease(connections);
    }

    if (anyStrings)
        return result;
    else
        CFRelease(result);

    // Here, either the endpoint had no connections, or we failed to obtain names for any of them.
    return CreateEndpointName(endpoint, false);
}

//////////////////////////////////////
// Obtain the name of an endpoint without regard for whether it has connections.
// The result should be released by the caller.
static CFStringRef CreateEndpointName(MIDIEndpointRef endpoint, bool isExternal)
{
    CFMutableStringRef result = CFStringCreateMutable(NULL, 0);
    CFStringRef str;

    // begin with the endpoint's name
    str = NULL;
    MIDIObjectGetStringProperty(endpoint, kMIDIPropertyName, &str);
    if (str != NULL) {
        CFStringAppend(result, str);
        CFRelease(str);
    }

    MIDIEntityRef entity = NULL;
    MIDIEndpointGetEntity(endpoint, &entity);
    if (entity == NULL)
        // probably virtual
        return result;

    if (CFStringGetLength(result) == 0) {
        // endpoint name has zero length -- try the entity
        str = NULL;
        MIDIObjectGetStringProperty(entity, kMIDIPropertyName, &str);
        if (str != NULL) {
            CFStringAppend(result, str);
            CFRelease(str);
        }
    }

    // now consider the device's name
    MIDIDeviceRef device = NULL;
    MIDIEntityGetDevice(entity, &device);
    if (device == NULL) return result;

    str = NULL;
    MIDIObjectGetStringProperty(device, kMIDIPropertyName, &str);
    if (str != NULL) {
        // if an external device has only one entity, throw away
                // the endpoint name and just use the device name
        if (isExternal && MIDIDeviceGetNumberOfEntities(device) < 2) {
            CFRelease(result);
            return str;
        } else {
            // does the entity name already start with the device name?
                        // (some drivers do this though they shouldn't)
            // if so, do not prepend
            if (CFStringCompareWithOptions(str /* device name */,
                                    result /* endpoint name */,
                                         CFRangeMake(0, CFStringGetLength(str)), 0) != kCFCompareEqualTo) {
                // prepend the device name to the entity name
                if (CFStringGetLength(result) > 0)
                    CFStringInsert(result, 0, CFSTR(" "));
                CFStringInsert(result, 0, str);
            }
            CFRelease(str);
        }
    }

    return result;
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-24 | Editorial |
| 2014-01-21 | Editorial |
| 2013-08-06 | Editorial |
| 2004-12-01 | New document that get the names of external MIDI Devices from MIDI Endpoints. |

