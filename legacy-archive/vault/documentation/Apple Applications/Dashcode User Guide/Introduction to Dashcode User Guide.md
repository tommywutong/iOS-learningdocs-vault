---
title: Dashcode User Guide
apple_id: TP40004692
resource_type: Guide
platform: Safari|Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashcode_UserGuide/Contents/Resources/en.lproj/Introduction/Introduction.html
archived_at: '2026-07-15T05:17:37.981303Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Dashboard%20Widget%20Tutorial.md)

# Introduction to Dashcode User Guide

This document provides an overview of the Dashcode development environment. It describes how to use Dashcode to create two types of projects:

- Dashboard widgets—simple, lightweight applications that perform a single task in the OS X Dashboard environment. Widgets are actually packaged webpages powered by standard web technologies such as Hypertext Markup Language (HTML), Cascading Style Sheets (CSS), and JavaScript.
- Web applications—webpages that provide discrete functionality to users. Web applications also make use of web technologies such as HTML, CSS, and JavaScript. Dashcode helps you create mobile Safari web applications, which are also known as iPhone web applications (that is, web applications optimized to run in Safari on iPhone), and Safari web applications (that is, web applications optimized to run in Safari).

Dashcode’s integrated environment allows you to lay out, code, and even test widgets and web applications without opening any other applications. Its layout tools, composers, and editors simplify the process of creating all the resources these projects need. Dashcode also includes handy coding and debugging tools that help you manage and test the code you write.

Read _Dashcode User Guide_ to learn how to use Dashcode to create web applications and Dashboard widgets. Developers who are new to either widget or web application creation learn how to build simple projects and find out more about Dashcode’s capabilities. Experienced developers learn how to speed up development using Dashcode.

This document contains the following chapters:

- [Dashboard Widget Tutorial](Dashboard%20Widget%20Tutorial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmznknltc) walks you through creating your first Dashboard widget with Dashcode.
- [Mobile Safari Web Application Tutorial](Mobile%20Safari%20Web%20Application%20Tutorial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjyfvjvomi) shows you how to create a simple mobile Safari web application with Dashcode.
- [Dual-Product Web Application Tutorial](Dual-Product%20Web%20Application%20Tutorial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjzfvjvomq) shows you how to create a project that produces both a mobile Safari web application and a Safari web application.
- [Starting a Project](Starting%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnbnknltc) discusses the different starting points when working with Dashcode.
- [Designing the User Interface of a Widget or Web Application](Designing%20the%20User%20Interface%20of%20a%20Widget%20or%20Web%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnjnknltq) shows you the tools Dashcode provides for designing the user interface of a widget or web application.
- [Adding Source Code and Creating Bindings](Adding%20Source%20Code%20and%20Creating%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltm) details the source code editing tools included with Dashcode.
- [Testing and Sharing](Testing%20and%20Sharing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjwfvjvomq) includes information on testing, debugging, and distributing a widget or web application.
- [Advanced Topics for Widgets](Advanced%20Topics%20for%20Widgets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjxfvjvomi) talks about localizing a widget using Dashcode and including a widget plug-in.

_Dashcode User Guide_ also includes these appendixes:

- [Dashcode Templates](Dashcode%20Templates.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjvfvjvomi) describes the project templates included with Dashcode.
- [Dashcode Parts](Dashcode%20Parts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjufvjvoni) includes information on Dashcode-originated elements, called parts, and how to customize them.

To obtain Dashcode, download it from [http://developer.apple.com](https://developer.apple.com/). Registration is required, but free.

If you encounter bugs in Apple software or documentation, you are encouraged to report them to Apple. You can also file enhancement requests to describe features you would like to see in future revisions of a product or document. To file bugs or enhancement requests, go to: [http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/)

You must have a valid login name and password to file bugs. You can obtain a login name for free by following the instructions found on the Bug Reporting page. To file a bug for Dashcode, use the Dashcode component, version X.

For in-depth information on how to create web applications that work well on iPhone and iPod touch, see _[Safari Web Content Guide](../Safari%20Web%20Content%20Guide/Developing%20Web%20Content%20for%20Safari.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjr)_. For guidance on how to design the user interface of such an application, see _iOS Human Interface Guidelines_.

Read _[Dashboard Programming Topics](../Dashboard%20Programming%20Topics/Introduction%20to%20Dashboard%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqmzx)_ for information on the technologies available to you when creating a Dashboard widget. All of the Dashboard-specific information discussed in this document is covered in more depth in _[Dashboard Reference](../Dashboard%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmzz)_.

The [Safari Dev Center](https://developer.apple.com/internet/safari/) contains useful information on WebKit, the technology that powers Dashboard widgets, and other Safari-related topics. For more information on the HTML, CSS, and JavaScript capabilities found in WebKit, consult:

- _[Safari HTML Reference](../Safari%20HTML%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanbz)_
- _[Safari CSS Reference](../Safari%20CSS%20Reference/Introduction%20to%20Safari%20CSS%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjq)_
- _[Safari JavaScript Reference](https://developer.apple.com/documentation/webkitjs)_

The `XMLHttpRequest` object allows you to parse XML in JavaScript and use the results. Read [Dynamic HTML and XML: The XMLHttpRequest Object](https://developer.apple.com/internet/webcontent/xmlhttpreq.html) for more information.

[Next](Dashboard%20Widget%20Tutorial.md)

