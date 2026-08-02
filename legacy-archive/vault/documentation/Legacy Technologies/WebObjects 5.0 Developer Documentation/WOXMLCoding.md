---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/XML/Protocols/WOXMLCoding.html
archived_at: '2026-07-15T08:14:47.382376Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/XML/Art/up.gif)](../XMLTOC.md) 

# WOXMLCoding

> __Implemented by:__ Custom objects that need to be encoded as XML

> __Package:__ com.webobjects.appserver.xml

---

## Interface Description

---

When operating without a mapping model, the [WOXMLCoding](#apple-k5hug33oorsxq5a) class is capable of encoding a predefined set of Java classes, any object that is an instance of EOEnterpriseObject, and any object that implements the WOXMLCoding interface. This interface consists of a single method, [encodeWithWOXMLCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6v2plbguyq3pmruw4zzpmvxgg33emvlws5dik5hvqtkminxwizls), in which you encode your object's instance variables using WOXMLCoder's various __encode...ForKey__ methods.

If you'll be reconstituting objects from XML using [WOXMLCoding](#apple-k5hug33oorsxq5a), your classes must have a constructor that takes a WOXMLDecoder object as its sole argument. This constructor should consist of a series of __decode...ForKey__ method invocations that restore each of your object's instance variables.

The following simple "Person" class implements both the WOXMLCoding interface and the single-argument constructor needed to later decode objects of this class.

```
import com.webobjects.appserver.xml.*;
import com.webobjects.foundation.*;
import java.lang.*;
import java.net.*;
import java.math.*;

public class Person extends Object implements WOXMLCoding {
    String name;
    boolean married;
    int children;

    public Person() {
        name = "John Smith";
        married = true;
        children = 2;
    }

    public void encodeWithWOXMLCoder(WOXMLCoder coder) {
        coder.encodeObjectForKey(name, "Name");
        coder.encodeBooleanForKey(married, "MaritalStatus");
        coder.encodeIntForKey(children, "NumberOfChildren");
   }

    // constructor required for decoding
    public Person(WOXMLDecoder decoder) {
        name = (String)decoder.decodeObjectForKey("Name");
        married = decoder.decodeBooleanForKey("MaritalStatus");
        children = decoder.decodeIntForKey("NumberOfChildren");
    }
}
```

See the XMLArchiving example (accessible through the WebObjects Info Center under Examples > WebObjects > Java > XMLArchiving) for a more complete example illustrating the use of the WOXMLCoding interface.

## Instance Methods

---

### classForCoder

`public abstract Class classForCoder()`

Description forthcoming.

---

### encodeWithWOXMLCoder

`public abstract void encodeWithWOXMLCoder(WOXMLCoder aCoder)`

Implement this method using WOXMLCoder's various __encode...ForKey__ methods (invoked on _aCoder_) to encode your object's instance variables.

__See Also:__ [WOXMLCoding](#apple-k5hug33oorsxq5a) class

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/Reference/XML/Art/up.gif)](../XMLTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
