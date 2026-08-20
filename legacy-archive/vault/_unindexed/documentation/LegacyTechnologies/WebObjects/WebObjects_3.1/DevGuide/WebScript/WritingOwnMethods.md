---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/WritingOwnMethods.html
archived_at: '2026-07-15T07:48:08.922616Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](CreatingObjects.md)

# Writing Your Own Methods

You can write your own methods in WebScript. The methods you write can be associated with one of two types of objects: the WOApplication object that's automatically created when you run your script, or a WOComponent object that's associated with a particular grouping of a script, an HTML template, and a declarations file (for more information, see the section "[The Role of Scripts in a WebObjects Application](RoleOfScripts.md#apple-kjcummrtgi4tm)"). When you write your own methods, you're effectively extending the behavior of the object associated with the script.

You implement WOApplication methods in the application script. You implement WOComponent methods in a _component script_---that is, a script that has a corresponding HTML template and declarations file. This grouping of three files most commonly maps to a single, dynamically generated HTML page, but this isn't always the case---a component can also represent just a portion of a page.

To define a new method, simply put its implementation in the appropriate application or component script file. You don't need to declare it ahead of time. For example, the following method __addFirstValue:toSecondValue:__ adds one value to another and returns the result:

```
- addFirstValue:firstValue toSecondValue:secondValue {
  id result;
  result = firstValue + secondValue;
  return result;
}
```

In this example, note the following:

- There is no type information supplied for the method's arguments and return types. These types are assumed to be (and must be) __id__, and if you supply any type information, you will get an error.

```objc
    // This is fine.
      - aMethod:anArg {
      // NO!! This won't work.
      - (void) aMethod:(NSString *)anArg {
      // This won't work either.
      - (id)aMethod:(id)anArg {
```

- This method returns a value, stored in __result__. If a method doesn't return a meaningful value, you don't have to include a return statement (and, as stated above, even if a method returns no value you shouldn't declare it as returning __void__).

To invoke the __addFirstValue:toSecondValue:__ method shown above from another method in the same script, you'd simply do something like the following:

```
id sum, val1 = 2, val2 = 3;
sum = [self addFirstValue:val1 toSecondValue:val2];
```

To access the method from another script, you'd first return the page associated with the script in which the method is implemented. You'd then ask the page object to perform the method:

```
id sum, val1 = 2, val2 = 3;
// Get the page in which the method is implemented
id computePage = [WOApp pageWithName:@"Compute"];
// Send the page object to perform the method
sum = [computePage addFirstValue:val1 toSecondValue:val2];
```

The __pageWithName:__ method is discussed in more detail in the section "[Accessing and Sharing Variables](AccessingAndSharingVars.md#apple-kjcummzxgi2dm)."

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](WhatIsSelf.md)
