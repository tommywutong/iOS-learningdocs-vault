---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.22.html
archived_at: '2026-07-15T07:59:43.390582Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.21.md) | [Back Up One Level](CSJ_Tutorial.20.md) | [Next](CSJ_Tutorial.23.md)

###  Generating Source Files

To begin creating your custom classes, generate source files for the Studio and Talent entities. You'll use these source files as a basis for adding custom behavior to your enterprise objects. Generating source files in a Java Client application typically produces "skeletal" __.java__
files for the associated class. These files are put in the __ClientSideJava.subproj__
subproject.

To generate source files for an entity, you must have replaced the text "EOGenericRecord" in the Class Name and Client-Side Class Name fields with a package name concatenated with a class name.

__1. Generate source files.__

> In the Model Editor, select the entity for which you want to generate source files.
>
> 
>
> Choose Property !
> Generate Client Java File.
>
> 
>
> In the Choose Class Name panel verify the file name and location (__ClientSideJava.subproj__
> ) and click Save.
>
> 
>
> Click OK when you're asked if you want to insert the files in the subproject.
>
> 
>
> For the same entity, choose Property !
> Generate Java FIle.
>
> 
>
> In the Choose Class Name panel verify the file name and location (main project) and click Save.
>
> 
>
> Click OK when you're asked if you want to insert the files in the main project.
>
> ###### 
>
> !
>
> 
>
> When Project Builder generates a class file (such as __Studio.java),__
> it strips off the package prefix and inserts a package declaration near the top of the file. The class file also includes the necessary import declarations as well as the instance variables and accessor methods derived from the properties of the Studio entity.

####  Studio.java (ClientSideJava.subproj)

`package businesslogic.client;

import com.apple.client.foundation.*;

import com.apple.client.eocontrol.*;

import java.math.BigDecimal;

import java.util.*;

public class Studio extends EOCustomObject {

        protected Number budget;

        protected String name;

    protected NSMutableArray movies;

    public Studio(EOEditingContext context, EOClassDescription classDesc, EOGlobalID gid) {

        super(context, classDesc, gid);

    }

    public Number budget() {

        willRead();

        return budget;

    }

    public void setBudget(Number value) {

        willChange();

        budget = value;

    }

    public String name() {

        willRead();

        return name;

    }

    public void setName(String value) {

        willChange();

        name = value;

}

    public NSArray movies() {

        willRead();

        return movies;

    }

    public void setMovies(NSMutableArray value) {

        willChange();

        movies = value;

    }

    public void addToMovies(EOEnterpriseObject object) {

        willChange();

        movies.addObject(object);

    }

    public void removeFromMovies(EOEnterpriseObject object) {

        willChange();

        movies.removeObject(object);

    }

}`

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.21.md) | [Back Up One Level](CSJ_Tutorial.20.md) | [Next](CSJ_Tutorial.23.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
