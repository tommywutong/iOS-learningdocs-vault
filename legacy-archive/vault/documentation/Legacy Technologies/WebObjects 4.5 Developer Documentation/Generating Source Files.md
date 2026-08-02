---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.2d.html
archived_at: '2026-07-15T08:09:08.787595Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects-2.md) [!](Specifying%20Custom%20Enterprise%20Object%20Classes-2.md) [!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md)

---

#  Generating Source Files

To begin creating your custom classes, generate source files for the Studio and Talent entities. You'll use these source files as a basis for adding custom behavior to your enterprise objects. Generating source files in a Java Client application typically produces "skeletal" __.java__ files for the associated class. These files are put in the __ClientSideJava.subproj__ subproject.
__Note:__

To generate source files for an entity, you must have replaced the text "EOGenericRecord" in the Class Name and Client-Side Class Name fields with a package name concatenated with a class name.

1. 

   Generate source files.

   In the Model Editor, select the entity for which you want to generate source files.

   Choose Property !
   Generate Client Java File.

   In the Choose Class Name panel verify the file name and location (__ClientSideJava.subproj__
   ) and click Save.

   Click OK when you're asked if you want to insert the files in the subproject.

   For the same entity, choose Property !
   Generate Java FIle.

   In the Choose Class Name panel verify the file name and location (main project) and click Save.

   Click OK when you're asked if you want to insert the files in the main project.

   !

   When Project Builder generates a class file (such as __Studio.java),__ it strips off the package prefix and inserts a package declaration near the top of the file. The class file also includes the necessary import declarations as well as the instance variables and accessor methods derived from the properties of the Studio entity.

   ####  Studio.java (ClientSideJava.subproj)

   package businesslogic.client;

   import com.apple.client.foundation.\*;
   import com.apple.client.eocontrol.\*;
   import java.util.\*;
   import java.math.BigDecimal;

   public class Studio extends EOGenericRecord {

      public static final String BudgetKey = "budget";
      public static final String NameKey = "name";
      public static final String MoviesKey = "movies";

      public Studio(EOEditingContext context, EOClassDescription
        classDesc, EOGlobalID gid) {
        super(context, classDesc, gid);
      }

      public String name() {
        return (String)storedValueForKey(NameKey);
      }

      public void setName(String value) {
        takeStoredValueForKey(value,NameKey);
      }

      public Number budget() {
        return (Number)storedValueForKey(BudgetKey);
      }

      public void setBudget(Number value) {
        takeStoredValueForKey(value,BudgetKey);
      }

      public NSArray movies() {
        return (NSArray)storedValueForKey(MoviesKey);
      }

      public void setMovies(NSMutableArray value) {
        takeStoredValueForKey(value,MoviesKey);
      }

      public void addToMovies(EOEnterpriseObject object) {
        NSMutableArray movies;
        movies = (NSMutableArray)storedValueForKey(MoviesKey);
        willChange();
        movies.addObject(object);
      }

      public void removeFromMovies(EOEnterpriseObject object) {
        NSMutableArray movies;
        movies = (NSMutableArray)storedValueForKey(MoviesKey);
        willChange();
        movies.removeObject(object);
      }

   public void buyAllMoviesStarringTalent(Talent talent) {
      invokeRemoteMethod
         ("clientSideRequestBuyAllMoviesStarringTalent",
        new Object[] {talent});
      }

   }

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects-2.md) [!](Specifying%20Custom%20Enterprise%20Object%20Classes-2.md) [!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md)
