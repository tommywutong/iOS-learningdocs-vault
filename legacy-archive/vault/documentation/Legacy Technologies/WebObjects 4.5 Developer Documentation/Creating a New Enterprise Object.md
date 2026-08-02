---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.22.html
archived_at: '2026-07-15T08:09:58.670498Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Assigning%20Default%20Values%20to%20Enterprise%20Objects.md) [!](Generating%20Primary%20Key%20Values.md)

#   Creating a New Enterprise Object

##  Synopsis

Describes how to create a new instances of custom objects and EOGenericRecords, both types of enterprise objects.

##  Discussion

New enterprise objects are created when your application adds a new instance of an entity. For example,

- 

  You might create a Movie object to store information about the latest film released by your company.
- 

  You might create a new Customer object when your banking application adds a new customer.

Enterprise objects encapsulate the attributes and behaviors that define the object. When you only need to get and set the object's attributes, the default EOGenericRecord suffices as the business object. EOGenericRecords are part of EOF, and provide functionality to create, read, update, and delete information from a variety of data stores. When your EO must have its own behavior in addition to the get and set behaviors, you need to create a custom enterprise object and add the extra functionality to it.

The programming examples below outline how new instances of EOGenericRecord and custom enterprise objects are created in Java, Objective-C, and WebScript. The Objective-C and WebScript code is identical. Each example assumes you have used EOModeler to define both your application's business objects and the mapping between the object's attributes and the data store schema's tables and columns. In the code examples, the Movie entity has two attributes: title and revenue.

###  Creating EOGenericRecords

Only basic get and set behavior is supported in this application.

####  Creating EOGenericRecords (Java)

```

import com.apple.yellow.foundation.*;
import com.apple.yellow.webobjects.*;
import com.apple.yellow.eocontrol.*;
public class Main extends WOComponent {
    /** @TypeInfo Movie */
    protected EOEnterpriseObject aMovie;
    public WOComponent makeAMovie()
    {
        String entName = "Movie";  // Name of entity within eomodeld
        EOEditingContext ec = session().defaultEditingContext();
        EOClassDescription movieClassDesc;
        // create a Movie instance
        movieClassDesc = EOClassDescription().
            classDescriptionForEntityName(entName);
        aMovie = (EOEnterpriseObject) movieClassDesc.
            createInstanceWithEditingContext(ec, null);
        // set some default values.
        aMovie.takeValueForKey("DefaultTitle", "title");
        aMovie.takeValueForKey("1000000", "revenue");
        return null;  // updates the current component
    }
}
```

####  Creating EOGenericRecords (WebScript and Objective-C)

```objc

/** @TypeInfo Movie */
id aMovie;

- (WOComponent *)makeAMovie
{
    EOEditingContext *ec = [[self session] defaultEditingContext];
    aMovie = [[EOClassDescription classDescriptionForEntityName: @"Movie"]
        createInstanceWithEditingContext: ec
        globalID: nil
        zone: nil];
    [aMovie
        takeValue:@"DefaultTitle"
        forKey: @"title"];
    [aMovie
        takeValue:@"1000000"
        forKey: @"revenue"];

    return nil;
}
```


###  Custom Enterprise Object

You can add your own business logic to this code.

####  Creating a custom enterprise object (Java)

```

import com.apple.yellow.foundation.*;
import com.apple.yellow.webobjects.*;
import com.apple.yellow.eocontrol.*;
import Movie;
public class Main extends WOComponent {
    Movie aMovie;
    public WOComponent makeAMovie()
    {
        // create an instance of a Movie
        aMovie = new Movie(null,null,null);
        // set default values
        aMovie.setTitle("DefaultTitle");
        aMovie.setRevenue(new Float("1000000"));
        return null;  // return the updated component.
    }
}
```


Also link
Movie.java
into the application by adding it to the Classes folder within Project Builder. Generating
Movie.java
from EOModeler provides you with the common get and set methods. Additional business logic can be added directly to the
Movie.java
file.

Here's a portion of the
Movie.java
file:

####  Example custom enterprise object (Java)

```

//
// Created on Mon Oct 26 22:43:39  1998 by Apple EOModeler Version 377

import com.apple.yellow.foundation.*;
import com.apple.yellow.eocontrol.*;
import java.util.*;
import java.math.BigDecimal;

public class Movie extends EOCustomObject {
    protected Number revenue;
    protected String title;
    // This is the constructor that EOF uses.
    // Later (perhaps upon a willRead()) it will be populated with
    // values via EOCustomObject's takeValueForKey() method.
    public Movie(EOEditingContext context, EOClassDescription classDesc,
        EOGlobalID gid) {
        super(context, classDesc, gid);
    }
    public String category() { willRead(); return category; }
    public void setCategory(String value) {
        willChange();
        category = value;
    }
    public Number revenue() { willRead(); return revenue; }
    public void setRevenue(Number value) {
        willChange();
        revenue = value;
    }
    public String title() { willRead(); return title; }
    public void setTitle(String value) {
        willChange();
        title = value;
    }
 }
}
```

####  Creating a custom enterprise object (WebScript and Objective-C)

```objc

//**************
// Main.wos
//**************
// Assumes Movie.h and Movie.m have been linked into your application.
// (Movie.h was generated from EOModeler and is shown below)
//
Movie *aMovie;
- (WOComponent *)makeAMovie
{
    // Create new instance of a Movie
    aMovie = [[Movie alloc] init];
    // Set some of the attrs of the Movie
    [aMovie setTitle: @"Default Title"];
    [aMovie setRevenue: @"1000000"];
    return nil;
}
```

####  Example custom enterprise object (Objective-C)

```objc

//*************************************
//  Movie.h - generated from EOModeler
//*************************************
#import <EOControl/EOControl.h>
@interface Movie : NSObject <NSCoding>
{
    NSNumber *revenue;
    NSString *title;
}
- (void)setRevenue:(NSNumber *)value;
- (NSNumber *)revenue;
- (void)setTitle:(NSString *)value;
- (NSString *)title;
@end
```


##  See Also

##  Questions

- 

  How do I create an object?
- 

  When should I use a custom object?
- 

  When should I use a generic record?
- 

  How do I set default values for an object?

##  Keywords

- 

  EOGenericRecord
- 

  Instantiate
- 

  EOCustomObject
- 

  Enterprise Object

##  Revision History

9 July 1998, Rich Flewelling. First Draft.
28 October 1998. Clif Liu. Second Draft.

```

```


---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Assigning%20Default%20Values%20to%20Enterprise%20Objects.md) [!](Generating%20Primary%20Key%20Values.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
