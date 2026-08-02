---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Enhancing/Adding_Beha_ise_Objects.html
archived_at: '2026-07-15T08:14:19.719268Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](Expanding_t_ovies_Model.md)[![Next](attachments/JavaClient/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Advanced/index.html)

## Adding Behavior to Your Enterprise Objects

As the preceding sections illustrate, you can go quite far
in a Java Client application without writing any code. However,
the real power of such an application or any Enterprise Objects
Framework application lies in the enterprise objects you create.
The behavior (business logic) you add to your objects is what brings
your stored data to life.

### Specifying Custom Enterprise Object Classes

When creating a model of a database using the EOModeler application's
wizard, you have the option of creating custom enterprise objects.
If this option is selected, EOModeler derives both entity name and
class name from the name of the associated database table. Otherwise,
EOModeler maps entities to the EOGenericRecord class, which can
be thought of as the default enterprise object class.

The EOGenericRecord class is sufficient when all you want
the entity to do is get and set properties. However, when you want
to add custom behavior to a class (for example, to assign default
values when you create new objects or to perform validation), you
need to implement a custom enterprise object class. This class includes
the default behavior provided in EOGenericRecord as well as the
custom behavior you implement.

To use a custom class instead of EOGenericRecord follow these
steps:

1. In EOModeler,
   select the Movies model root (top of the tree).

   Make sure you're
   in Table mode.

   If the Client-Side Class Name column
   is not visible, choose Client-Side Class Name from the Add Column
   pop-up menu at the bottom of the window.
2. Double-click the Studio's Class Name cell in the table.
3. Type businesslogic.server.Studio in
   the cell (businesslogic.server is the package name).
4. Double-click the Client-Side Class Name cell.
5. Type businesslogic.client.Studio in
   this cell (businesslogic.client is the package name).

Repeat the above steps for the Talent entity (append "Talent"
to the package names).

Save the model.

![[image: ../Art/customjavaclassnames.gif]](../Art/customjavaclassnames.gif)

By convention, the names of classes (minus the package prefix)
are based on the name of the corresponding entity and the initial
letter of the name is capitalized.

There is no requirement that you create matching server and
client classes. You can implement a class only on the server or
the client, whichever suits your needs; the unimplemented class
assumes the default behavior of EOGenericRecord.

Once you specify a custom class for an entity in EOModeler,
you can generate source files for that entity.

For more information on custom enterprise objects, see ["When Do You Use a Custom Enterprise Object Class?"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Concepts/iWhen_Do_You_ject_Class_.html).

### Getting Your Project Ready to Receive Custom Classes

Project Builder stores most of the files for a project at
the top level of the project directory. To separate _business
logic_ files from normal WebObjects files, it is recommended
that a group called Business Logic be created in the project. In
it, all the business logic files can be stored. To further separate
server-side files from client-side files, the Business Logic group
should contain at least two subgroups: Server and Client. And additional
subgroup, Common, can be added under Business Logic when you want
to share behavior with the server and client applications.

To create the recommended grouping for Java Client projects,
follow these steps:

1. Create the
   directory structure.

   Create the following directories at the
   top level of your project directory:

   - `BusinessLogic`
   - `BusinessLogic/Server`
   - `BusinessLogic/Client`
   - `BusinessLogic/Common` (optional,
     not needed for this tutorial)
2. Create the Business Logic group in the project.

   In the
   Groups & Files list of Project Builder's main window, select
   the StudioManager root group.

   Choose Project > New
   Group.

   Name the group "Business Logic".

### Generating Source Files

To begin creating your custom classes, generate source files
for the Studio and Talent entities. You'll use these source files
as a basis for adding custom behavior to your enterprise objects.
Generating source files in a Java Client application typically produces skeletal
Java (`.java`) files for
the associated class. You then add these files to your project.

|  |
| --- |
| __Note:__ To generate source files for an entity, you must have replaced the text "EOGenericRecord" in the Class Name and Client-Side Class Name fields with a package name concatenated with a class name. |

