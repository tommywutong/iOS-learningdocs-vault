---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/Connect2.html
archived_at: '2026-07-15T08:02:56.315338Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Connecting%20to%20a%20Database.md) [!Previous Section](When%20Database%20Connections%20Are%20Opened%20and%20Closed.md)

# Logging into a Database

An EOAdaptor defines how an application logs into a database through a dictionary of connection information. The keys of this dictionary identify the login information the server expects; the values associated with those keys are the values that the adaptor tries when logging in. The number of connection dictionary keys and the keys themselves vary from adaptor to adaptor. For example, the dictionary keys required by the Sybase adaptor are __databaseName__, __userName__, __password__, and __hostName__. For more information on connection dictionary keys, see the class specification for the adaptor you're using.
An EOAdaptor object must have a valid connection dictionary before its application can connect to a database. There are three ways you can provide one:

- Store the connection information in a model file.
- Run the adaptor's login panel so that the user can enter login information.
- Set the connection dictionary programmatically.

The approach you choose to provide connection information hinges on the following questions:

- Do all users log in with the same connection information?
- Is any connection information sensitive?
- Does the application have an NSApplication object?
- Are users database savvy?
- Do I have time to write a custom login mechanism?

The following sections describe how to choose between and implement each of these approaches.

## Storing the Connection Information in a Model File

This approach is useful when all users log in with the same connection information. It doesn't require any code, and users aren't exposed to the login process. However, you shouldn't use this approach to store connection information that is sensitive. Models are stored in an ASCII file format, and connection information is stored unencrypted. However, you can store some connection information in a model file, and use another approach to get the rest (such as requiring the user to enter a database password.)
To implement this approach just use EOModeler to add connection information to a model (see the book _Enterprise Objects Framework Tools and Techniques_).
All EOAdaptor objects that are created behind the scenes (that is, all adaptors that Enterprise Objects Framework creates automatically) are created with __adaptorWithModel__ (__adaptorWithModel:__ in Objective-C). This method initializes a new adaptor's connection dictionary with the connection information in the specified model. If the model's connection information is valid, no further action is required. Only adaptors that you create programmatically with __adaptorWithName__ (__adaptorWithName:__ in Objective-C) don't take advantage of a model's connection information.

### Storing Partial Information in a Model File

When you store connection information in a model file, you don't have to store a complete connection dictionary. For example, you could store everything but the user name and password. An EOAdaptor is still initialized with the model's connection information. You can supply the missing information at run-time, either programmatically or by running the adaptor's login panel.

## Running the Adaptor's Login Panel

Adaptors provide login panels for use by Enterprise Objects Framework applications. Running the login panel is a simple, no-code approach that you can use in Application Kit applications. It's useful when users have different connection information-different user names and passwords, for example. It can't, however, be used in applications that don't use the Application Kit-in other words, not in command-line or web applications.
One disadvantage of the adaptors' login panels is that they aren't configurable. Each adaptor exposes specific connection keys in the login panel. For example, the Oracle login panel has fields for server ID, user name, and password. If the panel contains fields (such as server ID) that you don't want users to see, you should use another approach. Similarly, a login panel may not provide an interface for all of an adaptor's connection keys. For example, the Oracle adaptor defines keys for language and database encoding that don't exist in the Oracle login panel.
Enterprise Objects Framework automatically runs the login panel when an EOAdaptor object doesn't have a valid connection dictionary. For example, suppose you have an EODisplayGroup that's configured to _fetch on load_. Before a user performs a single action, the application:

- Creates a network of objects under the display group
- Connects to the database
- Performs a database operation to retrieve enterprise objects

If your model doesn't have valid connection information, the application runs a login panel until the user enters valid connection information or cancels the panel. Specifically, when an EODatabaseContext is about to use an EODatabaseChannel to interact with a database:

- The EODatabaseContext checks to see if the EODatabaseChannel's underlying EOAdaptorChannel is open.
- If the EOAdaptorChannel isn't open, the EODatabaseContext attempts to open the adaptor channel by sending it an __openChannel__ message.
- If __openChannel__ fails, the EODatabaseContext runs the adaptor's login panel by sending the EOAdaptorChannel's adaptor a __runLoginPanelAndValidateConnectionDictionary__ message.

Canceling the panel has the effect of canceling whatever operation is in progress. In the example above, canceling the panel cancels the fetch, and the user interface opens without any data to display.

### Suppressing the Login Panel

You can suppress the database adaptor's login panel by implementing the EODatabaseContext delegate method __databaseContextWillRunLoginPanelToOpenDatabaseChannel__ (__databaseContext:willRunLoginPanelToOpenDatabaseChannel:__ in Objective-C). For more information, see the EODatabaseContext class specification in the _Enterprise Objects Framework Reference_.
Alternatively, you can prevent an application from even attempting to run a login panel by ensuring that its EOAdaptor objects have valid connection dictionaries. Before an application's first attempt to connect to a database, send an __assertConnectionDictionaryIsValid__ message to an EOAdaptor. If the adaptor doesn't have sufficient information to log in (for example, it's common to leave the user name and password unspecified in the model file), __assertConnectionDictionaryIsValid__ throws an exception. In your exception handler, set the adaptor's connection dictionary programmatically.

## Setting the Connection Dictionary Programmatically

If you don't store connection information in your model and your application doesn't have an Application Kit user interface, you have to set an adaptor's connection dictionary programmatically. It requires code, but this approach is also useful if you want to implement a login panel that's tailored to your application. For example, you can implement a login component for a WebObjects application, a custom login panel for an Application Kit Framework application, or a mechanism for tools and background processes that gets connection information from command line arguments.
How you get the connection information is up to you. Once you get it, setting the connection dictionary is simple:

- Insert the connection information into an NSDictionary object using adaptor-defined keys.
- Assign the dictionary to the adaptor using the EOAdaptor method __setConnectionDictionary__ (__setConnectionDictionary:__ in Objective-C).
- Verify that the connection dictionary is valid using the EOAdaptor method __assertConnectionDictionaryIsValid__.

For more information, see the EOAdaptor class specification in the _Enterprise Objects Framework Reference_.

### Getting Partial Information from a Model File

If you store some connection information in a model file, an EOAdaptor is object is initialized with an incomplete connection dictionary.
To supply the missing information:

- Get the adaptor's incomplete connection dictionary using the EOAdaptor method __connectionDictionary__.
- Create a mutable copy.
- Insert the missing key-value entries.
- Assign the new, complete connection dictionary to the EOAdaptor with __setConnectionDictionary__ (__setConnectionDictionary:__ in Objective-C).

[!Table of Contents](Connecting%20to%20a%20Database.md) [!Next Section](Limiting%20the%20Number%20of%20Database%20Connections.md)
