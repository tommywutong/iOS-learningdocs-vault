---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOCustomObjects/Modifying_t_ors_Project.html
archived_at: '2026-07-15T08:13:00.749843Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Generating_a_Custom_Class.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Adding_Custom_Logic.md)

## Modifying the Authors Project

Your code is written to work with EOGenericRecords. To take
advantage of the Author class, you need to alter the definitions
of variables and methods that interact with Author objects in your
program, making them Author objects rather than EOGenericRecords.

Make the following changes to the `Main.java` class:

1. Change the `@TypeInfo` line
   above the `authorList`'s
   definition so that it reads

   ```
   /** @TypeInfo Author */
   ```
2. Change the class of the `authorItem` and `author` instance
   variables from EOGenericRecord to Author.
3. Delete the `authorClassDescription` instance-variable
   definition and its assignment in the constructor.

   You only
   needed the class description to create new instances of EOGenericRecord with
   the correct type information. Now that you'll be using the Author
   class, the class description is no longer needed.
4. Change the constructor, `addAuthor`,
   and `updateAuthor` methods to create a new
   Author object instead of a new EOGenericRecord object.

   ```
   author = new Author();
   ```
5. Save `Main.java`.

After making those changes, Main.java should
look similar to [Listing 11-2](#apple-ijauuqscjjbek).

__Listing
11-2 Main.java modified to use Author class
instead of EOGenericRecord__

```
Main.java modified to use custom Author class instead of EOGenericRecord

import com.webobjects.foundation.*;
import com.webobjects.appserver.*;
import com.webobjects.eocontrol.*;
import com.webobjects.eoaccess.*;

public class Main extends WOComponent {
    protected Author author;
    protected Author authorItem;
    private EOEditingContext editingContext;
    private EOFetchSpecification fetchSpec;

    /** @TypeInfo Author */
    protected NSMutableArray authorList;

    public Main(WOContext context) {
        super(context);

        // build fetch specification
        fetchSpec = new EOFetchSpecification("Author", null, null);

        // get editing context
        editingContext = session().defaultEditingContext();

        // fetch
        authorList = new  NSMutableArray(editingContext.objectsWithFetchSpecification(fetchSpec));

        // create a new Author object (where form data is stored)
        author = new Author();
    }

    public WOComponent addAuthor() {
        // add only if the author is not already in the list
        if (! authorList.containsObject(author)) {
            // add author to list
            authorList.addObject(author);

            // insert author into editing context
            editingContext.insertObject(author);

            // create a new author
            author = new Author();
        }
        return null;
    }

    public WOComponent deleteAuthor() {
        // remove author from authorList
        authorList.removeObject(authorItem);

        // get object's editing context
        EOEditingContext ec = authorItem.editingContext();

        // remove author from object graph
        ec.deleteObject(authorItem);

        return null;
    }

    public WOComponent editAuthor() {
        // set the author to edit to the one the user selected
        author = authorItem;

        return null;
    }

    public WOComponent revertChanges() {
        // revert changes made in editing context
        editingContext.revert();

        // refetch
        authorList = new  NSMutableArray(editingContext.objectsWithFetchSpecification(fetchSpec));

        return null;
    }

    public WOComponent saveChanges() {
        // save changes made in editing context to object store
        editingContext.saveChanges();

        return null;
    }

    public WOComponent updateAuthor() {
        // create a new author
        author = new Author();

        return null;
    }

}
```

No further changes need to be made for the application to
run just as before. Because Author is a subclass of EOGenericRecord,
it still responds to the keypaths in the WOD file of the Main component.
Build and run the application to confirm it.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Generating_a_Custom_Class.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Adding_Custom_Logic.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
