---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/FetchSpecs3.html
archived_at: '2026-07-18T01:18:24.128322Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Fetch%20Specifications.md) [!Previous Section](Creating%20a%20Fetch%20Specification.md)

# Building a Qualifier

EOModeler's Fetch Specification Builder mode provides an interface for building a qualifier graphically. To use it, select your fetch specification, and choose the Qualifier tab in the Fetch Specification Builder.
For example, a Movie has a Voting object that keeps a __runningAverage__ of how reviewers have voted on the movie. Suppose you want to create a fetch specification for the Movie entity that fetches all movies whose __runningAverage__ is greater than eight. To build the qualifier for such a query:

- In the attribute browser, click Movie's __voting__ relationship.
- In the second column of the browser, select the __runningAverage__ attribute.

The text field just under the browser is updated to display the attribute as the left hand side of an expression. Note that the __runningAverage__ attribute is represented by a _key path_ (__voting.runningAverage__) that identifies the relationship (__voting__) through which the attribute is accessed.

!

Figure 41. Building an Expression.

- Click the >= button.

EOModeler adds a greater than or equal to operator to the expression.

- In the text field, type "8" as the right hand side of the expression.

Instead of building the expression by choosing attributes in the attribute browser and by clicking an operator button, you can type directly into the text field for the expression.

## Creating Compound Qualifiers

You can also use the Query Builder to create compound qualifiers made up of multiple expressions. Click the And button to create a new expression and AND it with the first one. Click the Or button to create a new expression and OR it with the first.
For example, building on the example in the previous section, suppose that you want to fetch movies with a __runningAverage__ greater than or equal to eight but that also have at least ten voters contributing to the average. To further restrict the fetch specification:

- Click the And button.

EOModeler adds a second expression and ANDs it to the first expression.

- Choose __voting.numberOfVotes__ in the attribute browser.
- Click the >= button.
- Type 10 as the right hand side of the expression.

As you build up a complex query, the text field at the bottom of the Query Builder updates to include the full text of the compound qualifier. Instead of building up expressions one by one with the And and Or buttons, you can type directly into this lower text field. The Qualifier Builder parses the qualifier string and displays the individual expressions.

!

Figure 42. Creating a Compound Qualifier

To negate an expression, click in the text of the expression you want to negate, and then click the Not button. Similarly, to remove an expression click in the text of the expression you want to negate, and then click the Remove button.

## Using Qualifier Variables

You can specify absolute criteria for a fetch specification's qualifier- "voting.runningAverage >= 8", for example. However, such a fetch specification is of limited use. More frequently, you want to specify the form of a qualifier and let users supply specific values when they run the application. You can do this with _qualifier variables_.
You specify a qualifier variable using the dollar sign character ($), as in the following:

```
dateReleased = $aDate
```


For example, suppose you want to allow users to search for movies by title, date released, or studio. The query would look like this:

```
((title = $title) OR
(dateReleased = $date) OR
(studio.name = $studioName))
```


You can build this qualifier in EOModeler as specified in the previous sections, and then bind its qualifier variables (__title__, __date__, __studioName__) to your application's user interface. When the application runs, Enterprise Objects Framework automatically replaces the qualifier variables with values supplied in the user interface. You can set this up as follows:

- Create the fetch specification with EOModeler.
- Use Query Builder's user interface to set up a query on the __title__, __date__, and __studio.name__ attributes.

On the right side of each expression, use the $ syntax to identify the qualifier variables.

Depending on the type of graphical user interface your application uses, you access the fetch specification's query bindings differently. For example, in WebObjects Builder, you access the query bindings in the following way:

- Use WebObjects builder to create a component that allows the user to enter the query criteria.

You might create text fields for the title and date released and a pop-up list for the studio name, for example.

- Drag the fetch specification from EOModeler into your component.

This has the effect of creating a new display group for your specification's entity.

- In the WebObjects Builder panel that opens, choose "Add and Configure."
- Configure the new display group, setting its fetch specification to the one you defined in your model.
- In WebObjects Builder, bind the user interface elements to the __queryBindings.title__, __queryBindings.date__, and __queryBindings.studioName__ keys of your display group (__movieDisplayGroup__, for example).

In Interface Builder, the steps are similar except that you bind the user interface elements to __@bindings.title__, __@bindings.date__, and __@bindings.studioName__ keys of your display group. The @bindings syntax represents the value associated with the named qualifier variable.

[!Table of Contents](Fetch%20Specifications.md) [!Next Section](Assigning%20a%20Sort%20Ordering.md)