1. Generate
   the client-side `.java` files.

   Open
   the Movies model file (if it's not already open).

   Select
   the Studio entity.

   Choose Property > Generate Client
   Java Files.

   Select the Client directory inside the BusinessLogic
   directory.

   Click Save.

   ![[image: ../Art/creatingclientclasses.gif]](../Art/creatingclientclasses.gif)

   Repeat the process
   for the Talent entity.
2. Generate server-side `.java` files.

   Select
   the Studio entity.

   Choose Property > Generate Java
   Files.

   Select the Server directory
   inside the BusinessLogic directory.

   Click
   Save.

   Repeat the process for the Talent entity.

When EOModeler generates a class file (such as `Studio.java),` it
strips off the package prefix and inserts a package declaration
near the top of the file. The class file also includes the necessary
import declarations as well as the instance variables and accessor
methods derived from the properties of the entity as defined in
the model file.

### Adding Custom Java Files to Your Project

After you have generated custom Java files for the enterprise
objects that you wish to customize, you can add them to your project.
Remember that you must first prepare your project file as explained
in ["Getting Your Project Ready to Receive Custom Classes"](#apple-krifqusfiyytknq).

1. Add the custom
   client-side classes to the project file in Project Builder.

   In
   the Groups & Files list in Project Builder's main window,
   select the Business Logic group.

   Choose Project >
   Add Files.

   Select the Client directory
   in the BusinessLogic directory.

   Click
   Open.

   ![[image: ../Art/addingcustomclientclasses.gif]](../Art/addingcustomclientclasses.gif)

   The target selection sheet
   appears.

   Select the Client target.

   Click
   Add.

   ![[image: ../Art/selectingtargetforclasses.gif]](../Art/selectingtargetforclasses.gif)
2. Add the custom server-side classes.

   In the Groups &
   Files list in Project Builder's main window, select the Business
   Logic group.

   Choose Project > Add Files.

   Select
   the Server directory in the BusinessLogic directory.

   Click
   Open.

   The target selection sheet appears.

   Select
   the Server target.

   Click Add.

Now the project uses custom classes for the Studio and Talent
enterprise objects instead of EOGenericRecord. These class files
can now be edited to implement custom behavior.

If you examine the code in [Listing 3-1](#apple-infeescbjjfeq), you'll notice that
the class generated by EOModeler does not have actual instance variables
or _fields_. The methods to access the attributes
of the custom enterprise object are implemented using key-value
coding.

__Listing
3-1 Client-side Studio.java file generated
by EOModeler__

```
package businesslogic.client;

import com.webobjects.foundation.*;
import com.webobjects.eocontrol.*;

public class Studio extends EOGenericRecord {

    public Studio() {
        super();
    }

    public Studio(EOEditingContext context, EOClassDescription classDesc, EOGlobalID  gid) {
        super(context, classDesc, gid);
    }

    public String name() {
        return (String)storedValueForKey("name");
    }

    public void setName(String value) {
        takeStoredValueForKey(value, "name");
    }

    public Number budget() {
        return (Number)storedValueForKey("budget");
    }

    public void setBudget(Number value) {
        takeStoredValueForKey(value, "budget");
    }

    public NSArray movies() {
        return (NSArray)storedValueForKey("movies");
    }

    public void setMovies(NSMutableArray value) {
        takeStoredValueForKey(value, "movies");
    }

    public void addToMovies(EOGenericRecord object) {
        NSMutableArray array = (NSMutableArray)movies();

        willChange();
        array.addObject(object);
    }

    public void removeFromMovies(EOGenericRecord object) {
        NSMutableArray array = (NSMutableArray)movies();

        willChange();
        array.removeObject(object);
    }
}
```


### Implementing Custom Behavior for Your Classes

The user interface you designed in Interface Builder already
allows you to insert and delete Studio objects. However, it doesn't
do any additional processing when these operations take place. For
example, what if you want to assign default values to newly created
objects? And how can you prevent users from inserting objects that
contain invalid data? You can add methods to your enterprise objects
to handle such issues.

For more information, see ["Adding Behavior to Enterprise Objects"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Concepts/iAdding_Beha_ise_Objects.html).

#### Distributing Business Logic in Java Client Applications

The value of Java Client applications, of course, lies in
their ability to distribute processing duties among objects on the
server and objects on the client. Primarily for security and performance
reasons, you can have only objects on the server performing some
tasks and only objects on the client performing others.

For example, sometimes you want only objects behind the firewalls
and other security mechanisms of the server to have access to sensitive
information, such as account numbers. On the other hand, processing
tasks such as calculation of balances should be performed by objects
on the client, thereby improving application performance by eliminating
the need for a cycle of the request-response loop.

There are no hard and fast rules for how to distribute object
behavior. An enterprise object on the client can have the same set
of methods and instance variables as its counterpart on the server,
or what it has can be a subset (or superset) of the other object's
methods and instance variables. The best way to distribute business
logic among objects depends on the particular nature of your application.

#### Managing Relationships

In ["Transferring Movies Between Studios"](Adding_Relationships.md#apple-krifqusfiyytgmy) you added a pop-up list to
the user interface to transfer movies between studios. However,
there is still work to be done. When a movie is sold to a new studio,
you need to add the amount of the movie's revenue to the old studio's budget
(to show the studio's profit from the sale). Likewise, you need
to subtract the amount of the movie's revenue from the new studio's
budget (to reflect the expense of purchasing the movie).

When you transfer movies between studios, you're actually
manipulating the `movies` relationship
property in each of the Studio objects, deleting the Movie object
from the `movies` array
of the old studio, and adding the Movie object to the `movies` array
of the new studio. Enterprise Objects Framework automatically invokes
the method `addObject` when you
add an object to an array that represents a relationship property,
and invokes `removeObject` when
you delete an object from the array. These methods are part of the EORelatioshipManipulation
protocol. See the _EOControl Java API Reference_ for
details.

When passed a key (such as `movies`),
the default implementations of these methods look for a method that
has the name `addTo`_Key_ (when
an object is being added) and `removeFrom`_Key_ (when
an object is being removed). Skeletal versions of these methods
are provided in the source code you created using EOModeler in ["Generating Source Files"](#apple-krifqusfiyytgny).

To intervene and perform your own processing when objects
are added to and removed from the `movies` relationship
array, you add code to the methods `addToMovies` and `removeFromMovies` in
the Studio class of the Client target, as shown in [Listing 3-2](#apple-infeesscivcuk).

__Listing
3-2 Studio.java (server and client) - Extending
default behavior__

```
import java.math.*;

public void addToMovies(EOGenericRecord object) {
        NSMutableArray array = (NSMutableArray)movies();

        willChange();

        // Subtract movie's revenue from budget.
        Number newBudget;
        Number movieRevenue = (Number)object.storedValueForKey("revenue");
        newBudget = new BigDecimal(budget().doubleValue() -  movieRevenue.doubleValue());
        setBudget(newBudget);

        array.addObject(object);
    }

    public void removeFromMovies(EOGenericRecord object) {
        NSMutableArray array = (NSMutableArray)movies();

        willChange();

        // Add movie's revenue to budget.
        Number newBudget;
        Number movieRevenue = (Number)object.storedValueForKey("revenue");
        newBudget = new BigDecimal(budget().doubleValue() +  movieRevenue.doubleValue());
        setBudget(newBudget);

        array.removeObject(object);
    }
```


#### Writing Derived Methods

One kind of behavior you might want to add to your enterprise
object class is the ability to perform computations based on the
values of class properties. For example, studios have movies, and
the total revenue of the movies times 1.5 constitutes the studio's
portfolio value. To calculate a studio's portfolio value, you
could have a method in `Studio.java` like the
one shown in [Listing 3-3](#apple-infeerckizaum).

__Listing
3-3 Studio.java (client) - Calculating a
studio's revenue__

```
import java.math.*;
public Number portfolioValue() {
    int i, count;
    double total;
    NSArray revenues;

    total = 0.0;
    revenues = (NSArray)(movies().valueForKey("revenue"));

    count = revenues.count();
    for (i = 0; i < count; i++) {
        total +=
            ((Number)(revenues.objectAtIndex(i))).doubleValue();
    }

    return new BigDecimal(total * 1.5);
}
```

You can display the results of this method in the user interface
by forming an association between a control and the method. That
way, whenever a new studio is selected or when a selected studio's
movie revenues change, its portfolio value is dynamically recalculated and
displayed.

1. Add methods
   to your custom enterprise object classes.

   Add the code in [Listing 3-3](#apple-infeerckizaum) to
   the client-side Studio.java file.

   Save
   the Studio.java file.
2. Add a custom methods as a display-group properties.

   Open
   the project's interface (nib) file.

   Display the Attributes
   pane of the Info window for the Studio EODisplayGroup.

   Enter
   the name of the method (`portfolioValue`)
   you want to use in an association into the text field.

   Click
   Add.

   ![[image: ../Art/addingcustommethod.gif]](../Art/addingcustommethod.gif)
3. Add the necessary user-interface controls.

   Once you've
   added the method as a class key, you can use it in associations.

   Using [Figure 3-3](#apple-ijbusr2hizduk) as a
   guide, do the following:

   - Add three text fields
     to the user interface.
   - Add labels to the left of fields: "Name:", "Budget:",
     and "Revenue:".
   - Right-justify the Budget and Revenue text fields.

   __Figure
   3-3 Adding elements to the interface__

   ![[image: ../Art/addinginterfaceelements.gif]](../Art/addinginterfaceelements.gif)
4. Associate interface controls with custom methods.

   Associate
   the Revenue text field with the `portfolioValue` method:

   - Control-drag from
     the Revenues text field to the Studio EODisplayGroup.
   - Display the Connections view of the Info window.
   - Choose EOTextAssociation from the pop-up menu.
   - Select `value` in
     the left column.
   - Select `portfolioValue` in
     the right column.
   - Click Connect.![[image: ../Art/assoccontrolswithmethods.gif]](../Art/assoccontrolswithmethods.gif)

   Repeat the process
   to connect the Name field to Studio's `name` attribute
   and the Budget field to the `budget` attribute.
5. Add the necessary formatters to the interface controls and
   choose the format.

   Currency formatters aren't added automatically,
   because a field has no way of knowing that it's going to be used
   to display currency values-it's just connected to a property.

   From
   the Data Views palette, drag the currency formatter into the Budget
   text field.

   ![[image: ../Art/addingcurrencyformatter.gif]](../Art/addingcurrencyformatter.gif)

   Once you've added the formatter,
   you can use the Info window to change the display format.

   Select
   the standard currency format.

   ![[image: ../Art/ibtextfieldinfofmt.gif]](../Art/ibtextfieldinfofmt.gif)

   Repeat the process
   for the Revenue text field.
6. Save the interface file.
7. Build and test the application on the client.

   (See ["Building and Testing Your Application"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Creating/iBuilding_an_Application.html) for details.)

#### Performing Validation

Another behavior you'll likely want to add to your enterprise
object classes is validation. For example, suppose that when a studio
buys a new movie, you want to make sure that acquiring the movie
won't cause the studio to exceed its budget. You could implement
a method in the Studio class like the one shown in [Listing 3-4](#apple-infeeskfjffei).

__Listing
3-4 Studio.java (server and client) - Validation__

```
public void validateBudget(Number budget) throws
    NSValidation.ValidationException {
    if (budget.intValue() < 100) {
        throw new NSValidation.ValidationException
            ("A budget cannot be less than $100");
    }
}
```

You use a NSValidation.ValidationException object to tell
Enterprise Objects Framework that the current object graph is not
cleared to be saved to the database.

Now when a studio buys more movies than it can afford, a panel
displaying the message "A budget cannot be less than $100" appears
when the user attempts to save the changes to the database.

Validation methods must be of the form `validate`_Attribute_.
The `validateBudget` method
is invoked by the `validateValueForKey` method,
which is part of the EOValidation interface that uses the EOClassDescription
class to provide default implementations of validation methods.
These methods are invoked automatically by framework components
such as EODisplayGroup and EOEditingContext. They are

- validateClientUpdate
- validateForSave
- validateForDelete
- validateForInsert
- validateForUpdate

You can find more information on this topic in the book _Enterprise
Objects Framework Developer's Guide_.

#### Providing Default Values for Newly Inserted Objects

When new objects are created in your application and inserted
into the database, it's common to assign default values to some
of their properties. For example, you might decide to assign newly
created Studio objects a default budget (the budget is the amount
a studio is allowed to spend on new movies).

To assign default values to newly created enterprise objects,
use the method `awakeFromInsertion`.
This method is automatically invoked right after your enterprise object
class creates a new object and inserts it into an EOEditingContext.

[Listing 3-5](#apple-infeerkgizces) shows the implementation of `awakeFromInsertion` in
the Studio class. It sets the default value of the `budget` property
to be one million dollars.

__Listing
3-5 Studio.java (server and client) - Default
values__

```
public void awakeFromInsertion(EOEditingContext context) {
    super.awakeFromInsertion(context);
    if (budget() == null) {
        setBudget(new BigDecimal("1000000"));
    }
}
```

When a user clicks the Add Studio button in the StudioManager
application, a new record is inserted, with "$1,000,000.00"
already displayed as a value in the Budget column.

#### Invoking Server Methods Remotely

In a Java Client application you may want some methods to
execute only on the server. This is particularly the case when security
is an issue, but performance can be a reason as well (as when the
method consumes a lot of system resources). Objects on the client
side of a Java Client application can use two methods to invoke
a server method:

- __invokeRemoteMethod__ An
  enterprise object on the client side can use this method to invoke
  a method in the corresponding enterprise object on the server. The
  arguments are the name of the method to invoke and an array of arguments.
  Before the method is invoked on the server, the current state of
  the client-side editing context is "pushed" to the server to
  ensure that the method executes in an identical context. (Note that EODistributedObjectStore
  has a version of this method that includes a flag as an argument;
  setting this flag to `false` prevents
  the client from pushing its editing-context state to the server.)
- __invokeRemoteMethodWithKeyPath__ You can
  send a message to _any_ object on the server
  with this method, which is defined in EODistributedObjectStore.
  For more on this method, see the specification for this EODistribution
  class.

If you want to give studios the ability to buy all of the
movies that star a specified actor but consider this a sensitive
computation, you can implement a method like the one in [Listing 3-6](#apple-infeeqsfivcei) in
the client's `Studio.java`.

__Listing
3-6 Studioi.java (client) - Buying all the
movies starring a specific talent__

```
public void buyAllMoviesStarringTalent(Talent talent) {
    invokeRemoteMethod("clientSideRequestBuyAllMoviesStarringTalent",      new Class[] {Object.class}, new Object[] {talent});
}
```

The method begins with `clientSideRequest`;
this is not accidental. The EODistributionContext object on the
server-side EODistribution layer will reject a remote invocation
unless it has this prefix _or_ its delegate implements
the proper delegation methods (see the reference documentation for
EODistributionContext or EODistributedObjectStore for more information).

[Listing 3-7](#apple-infeer2ci5duc) shows the invoked method, which is implemented in
the server's `Studio.java`.

__Listing
3-7 Studio.java (server) - Buying all the
movies starring a specific talent__

```
public void buyAllMoviesStarringTalent(Talent talent) {
    int i, count;
    NSArray talentMovies;
    EOEnterpriseObject movie, studio;

    talentMovies = talent.moviesStarredIn();
    count = talentMovies.count();
    for (i = 0; i < count; i++) {
        movie =
            (EOEnterpriseObject)(talentMovies.objectAtIndex(i));
        if (!(movies().containsObject(movie))) {
            studio =
                (EOEnterpriseObject)(movie.valueForKey("studio"));
            if (studio != null)
                studio.
                removeObjectFromBothSidesOfRelationshipWithKey
                (movie,"movies");
            addObjectToBothSidesOfRelationshipWithKey
                (movie,"movies");
        }
    }
}

public void clientSideRequestBuyAllMoviesStarring(Object object) {
    buyAllMoviesStarringTalent((Talent)object);
}
```

[Listing 3-8](#apple-infeesceivbes) shows server's `buyAllMoviesStarringTalent` method,
which invokes the `moviesStarredIn` method.

__Listing
3-8 Talent.java (server) - Buying all the
movies starring a specific talent__

```
public NSArray moviesStarredIn() {
    int i, count;
    NSArray movies;
    NSMutableArray moviesStarredIn;
    EOEnterpriseObject movie;

    moviesStarredIn = new NSMutableArray();
    movies = (NSArray)(movieRoles().valueForKey("movie"));

    count = movies.count();
    for (i = 0; i < count; i++) {
        movie = (EOEnterpriseObject)(movies.objectAtIndex(i));
        if (!(moviesStarredIn.containsObject(movie))) {
            moviesStarredIn.addObject(movie);
        }
    }
    return moviesStarredIn;
}
```

You can associate the `buyAllMoviesStarringTalent` method
with a user interface control. But first you need to add to your
user interface a table that lists all actors (talent).

1. Add a new
   table view to your user interface.

   Drag the Talent entity from
   your model into the nib file window in Interface Builder.

   Drag
   a table view from the Palette onto your window.

   ![[image: ../Art/addingtableviewtonib.gif]](../Art/addingtableviewtonib.gif)
2. Associate the table view columns with enterprise objects.

   Control-drag
   from the first table view column into the Talent EODisplayGroup.

   Using
   the value aspect of the EOTableColumnAssociation, connect the table
   view column to the `firstName` attribute
   of the Talent EODisplayGroup.

   Using a similar process,
   connect the second column of the table view to the `lastName` property
   of the Talent EODisplayGroup.
3. Add a button to the window.

   Drag a button into the window
   and place it below the Revenue field.

   Give it the title
   "Buy Movies Starring Selected Talent".
4. Add a method to an EODisplayGroup.

   Now that you've
   added the table view, connected it to the `firstName` and `lastName` properties
   of the Talent EODisplayGroup, and added a Buy button to the window, you're
   ready to use an EOActionAssociation to connect the button to the `buyAllMoviesStarringTalent` method.

   Display
   the Attributes pane of the Info window for the Studio EODisplayGroup.

   In
   the text field type the name of the method (`buyAllMoviesStarringTalent`)
   you want to use in an association.

   Click Add.

   ![[image: ../Art/assoccontrolswithmethods2.gif]](../Art/assoccontrolswithmethods2.gif)

   You can now use the `buyAllMoviesStarringTalent` method
   in associations.
5. Associate a user interface element with a method.

   Control-drag
   from the Buy Movies Starring Selected Talent button to the Studio EODisplayGroup.

   In
   the Connections pane of the Info window, choose EOActionAssociation
   from the pop-up menu at the top of the left column.

   Select `action` in
   the left column, and the method you want to connect to (`buyAllMoviesStarringTalent`)
   in the right column.

   Click Connect.

   ![[image: ../Art/connectingbuttonwithmethod.gif.gif]](../Art/connectingbuttonwithmethod.gif)
6. Associate a user interface element with the arguments it provides
   to its method.

   Because the `buyAllMoviesStarringTalent` method
   takes a Talent object as an argument, you also need to make a connection
   from the Buy button to the Talent EODisplayGroup.

   Control-drag
   from the Buy Movies Starring Selected Talent button to the Talent EODisplayGroup.

   In
   the Info window, select `argument` in
   the left column. The argument aspect takes the destination of the
   connection (Talent) as an argument, which will be supplied to the `buyAllMoviesStarringTalent` method.

   Click
   Connect.

   ![[image: ../Art/connectingbuttontoargument.gif]](../Art/connectingbuttontoargument.gif)

   Once you finish connecting
   the button, you can use it to purchase all of the movies starring
   the selected actor for the selected studio.
7. Save the interface.
8. Build and test your application.

### Controlling the User Interface

In Java Client applications you can give the interface controller
(implemented in this project in `StudioManagerInterfaceController.java` on
the client) a _controller display group._ By
creating associations between the controller display group and aspects
of user-interface elements, you can use the interface controller
to manage various facets of the user interface. In the following
steps, you add a method as a property of the controller display group
and bind this method to the `enabled` aspect
of the Revenue field through an EOControlAssociation; since this
method simply returns `false`,
the field is disabled.

1. Add a display
   group to the nib file.

   Drag a display group from the EnterpriseObjects
   Palette to the nib file window.

   ![[image: ../Art/displaygroupdrag.gif]](../Art/displaygroupdrag.gif)

   Double-click
   the title of the display group to select it.

   Give the
   display group the name "Controller".
2. Connect the interface controller to its display group.

   As
   mentioned earlier, the owner of the nib file (File's Owner) is
   an instance of the custom EOInterfaceController automatically created
   by Project Builder. EOIntefaceController has a `controllerDisplayGroup` outlet;
   you'll connect the interface controller to this outlet.

   Control-drag
   from File's Owner to the Controller icon.

   In the Connections
   pane of the Info window, select controllerDisplayGroup.

   Click
   Connect.

   ![[image: ../Art/fileownersdisplaygroupinfo.gif]](../Art/fileownersdisplaygroupinfo.gif)
3. Add a property to the controller display group.

   Now you'll
   add the `neverEnabled` method
   as a property of the controller display group.

   Select
   the Controller display group in the nib file.

   In the
   Attributes pane of the Info window, enter `neverEnabled` in
   the field.

   Click Add.

   ![[image: ../Art/ownerdisplaygroupinfo.gif]](../Art/ownerdisplaygroupinfo.gif)
4. Connect an interface element to a property of the controller's
   display group.

   Now you'll hook up the field to the display
   group using an EOActionAssociation to bind its `enabled` aspect
   to the `neverEnabled` method.

   Control-drag
   from the Revenue field to the Controller display group.

   In
   the Connections pane of the Info window, choose EOActionAssociation
   from the pop-up list at the top of the left column.

   Select `enabled` in
   the left column.

   Select `neverEnabled` in
   the right column.

   Click Connect.

   ![[image: ../Art/interfacetocontroller.gif]](../Art/interfacetocontroller.gif)
5. Implement the `neverEnabled` method.

   Now
   that the interface controller, the controller display group, and
   the Revenue field are interconnected via their outlets and associations,
   you can implement the method bound to the `enabled` aspect
   (in `StudioManagerInterfaceController.Java` on
   the client) as [Listing 3-9](#apple-infeer2kjjeuk) shows.

   __Listing 3-9 neverEnabled
   method__

   ```
   public boolean neverEnabled() {
           return false;
   }
   ```
6. Build, run, and test the application.

   Build the project
   and test the application. The user can copy the contents of the
   Revenue field but it cannot be written into.

[![Previous](attachments/JavaClient/Images/previous.gif)](Expanding_t_ovies_Model.md)[![Next](attachments/JavaClient/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Advanced/index.html)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
