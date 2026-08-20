---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Script/VariableTypes.html
archived_at: '2026-07-15T07:51:06.488141Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Script.book.md)
[!Previous Section](CreateVariables.md)

 Application, Session, and Component Variables

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | ---  Application, Session, and Component Variables    | Where to create | Lifetime | Access in Component Script || Component variables | The component window's object browser | The component's lifetime | _myvar_ | | Application variables | Application tab of application window | The application's lifetime | `self.application.`myvar | | Session variables | Session tab of application window | The session's lifetime | `self.session.`myvar |   When you create a variable in a component window, you are creating a _component variable_ that's visible only inside that component. No other components can access it. A component variable lives only as long as the component that created it. If the component's page is deallocated, so is the component variable. If the page is redrawn after the component has been deallocated, the component variable is reinitialized.  To create a variable with a longer lifetime, create an application or session variable. An _application variable's_ lifetime is the lifetime of the application. One instance of an application variable is created per application. That is, if three users are running sessions of the same application, they will share an instance of that application variable.  _Session variables_ live as long as a session. An instance of a session variable is created for each session. If three users are running sessions of the same application, three instances of a session variable are created. If one user changes the value of that session variable, only that user sees the change. You can read more about application variables, session variables, and component variables in "[Using WebScript](../../DevGuide/WebScript/WebScript.mif.book.md)" in the _WebObjects Developer's Guide_.     --- |

[!Table of Contents](Script.book.md)
[!Next Section](ObjectBrowser.md)
