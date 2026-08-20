---
title: Apple Media Service Reference
apple_id: TP40014716
resource_type: Guide
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreBluetooth
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/CoreBluetooth/Reference/AppleMediaService_Reference/Specification/Specification.html
archived_at: '2026-07-15T07:22:04.137721Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Media Service Reference](Introduction.md)


[Next](Reference.md)[Previous](Introduction.md)

# The Apple Media Service

The Apple Media Service is a primary Bluetooth 4.0 service whose service UUID is `89D3502B-0F36-433A-8EF4-C502AD55F8DC`.

Only one instance of the AMS may be present on an MS. Due to the nature of iOS, the AMS is not guaranteed to always be present. As a result, the MR should look for and subscribe to the Service Changed characteristic of the GATT service in order to monitor the potential publishing and unpublishing of the AMS at any time.

The MS exposes information about its state by the way of pre-defined __entities,__ each of which exposes its state by the way of pre-defined __attributes.__ The AMS defines 3 distinct entities, each with a different set of attributes:

- __Player:__ The currently active media app. Attributes for this entity include values such as its name, playback state, and playback volume.
- __Queue:__ The currently loaded playback queue. Attributes for this entity include values such as its size and its shuffle and repeat modes.
- __Track:__ The currently loaded track. Attributes for this entity include values such as its artist, title, and duration.

The complete list of attributes for each of these entities is available in Appendix A, [Reference](Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2domjwfvbuqmznknltc).

The MR may want to know only the value of a specific subset of entity/attribute pairs.
For each entity, the MR must indicate once to the MS which entity/attribute pairs, if any, it wants to monitor. The MS will then notify the MR of the initial, current values of all registered entity/attribute pairs, and subsequently notify the MR whenever these values change.

__Figure 2-1__  Typical operation of the Media Service

!

In its basic form, the AMS exposes three characteristics:

- __Remote Command:__ `UUID 9B3C81D8-57B1-4A8A-B8DF-0E56F7CA51C2` (writeable, notifiable)
- __Entity Update:__ `UUID 2F7CABCE-808D-411F-9A0C-BB92BA96C102` (writeable with response, notifiable)
- __Entity Attribute:__ `UUID C6B2F38C-23AB-46D8-A6AB-A3A870BBD5D7` (readable, writeable)

Any subset of these characteristics can be supported.

The Remote Command characteristic is the characteristic by which an MR can send remote commands to affect the playback state of an MS, such as Play, Next Track, Increase Volume, etc. This characteristic is also used to report to the MR the list of commands supported by the MS.
The complete list of possible commands is available in the Appendix.

The format of a Remote Command request written by the MR is shown below:

| Byte | Value |
| --- | --- |
| 1 | `RemoteCommandID` |

A Remote Command request contains the following information:

- __RemoteCommandID:__ The media command to be executed.

A successful write implies that the command has been successfully forwarded to the active media player. It does not guarantee that the player actually acted on it.

When the list of commands supported by the media player changes, the MS generates a notification on the Remote Command characteristic containing a list of the currently supported commands, using the fomat shown below:

| Byte | Value |
| --- | --- |
| 1 | `RemoteCommandID` 1 |
| 2 | `RemoteCommandID` 2 |
| ... | other `RemoteCommandID`s |

Each of the RemoteCommandID values in the notification is one of the media commands listed in the Appendix.

The Entity Update characteristic is the characteristic by which an MR can inform the MS which entity/attribute pairs it is interested in, and be informed about changes on these whenever they occur. For example, the MR can be informed about the title of the currently loaded track, or the name of the active media app.

By default, the MR does not receive any information about any attribute of any entity.
In order to receive this data, an MR first needs to subscribe for GATT notifications on the Entity Update characteristic. Then, the MR writes commands to the Entity Update characteristic to inform the MS which entity/attribute pair values it wants to know.

The format of an Entity Update command sent by the MR is shown below:

| Byte | Value |
| --- | --- |
| 1 | `EntityID` |
| 2 | `AttributeID` 1 |
| 3 | `AttributeID` 2 |
| ... | other `AttributeID`s |

An Entity Update command contains the following information:

- __EntityID:__ The entity the subsequent attributes correspond to.
- __AttributeIDs:__ A list of attributes the MR wants to know.

If the write is successful, the MR will immediately start getting the values of entity/attribute pairs it registered to monitor, in the form of GATT notifications for the same characteristic.

The format of GATT notifications delivered by the MS is shown below:

| Byte | Value |
| --- | --- |
| 1 | `EntityID` |
| 2 | `AttributeID` |
| 3 | `EntityUpdateFlags` |
| 4... | `Value` |

A GATT notification delivered through the Entity Update characteristic contains the following information:

- __EntityID:__ The entity to which the subsequent attribute corresponds.
- __AttributeID:__ The attribute whose value is being sent in the notification.
- __EntityUpdateFlags:__ A bitmask whose set bits give the MR specific information about the notification. For example, an MR could be informed that the data had to be truncated in order to fit into the GATT notification.
- __Value:__ A string which corresponds to the value associated with the given attribute.

The Entity Attribute characteristic is the characteristic by which an MR can retrieve the extended value of an attribute.

This characteristic should ideally only be used if the value of an entity/attribute pair was marked as truncated in the corresponding Entity Update notification, and the MR wants to display more of the associated value.

To retrieve the full value of a specific entity/attribute pair, the MR must first send a command by writing to the Entity Attribute characteristic.

The format of an Entity Attribute command is shown below:

| Byte | Value |
| --- | --- |
| 1 | `EntityID` |
| 2 | `AttributeID` |

An Entity Attribute command contains the following information:

- __EntityID:__ The entity the subsequent attribute corresponds to.
- __AttributeID:__ The attribute whose value is to be loaded as the characteristic’s value.

If the write is successful, the value of the corresponding entity/attribute pair is loaded as the Entity Attribute characteristic’s value, and can simply be read by the MR at its convenience.

When writing to any characteristic, or when reading the Entity Attribute, an MR may receive the following AMS-specific error codes:

- __Invalid State (0xA0):__ The MR has not properly set up the AMS, e.g. it wrote to the Entity Update or Entity Attribute characteristic without subscribing to GATT notifications for the Entity Update characteristic.
- __Invalid Command (0xA1):__ The command was improperly formatted.
- __Absent Attribute (0xA2):__ The corresponding attribute is empty.

The following examples illustrate typical interactions between an MS and an MR.

__Figure 2-2__  Example: service setup

!

__Figure 2-3__  Example: remote command

!

__Figure 2-4__  Example: retrieving the full value of a truncated value

!

[Next](Reference.md)[Previous](Introduction.md)

