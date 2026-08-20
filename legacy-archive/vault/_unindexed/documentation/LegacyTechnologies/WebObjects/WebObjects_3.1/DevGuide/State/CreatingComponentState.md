---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/CreatingComponentState.html
archived_at: '2026-07-15T07:47:42.381210Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](ControllingComponentState.md)

# Creating and Accessing Component State

Common uses for component state include storing:

- A list of items that a user can choose from within a particular page
- The user's selection from that list
- Information that the user enters in a form
- Default values for a component's attributes

A simple example of component state can be seen in the first page of the DodgeLite example application, which list models, prices, and types of vehicles for the user to choose from:

!

__Figure 1.__  First Page of the DodgeLite Example

The script for this component (__Main.wos__) declares instance variables for the values displayed in the browser and for the user's selection from the browsers. Before the page can be sent to the user, the instance variables that hold the values to be displayed (__model__, __price__, __type__) are initialized:

```
id models, model, selectedModels;
id prices, price, selectedPrices;
id types, type, selectedTypes;
- init {
    [super init];
    models = [[WOApp modelsDict] allValues];
    types = [[WOApp typesDict] allValues];
    prices = [WOApp prices];
    return self;
}
```

(The __selectedModels__, __selectedPrices__, and __selectedTypes__ instance variables are bound to the __selections__ attributes of the three WOBrowsers and so will contain the user's selections when the Display Cars button is clicked.)

When a user starts a session of the DodgeLite application, the Main component's __init__ method is invoked, initializing the component's instance variables from data accessed through the application object. From this point on (subject to conditions discussed below), the Main component and its instance variables become part of the state stored for that user's session of the DodgeLite application. When the session is released, the component is also released. However, there are other techniques that allow you to control resource allocation on a component basis, as you'll see in the next section.

As with the session state, a component's state is accessible to other objects within the same session. As the result of a user's action, for example, it's quite common for one component to create the component for the next page and set its state. Looking again at the DodgeLite application, consider what happens when the user makes a selection in the first page and clicks Display Cars. The __displayCars__ method in the Main component is invoked:

```
- displayCars {
    id selectedCarsPage = [[self application] pageWithName:@"SelectedCars"];
    ...
    [selectedCarsPage setModels:selectedModels];
    [selectedCarsPage setTypes:selectedTypes];
    [selectedCarsPage setPrices:selectedPrices];
    ...
    [selectedCarsPage fetchSelectedCars];
    return selectedCarsPage;
}
```

The new component is created by sending a __pageWithName:__ message to the WOApplication object, and then a series of messages is sent to this new object to set its state before the object is returned as the response page.

[!Table of Contents](ManagingState.book.md)
[!Next Section](ManagingComponentResources.md)
