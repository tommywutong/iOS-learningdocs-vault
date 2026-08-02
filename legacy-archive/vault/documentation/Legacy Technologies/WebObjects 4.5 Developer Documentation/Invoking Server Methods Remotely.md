---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.33.html
archived_at: '2026-07-15T08:09:12.387495Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Providing%20Default%20Values%20for%20Newly%20Inserted%20Objects.md) [!](Controlling%20the%20User%20Interface.md)

---

#  Invoking Server Methods Remotely

In a Java Client application you may want some methods to execute only on the server. This is particularly the case when security is an issue, but performance can be a reason as well (as when the method consumes a lot of system resources). Objects on the client side of a Java Client application can use two methods to invoke a server method:

- 

  __invokeRemoteMethod__. An enterprise object on the client side can use this method to invoke a method in the corresponding enterprise object on the server. The arguments are the name of the method to invoke and an array of arguments. Before the method is invoked on the server, the current state of the client-side editing context is "pushed" to the server to ensure that the method executes in an identical context. (Note that EODistributedObjectStore has a version of this method that includes a flag as an argument; setting this flag to __false__ prevents the client from pushing its editing-context state to the server.)
- 

  __invokeRemoteMethodWithKeyPath__. You can send a message to _any_ object on the server with this method, which is defined in EODistributedObjectStore. For more on this method, see the specification for this EODistribution class.

In our StudioManager example, let's say that you want to give studios the ability to buy all of the movies that star a specified actor, but you consider this a sensitive computation. You can implement a method such as the following in __Studio___._
__java__:

####  Studio.java (client)

public void buyAllMoviesStarringTalent(Talent talent) {

invokeRemoteMethod("clientSideRequestBuyAllMoviesStarringTalent",
   new Object[] {talent});

}

The method begins with "clientSideRequest"; this is not accidental. The EODistributionContext object on the server-side EODistribution layer will reject a remote invocation unless it has this prefix _or_ its delegate implements the proper delegation methods (see the reference documentation for EODistributionContext or EODistributedObjectStore for more information).

The following is the invoked method, which is implemented in the server's __Studio.java__:

####  Studio.java (server)

public void clientSideRequestBuyAllMoviesStarringTalent(Talent talent) {

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

This method invokes the __moviesStarredIn__ method:

####  Talent.java (server)

public NSArray moviesStarredIn() {

      int i, count;

      NSArray movies;

      NSMutableArray moviesStarredIn;

      EOEnterpriseObject movie;

      moviesStarredIn = new NSMutableArray();

      movies = (NSArray)(roles().valueForKey("movie"));

      count = movies.count();

      for (i = 0; i < count; i++) {

         movie = (EOEnterpriseObject)(movies.objectAtIndex(i));

         if (!(moviesStarredIn.containsObject(movie))) {

            moviesStarredIn.addObject(movie);

         }

      }

      return moviesStarredIn;

}

You can associate the __buyAllMoviesStarringTalent__ method with a user interface control. But first you need to add to your user interface a table view that lists all actors (talent).

1. 

   Add a new table view to your user interface.

   Drag the Talent entity from your model into the nib file window in Interface Builder.

   Drag a table view from the Palette onto your window.

   Control-drag from each table view column to the Talent EODisplayGroup.

   Using the __value__
   aspect of the EOColumnAssoc, connect the table view columns to the __firstName__
   and __lastName__
   class keys, respectively.
2. 

   Add a button to the window.

   Drag a button into the window.

   Place it below the Revenue field.

   Resize it.

   Give it the title "Buy Movies Starring Selected Talent".

   !

   Now that you've added the table view, connected it to the __firstName__ and __lastName__ properties of the Talent EODisplayGroup, and added a Buy button to the window, you're ready to use an EOActionAssociation to connect the button to the __buyAllMoviesStarringTalent__ method.
3. 

   Associate a method with a user interface control.

   Display the Attributes view of the Inspector for the Studio EODisplayGroup.

   In the text field type the name of the method (__buyAllMoviesStarringTalent__
   ) you want to use in an association.

   Click Add.

   !

   You can now use the __buyAllMoviesStarringTalent__
   method in associations.

   Control-drag from the "Buy Movies Starring Selected Talent" button to the Studio EODisplayGroup.

   In the Connections Inspector, choose EOActionAssociation from the pop-up list at the top of the left column.

   Select __action__
   in the left column, and the method you want to connect to (__buyAllMoviesStarringTalent__
   ) in the right column.

   Click Connect.

   !

   Because the __buyAllMoviesStarringTalent__ method takes a Talent object as an argument, you also need to make a connection from the Buy button to the Talent EODisplayGroup.

   Control-drag from the "Buy Movies Starring Selected Talent" button to the Talent EODisplayGroup.

   In the Inspector, select __argument__
   in the left column. The __argument__
   aspect takes the destination of the connection (Talent) as an argument, which will be supplied to the __buyAllMoviesStarringTalent__
   method.

   Click Connect.

   !

   Once you finish connecting the button, you can use it to purchase all of the movies starring the selected actor for the selected studio.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Providing%20Default%20Values%20for%20Newly%20Inserted%20Objects.md) [!](Controlling%20the%20User%20Interface.md)
