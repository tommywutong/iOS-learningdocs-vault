---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/Connect5.html
archived_at: '2026-07-15T08:02:58.226803Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Connecting%20to%20a%20Database.md) [!Previous Section](Using%20Multiple%20EODatabaseChannels.md)

# Character Encodings

An Enterprise Objects Framework adaptor and a database must communicate with one another using the same character encoding. For example, if the database sends data to your application using the EUC (Japanese) encoding, your application must interpret the data as EUC-encoded. Consequently, you have to tell both the database and the database adaptor what encoding to use.

## Choosing an Encoding

In choosing the encoding to use, you should attempt to minimize the amount of data conversion the database has to perform. For example, if the database stores EUC-encoded data, you should configure the database and adaptor to communicate with one another using the EUC encoding so the database doesn't have to perform a conversion. On the other hand, if your database stores data in an encoding that Enterprise Objects Framework doesn't support (such as EBCDIC), the database must convert its data to a supported encoding before sending it to your application. Similarly, it must convert data that it receives from your application into the encoding it uses for data storage. See the "Types and Constants" section of the _Foundation Reference_ for a complete list of supported encodings.
You should also attempt to minimize information loss by choosing an encoding that is as rich as the encoding the database uses for data storage. For example, if you choose a 7 bit ASCII encoding for communication when the database stores data in Unicode, the Unicode-encoded character `Á' loses its accent during conversion.

## Setting an Adaptor's Character Encoding

By default, Enterprise Objects Framework adaptors send and expect to receive data that is encoded with the default C string encoding. Since this encoding is unlikely to match the encoding the database uses for storage, you usually have to set it to a different encoding.
To change an adaptor's character encoding from the default, add a __databaseEncoding__ entry to the adaptor's connection dictionary specifying the encoding. The adaptors expect the __databaseEncoding__ entry to contain the localized name of an encoding. To get the localized name of an encoding, use the NSStringReference static method __localizedNameOfStringEncoding__ (in Objective-C, NSString's class method __localizedNameOfStringEncoding:__).

## Setting the Database Character Encoding

The default encoding a database uses for communicating with applications is database-dependent. Check your database server's documentation for more information.
If you need to use an encoding other than the default, Enterprise Objects Framework adaptors define adaptor-specific connection keys for setting the encoding. For example, the Sybase adaptor has the key __LC_ALL__ and the Oracle adaptor has the key __NLS_LANG__. To set the encoding the database should use to send data to and receive data from your application, add an entry to the adaptor's connection dictionary for the adaptor-specific key. Check your database server's documentation for the available character encodings.
__Note:__  The __databaseEncoding__ and the adaptor-specific encoding entries in a connection dictionary must specify the same encoding. However, the string that identifies the encoding may differ. For example, to tell a Sybase database to use the ISO Latin 1 encoding, you set the __LC_ALL__ connection key to "iso-1" and the __databaseEncoding__ connection key to "ISO Latin-1" .
[!Table of Contents](Connecting%20to%20a%20Database.md) [!Next Section](Behind%20the%20Scenes.md)
