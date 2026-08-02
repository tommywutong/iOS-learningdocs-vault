---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.23.html
archived_at: '2026-07-15T07:59:44.597869Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.22.md) | [Back Up One Level](CSJ_Tutorial.20.md) | [Next](CSJ_Tutorial.24.md)

###  Implementing Custom Behavior for Your Classes

The user interface you designed in Interface Builder already allows you to insert and delete Studio objects. However, it doesn't do any additional processing when these operations take place. For example, what if you want to assign default values to newly created objects? And how can you prevent users from inserting objects that contain invalid data? You can add methods to your enterprise objects to handle such issues.

__Related Concepts:__

[Adding Behavior to Enterprise Objects](CSJ_Tutorial.30.md#apple-gqydsmzz)

###  Distributing Business Logic in Java Client Applications

The value of Java Client applications, of course, lies in their ability to distribute processing duties among objects on the server and objects on the client. Primarily for security and performance reasons, you can have only objects on the server performing some tasks and only objects on the client performing others.

For example, sometimes you want only objects behind the firewalls and other security mechanisms of the server to have access to sensitive information, such as account numbers. On the other hand, processing tasks such as calculation of balances should be performed by objects on the client, thereby improving application performance by eliminating the need for a cycle of the request-response loop.

There are no hard and fast rules for how to distribute object behavior. An enterprise object on the client can have the same set of methods and instance variables as its counterpart on the server, or what it has can be a subset (or superset) of the other object's methods and instance variables. The best way to distribute business logic among objects depends on the particular nature of your application.

###   Writing  Derived Methods

One kind of behavior you might want to add to your enterprise object class is the ability to perform computations based on the values of class properties. For example, studios have movies, and the total revenue of the movies times 1.5 constitutes the studio's portfolio value. To calculate a studio's portfolio value, you could have a method in __Studio.java__
like the following:

####  Studio.java (server and client)

`

public Number portfolioValue() {

    int i, count;

    BigDecimal total;

    NSArray revenues;

    total = new BigDecimal(0);

    revenues = (NSArray)(movies().valueForKey("revenue"));

    count = revenues.count();

    for (i = 0; i < count; i++) {

        total =
total.add((BigDecimal)(revenues.objectAtIndex(i)));

    }

    return total.multiply(new BigDecimal(1.5));

}`

You can display the results of this method in the user interface by forming an association between a control and the method. That way, whenever a new studio is selected or when a selected studio's movie revenues change, its portfolio value is dynamically recalculated and displayed.

__2. Add a method as a display-group property.__
> 
>
> Display the Attributes view of the Inspector for the Studio EODisplayGroup.
>
> 
>
> Add the name of the method (__portfolioValue__
> ) you want to use in an association.
>
> 
>
> Click Add.
>
> ###### 
>
> !
>
> 
>
> Once you've added the method as a class key, you can use it in associations. But before you do this, add the necessary user-interface control.
>
> 
>
> __3. Add text fields to the user interface.__
> > 
> >
> > Drag three text fields from the Views palette.
> >
> > 
> >
> > Make them the same size and align them in a column.
> >
> > 
> >
> > Add labels (as shown at right) to each text field.
> >
> > 
> >
> > Justify the fields' contents (as shown).
> >
> > ###### 
> >
> > !
> >
> > 
> >
> > Now make an association between the Revenue text field and the __portfolioValue__
> > method.
>
> 
>
> __4. Associate a 
>
> method with a user interface control.__
> > 
> >
> > Control-drag from the Revenue text field to the Studio EODisplayGroup.
> >
> > 
> >
> > In the Connections Inspector, choose EOControlAssoc from the pop-up list at the top of the left column.
> >
> > 
> >
> > Select __value__
> > in the left column.
> >
> > 
> >
> > In the right column select the method (__portfolioValue__
> > ) you want to associate with the control.
> >
> > 
> >
> > Double-click __portfolioValue__
> > to connect.
> >
> > 
> >
> > Repeat the above steps, connecting the Name field to Studio's __name__
> > attribute and the Budget field to the __budget__
> > attribute.
> >
> > ###### 
> >
> > !
> >
> > 
> >
> > You now need to add a formatter to the Revenue and Budget fields. The formatter isn't added automatically, because the field has no way of knowing that it's going to be used to display currency values--it's just connected to a property.
>
> 
>
> __5. From the DataViews palette, drag the currency formatter into the new text field.__
> > ###### 
> >
> > !
> >
> > 
>
> Once you've added the formatter, you can use the Inspector to change the format.
>
> __6. Set the format.__
> > 
> >
> > Select the text field, and display the Formatter view of the NSTextField Inspector. Change the format as shown.
> >
> > ###### 
> >
> > !
> > 
> >
> > __7. Build and test the application on the client.__
> > > 
> > >
> > > (See "[Building and Testing Your Application](CSJ_Tutorial.16.md#apple-geytimjt)
> > > " for details.)
> >
> > ###### 
>
> ###  Performing  Validation
>
> 
>
> Another element you'll likely want to add to your enterprise object classes is validation. For example, suppose that when a studio buys a new movie, you want to check to make sure that acquiring the movie won't cause the studio to exceed its budget. You could implement a method in the Studio class like the following:
>
> ####  Studio.java (server and client)
>
> 
>
> `public void validateBudget(Number budget) {
>     if (budget.intValue() < 100) {
> 
>
>         throw new EOValidation.Exception("A budget cannot be less than $100");
> 
>
>     }
> 
>
> }`
>
> 
>
> Now when a studio buys more movies than it can afford, a panel displaying the message "A budget cannot be less than $100" appears when the user attempts to save the changes to the database.
>
> 
>
> Validation methods must be of the form __validate__
> _Attribute_
> . The __validateBudget__
> method is invoked by the __validateValueForKey__
> method, which is part of the EOValidation interface that uses the EOClassDescription class to provide default implementations of validation methods. These methods are invoked automatically by framework components such as EODisplayGroup and EOEditingContext. They are:
>
> 
>
>
> - validateValueForKey
>   
> - validateForSave
>   
> - validateForDelete
>   
> - validateForInsert
> 
> - validateForUpdate
>
>   
>
>   For more discussion of this topic, see the chapter "Designing Enterprise Objects" in the _Enterprise Objects Framework Developer's Guide_ and the NSObject Additions class specification in the _Enterprise Objects Framework Reference_.
>
> ###  Providing Default Values for Newly Inserted Objects
>
> 
>
> When new objects are created in your application and inserted into the database, it's common to assign default values to some of their properties. For example, you might decide to assign newly created Studio objects a default budget (the budget is the amount a studio is allowed to spend on new movies).
>
> 
>
> To assign default values to newly created enterprise objects, use the method __awakeFromInsertion__
> 
>
> . This method is automatically invoked right after your enterprise object class creates a new object and inserts it into an EOEditingContext.
>
> 
>
> The following implementation of __awakeFromInsertion__
> in the Studio class sets the default value of the __budget__
> property to be one million dollars:
>
> ####  Studio.java (server and client)
>
> `
>
> public void awakeFromInsertion(EOEditingContext ec) {
> 
>
>     super.awakeFromInsertion(ec);
> 
>
>
> 
>
>     // no need to invoke willChange here since we're just being inserted
> 
>
>     if (budget == null) {
> 
>
>         budget = new BigDecimal("1000000.00");
> 
>
>     }
> 
>
> }`
>
> 
>
> When a user clicks the Add Studio button in the StudioManager application, a new record is inserted, with "$1,000,000.00" already displayed as a value in the __budget__
> column.
>
> ###  Invoking Server Methods Remotely
>
> 
>
> In a Java Client application you may want some methods to execute only on the server. This is particularly the case when security is an issue, but performance can be a reason as well (as when the method consumes a lot of system resources). Objects on the client side of a Java Client application can use two methods to invoke a server method:
>
> 
>
> - __invokeRemoteMethod__
>   . An enterprise object on the client side can use this method to invoke a method in the corresponding enterprise object on the server. The arguments are the name of the method to invoke and an array of arguments. Before the method is invoked on the server, the current state of the client-side editing context is "pushed" to the server to ensure that the method executes in an identical context. (Note that EODistributedObjectStore has a version of this method that includes a flag as an argument; setting this flag to __false__
>   prevents the client from pushing its editing-context state to the server.)
>
>   
> - __invokeRemoteMethodWithKeyPath__
>   . You can send a message to _any_
>   object on the server with this method, which is defined in EODistributedObjectStore. For more on this method, see the specification for this EODistribution class.
>
> 
>
> In our StudioManager example, let's say that you want to give studios the ability to buy all of the movies that star a specified actor, but you consider this a sensitive computation. You can implement a method such as the following in __Studio__
> __.__
> __java__
> :
>
> ####  Studio.java (client)
>
> `
>
> public void buyAllMoviesStarringTalent(Talent talent) {
>
> 
>
> invokeRemoteMethod("clientSideRequestBuyAllMoviesStarringTalent",
>     new Object[] {talent});
> }`
>
> 
>
> The method begins with "clientSideRequest"; this is not accidental. The EODistributionContext object on the server-side EODistribution layer will reject a remote invocation unless it has this prefix _or_
> its delegate implements the proper delegation methods (see the reference documentation for EODistributionContext or EODistributedObjectStore for more information).
>
> 
>
> The following is the invoked method, which is implemented in the server's __Studio.java__
> :
>
> ####  Studio.java (server)
>
> `
>
> public void clientSideRequestBuyAllMoviesStarringTalent(Talent talent) {
> 
>
>     int i, count;
> 
>
>     NSArray talentMovies;
> 
>
>     EOEnterpriseObject movie, studio;
> 
>
>
> 
>
>     talentMovies = talent.moviesStarredIn();
> 
>
>     count = talentMovies.count();
> 
>
>     for (i = 0; i < count; i++) {
> 
>
>         movie =
>  (EOEnterpriseObject)(talentMovies.objectAtIndex(i));
> 
>
>     if (!(movies().containsObject(movie))) {
> 
>
>         studio = (EOEnterpriseObject)(movie.valueForKey("studio"));
> 
>
>         if (studio != null) {
> 
>
> studio.removeObjectFromBothSidesOfRelationshipWithKey(movie,
> 
>
> "movies");
> 
>
>             }
> 
>
>         addObjectToBothSidesOfRelationshipWithKey(movie,
> 
>
> "movies");
> 
>
>         }
> 
>
>     }
> 
>
> }`
>
> 
>
> This method invokes the __moviesStarredIn__
> method:
>
> ####  Talent.java (server)
>
> `
>
> public NSArray moviesStarredIn() {
> 
>
>         int i, count;
> 
>
>         NSArray movies;
> 
>
>         NSMutableArray moviesStarredIn;
> 
>
>         EOEnterpriseObject movie;
> 
>
>
> 
>
>         moviesStarredIn = new NSMutableArray();
> 
>
>         movies = (NSArray)(roles().valueForKey("movie"));
> 
>
>
> 
>
>         count = movies.count();
> 
>
>         for (i = 0; i < count; i++) {
> 
>
>             movie = (EOEnterpriseObject)(movies.objectAtIndex(i));
> 
>
>             if (!(moviesStarredIn.containsObject(movie))) {
> 
>
>
> moviesStarredIn.addObject(movie);
> 
>
>             }
> 
>
>         }
> 
>
>         return moviesStarredIn;
> 
>
> }`
>
> 
>
> You can associate the __buyAllMoviesStarringTalent__
> method with a user interface control. But first you need to add to your user interface a table view that lists all actors (talent).
>
> 
>
> __8. Add a new table view to your user interface.__
> > 
> >
> > Drag the Talent entity from your model into the nib file window in Interface Builder.
> >
> > 
> >
> > Drag a table view from the Palette onto your window.
> >
> > 
> >
> > Control-drag from each table view column to the Talent EODisplayGroup.
> >
> > 
> >
> > Using the __value__
> > aspect of the EOColumnAssoc, connect the table view columns to the __firstName__
> > and __lastName__
> > class keys, respectively.
>
> 
>
> __9. Add a button to the window.__
> > 
> >
> > Drag a button into the window.
> >
> > 
> >
> > Place it below the Revenue field.
> >
> > 
> >
> > Resize it.
> >
> > 
> >
> > Give it the title "Buy Movies Starring Selected Talent".
> >
> > ###### 
> >
> > !
> >
> > 
> >
> > Now that you've added the table view, connected it to the __firstName__
> > and __lastName__
> > properties of the Talent EODisplayGroup, and added a Buy button to the window, you're ready to use an EOActionAssociation to connect the button to the __buyAllMoviesStarringTalent__
> > method.
>
> 
>
> __10. Associate a method with a user interface control.__
> > 
> >
> > Display the Attributes view of the Inspector for the Studio EODisplayGroup.
> >
> > 
> >
> > In the text field type the name of the method (__buyAllMoviesStarringTalent__
> > ) you want to use in an association.
> >
> > 
> >
> > Click Add.
> >
> > ###### 
> >
> > !
> >
> > 
> >
> > You can now use the __buyAllMoviesStarringTalent__
> > method in associations.
> >
> > 
> >
> > > Control-drag from the "Buy Movies Starring Selected Talent" button to the Studio EODisplayGroup.
> > >
> > > 
> > >
> > > In the Connections Inspector, choose EOActionAssociation from the pop-up list at the top of the left column.
> > >
> > > 
> > >
> > > Select __action__
> > > in the left column, and the method you want to connect to (__buyAllMoviesStarringTalent__
> > > ) in the right column.
> > >
> > > 
> > >
> > > Click Connect.
> >
> > ###### 
> >
> > !
> >
> > 
> >
> > Because the __buyAllMoviesStarringTalent__
> > method takes a Talent object as an argument, you also need to make a connection from the Buy button to the Talent EODisplayGroup.
> >
> > 
> >
> > > Control-drag from the "Buy Movies Starring Selected Talent" button to the Talent EODisplayGroup.
> > >
> > > 
> > >
> > > In the Inspector, select __argument__
> > > in the left column. The __argument__
> > > aspect takes the destination of the connection (Talent) as an argument, which will be supplied to the __buyAllMoviesStarringTalent__
> > > method.
> > >
> > > 
> > >
> > > Click Connect.
> >
> > ###### 
> >
> > !
> >
> > 
> >
> > Once you finish connecting the button, you can use it to purchase all of the movies starring the selected actor for the selected studio.
>
> ###  Controlling the User Interface
>
> 
>
> In Java Client applications you can give the interface controller (implemented in this project in __StudioManager.java__
> on the client) a _controller display group._
> By creating associations between the controller display group and aspects of user-interface objects, you can use the interface controller to manage various facets of the user interface. In the following steps, you add a method as a property of the controller display group and bind this method to the __enabled__
> aspect of the Revenue field through an EOControlAssociation; since this method simply returns __false__
> , the field is disabled.
>
> 
>
> __1. Add a display group to the nib file.__
> > 
> >
> > Drag a display group from the EOPalette to the nib file window.
> >
> > 
> >
> > Double click the title of the display group to select it.
> >
> > 
> >
> > Give the display group the name "Controller".
> >
> > 
> >
> > !
> >
> > 
>
> As mentioned earlier, the owner of the nib file (File's Owner) is an instance of the custom EOInterfaceController automatically created by Project Builder. EOIntefaceController has a __controllerDisplayGroup__
> outlet; in the following step, connect the interface controller to this outlet.
>
> __2. Connect the interface controller to its display group.__
> > 
> >
> > Control-drag from File's Owner to the Controller icon.
> >
> > 
> >
> > In the Connections inspector, select __controllerDisplayGroup__
> > .
> >
> > 
> >
> > Click Connect.
> >
> > ###### 
> >
> > !
> >
> > 
> >
> > Next add the __neverEnabled__
> > method as a property of the controller display group.
>
> 
>
> __3. Add a property to the controller display group.__
>
> 
>
> Select the Controller display group in the nib file.
>
> 
>
> In the Attributes inspector, enter "neverEnabled" in the field.
>
> 
>
> Click Add.
>
> ###### 
>
> !
>
> 
>
> Now hook up the field to the display group using an EOControlAssocation to bind its __enabled__
> aspect to the __neverEnabled__
> method.
>
> 
>
> __4. Connect the field's enabled aspect to the display group property.__
> > 
> >
> > Control-drag from the Revenue field to the Controller display group.
> >
> > 
> >
> > In the Connections inspector, select EOControlAssoc from the pop-up list at the top of the left column.
> >
> > 
> >
> > Select __enabled__
> > in the left column.
> >
> > 
> >
> > Select __neverEnabled__
> > in the right column.
> >
> > 
> >
> > Click OK.
> >
> > ###### 
> >
> > !
>
> 
>
> __5. Implement the neverEnabled method.__
>
> 
>
> Now that the interface controller, the controller display group, and the Revenue field are interconnected via their outlets and associations, you can implement the method bound to the __enabled__
> aspect (in StudioManager.Java on the client).
>
> `
>
> public boolean neverEnabled() {
> 
>
>     return false;
> 
>
> }`
>
> __6. Build, run, and test the application.__
>
> 
>
> Build the project and test the application. The Revenue field has a gray background and cannot be written into.
>
> ---
>
> \xA9 1999 Apple Computer, Inc.
>
> [Previous](CSJ_Tutorial.22.md) | [Back Up One Level](CSJ_Tutorial.20.md) | [Next](CSJ_Tutorial.24.md)
>
> 
>
> Copyright © 2016 Apple Inc. All rights reserved.
>
> - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
> - [Privacy Policy](http://www.apple.com/privacy/)
