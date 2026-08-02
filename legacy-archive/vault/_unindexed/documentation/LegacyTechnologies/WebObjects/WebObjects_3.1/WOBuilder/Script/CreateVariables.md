---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Script/CreateVariables.html
archived_at: '2026-07-15T07:50:53.465198Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Script.book.md)

Creating Variables

# Creating Variables

You can create three different types of variables: application, session, and component. Create application variables in the application window's Application tab, session variables in the application window's Session tab, and component variables in the bottom part of the component window (called the [object browser](ObjectBrowser.md)). Application and session variables have a longer lifetime than component variables. For more information, see "[Application, Session, and Component Variables](VariableTypes.md#apple-kjcumnzygmzdk)."

To create a variable:

Click the add variable button.

Type the variable's name in the Name field and press Enter.

Choose the variable's class in the Class field.

If the variable is an array, click the Array check box.

!

All variables that you create in WebScript are objects. Each object is an instance of a particular [class](Classes.md). No matter what you set the class to, the variable is declared in the script this way:

```
id myVar;
```

Setting a variable's class helps when you [bind dynamic elements](../DynElem/BindElements.md) to it because WebObjects Builder can then determine which attributes match the variable's class.

[!Table of Contents](Script.book.md)
[!Next Section](VariableTypes.md)
