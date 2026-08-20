---
title: Distributed Objects Programming Topics
apple_id: 10000102i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2017-06-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html
archived_at: '2026-07-15T07:15:00.773934Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Distributed%20Objects.md)

For interprocess communication, you should use XPC instead; see _[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_ for more information.

# Introduction to Distributed Objects

The Objective-C runtime supports an interprocess messaging solution called “distributed objects.” This mechanism enables a Cocoa application to call an object in a different Cocoa application (or a different thread in the same application). The applications can even be running on different computers on a network.

This programming topic describes the Cocoa classes that form the distributed objects system.

Cocoa’s distributed objects system is available only to Objective-C applications.

The Objective-C language support for distributed objects is described in detail in the “Remote Messaging” section of The Runtime System in _[The Objective-C Programming Language](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_. You should be familiar with it before reading this topic. This topic extends that discussion by describing the Cocoa classes used to implement distributed objects.

The classes are divided into the following categories:

- [Distributed Objects Architecture](Distributed%20Objects%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dalkdjjbeksscjbea)
- [Connections and Proxies](Connections%20and%20Proxies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dclkcijbugsskjjbq)
- [Ports and Name Servers](Ports%20and%20Name%20Servers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43delkciffemskdjfcq)
- [Message Encapsulation](Message%20Encapsulation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dglkdjjbemrkdivfa)

More detailed discussion and examples of how to use distributed objects are covered in the following tasks:

- [Vending an Object](Vending%20an%20Object.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dilkdjjbekscbifdq)
- [Getting a Vended Object](Getting%20a%20Vended%20Object.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dklkciffeoqsbijdq)
- [Configuring a Connection](Configuring%20a%20Connection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dmlkcineuoqkcjbda)
- [Handling Connection Errors](Handling%20Connection%20Errors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dolkcineuqrskivea)
- [Authenticating Connections](Authenticating%20Connections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dqlkdjjbeqscfirdq)
- [Making Substitutions During Message Encoding](Making%20Substitutions%20During%20Message%20Encoding.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dslkcijbuussei5eq)
- [Using NSInvocation](Using%20NSInvocation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42dilkdjjbeeqkdjjea)

[Next](About%20Distributed%20Objects.md)

