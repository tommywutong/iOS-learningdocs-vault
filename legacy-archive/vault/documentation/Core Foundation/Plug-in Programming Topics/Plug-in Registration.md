---
title: Plug-in Programming Topics
apple_id: 10000128i
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2005-03-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPlugIns/Concepts/registration.html
archived_at: '2026-07-15T07:22:39.367107Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Plug-in Programming Topics](Introduction%20to%20Plug-ins.md)


[Next](Defining%20Types%20and%20Interfaces.md)[Previous](Conceptual%20Building%20Blocks.md)

# Plug-in Registration

For the plug-in host to know what types are available, each plug-in must register with the host. Registration consists of making the host aware of the types a plug-in implements and their associated factory functions. This information can be declared statically using a few special keys in the plug-in’s information property list or it can be registered dynamically by code in the plug-in. See [Implementing a Plug-in](Implementing%20a%20Plug-in.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dilkdjjbekscbifdq) for an example.

When a plug-in is found by a host, plug-ins use the value of the `CFPlugInDynamicRegistration` key in the plug-in’s information property list to determine whether a plug-in requires static or dynamic registration. If a plug-in uses dynamic registration, the plug-in’s code must be loaded immediately so the dynamic registration can take place. If the plug-in uses static registration, its code need not be loaded until the application actually needs to instantiate a type. For this reason, static registration is preferred when there’s no overriding reason for using dynamic registration.

For static registration, the information property list contains the `CFPlugInFactories` key whose value is a dictionary whose keys are factory UUIDs (expressed in the standard string format) and whose values are function names. Each key-value pair in this dictionary registers a factory function when the plug-in’s CFBundle is created. The information property list also contains a `CFPlugInTypes` key. The value of this key is a dictionary whose keys are type UUIDs and whose values are arrays of factory UUIDs. For each type then, there is a list of the factories within the plug-in that can create that type. See [Implementing a Plug-in](Implementing%20a%20Plug-in.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dilkdjjbekscbifdq) for an example plug-in’s information property list.

For dynamic registration, plug-ins load the plug-in’s code and allows it to do its dynamic registration as soon as the associated CFBundle is created. For plug-ins that do dynamic registration, the optional `CFPlugInDynamicRegisterFunction` key can be set to the name of the function that should be called to do the dynamic registration. If this key is not provided, plug-ins attempt to call a function named `CFPlugInDynamicRegister`. When you implement the `CFPlugInDynamicRegister` function (or your custom version) you use dynamic registration functions of plug-ins to create the type/factory associations that would otherwise be declared in the plug-in’s information property list.

A code entity can also register built-in types and factories using the dynamic registration functions. The code with built-in types could then use the plug-in model internally, or allow plug-ins to query the host for the built-in types and interfaces. This might be necessary if plug-ins need to discover some information about the host’s state before being used.

The keys described in this section are defined by plug-ins and are used either to statically register the types supported by the plug-in or to define the plug-in’s dynamic registration behavior.

__`kCFPlugInDynamicRegistration`__: Used to determine the method of registration required by the plug-in. Its value is a string—`YES` for dynamic registration, `NO` for static registration.

__`CFPlugInDynamicRegisterFunction`__: The name of a custom function to be called to perform dynamic registration. If dynamic registration is enabled and this key is not present, the function `CFPlugInDynamicRegister` is called.

__`CFPlugInUnloadFunction`__: The name of a custom function to be called to when a plug-in’s code is to be unloaded.

__`CFPlugInFactories`__: Used for static registration. Its value should be a dictionary whose keys are factory UUIDs (expressed in the standard string format) and whose values are function names.

__`CFPlugInTypes`__: Used for static registration. Its value should be a dictionary whose keys are type UUIDs and whose values are arrays of factory UUIDs.

[Next](Defining%20Types%20and%20Interfaces.md)[Previous](Conceptual%20Building%20Blocks.md)

