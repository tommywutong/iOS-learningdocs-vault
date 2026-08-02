---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.31.html
archived_at: '2026-07-15T08:09:59.453604Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Accessing%20Adaptor%20Sublayer%20Objects.md) [!](Executing%20Arbitrary%20SQL%20Statements.md)

#   Creating Adaptor Sublayer Objects and Connecting Them to the Server

##  Synopsis

Discusses how to create adaptor sublayer objects without using higher level objects. Presents a robust way to connect to the database server.

##  Discussion

Not all applications require higher level objects to drive the adaptor sublayer. For example, you might bypass the database sublayer and control layer entirely if you're writing an application, such as a report writer, that is concerned only with raw data and not with the methods that an enterprise object couples to that data. At the adaptor sublayer, each database row is returned as a dictionary. An application that bypasses higher level database sublayer and control layer objects must create its own adaptor sublayer objects.

You normally create an adaptor with the method
adaptorWithModel
, specifying an existing EOModel object (see the EOModel class specification for information on loading a model file). The model contains the name of the adaptor bundle that corresponds to the type of database server you are using. It also contains database connection information specifying the values, such as user name and password, needed to connect to the database server. The connection information is stored in a dictionary whose keys identify the information the server expects, and whose values are the values that the adaptor will try when connecting. Each adaptor uses different keys; see your adaptor's documentation for keys it uses. The dictionary may contain incomplete connection information. In such cases, the user must specify the remaining information at runtime.

A newly created adaptor has no adaptor contexts; to create a new context send your adaptor a
createAdaptorContext
message. In Objective-C, an EOAdaptorContext retains its adaptor when created and an EOAdaptorChannel retains its context, so when you create a set of these objects, you need only retain the channel for all objects to remain valid.

You can create a connection dictionary and assign it to your adaptor with the
setConnectionDictionary
method. When you ask an adaptor to validate its connection dictionary with an
assertConnectionDictionaryIsValid
message, it briefly forms a connection to confirm that the server will accept the values in the dictionary. An adaptor doesn't form a lasting connection to the database server until one of its channels receives an
openChannel
message.

The following code excerpt shows one way to set up a suite of adaptor objects, given a model that's already loaded:

####  Objective-C Code

```

EOModel *myModel;    /* Assume this exists. */
EOAdaptor *myAdaptor;
EOAdaptorContext *myContext;
EOAdaptorChannel *myChannel;

myAdaptor = [EOAdaptor adaptorWithModel:myModel];
myContext = [myAdaptor createAdaptorContext];
myChannel = [myContext createAdaptorChannel];
NS_DURING
    [myAdaptor assertConnectionDictionaryIsValid];
NS_HANDLER
    /* Get database login information from the user */
NS_ENDHANDLER

[myChannel openChannel];
```

####  Java Code

```

EOModel myModel;    /* Assume this exists. */
EOAdaptor myAdaptor;
EOAdaptorContext myContext;
EOAdaptorChannel myChannel;

myAdaptor = EOAdaptor.adaptorWithModel(myModel);
myContext = myAdaptor.createAdaptorContext();
myChannel = myContext.createAdaptorChannel();
try {
    myAdaptor.assertConnectionDictionaryIsValid();
catch (NSException exception) {
    /* Get database login information from the user */
}

myChannel.openChannel();
```


The
assertConnectionDictionaryIsValid
invocation verifies that the adaptor has the information needed to log in to the server. This method raises an exception if it's unable to connect to the database server. Thus, it's invoked within an exception handling domain (bracketed by
NS_DURING
and
NS_HANDLER
macros in Objective-C, and in the
try
clause in Java). If the connection dictionary contains invalid information (for example, it's common to leave the user name and password unspecified in the model file),
assertConnectionDictionaryIsValid
raises an exception. As a result, the local exception handler (bracketed by
NS_HANDLER
and
NS_ENDHANDLER
macros in Objective-C, and in the
catch
clause in Java) invokes code

to allow the user to enter the necessary connection information. The invocation of
openChannel
at the end of the excerpt causes the application to form a connection to the database.

If you don't have a model, you can also create the EOAdaptor sublayer objects using the EOAdaptor
adaptorWithName
method. See the programming topic [Accessing Schema Information from the Database Server](Accessing%20Schema%20Information%20from%20the%20Database%20Server.md#apple-gi2denrx)
for an example.

##  See Also

- 

  [Accessing Schema Information from the Database Server](Accessing%20Schema%20Information%20from%20the%20Database%20Server.md#apple-gi2denrx)

##  Questions

- 

  How do I create adaptor sublayer objects?
- 

  How do I use the adaptor sublayer without using higher level objects?

##  Keywords

- 

  Adaptor
- 

  EOAdaptorChannel
- 

  Login
- 

  Connection Dictionary
- 

  EOModel
- 

  Database Server

##  Revision History

8 February, 1999. Clif Liu. First Draft.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Accessing%20Adaptor%20Sublayer%20Objects.md) [!](Executing%20Arbitrary%20SQL%20Statements.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
