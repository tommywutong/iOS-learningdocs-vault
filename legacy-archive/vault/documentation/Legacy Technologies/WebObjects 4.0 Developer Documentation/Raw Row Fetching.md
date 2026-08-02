---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.010.html
archived_at: '2026-07-15T07:57:54.337228Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](Merging%20Object%20Changes.md)

# Raw Row Fetching

When you perform a fetch in an Enterprise Objects Framework application, the information from the database is fetched and stored in a graph of enterprise objects. This object graph provides many advantages, but it can be large and complex. If you're creating a simple application, you may not need all of the benefits of the object graph. For example, a WebObjects application that merely displays information from a database without ever performing database updates and without ever traversing relationships might be just as well served by fetching the information into a set of dictionaries rather than a set of enterprise objects.
More specifically, suppose you want to display the first name, last name, and the department for a set of employees. Using objects, you would bind Employee's __firstName__, __lastName__, and __department.name__ keys to your user interface. This configuration requires fetching of all of the attributes in an Employee entity-the ones you want to display (__firstName__ and __lastName__) as well as the ones you don't (__salary__, __birthDate__, __address__, and so on, for example). In addition, this configuration requires faulting in (or perhaps prefetching) all of the related Department objects. Again you fetch all the Department attributes, those you want to display (__departmentName__) as well as those you don't (__budget__, __location__, and so on). In addition to fetching a large amount of data that your application doesn't use, this object-based fetch incurs the additional overhead of creating real enterprise objects from the returned data and of uniquing those objects in the EOEditingContext.
In this kind of display-only scenario, it might be preferable to fetch only the attributes that you need, and to fetch them as lightweight, non-uniqued, rows. In this example, you could fetch only the __firstName__, __lastName__, and __department.name__ for each employee. In addition to fetching less data, you'd also fetch with one trip to the database instead of two (one for Employee objects and one for the related Departments).
Enterprise Objects Framework 3.0 supports this concept of a simplified fetch, called _raw row_ fetching. In raw row fetching, each row from the database is fetched into an NSDictionary object.
To set up an application to perform raw row fetching, create an EOFetchSpecification, and send it a __setFetchesRawRows:YES__ (or __setFetchesRawRows(true)__ in Java) message. By default, the keys in the raw row dictionaries are the attribute names as given by the EOEntity's __attributesToFetch__ method.
If you want more control over the attributes that are fetched for the raw row, use the __setRawRowKeyPaths:__ method to specify the attribute paths you want. The key paths you provide can be simple attribute keys, such as __title__, as well as key paths, such as __studio.name__. After the fetch, each row is returned as a separate dictionary whose keys are the key paths you specified. If you use __setRawRowKeyPaths:__, you don't have to invoke __setFetchesRawRows:__; it's automatic.
When you use raw row fetching, you lose some important features:

- The NSDictionary objects are not uniqued.
- The NSDictionary objects aren't tracked by an editing context.
- You can't access to-many relationship information. (To access to-one relationship information, you use key paths such as "__movie.dateReleased__".)

Should you fetch a row into an NSDictionary and later want to fetch the corresponding enterprise object, send __faultForRawRow:entityNamed:editingContext:__ (or __faultForRawRow__ in Java) to the EOEditingContext. This creates a fault for the row (an EOFault object in Objective-C or an empty object of the correct enterprise object class in Java). The raw row dictionary must contain the primary key attributes for this method to work properly. When your code tries to access the object for that row, the fault forces another database fetch, and a true enterprise object is created.
The following tables describe the API added to support raw row fetching.

|  EOFetchSpecification |  EOFetchSpecification |
|  rawRowKeyPaths |  Returns an array of attribute keys that should be fetched as raw data. The default value is nil or null, indicating that full enterprise objects are to be returned from the fetch. If the array contains no objects, the entity specifies which attributes to fetch (EOEntity's attributesToFetch method). |
|  setRawRowKeyPaths: |  Sets the array of attribute keys that should be fetched as raw data. You can disable the fetching of raw rows by sending nil or null to this method. If you want to perform raw row fetching, but you want the entity to specify which attributes to fetch, you can pass an empty array to this method or you can use the setFetchesRawRows: method to enable raw row fetching. |
|  fetchesRawRows |  Returns whether raw row fetching is performed. YES or true if rawRowKeyPaths is non-nil or non-null. |
|  setFetchesRawRows: |  Sets whether raw row fetching is performed. If the value passed to this method is YES or true, then the rawRowKeyPaths array is set to an empty array. If NO or false, then the rawRowKeyPaths array is set to nil or null. |

```
```

|  EOObjectStore |  EOObjectStore |
|  faultForRawRow:entityNamed:editingContext: (Objective-C)  faultForRawRow (Java) |  Returns a fault for the given raw row dictionary. The raw row dictionary must include the primary key attributes for this method to work properly. If the dictionary does not include the primary key, this method raises or throws an exception.  Note that as EOObjectStore subclasses, EOEditingContext and EODatabaseContext also provide this method. |

```
```


In addition to these methods, EOUtilities also provides raw row fetching methods. For more information, see section "[New Convenience API](New%20Convenience%20API.md#apple-ge3deojv)."

[!Table of Contents](Table%20of%20Contents-2.md) [!Next Section](Support%20for%20Multi-Threaded%20Applications.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
