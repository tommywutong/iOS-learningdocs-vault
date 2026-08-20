---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/Create_EO.html
archived_at: '2026-07-15T08:00:59.916313Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Creating a New Enterprise Object

##  Synopsis

Describes how to create a new instances of custom objects and EOGenericRecords, both types of Enterprise Objects.

##  Discussion

New Enterprise Objects (EOs) are created when your application adds a new instance of an entity. For example,

· You might create a Movie object to store information about the latest film released by your company.

· You might create a new Customer object when your Banking application adds a new customer.

EOs encapsulate the attributes and behaviors that define the object. When you only need to "get" and "set" the EO's attributes, the default EOGenericRecord suffices as the business object. EOGenericRecords are part of the Enterprise Objects Framework (EOF), and provide functionality to create, read, update, and delete information from a variety of data stores. When your EO must define its own behavior, in addition to the "get" and "set", you need to create a Custom Enterprise Object and add the extra functionality to it.

The programming examples below outline how new instances of EOGenericRecord and custom EOs are created in Java, Objective-C, and WebScript. The Objective-C and WebScript code is identical. Each example assumes you have used EOModeler to define both your application's business objects and the mapping between the object's attributes and the data store schema's tables and columns. In the code examples, the Movie entity has two attributes: title and revenue.

####  Creating EOGenericRecords

Only basic `get' and `set' behavior is supported in this application.

#####  Figure 1. Java Sample Code

```
import com.apple.yellow.foundation.*;
```



```
import com.apple.yellow.webobjects.*;
```



```
import com.apple.yellow.eocontrol.*;
```



```
public class Main extends WOComponent {
```



```
    /** @TypeInfo Movie */
```



```
    protected EOEnterpriseObject aMovie;
```



```
    public WOComponent makeAMovie()
```



```
    {
```



```
        String entName = "Movie";  // Name of entity within eomodeld
```



```
        EOEditingContext ec = session().defaultEditingContext();
```



```
        EOClassDescription movieClassDesc;
```



```
        // create a Movie instance
```



```
        movieClassDesc = EOClassDescription().
            classDescriptionForEntityName(entName);
```



```
        aMovie = (EOEnterpriseObject) movieClassDesc.
            createInstanceWithEditingContext(ec, null);
```



```
        // set some default values.
```



```
        aMovie.takeValueForKey("DefaultTitle", "title");
```



```
        aMovie.takeValueForKey("1000000", "revenue");
```



```
        return null;  // updates the current component
```



```
    }
```



```
}
```


#####  Figure 2. WebScript or Objective C Sample Code

```
/** @TypeInfo Movie */
```



```
id aMovie;
```



```

```



```objc
- (WOComponent *)makeAMovie
```



```
{
```



```
    EOEditingContext *ec = [[self session] defaultEditingContext];
```



```
    aMovie = [[EOClassDescription classDescriptionForEntityName: @"Movie"]
```



```
            createInstanceWithEditingContext: ec
```



```
            globalID: nil
```



```
            zone:[ec zone]];
```



```
    [aMovie
```



```
    takeValue:@"DefaultTitle"
```



```
    forKey: @"title"];
```



```
    [aMovie
```



```
    takeValue:@"1000000"
```



```
    forKey: @"revenue"];
```



```

```



```
    return nil;
```



```
}
```


####  Custom Enterprise Object

You can add your own business logic to this code.

#####  Figure 3. Java Sample Code

```
import com.apple.yellow.foundation.*;
```



```
import com.apple.yellow.webobjects.*;
```



```
import com.apple.yellow.eocontrol.*;
```



```
import Movie;
```



```
public class Main extends WOComponent {
```



```
    Movie aMovie;
```



```
    public WOComponent makeAMovie()
```



```
    {
```



```
        // create an instance of a Movie.
```



```
        aMovie = new Movie(null,null,null);
```



```
        // set default values.
```



```
        aMovie.setTitle("DefaultTitle");
```



```
        aMovie.setRevenue(new Float("1000000"));
```



```
        return null;  // return the updated component.
```



```
    }
```



```
}
```


Also link Movie.java into the application by adding it to the `classes' folder within Project Builder. Generating Movie.java from EOModeler provides you with the common `get' and `set' methods. Additional business logic can be added directly to the Movie.java file.

Here's a portion of the Movie.java file:

#####  Figure 4. Java Sample Code

```
//
```



```
// Created on Mon Oct 26 22:43:39 1998 by Apple EOModeler Version 377
```



```
import com.apple.yellow.foundation.*;
```



```
import com.apple.yellow.eocontrol.*;
```



```
import java.util.*;
```

```
import java.math.BigDecimal;
```



```
public class Movie extends EOCustomObject {
```



```
    protected Number revenue;
```



```
    protected String title;
```



```
    // this is the constructor that EOF uses.
```



```
    // Later (perhaps upon a willRead()) it will
```



```
    // be populated with values via EOCustomObject's takeValueForKey() method
```



```
    public Movie(EOEditingContext context, EOClassDescription classDesc, EOGlobalID gid) {
```



```
        super(context, classDesc, gid);
```



```
    }
```



```
    public String category() { willRead(); return category; }
```



```
    public void setCategory(String value) {
```



```
        willChange();
```



```
        category = value;
```



```
    }
```



```
    public Number revenue() { willRead(); return revenue; }
```



```
    public void setRevenue(Number value) {
```



```
        willChange();
```



```
        revenue = value;
```



```
    }
```



```
    public String title() { willRead(); return title; }
```



```
    public void setTitle(String value) {
```



```
        willChange();
```



```
        title = value;
```



```
    }
```



```
 }
```



```
}
```


#####  Figure 5. WebScript or Objective C

```
//**************
```



```
// Main.wos
```



```
//**************
```



```
// Assumes Movie.h and Movie.m have been linked into your application.
```



```
// (Movie.h was generated from EOModeler and is shown below)
```



```
//
```



```
Movie *aMovie;
```



```objc
- (WOComponent *)makeAMovie
```



```
{
```



```
    // Create new instance of a Movie.
```



```
    aMovie = [[Movie alloc] init];
```



```
    // Set some of the attrs of the Movie.
```



```
    [aMovie setTitle: @"Default Title"];
```



```
    [aMovie setRevenue: @"1000000"];
```



```
    return nil;
```



```
}
```



```
//*************************************
```



```
//  Movie.h - generated from EOModeler
```



```
//*************************************
```



```
#import
```



```objc
@interface Movie : NSObject
```



```
{
```



```
    NSNumber *revenue;
```



```
    NSString *title;
```



```
}
```



```objc
- (void)setRevenue:(NSNumber *)value;
```



```objc
- (NSNumber *)revenue;
```



```objc
- (void)setTitle:(NSString *)value;
```



```objc
- (NSString *)title;
```



```objc
@end
```


##  See Also

· Inserting a New Enterprise Object into an Editing Context.

##  Questions

· How do I create an object?

· When should I use a custom object?

· When should I use a generic record?

· How do I set default values for an object?

##  Keywords

· EOGenericRecord

· Instantiate

· Custom Object

· Enterprise Object

##  Revision History

9 July 1998, Rich Flewelling. First Draft.
28 October 1998. Clif Liu. Second Draft.

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
