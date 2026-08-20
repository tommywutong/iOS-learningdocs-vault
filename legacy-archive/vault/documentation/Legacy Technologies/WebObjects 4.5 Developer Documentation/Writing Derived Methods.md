---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.30.html
archived_at: '2026-07-15T08:09:10.571497Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Distributing%20Business%20Logic%20in%20Java%20Client%20Applications.md) [!](Performing%20Validation.md)

---

#   Writing  Derived Methods

One kind of behavior you might want to add to your enterprise object class is the ability to perform computations based on the values of class properties. For example, studios have movies, and the total revenue of the movies times 1.5 constitutes the studio's portfolio value. To calculate a studio's portfolio value, you could have a method in __Studio.java__ like the following:

####  Studio.java

public Number portfolioValue() {
   int i,count;
   double total;
   NSArray revenues;

   total = 0.0;
   revenues = (NSArray)(movies().valueForKey("revenue"));

   count = revenues.count();
   for (i=0; i<count; i++) {
      total +=

((Number)(revenues.objectAtIndex(i))).doubleValue();
   }
   return new BigDecimal(total \* 1.5);
}

You can display the results of this method in the user interface by forming an association between a control and the method. That way, whenever a new studio is selected or when a selected studio's movie revenues change, its portfolio value is dynamically recalculated and displayed.

1. 

   Add the code above to the client-side Studio.java file.
2. 

   Add a method as a display-group property.

   Display the Attributes view of the Inspector for the Studio EODisplayGroup.

   Add the name of the method (__portfolioValue__
   ) you want to use in an association.

   Click Add.

   !

   Once you've added the method as a class key, you can use it in associations. But before you do this, add the necessary user-interface control.
3. 

   Add text fields to the user interface.

   Drag three text fields from the Views palette.

   Make them the same size and align them in a column.

   Add labels (as shown at right) to each text field.

   Justify the fields' contents (as shown).

   !

   Now make an association between the Revenue text field and the __portfolioValue__ method.
4. 

   Associate a 

   method with a user interface control.

   Control-drag from the Revenue text field to the Studio EODisplayGroup.

   In the Connections Inspector, choose EOControlAssoc from the pop-up list at the top of the left column.

   Select __value__
   in the left column.

   In the right column select the method (__portfolioValue__
   ) you want to associate with the control.

   Double-click __portfolioValue__
   to connect.

   Repeat the above steps, connecting the Name field to Studio's __name__
   attribute and the Budget field to the __budget__
   attribute.

   !

   You now need to add a formatter to the Revenue and Budget fields. The formatter isn't added automatically, because the field has no way of knowing that it's going to be used to display currency values--it's just connected to a property.
5. 

   From the DataViews palette, drag the currency formatter into the new text field.

   !

   Once you've added the formatter, you can use the Inspector to change the format.
6. 

   Set the format.

   Select the text field, and display the Formatter view of the NSTextField Inspector. Change the format as shown.

   !
7. 

   Build and test the application on the client.

   (See "[Building and Testing Your Application](Building%20and%20Testing%20Your%20Application.md#apple-geytimjt)
   " for details.)

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Distributing%20Business%20Logic%20in%20Java%20Client%20Applications.md) [!](Performing%20Validation.md)
