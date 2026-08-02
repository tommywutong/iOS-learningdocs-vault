---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Movies/2_Main.html
archived_at: '2026-07-15T07:48:58.371457Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Movies.book.md) [!Previous Section](1_Main.md)

# Refine the Main page

When you run your application, you may notice that the date values are unformatted. Also, if you try to edit a movie or to create a new one, the application returns an error page. At this point, saving changes to the database doesn't work.
To enable inserting and updating, you need to add a date format for the dateReleased text field element. The __dateReleased__ attribute is stored as an NSCalendarDate object in Movie objects, but it is represented as an NSString object in the text field. Assigning a date format alerts the Movies application that it needs to translate between NSCalendarDates and NSStrings. For more information, see the NSCalendarDate and NSString class specifications in the _Foundation Reference_.
Assigning a date format also allows you to display dates in a more customary format. For example, you can transform a date from its default format (1981-12-27 00:00:00 -0700, for example) to any of the following:

- 12/27/81
- December 21, 1981
- 21 Dec 1981

Similarly, you can specify a number format for the revenue text field element. For example, you can add a dollar sign and thousands separators.
In this section, you'll enable inserting and updating by adding a date format, and you'll improve the display by adding a number format. In addition, you'll configure the __movies__ display group to sort the movies it displays. You should also consider changing the labels of your text fields (for example, change "title" to "Title").

## Add a date format

- Select the dateReleased text field element, which is near the bottom of the Main component window.
- Click the inspector button to open the inspector panel.
!

The inspector that opens displays bindings, attributes, and other settings for elements in a component. Each element occupies a place in the component's HTML hierarchy. For example, a text field element is contained in a form element, which is contained in a page. A page is the highest level in the hierarchy. As shown below, you can use the inspector to traverse the hierarchy from the selected element on up.

!

The dateReleased text field element is selected, so the inspector shows icons for the text field and its parent elements-the surrounding form and the page. All dynamic elements can have as many as two icons in the inspector's icon path: one for inspecting the HTML attributes of the element and a gears icon for inspecting the element's bindings.

- In the inspector, click the rightmost gears icon to inspect the text field's bindings.
- Select the __dateformat__ attribute.
- Type (including the quotes): __"%d %b %Y"__.
- Click Connect.
!

Using this date format ("%d %b %Y"), the Movies application formats the date "1995-12-3 00:00:00 -0700" as "3 Dec 1995". The %d conversion specifier stands for day of the month, %b stands for the abbreviated month name, and %Y stands for year with century. You can create your own date formats with any of the conversion specifiers defined for dates. For more information, see the NSCalendarDate class specification in the _Foundation Reference_.

## Add a number format

- Inspect the revenue text field bindings.
- Bind the text field's __numberformat__ attribute to the string (including the quotes): __"$ #,##0.00"__.

Using this number format ("$ #,##0.00"), the Movies application formats the number 1750000 as "$ 1,750,000". For more information on creating number formats, see the NSNumberFormatter class specification in the _Foundation Reference_.

## Specify a sort order

- Select the __movies__ variable in the Main component's object browser.
- Click the checkmark button.

The checkmark button is only enabled when a WODisplayGroup object is selected in the object browser.

!

In the DisplayGroupEditor panel that opens, you can configure the __movies__ display group to sort the Movie objects it fetches from the database.

- Select the __title__ attribute in the Sort order pop-up list.
- Select Ascending sort order.
!

## Save and run your application

Start a new session with your Movies application by opening the URL you used in the last section. This time, the movies are sorted and the date and revenue values are formatted.
Try inserting and updating movies using dates and numbers in different formats. In particular, date formatters are very flexible. Try entering the following date released values for a selected movie:

- 12/3/95
- 95-12-3
- December 3, 1995
- today

[!Table of Contents](Movies.book.md) [!Next Section](3_Search.md)
