---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.d.html
archived_at: '2026-07-15T08:10:01.264404Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Localizing%20a%20WebObjects%20Application.md) [!](Implementing%20a%20Login%20Panel.md)

#   Handling International Character Sets with EOF

##  Synopsis

Describes how to configure Enterprise Objects Framework (EOF) to handle international character sets with Oracle, Sybase, and Informix databases.

##  Discussion

When using databases such as Oracle, Sybase, or Informix, you can configure EOF to handle the character set used in the database. If you don't configure it, your application may read and write incorrect characters from the database and display them incorrectly. For example, an unconfigured application will display "il _tait une fois..." instead of "il était une fois". Only strings with extended characters (ASCII code greater than 127) are affected.

You can configure the character set to be used with EOF by adding information to the connection dictionary of your EOModel file under two keys.

The first key is
databaseEncoding
. This key tells the foundation classes which encoding to use when it builds strings from char \* strings. The possible values for this key can be found in the NSString class documentation in the paragraph about string encoding.

The name of the second key depends on the type of database. It tells the database client library what character set to use for sending or retrieving strings. For Oracle, the key name is
NLS_LANG
and for Sybase it is
LC_ALL
. For Informix you must specify two keys:
DB_LOCALE
and
CLIENT_LOCALE
.

You can add these keys by using the model inspector inside EOModeler.

The following are some examples of connection dictionaries

####  Oracle_(Continued)_

```

databaseEncoding = "ISO Latin-1";
NLS_LANG = "FRENCH_FRANCE.WE8ISO8859P1";
```


.

####  Sybase_(Continued)_

```

databaseEncoding = NEXTSTEP;
LC_ALL = "iso_1";
```

####  Informix

```

databaseEncoding = "ISO Latin-1";
DB_LOCALE = "en_us.8859-1";
CLIENT_LOCALE = "en_us.8859-1";
```


Refer to your database documentation to determine the character sets available in your configuration and the names of the environment variables.

###  When to Configure

Your application will sometimes handle character sets correctly even if you haven't set the connection dictionary values because when no entries are found in the connection dictionary, EOF uses the environment variables defined in the system. However, it is best to set the values in the connection dictionary to avoid potential problems. For example, moving your application to another computer with different environment variables may cause it to fail.

You should also configure the connection dictionary if your application uses a database shared with non-EOF applications. This guarantees that your data will be read and written correctly by those applications also.

###  When the Connection Dictionary Values Are Used

The entries you specified in your EOModel file are used the first time EOF connects to the database.

###  Databases With Mixed Encodings

Sometimes a database contains mixed encodings. This generally happens when different applications running on different platforms insert or modify values in a database.

One solution to this problem is to use a custom value class to try to figure out and decode the characters at fetch time. You can supply a class with a factory method that takes bytes and a length as arguments. This custom class can try to figure out the correct character set and then create and return the correct string. The class-and-methods specification is done inside EOModeler by selecting the internal data type as Custom in the Attribute inspector, and filling all appropriate fields.

Note: The custom value class must be written in Objective-C.

##  See Also

- 

  [Localizing a WebObjects Application](Localizing%20a%20WebObjects%20Application.md#apple-gm2dsmrr)

##  Questions

- 

  How can I display strings from my database containing international characters?
- 

  Why are accentuated character strings incorrectly displayed in my interface?
- 

  Why can't other applications read data created from an EOF application?
- 

  Which property entries are available for handling character inside EOF?
- 

  How can EOF work with a database containing mixed encodings?

##  Keywords

- 

  Localization
- 

  Character
- 

  Connection
- 

  Dictionary
- 

  Oracle
- 

  Sybase
- 

  Informix

##  Revision History

10 July 1998. Stéphane Lunati. First Draft.
26 July 1998. Stéphane Lunati. Added databases and mixed encodings.
18 November 1998. Clif Liu. Second Draft.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Localizing%20a%20WebObjects%20Application.md) [!](Implementing%20a%20Login%20Panel.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
